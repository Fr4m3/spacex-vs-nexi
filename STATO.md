# Stato di lavoro — SpaceX vs Nexi (+ Ferrari)

> File di ripristino della sessione. Ultimo aggiornamento: 10 agosto 2026.

## Fatto

1. **Ricerca completata**: IPO SpaceX (SPCX, 12/06/2026: $135 fissi, $75 mld, float 4,3%, cap ~$1,75 trn; oggi ~$130-133) · Nexi (16/04/2019: €9, €2,01 mld, float 35,6%; oggi ~€3,9-4,2, OPA CVC/CDP) · Ferrari (21/10/2015: $52, $893 mln, float 9%; oggi ~$407-412, cap ~$79 mld, float ~64%, MAI in S&P 500 perché olandese).
2. **Pagina principale** `index.html` (SpaceX vs Nexi): confronti, grafici SVG, timeline inclusioni, calendario eventi SPCX con countdown JS (16-17 ondate di lockup), scenari 3 anni, fonti.
3. **Pagina Ferrari** `ferrari.html` (SpaceX vs Ferrari): stesso stile, tabelle, grafici (flottante 9→64%, cap annua), confronto indici, lezione finale.
4. **Aggiornamento automatico**: `.github/workflows/aggiorna-dati.yml` (cron giornaliero 22:00 UTC + manuale) + `.github/scripts/aggiorna_dati.py` (Yahoo Finance) → `dati.json`; le pagine leggono dati.json e aggiornano prezzi/variazioni/countdown. Testato localmente (OK: SPCX 130,3 · NEXI 4,20 · RACE 407,68).
5. **Pubblicato**: repo `Fr4m3/spacex-vs-nexi` (public, main). Pages: `index.html` + `ferrari.html`.

## Link

- https://fr4m3.github.io/spacex-vs-nexi/ (SpaceX vs Nexi)
- https://fr4m3.github.io/spacex-vs-nexi/ferrari.html (SpaceX vs Ferrari)

## In sospeso / idee

- [ ] Verificare il primo run del workflow Actions dopo il push (tab Actions → run manuale)
- [ ] Eventuali correzioni alle date "stima" del calendario (Q3 earnings SPCX ~17/11/2026 da confermare)
- [ ] Vedere se aggiungere un terzo comparatore o un grafico sparkline 5 giorni
- [ ] (Fatto) Otimizzazione mobile/accessibilità → rivedere se servono ulteriori ritocchi

## Come riprendere

Dire "riprendiamo": leggere questo file, controllare l'ultimo run del workflow e `dati.json`, proseguire dalle idee sopra.