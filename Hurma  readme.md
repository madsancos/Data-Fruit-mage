# 🌴 Hurma Türleri Görüntü Sınıflandırma ve Hata Analizi Projesi

<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/TensorFlow-FF6F00?style=for-the-badge&logo=tensorflow&logoColor=white" />
  <img src="https://img.shields.io/badge/ResNet50-98.78%25_Success-brightgreen?style=for-the-badge&logo=target&logoColor=white" />
  <img src="https://img.shields.io/badge/MobileNetV2-93.92%25-blue?style=for-the-badge&logo=android&logoColor=white" />
  <img src="https://img.shields.io/badge/Gradio-FFBB00?style=for-the-badge&logo=huggingface&logoColor=black" />
</p>

<br>

Bu proje, 9 farklı hurma türünün derin öğrenme ve transfer learning teknikleri kullanılarak sınıflandırılmasını kapsayan kapsamlı bir teknik çalışmadır.

---

* **Canlı Demo:** Modeli anlık olarak test etmek için aşağıdaki linki kullanabilirsiniz:

  👉 [Hugging Face Live Demo](https://huggingface.co/spaces/sancos/date_fruit_image)


## 1. Giriş (Introduction)
Tarım teknolojilerinde kalite kontrol süreçlerini otomatize etmek, verimliliği artıran en önemli unsurlardan biridir. Bu proje kapsamında; görsel veriler üzerinden Ajwa, Galaxy, Medjool, Meneifi, Nabtat Ali, Rutab, Shaishe, Sokari ve Sugaey türlerini yüksek doğruluk oranıyla ayırt edebilen modeller geliştirilmiştir. Çalışmanın temel amacı, özgün bir CNN mimarisi ile önceden eğitilmiş (Pre-trained) modeller arasındaki performans farkını analiz etmektir.

---

## 2. Analiz (Analysis)
Veri seti, hurmaların doku, renk ve form özelliklerini yansıtan yüksek çözünürlüklü görüntülerden oluşmaktadır.

- **Veri Dağılımı:** %80 eğitim, %20 doğrulama (validation)
- **Keşifsel Analiz:** Meneifi ve Medjool türleri yüksek benzerlik göstermektedir
- **Hata Analizi:** Ajwa net ayrılırken, Meneifi zaman zaman karışmaktadır

---

## 3. Yöntemler (Methods)

### 🏗️ Model 1: Sıfırdan CNN (From Scratch)
- 5 Convolution Layer
- 3 MaxPooling Layer
- Dropout (%50)
- Adam Optimizer
- Categorical Crossentropy

### 🚀 Model 2: Transfer Learning
- ResNet50
- MobileNetV2
- InceptionV3
- Xception

---

## 4. Sonuçlar (Results)

| Model Türü | Mimari | Accuracy | Loss |
|-----------|--------|----------|------|
| Custom CNN | 5-Layer CNN | %86.93 | 0.4290 |
| 🏆 ResNet50 | Transfer | %98.78 | 0.0528 |
| MobileNetV2 | Transfer | %93.92 | 0.1724 |
| InceptionV3 | Transfer | %93.01 | 0.1924 |
| Xception | Transfer | %86.32 | 0.4259 |

---

## 5. Refleks ve Düşünceler (Reflection)

- Scratch CNN modeli beklenenin üzerinde performans göstermiştir
- Transfer Learning açık ara daha başarılıdır
- Doku benzerliği modelin en büyük hata kaynağıdır
- Data augmentation performansı artırabilir


---

<div align="center">
  <br>
  <p><b>Serdar ÖNAL</b></p>
  <p><i>Kıdemli İnşaat Mühendisi & Yapay Zeka Uygulayıcısı</i></p>
  <br>
 <a href="https://github.com/madsancos">
    <img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white" alt="GitHub" />
  </a>
  <a href="https://www.linkedin.com/in/serdar%C3%B6nal1981/">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
  </a>
  <a href="https://www.kaggle.com/serdaronal">
    <img src="https://img.shields.io/badge/Kaggle-20BEFF?style=for-the-badge&logo=Kaggle&logoColor=white" alt="Kaggle" />
  </a>
  <br>

</div>