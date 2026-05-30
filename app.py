import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications import ResNet50

# 1. Sayfa Ayarları ve Başlık
st.set_page_config(page_title="Hurma Türü Tespit Sistemi", page_icon="🌴")
st.title("🌴 Hurma Türü Sınıflandırma Sistemi")
st.write("ResNet50 Şampiyon Modeli ile %98.78 Doğruluk Payı")

# 3. Kategorileri Tanımlayalım (Kaggle'daki sırayla aynı olmalı)
categories = ['Ajwa', 'Galaxy', 'Medjool', 'Meneifi', 'Nabtat Ali', 'Rutab', 'Shaishe', 'Sokari', 'Sugaey']


# 2. Şampiyon Modeli Yükleyelim
# 2. Model
@st.cache_resource
def load_my_model():
    base_model = ResNet50(weights=None, include_top=False, input_shape=(224, 224, 3))
    
    model = tf.keras.models.Sequential([
        base_model,
        tf.keras.layers.GlobalAveragePooling2D(),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dropout(0.5),
        tf.keras.layers.Dense(len(categories), activation='softmax')
    ])

    model.load_weights('dates_resnet50_champion_v1.keras')
    
    return model

with st.spinner('Model yükleniyor...'):
    model = load_my_model()



# 4. Dosya Yükleme Alanı
uploaded_file = st.file_uploader("Bir hurma fotoğrafı yükleyin...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Görüntüyü göster
    image = Image.open(uploaded_file)
    st.image(image, caption='Yüklenen Fotoğraf', use_container_width=True)
    
    # 5. Görüntüyü Modelin İstediği Formata Getirelim (Pre-processing)
    st.write("🧠 Analiz ediliyor...")
    
    # Boyutlandırma (ResNet50 için 224x224)
    img = image.resize((224, 224))
    img_array = np.array(img)
    
    # Eğer görüntüde 4 kanal varsa (RGBA), 3 kanala indir (RGB)
    if img_array.shape[-1] == 4:
        img_array = img_array[:, :, :3]
        
    # ResNet50 için özel ön işlem (Kaggle'da yaptığımız gibi)
    img_array = tf.keras.applications.resnet50.preprocess_input(img_array)
    img_array = np.expand_dims(img_array, axis=0) # (1, 224, 224, 3) formatı

    # Giriş tipinin float32 olduğundan emin olalım
    img_array = img_array.astype('float32')


    # 6. Tahmin Yapalım
    predictions = model.predict(img_array)
    score = tf.nn.softmax(predictions[0]) # Olasılıkları hesapla
    
    class_idx = np.argmax(predictions[0])
    result_label = categories[class_idx]
    confidence = np.max(predictions[0]) * 100

    # 7. Sonucu Ekrana Yazdıralım
    st.success(f"### Tahmin: {result_label}")
    st.info(f"🎯 Doğruluk Olasılığı: %{confidence:.2f}")

    # Olasılık Dağılım Grafiği (Opsiyonel)
    st.bar_chart({cat: float(prob) for cat, prob in zip(categories, predictions[0])})

st.divider()
st.caption("Serdar ÖNAL | İnşaat Mühendisi & Yapay Zeka Geliştiricisi   2026")