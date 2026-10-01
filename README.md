# Naruto Hikoya Bot

Ushbu repo Naruto olami uchun professional hikoya yaratuvchi Streamlit appidir.

## Nima qiladi?
- Naruto universe'dan foydalanib hikoya yaratadi
- Epic, romance, dark, comedy, drama, action uslubingizni tanlashingiz mumkin
- Qahramon yaratish funksiyasi mavjud
- O'zbek tilida professional tarzda javob beradi

## Ishga tushirish

1. Virtual environment yarating:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

2. Paketlarni o'rnating:
   ```bash
   pip install -r requirements.txt
   ```

3. `.env` faylini yarating:
   ```bash
   cp .env.example .env
   ```

4. `.env` ichiga Anthropic API kalitingizni kiriting:
   ```env
   ANTHROPIC_API_KEY=your_key_here
   ```

5. Appni ishga tushiring:
   ```bash
   streamlit run app.py
   ```

## Fayllar
- `app.py` - Streamlit frontend va story generator
- `requirements.txt` - kerakli paketlar
- `.env.example` - environment namuna

## Misol mavzu
- Naruto vs Sasuke final battle
- Hinata va Naruto sevgi hikoyasi
- Dark village conspiracy

## Eslatma
Proyektda API kalit kerak bo'ladi. Kalit yo'q bo'lsa, app ishlamaydi.
