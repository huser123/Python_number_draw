# Python Drawing Scripts

## Leírás
Ez a gyűjtemény három Python szkriptet tartalmaz, amelyek különböző geometriai és matematikai minták rajzolására szolgálnak. Az alábbiakban megtalálhatóak a fájlok és funkcióik rövid leírásai.

---

## Fájlok listája és funkcióik

1. **Fibonacci-number-draw.py**
   - Fibonacci-számok alapján rajzol vonalakat különböző irányokba.
   - Turtle grafikával valósítja meg a Fibonacci sorozat vizuális reprezentációját.
   - Kimeneti fájl lehetőség: EPS formátum.

2. **Number-draw.py**
   - Számokat rajzol grafikus megjelenítésként 0-tól 100-ig.
   - Minden számjegyhez irányokat rendel (például 1 → balra, 2 → lefelé).
   - Turtle grafikát használ, a kimeneti kép EPS formátumban menthető.

3. **Theodorus-spiral.py**
   - A Teodorusz-spirál vizualizációját készíti el matplotlib segítségével.
   - Lépcsőzetes spirál generálása animációval.
   - Matematika tanulmányozásához és vizualizációhoz használható.

---

## Használat

1. **Fibonacci-number-draw.py** és **Number-draw.py** futtatása:
   - Ellenőrizd, hogy a Python 3 telepítve van a rendszeren.
   - Nyisd meg a terminált, és futtasd az adott szkriptet:
     ```bash
     python3 Fibonacci-number-draw.py
     ```
     vagy
     ```bash
     python3 Number-draw.py
     ```
   - A program végén a grafikus ablak tartalma menthető EPS fájlba.

2. **Theodorus-spiral.py** futtatása:
   - Győződj meg arról, hogy a matplotlib telepítve van:
     ```bash
     pip install matplotlib
     ```
   - Futtasd a szkriptet:
     ```bash
     python3 Theodorus-spiral.py
     ```
   - A program interaktív animációt jelenít meg a spirál fejlődéséről.

---

## Követelmények
- Python 3
- **Turtle Graphics** modul (beépített Python modul)
- Matplotlib (Theodorus-spiral.py esetén)

---
