# Day 4 — Research Assistant (ilk kod)

## Bugunun hedefi
Web aramasi yapabilen basit bir agent yazmak ve calistirmak.

## Parcalar (Day 2 baglantisi)
- LLM = beyin (Gemini)
- web_search = tool (el), 12sn timeout
- create_agent = loop

## Dosyalar
- `day-04/main.py` — agent kodu
- `day-04/requirements.txt` — kutuphaneler
- `day-04/.env.example` — API key ornegi
- Repo kok `.env` — gercek key (Git'e gitmez)

## Test
Calistirdim mi? Sonuc ne oldu?
A: Evet. Soru: "LangChain'i kim olusturdu?" → Harrison Chase. Sure ~39 sn (onceki DuckDuckGo hang ~4 dk idi; timeout'lu ddgs tool ile duzeltildi).

## Extension fikri
Arama sonucunu ozetletmek icin ne degistirirdim?
A: system_prompt'a "sonuclari 3 maddede ozetle" eklerdim / soruyu degistirirdim.
