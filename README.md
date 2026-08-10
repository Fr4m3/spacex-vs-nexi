# SpaceX vs Nexi — IPO a confronto

Analisi (in italiano) delle IPO di **SpaceX** (SPCX, Nasdaq, 12 giugno 2026), **Nexi** (NEXI, Borsa Italiana, 16 aprile 2019) e **Ferrari** (RACE, NYSE/Euronext Milan, 21 ottobre 2015), con focus su:

- flottante all'IPO (SpaceX 4,3% · Nexi 35,6% · Ferrari 9%)
- calendario lockup e crescita dell'offerta in circolazione
- inclusione negli indici e flussi dei fondi passivi (Nasdaq-100, Russell, S&P 500, MSCI, FTSE MIB, EURO STOXX 50)
- cosa è successo a Nexi e Ferrari negli anni successivi alla quotazione
- scenari a 3 anni per il titolo SpaceX (2026-2029)

Pubblicato con GitHub Pages:

- **https://fr4m3.github.io/spacex-vs-nexi/** (SpaceX vs Nexi)
- **https://fr4m3.github.io/spacex-vs-nexi/ferrari.html** (SpaceX vs Ferrari)

## Aggiornamento automatico

Il workflow GitHub Actions `.github/workflows/aggiorna-dati.yml` esegue ogni giorno (22:00 UTC, manuale dal tab Actions) lo script `.github/scripts/aggiorna_dati.py`, che legge i prezzi di SPCX, NEXI.MI e RACE da Yahoo Finance e scrive `dati.json`. Le pagine leggono `dati.json` via JavaScript e aggiornano prezzi, variazioni e countdown del calendario eventi.

> Contenuto di analisi, non consulenza finanziaria. Le fonti sono elencate in ogni pagina.