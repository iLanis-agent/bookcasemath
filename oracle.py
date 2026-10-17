#!/usr/bin/env python3
# Bookcase Math oracle - mirrors engine.js float-for-float.
import json, math

def _pos(x, msg):
    if not math.isfinite(x) or x <= 0:
        raise ValueError(msg)
    return x

def _round1(x):
    return math.floor(x * 10 + 0.5) / 10

def _fmt(x):
    return str(int(x)) if x % 1 == 0 else f"{x:.1f}"

def shelf_truth(width_in, books_per_foot):
    _pos(width_in, "width must be more than 0 inches")
    _pos(books_per_foot, "books a foot must be more than 0")
    books = math.floor(width_in * books_per_foot / 12)
    return f"Your {width_in}-inch shelf at {books_per_foot} books a foot holds {books}."

def collection_truth(books, per_shelf):
    _pos(books, "count at least 1 book")
    _pos(per_shelf, "shelf capacity must be more than 0")
    shelves = math.ceil(books / per_shelf)
    base = f"{books} books at {per_shelf} a shelf is {shelves}" + (" shelf" if shelves == 1 else " shelves")
    spare = shelves * per_shelf - books
    if spare == 0:
        return base + " exactly."
    return base + f" - {spare} to spare."

def wall_truth(shelves, width_in, wall_feet):
    _pos(shelves, "count at least 1 shelf")
    _pos(width_in, "width must be more than 0 inches")
    _pos(wall_feet, "wall must be more than 0 feet")
    need = _round1(shelves * width_in / 12)
    head = ((f"{shelves} shelf" if shelves == 1 else f"{shelves} shelves") + f" of {width_in}"
            f" inches need {_fmt(need)} feet of wall")
    if need == wall_feet:
        return head + f" - your {_fmt(wall_feet)} feet takes them exactly."
    if need > wall_feet:
        return head + f" - your {_fmt(wall_feet)} feet leaves {_fmt(_round1(need - wall_feet))} short."
    return head + f" - your {_fmt(wall_feet)} feet leaves {_fmt(_round1(wall_feet - need))} to spare."

CASES = [
    ("shelfTruth", (32, 9)),
    ("shelfTruth", (36, 10)),
    ("shelfTruth", (20, 7)),
    ("shelfTruth", (0, 9)),
    ("shelfTruth", (32, 0)),
    ("collectionTruth", (60, 24)),
    ("collectionTruth", (48, 24)),
    ("collectionTruth", (49, 24)),
    ("collectionTruth", (0, 24)),
    ("collectionTruth", (24, 24)),
    ("wallTruth", (3, 32, 8)),
    ("wallTruth", (3, 32, 6.5)),
    ("wallTruth", (3, 32, 10)),
    ("wallTruth", (0, 32, 8)),
]

FNS = {"shelfTruth": shelf_truth, "collectionTruth": collection_truth, "wallTruth": wall_truth}

out = []
for name, args in CASES:
    try:
        expected = FNS[name](*args)
    except ValueError as e:
        expected = "ERR:" + str(e)
    out.append({"fn": name, "args": list(args), "expected": expected})

with open("expected.json", "w") as f:
    f.write(json.dumps(out, indent=2) + "\n")
print(f"{len(out)} cases written")
