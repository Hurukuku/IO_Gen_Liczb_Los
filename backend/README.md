# Backend (Python)

API serwisu do losowania liczb (FastAPI).

## Uruchomienie

Wymagany Python 3.11+. Z katalogu `backend/`:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
uvicorn app.main:app --reload
```

API: http://127.0.0.1:8000, dokumentacja (Swagger): http://127.0.0.1:8000/docs

Testy: `pytest`

## Endpointy

| Metoda | Ścieżka       | Opis                         |
|--------|---------------|------------------------------|
| GET    | `/helloworld` | test działania API           |

## Struktura

```
app/
├── main.py            # punkt wejścia aplikacji
├── config.py          # konfiguracja (zmienne środowiskowe)
├── api/routes/        # endpointy HTTP (hello, generate, stats)
├── schemas/           # modele żądań i odpowiedzi (kontrakt API)
├── db/                # połączenie z bazą SQL i modele tabel
├── generators/        # algorytmy losowania (wspólny interfejs w base.py)
├── entropy/           # zamiana szumu z kamery/mikrofonu na ziarno
└── services/          # logika: generowanie z zapisem, statystyki
tests/                 # testy
```
