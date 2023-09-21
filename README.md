# Longbi

Writing an real-time WordHunt solver.

The native python implementation runs fast enough, but I'm writing stuff in C just for learning purposes.

Uses the 2019 Collins Scrabble word list, which can be found in [this thread](https://boardgames.stackexchange.com/questions/38366/latest-collins-scrabble-words-list-in-text-file).

## TesserOCR vs PyTesseract vs EasyOCR

Out of these three, TesserOCR was significantly faster (taking only around 0.01s on CPU--M1 Pro).

However, TesserOCR isn't playing nice my mac, so I am using PyTesseract for now: PSM 10 makes it faster than EasyOCR based of some quick tests.
