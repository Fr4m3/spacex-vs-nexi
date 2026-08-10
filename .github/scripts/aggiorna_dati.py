#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Aggiorna dati.json con i prezzi di SPCX, NEXI.MI e RACE (Yahoo Finance).

Uso: python3 aggiorna_dati.py
Scrive ./dati.json con: aggiornato (UTC ISO), e per ogni titolo {prezzo, precedente, varPct}.
Se un fetch fallisce, mantiene il valore precedente da dati.json (se esiste).
Esce sempre con 0: gli errori di rete non devono far fallire il workflow.
"""
import json
import os
import sys
import urllib.request
from datetime import datetime, timezone

TICKERS = ["SPCX", "NEXI.MI", "RACE"]
PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "dati.json")
PATH = os.path.normpath(PATH)
UA = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}


def fetch(ticker):
    url = f"https://query1.finance.yahoo.com/v8/finance/chart/{ticker}?range=5d&interval=1d"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=20) as r:
        meta = json.load(r)["chart"]["result"][0]["meta"]
    prezzo = meta.get("regularMarketPrice")
    prev = meta.get("chartPreviousClose") or meta.get("previousClose")
    ts = meta.get("regularMarketTime")
    if prezzo is None or ts is None:
        raise ValueError(f"meta incompleto per {ticker}")
    return {
        "prezzo": round(float(prezzo), 3),
        "precedente": round(float(prev), 3) if prev else None,
        "varPct": round((float(prezzo) / float(prev) - 1) * 100, 2) if prev else None,
        "time": ts,
    }


def main():
    dati = {}
    if os.path.exists(PATH):
        try:
            dati = json.load(open(PATH, encoding="utf-8"))
        except Exception:
            dati = {}

    ok = 0
    for t in TICKERS:
        try:
            dati[t] = fetch(t)
            ok += 1
            print(f"OK  {t}: {dati[t]['prezzo']} ({dati[t]['varPct']}%)")
        except Exception as e:
            print(f"ERR {t}: {e} (mantengo valore precedente se presente)")

    if ok == 0:
        print("Nessun dato aggiornato, dati.json invariato")
        return 0

    dati["aggiornato"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tmp = PATH + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(dati, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, PATH)
    print(f"Scritto {PATH}")
    return 0


if __name__ == "__main__":
    sys.exit(main())