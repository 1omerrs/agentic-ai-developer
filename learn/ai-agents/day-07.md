# Day 7 — Memory (hafiza)

## Short vs long
Q: Short-term ile long-term memory farki nedir? Birer ornek ver.
A: Short-term kisa sureli: yalnizca o sohbetteki mesajlari kisa sure hatirlar (ornek: "adim Omer" → ayni sohbette "adim ne?").
Long-term uzun sureli: sohbet kapansa dahi hatirlar (ornek: "hep Turkce cevap iste" tercihi).



## Neden lazim?
Q: Memory olmazsa agent'te ne bozulur? Kisa ornekle anlat.
A: Guvenilirlik / tutarlilik bozulur: onceki konuyu veya verdigimiz bilgileri katarak cevap veremez.
Ornek: "adim Omer" dememe ragmen sonra "adim ne?" diye sorunca bilmez.
(Dokumandan ilgili yeri bulmak da long-term / vector store tarafina yakindir.)



## Vector store
Q: Vector store ne ise yarar? (tek cumle + basit ornek)
A: Metni vektore cevirir; 100 sayfayi bastan sona taramak yerine benzer/ilgili yeri bulur.
Ornek: notlarda "odeme nasil?" deyince ilgili parcayi getirir.



## Thread fikri
Q: Ayni sohbet (ayni thread) ile yeni sohbet arasinda memory neden farkli davranir?
A: Short-term memory sohbet id'sine (thread) gore tutulur. Sohbet 1'de verdigin bilgiyi sohbet 2 (yeni id) tanimaz; temiz sayfa gibi baslar.


## Tasarim
Q: Kullanici tercihlerini uzun sure hatirlayan bir agent icin memory'yi nasil tasarlarsin? (short + long)
A: Tercihler icin long-term kullanirim; sohbet kapansa dahi hatirlar, kullaniciyi unutmaz, ogrendikleriyle daha iyi cikti verir.
Yanina short-term de koyarim: o anki sohbetin mesaj akisi icin.


## Kod pratigi
thread-1: adi ve favori rengi (mavi) hatirladi.
thread-2: ikisini de bilmedi (yeni sohbet).
A: Calisti — short-term memory thread_id ile bagli.

