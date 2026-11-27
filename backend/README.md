# Backend (Python)

API serwisu do losowania liczb.

> Status: tylko struktura katalogów. Szkielet API powstaje w osobnym zadaniu.

## Struktura

```
app/
├── main.py            # punkt wejścia aplikacji
├── config.py          # konfiguracja (zmienne środowiskowe)
├── api/routes/        # endpointy HTTP (generate, stats)
├── schemas/           # modele żądań i odpowiedzi (kontrakt API)
├── db/                # połączenie z bazą SQL i modele tabel
├── generators/        # algorytmy losowania (wspólny interfejs w base.py)
├── entropy/           # zamiana szumu z kamery/mikrofonu na ziarno
└── services/          # logika: generowanie z zapisem, statystyki
tests/                 # testy
```
