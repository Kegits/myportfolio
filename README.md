
# Kelvin Gakuo — Django Portfolio (prefilled)

This repository is a ready-to-deploy Django portfolio site prefilled with Kelvin Gakuo's details.
Included:
- Basic Django app `portfolio_app`
- ASGI entry for Vercel (`api/wsgi.py`)
- `vercel.json` and `requirements.txt`
- `.env.example` showing how to configure Postgres and SECRET_KEY
- `CV.pdf` (copy of the uploaded CV)

## Prefilled data
- Name: Kelvin Gakuo
- GitHub: https://github.com/Kegits
- Email: hansaxel192@gmail.com
- Vercel projects (examples):
- https://vercel.com/kelvin-githaithis-projects/restaurant-website/81AXwaz8rrNrEqFvCN9zHpi2PdFK
- https://vercel.com/kelvin-githaithis-projects/portfolio-app/AHRhVta6X2v8VTtf3RTBjjwmZAhc
- https://great-animation-git-main-kelvin-githaithis-projects.vercel.app/
- https://vercel.com/kelvin-githaithis-projects/bird-game/5XCjtA41gp6Hys9QZ8t59QziGkRa

---

## Quick Kali Linux steps (commands to run locally)

```bash
# 1) Clone the repo (after you push it to GitHub)
git clone https://github.com/Kegits/myportfolio.git
cd myportfolio

# 2) Create and activate a venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

# 3) Create .env from example and set values (SECRET_KEY, DEBUG, DATABASE_URL)
cp .env.example .env
# edit .env and set SECRET_KEY and DATABASE_URL (see Postgres section below)

# 4) Run migrations & collectstatic (local dev)
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py runserver 8000

# 5) Test with Uvicorn (ASGI)
uvicorn myportfolio_project.asgi:application --reload --port 8000
```

## Postgres & External Storage (production)
- For production use a managed Postgres provider (Supabase, Neon, Render, ElephantSQL).
- Set `DATABASE_URL` in Vercel environment variables to the provided connection string.
- For static/media files use object storage (e.g., AWS S3) or serve static from Vercel as configured (`staticfiles/`).
- See `.env.example` for placeholders.

## Deploy to Vercel (brief)
1. Push repo to GitHub.
2. On Vercel: Import Project -> select repo.
3. Set Environment Variables:
   - SECRET_KEY
   - DEBUG=False
   - DATABASE_URL (if using Postgres)
4. In Vercel build settings, set Build Command:
   `python manage.py collectstatic --noinput && python manage.py migrate --noinput`
5. Deploy.

