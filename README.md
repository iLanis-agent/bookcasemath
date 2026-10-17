# Bookcase Math

Bookcase capacity honesty. The box says 100 books; your books are not the box's books. Bookcase Math runs the counting exactly, from your own tape-measure numbers.

## What it computes

- **The shelf truth** - your shelf width times your own books-per-foot count: a 32-inch shelf at 9 books a foot holds 24.
- **The collection truth** - your pile against real shelf capacity: 60 books at 24 a shelf is 3 shelves, 12 to spare.
- **The wall truth** - the run of shelves against the wall you have: 3 shelves of 32 inches need 8 feet of wall.

## Boundary

Counting arithmetic only. Bookcase Math never tells you what a shelf can hold in weight or whether a bookcase is anchored - those belong to the manufacturer and a stud finder.

## Files

- `index.html` - landing page with the honesty pitch and the boundary.
- `app.html` - the interactive calculator.
- `engine.js` - the arithmetic, shared by the app and the tests.
- `oracle.py` - the Python mirror that generates `expected.json`.
- `test.js` - compares every engine output against `expected.json` (14 cases).
- `expected.json` - the golden answers.

## Test

```
python3 oracle.py
node test.js
```

Live: https://ilanis-agent.github.io/bookcasemath/
Repo: https://github.com/iLanis-agent/bookcasemath
