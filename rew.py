import streamlit as st

st.set_page_config(page_title="Fiyatlandırma Stratejisi Simülasyonu")

st.title("💡 Fiyatlandırma Stratejisi Simülasyonu")
st.write("Aşağıdaki bilgileri girerek ürününüz için en uygun fiyatlandırma stratejisini öğrenin.")

# Kullanıcıdan bilgi al
urun_turu = st.selectbox("Ürün Türü", ["Teknolojik Ürün", "Gıda Ürünü", "Lüks Ürün", "Hizmet", "Hızlı Tüketim", "Dijital Ürün"])
hedef_kitle = st.selectbox("Hedef Kitle", ["Fiyat Duyarlı", "Kaliteye Önem Veren", "Lüks Tüketici", "Genç Profesyonel", "Geniş Kitle"])
kalite = st.radio("Ürün Kalitesi", ["Düşük", "Orta", "Yüksek"])
rekabet = st.radio("Pazardaki Rekabet", ["Düşük", "Orta", "Yüksek"])
yenilik = st.radio("Ürün Yenilik Derecesi", ["Yeni Ürün", "Standart Ürün"])
satis_kanali = st.selectbox("Satış Kanalı", ["Fiziksel Mağaza", "Online Platform", "Her İkisi"])

# Karar Mantığı
def strateji_oner(urun, kitle, kalite, rekabet, yenilik, kanal):
    if urun == "Teknolojik Ürün":
        if yenilik == "Yeni Ürün":
            if kitle == "Genç Profesyonel":
                return "🎯 Kaymağını Alma Fiyatlandırması (Skimming)"
            else:
                return "📈 Penetrasyon Fiyatlandırması"
        else:
            return "💰 Değer Temelli Fiyatlandırma"

    elif urun == "Gıda Ürünü":
        if rekabet == "Yüksek":
            return "⚔️ Rekabet Temelli Fiyatlandırma"
        else:
            return "📉 Penetrasyon Fiyatlandırması"

    elif urun == "Lüks Ürün":
        return "👑 Kaymağını Alma Fiyatlandırması (Skimming)"

    elif urun == "Hizmet":
        if kalite == "Yüksek":
            return "💎 Değer Temelli Fiyatlandırma"
        else:
            return "🧠 Psikolojik Fiyatlandırma"

    elif urun == "Hızlı Tüketim":
        if rekabet == "Yüksek":
            return "🛒 Rekabet Temelli Fiyatlandırma"
        else:
            return "🧠 Psikolojik Fiyatlandırma"

    elif urun == "Dijital Ürün":
        if kanal == "Online Platform":
            return "🌐 Freemium Modeli veya Dinamik Fiyatlandırma"
        else:
            return "📈 Penetrasyon Fiyatlandırması"
    
    return "🤷 Uygun strateji belirlenemedi, daha fazla bilgi gerekebilir."

# Sonuç
if st.button("Stratejiyi Göster"):
    sonuc = strateji_oner(urun_turu, hedef_kitle, kalite, rekabet, yenilik, satis_kanali)
    st.success(f"Önerilen Fiyatlandırma Stratejisi: {sonuc}")
