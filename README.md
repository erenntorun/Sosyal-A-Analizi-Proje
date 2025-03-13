# Valorant Sosyal Ağ Analizi

Bu proje, **Valorant** oyunundaki ajan (agent) ve harita (map) ilişkilerini sosyal ağ analizi (Social Network Analysis - SNA) teknikleriyle incelemektedir. Python'un **NetworkX**, **Pandas**, **Matplotlib** ve **Seaborn** kütüphaneleri kullanılarak, ajanların haritalardaki oynanma sıklıkları üzerinden bir ağ (graph) oluşturulmuş ve analiz edilmiştir.

## 🚀 Proje İçeriği
Bu projede aşağıdaki analizler gerçekleştirilmiştir:

- **Veri Yükleme ve Ön İşleme**: Eksik değer analizi, veri temizleme.
- **Ajan ve Harita Analizi**: Ajanların ve haritaların oynanma sayılarının hesaplanması.
- **Ağ Oluşturma**: Haritalar ve ajanlar arasında bir iki modlu (bipartite) ağ oluşturulması.
- **Ağ Görselleştirme**: Graf yapısının çizimi ve analiz edilmesi.
- **Ağ Merkeziyet Ölçümleri**: Derece, yakınlık ve arasındalık merkeziyetlerinin hesaplanması.
- **Topluluk Algoritmaları**: Louvain algoritması kullanılarak toplulukların belirlenmesi.
- **Düğüm Derece Dağılımı**: Ajan ve haritaların düğüm derecelerinin analiz edilmesi.
- **Ağ Özellikleri**: Ortalama yol uzunluğu, kenar ve düğüm sayıları, ağ yoğunluğu ve ağ çapı hesaplamaları.

## 📂 Dosya ve Kod Açıklamaları

| Dosya | Açıklama |
|--------|----------|
| `Valorant.py` | Veri yükleme, ön işleme ve ajan-harita analizlerini içerir. |
| `ValorantMain.py` | Sosyal ağ oluşturma, analiz ve görselleştirme kodlarını içerir. |
| `valorant_games.csv` | Valorant oyun verisini içeren CSV dosyası. |
| `README.md` | Proje açıklamalarını içeren döküman. |

## 📊 Kullanılan Kütüphaneler
Bu projenin çalışması için aşağıdaki Python kütüphanelerinin yüklü olması gerekmektedir:

```bash
pip install pandas numpy matplotlib seaborn networkx python-louvain
```

## 📌 Kurulum ve Kullanım
1. **Projeyi Klonlayın**
   ```bash
   git clone https://github.com/erenntorun/Valorant-Social-Network-Analysis.git
   cd Valorant-Social-Network-Analysis
   ```
2. **Gerekli Kütüphaneleri Yükleyin**
   ```bash
   pip install -r requirements.txt
   ```
3. **Veri Setini İlgili Klasöre Ekleyin**
   - `valorant_games.csv` dosyanızın proje dizininde olduğundan emin olun.

4. **Python Scriptlerini Çalıştırın**
   ```bash
   python Valorant.py
   python ValorantMain.py
   ```

## 🖥️ Çıktılar ve Görseller
Proje çalıştırıldığında aşağıdaki görseller üretilmektedir:
- **Ajan-Harita İlişki Ağı** 📌
- **Derece Merkeziyet Dağılımı** 📈
- **Topluluk Algoritması Sonuçları** 🎯
- **Bağlı Bileşen Analizi** 🕸️
- **Ağ Yoğunluğu, Çap ve Ortalama Yol Uzunluğu** 🔢

## 📚 Kaynaklar
- [NetworkX Belgeleri](https://networkx.github.io/documentation/stable/)
- [Seaborn Görselleştirme](https://seaborn.pydata.org/)
- [Python Louvain Modülü](https://python-louvain.readthedocs.io/en/latest/)


---

📌 **Hazırlayan:** [Eren](https://github.com/erenntorun)  
