# Some notes

## Zadání práce 

Navrhněte a naprogramujte aplikaci, která bude detekovat šifrovaný provoz v síti a
zobrazovat jeho procentuální zastoupení oproti celkovému provozu v síti. Aplikace
bude vytvářet přehledné statistiky o použitém protokolu, původu/cíli, velikosti a
množství šifrovaných dat v síti. Aplikace dále bude v síti detekovat pakety, které by
mohly být z hlediska bezpečnosti šifrovány, ale nejsou. Aplikace bude vytvářet obraz
obvyklého provozu v síti a bude detekovat nastalé odchylky (změna velikosti a
množství šifrovaných dat, protokolů, zdrojových/cílových adres apod.). Simulujte různé
scénáře síťového provozu a na nich otestujte vytvořenou aplikaci.

Projekt naprogramujte ve Vámi zvoleném programovacím jazyku s využitím
dostupných knihoven.

## What is needed:
 - panda + matplob
 - wireshark
 - tshark
 - python3-tk

To install:
Tested for ubuntu 20 + 22
1)  Libraries needed to run:
sudo apt install wireshark
sudo apt install python3-tk
sudo apt install tshark
2) Install requirement for project:
pip3 install -r requirements.txt
3)
python3 gui.py