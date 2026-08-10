# Stato di lavoro — SpaceX vs Nexi (+ Ferrari)

> File di ripristino della sessione. Ultimo aggiornamento: 10 agosto 2026 (sera).

## Fatto (AGGIORNATO ✅)

1. **Ricerca completata**: IPO SpaceX (SPCX, 12/06/2026: $135 fissi, $75 mld, float 4,3%, cap ~$1,75 trn) · Nexi (16/04/2019: €9, €2,01 mld, float 35,6%; OPA CVC/CDP) · Ferrari (21/10/2015: $52, $893 mln, float 9%; oggi ~$407, cap ~$79 mld).
2. **Pagina principale** `index.html` (SpaceX vs Nexi) + **pagina Ferrari** `ferrara.html`. Pubblicate.
3. **Aggiornamento automatico ATTIVO**: `.github/workflows/aggiorna-dati.yml` (cron 22:00 UTC + manuale) → `dati.json`. Test run del 10/08/2026 19:57 UTC: **SUCCESSO** — SPCX 138,11 · NEXI.MI 4,20 · RACE 406,79, commit e push automatici funzionanti, Pages rebuild OK.
4. **Scope `workflow` sul token**: attivato via device-flow (gh auth refresh) — nessun token copiato in chiaro.

## Link

- https://fr4m3.github.io/spacex-vs-nexi/ (SpaceX vs Nexi)
- https://fr4m3.github.io/spacex-vs-nexi/ferrari.html (SpaceX vs Ferrari)

## In sospeso / idee

- [ ] Verificare il **primo run cron automatico** (22:00 UTC di stasera/domani — controllare dal tab Actions)
- [ ] Eventuali correzioni alle date "stima" del calendario (Q3 earnings SPCX ~17/11/2026 da confermare)
- [ ] Vedere se aggiungere un terzo comparatore o un grafico sparkline 5 giorni
- [ ] Rivedere il warning "Node.js 20 deprecated" su checkout@v4/setup-python@v5 (aggiornare a @v5/@v6 quando serve)

## Come riprendere

Dire "riprendiamo": leggere questo file, controllare l'ultimo run del workflow e `dati.json` sul sito. Il sistema è autonomo: i prezzi si aggiornano ogni giorno alle 22:00 UTC.
