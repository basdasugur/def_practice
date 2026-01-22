# Kütüphane importları en üste
import math 

print("###" * 20)
print("Hesaplama Motoruna Hoş Geldiniz..")

# SABİTLER (En tepede tanımlanır)
PI_SAYISI = 3.14

# --- FONKSİYONLAR ---

def kare_alani(kenar: float) -> float:
    """Bir kenarı girilen karenin alanını döndürür."""
    return kenar * kenar

def dikdortgen_alani(kisa: float, uzun: float) -> float:
    """Kısa ve uzun kenarı girilen dikdörtgenin alanını döndürür."""
    return kisa * uzun

def daire_alani(yaricap: float) -> float:
    """Yarıçapı girilen dairenin alanını hesaplar."""
    return PI_SAYISI * (yaricap ** 2)

# --- ANA PROGRAM ---

while True:
    print("\n" + "---" * 15)
    print("1. Kare")
    print("2. Dikdörtgen")
    print("3. Daire")
    print("q. Çıkış")

    secim = input("İşlem seçiniz: ").strip().lower()

    if secim == "q":
        print("Çıkış yapılıyor...")
        break

    # HATA YÖNETİMİ (Try-Except Bloğu)
    try:
        if secim == "1":
            # float() kullandık ki kullanıcı 5.5 gibi sayılar da girebilsin
            sayi = float(input("Kenar uzunluğu: "))
            
            # Fonksiyondan gelen sonucu formatlayarak yazdırıyoruz (.2f = virgülden sonra 2 basamak)
            sonuc = kare_alani(sayi)
            print(f"✅ Karenin Alanı: {sonuc:.2f}")

        elif secim == "2":
            kisa = float(input("Kısa Kenar: "))
            uzun = float(input("Uzun Kenar: "))
            sonuc = dikdortgen_alani(kisa, uzun)
            print(f"✅ Dikdörtgenin Alanı: {sonuc:.2f}")

        elif secim == "3":
            yaricap = float(input("Yarıçap: "))
            sonuc = daire_alani(yaricap)
            print(f"✅ Dairenin Alanı: {sonuc:.2f}")
        
        else:
            print("⚠️ Hatalı seçim, lütfen tekrar deneyin.")

    except ValueError:
        print("❌ HATA: Lütfen sayısal bir değer giriniz!")
