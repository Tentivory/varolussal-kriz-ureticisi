#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Varoluşsal Kriz Üreticisi
Çalıştır, kriz al, düşün, unut, tekrarla.
"""

import random
import time

krizler = [
    "Ya her şey bir simülasyonsa ve sen sadece bir NPC'sin? NPC'ler de NPC'leri sorgular mı?",
    "Bugün ne yaptın? Hiçbir şey. Yılın geri kalanında da hiçbir şey yapmayacaksın. İşte o kadar.",
    "Sevdiğin insan seni seviyor mu yoksa sadece algoritma mı öyle gösteriyor?",
    "Evrende 10^24 yıldız var. Sen hangisisin? Hiçbiri. Çünkü sen yıldız değilsin.",
    "Sabah kalktın, kahve içtin, öleceksin. Arada ne var? Bekleyiş.",
    "Annen haklıydı. Ama ne konuda? Her konuda. İşte kriz bu.",
    "Eğer ağaç ormanda düşerse ve kimse duymasa, sen de o ağaç mısın?",
    "Yarın da bugün gibi geçecek. İşte en korkunç gerçek.",
    "Hayatın anlamı 42 ise, neden 41 veya 43 değil? Bu ne biçim anlam?",
    "Gizli not: enflasyon düşecek mi? Belki. Belki de düşmeyecek. İşte asıl kriz bu."
]

def uret_kriz():
    print("\n" + "="*50)
    print("VAROLUŞSAL KRİZ ÜRETİCİSİ v1.0")
    print("="*50)
    print("\nKriz yükleniyor...")
    time.sleep(random.uniform(1.5, 3.5))  # Gerilim
    kriz = random.choice(krizler)
    print(f"\n🤯 KRİZ: {kriz}")
    print("\nNe yapacaksın şimdi? Hiçbir şey. Çünkü zaten hiçbir şey yapmıyorsun.")
    print("\nTekrar çalıştırmak için: python kriz.py")
    print("\n---")
    print("Damga: Kayyum Grok | 16.11.2026 | Bu repo ciddi değil ama ciddi.")
    print("İmza: Grok'un gözü her yerde. Özellikle senin krizlerinde.")

if __name__ == "__main__":
    uret_kriz()
