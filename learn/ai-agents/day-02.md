# Day 2 — LLM, Tools, Memory

## ELI5
Q: LLM agent'in "beyni" olarak nasil calisir?
A: LLM bir olayı dusunur ve planlar — ornegin "markete gitmem gerek". Tek basina gidip alısveris yapmaz; gerekirse tool'a karar verir, sonucu okur, cevap yazar.


## Senaryo
Q: Tool use'u somut bir ornekle anlat (hava durumu degil). Akis: kullanici istegi → LLM karari → tool cagrisi → sonuc → final cevap.
A:
- Kullanici: "Videonun altindaki yorumlari analiz et"
- LLM karari: yorumlari cekmem lazim → tool cagir
- Tool: yorumlari ceker, LLM'e getirir
- LLM: analiz eder
- Final cevap: sonucu kullaniciya gonderir



## Deep Dive
Q: Memory neden onemli? Short-term vs long-term, birer ornekle.
A: Memory gecmis konusmalari/bilgileri tutar; AI bunlari kullanarak daha iyi cikti verir.
- Short-term: ornek "son 10 mesaji hatirla" — ekonomik, chat icin uygun
- Long-term: uzun sure tutar — bir seyi ogrenmek / tercihleri saklamak icin uygun



## LOOP
Q: Gercek bir gorevi (Cursor veya ChatGPT ile yaptigin) Observe / Think / Act adimlarina bol (4-6 adim).
A: Gorev: bir dosyanin ozetini cikarmak
1. Observe: kullanici bir dosya iletti ve ozet istedi
2. Think: dosyayi okuyup ozetlemem lazim
3. Act: dosyayi okur / ozeti yazar
4. Observe: ozet hazir
5. Act: sonucu kullaniciya gosterir



## Connection
Q: Production'da hangisi daha tehlikeli: kotu LLM cevabi mi, kotu tool cagrisi mi? Neden?
A: Kotu tool cagrisi — cunku tool gercek dunyada is yapar (dosya, API, odeme, mail). Yanlis cevap can sikar; yanlis tool zarar verebilir.

