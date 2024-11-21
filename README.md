# 🎮 Higher Lower Game - Instagram Followers

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Találd ki, melyik híresség/márka rendelkezik több Instagram követővel! Játékos konzol alkalmazás Python nyelven.

## ✨ Jellemzők

- 📊 Valós Instagram követőszámok
- 🌟 50+ híresség és márka
- 🎯 Pontszámkövetés
- 🎨 ASCII art vizuális elemek
- 🔄 Folyamatos játékmenet

## 🚀 Telepítés

```bash
git https://github.com/namezor90/Quiz_Game.git
cd higher-lower-game
python main.py
```

## 💻 Használat

1. Futtasd a `main.py` fájlt
2. Hasonlítsd össze a két megjelenített profilt
3. Tippelj `A` vagy `B` beírásával, melyiknek van több követője
4. Minden helyes válasz után +1 pont
5. Játék vége helytelen válasz esetén

## 📁 Projekt Struktúra

```
higher-lower-game/
├── main.py      # Fő játék logika
├── game_data.py # Követési adatok
└── art.py       # ASCII művészet
```

## 🛠️ Fejlesztés

Új profilok hozzáadása a `game_data.py` fájlban:

```python
{
    'name': 'Profilnév',
    'follower_count': 123,
    'description': 'Leírás',
    'country': 'Ország'
}
```

## 📝 Licensz

[MIT](LICENSE)

## 🤝 Közreműködés

1. Fork-old a projektet
2. Hozz létre egy új branch-et (`git checkout -b feature/awesome`)
3. Commit-old a változtatásokat (`git commit -m 'Add awesome feature'`)
4. Push-old a branch-et (`git push origin feature/awesome`)
5. Nyiss egy Pull Request-et

## 👥 Szerzők

- [@namezor90](https://github.com/namezor90)
