
# AI Tööintervjuu Simulaator

See projekt kasutab FastAPI ja OpenAI API-t, et simuleerida tööintervjuud.

## Käivita lokaalselt

1. Kopeeri `.env.example` -> `.env` ja lisa oma OpenAI API võti
2. Paigalda moodulid:
   ```
   pip install -r requirements.txt
   ```
3. Käivita server:
   ```
   uvicorn main:app --reload
   ```
4. Ava `static/index.html` brauseris ja kasuta

## Deploy Render.com-i

1. Forki see repo GitHubis
2. Mine [https://render.com](https://render.com), vali "New Web Service"
3. Linki GitHub repo
4. Lisa keskkonnamuutujaks `OPENAI_API_KEY`
5. Deployi ja kasuta saadud linki HTML-is `fetch` aadressina
