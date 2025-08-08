# 💎 Diamonds Price Prediction - MLOps Pipeline

Bu proje, **Kaggle Diamonds** veri seti kullanılarak elmas fiyat tahmini yapmak için geliştirilmiş bir **MLOps pipeline** çalışmasıdır.  
Veri toplama, ön işleme, model eğitimi, model değerlendirme, versiyonlama ve dağıtım adımlarını içermektedir.

---

## 📊 Proje Özeti
- **Amaç:** Elmas fiyatlarını, kesim (cut), renk (color), berraklık (clarity), karat ve diğer özelliklere göre tahmin etmek.
- **Veri Seti:** [Kaggle Diamonds Dataset](https://www.kaggle.com/shivam2503/diamonds)
- **MLOps Hedefleri:**
  - Veri ön işleme ve temizleme
  - Model eğitim sürecini otomatikleştirme
  - Model versiyonlama
  - CI/CD entegrasyonu
  - Model performans takibi (MLflow, DVC vb.)

---

## ⚙️ Kullanılan Teknolojiler ve Araçlar
- **Python** (pandas, numpy, scikit-learn, matplotlib, seaborn)
- **MLOps Araçları:**
  - MLflow – Model izleme ve kayıt
  - DVC – Veri ve model versiyonlama
  - GitHub Actions – CI/CD otomasyonu
  - Docker – Ortam kapsülleme
- **Diğer Araçlar:**
  - Jupyter Notebook
  - Flask / FastAPI (model servisi için)

---

## 📂 Proje Yapısı

---

## 🔄 MLOps Süreci
1. **Veri Toplama & Ön İşleme**  
   - Eksik ve aykırı değerlerin temizlenmesi  
   - Özellik mühendisliği  
2. **Model Eğitimi**  
   - SVM algoritması kullanıldı  
   - GridSearchCV ile hiperparametre optimizasyonu  
3. **Model Versiyonlama**  
   - DVC ile veri ve model takip edildi  
   - MLflow ile deney sonuçları kaydedildi  
4. **Dağıtım (Deployment)**  
   - Flask/FastAPI API olarak servis edildi  
   - Docker ile konteynerize edildi  
   - GitHub Actions ile otomatik dağıtım  
5. **Takip & İzleme**  
   - Model performansı düzenli olarak ölçüldü  
   - Yeni veri geldiğinde pipeline otomatik çalıştırıldı  

---

## 🚀 Kurulum ve Çalıştırma

### 1. Depoyu Klonla
```bash
git clone https://github.com/kullaniciadi/diamonds-mlops.git
cd diamonds-mlops

### 2. Sanal Ortam Oluştur ve Bağımlılıkları Kur

python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate
pip install -r requirements.txt

### 3. DVC ile Veriyi Çek

```bash
dvc pull

### 4. Pipeline’ı Çalıştır

```bash
dvc repro

### 5. Model Servisini Başlat

```bash
python src/app.py
