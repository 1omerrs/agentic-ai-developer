# Day 9 — Evaluation ve debugging

## Evaluation
Q: Evaluation ne demek? Neden agent'te chatbot'tan daha zor olabilir?
A: Evaluation = agent'in iyi calisip calismadigini olcmek (basari, dogruluk, sure...).
Agent'te chatbot'tan zor olabilir cunku sadece son cevap degil; tool cagrilari, ara adimlar da kontrol edilir.
(API bozuldu mu, dongude mi, prompt mu eksik → bunlar daha cok debugging.)



## Metrik
Q: Task success rate ne olcer? Tek basina yeterli midir? Neden?
A: Isi bitirip bitirmedigini / sonucun basarili olup olmadigini olcer.
Tek basina yeterli degil: cevap dogru olsa bile tool'lar cok dolanmis / pahali olabilir veya prompt zayif kalabilir.



## Debugging
Q: Agent dongude takildi. Ilk 3 debug adimin ne olur?
A:
1) Nerede takildigina bakilir
2) Yanlis tool donup donmedigine / tekrar tekrar ayni tool mu bakilir
3) API/tool sonucu bos veya hatali mi bakilir



## Tracing
Q: Tracing / observability ne ise yarar?
A: Iceride hangi tool'larin cagrildigini ve islem hareketlerini adim adim gormemizi / okumamizi saglar.



## Day 4 baglantisi
Q: Day 4'te arama uzun surmustu. Bu bir debug ornegi mi? Ne yaptik?
A: Evet, debug ornegi. Takilma gorduk ve timeout ekledik.

