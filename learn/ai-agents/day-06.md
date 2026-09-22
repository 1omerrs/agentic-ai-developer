# Day 6 — Tools ve API'ler

## Tool nedir?
Q: Tool nedir? Day 4'ten bir ornek ver.
A: Tool agent'in elidir; agent'in istedigi seyi tool yapar.
Day 4 ornegi: web_search (internette arama).



## API nedir?
Q: API nedir? Tool ile iliskisi ne?
A: API'yi konusma agina / konusma kuralina benzetebiliriz. Tool API ile konusur ve secilen/istenen bilgiyi alip agent'e verir.



## Tool calling
Q: Agent bir tool'u ne zaman cagirir? Kisa ornekle anlat.
A: Agent tool'u, ne zaman / nerede kullanacagina karar verdiginde veya API'den veri cekilmesi gerektiginde cagirir.
Ornek: "Istanbul'da hava kac derece?" → API/tool lazim.
Ornek: "Merhaba" → tool gerekmez, direkt cevaplanir.



## Custom tool tasarimi
Q: Twitter'a post atan bir tool dusun. Ne alir, ne yapar, ne dondurur?
A:
- Ne alir: girdi — tweet metni
- Ne yapar: Twitter API'ye gonderir
- Ne dondurur: "gonderildi" veya hata



## Guvenlik
Q: Agent'e "istedigi her kodu calistir" tool'u vermek neden tehlikeli?
A: Kotu / sinirsiz tool gercek dunyada zarar verebilir (yanlis dosya silme, tehlikeli komut, istenmeyen istek). Bu yuzden tool'lar sinirli olmali.

