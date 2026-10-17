// Bookcase Math engine - capacity honesty, run exactly.
// Mirrored float-for-float by oracle.py; keep the op order identical.

function _pos(x, msg) {
  if (!isFinite(x) || x <= 0) throw new Error(msg);
  return x;
}

// floor(x*10+0.5)/10 matches Python identically for positive x.
function _round1(x) {
  return Math.floor(x * 10 + 0.5) / 10;
}

function _fmt(x) {
  return x % 1 === 0 ? String(x) : x.toFixed(1);
}

// The shelf truth: how many of YOUR books one shelf takes.
function shelfTruth(widthIn, booksPerFoot) {
  _pos(widthIn, "width must be more than 0 inches");
  _pos(booksPerFoot, "books a foot must be more than 0");
  var books = Math.floor(widthIn * booksPerFoot / 12);
  return "Your " + widthIn + "-inch shelf at " + booksPerFoot + " books a foot holds " + books + ".";
}

// The collection truth: how many shelves the pile really is.
function collectionTruth(books, perShelf) {
  _pos(books, "count at least 1 book");
  _pos(perShelf, "shelf capacity must be more than 0");
  var shelves = Math.ceil(books / perShelf);
  var base = books + " books at " + perShelf + " a shelf is " + shelves + (shelves === 1 ? " shelf" : " shelves");
  var spare = shelves * perShelf - books;
  if (spare === 0) return base + " exactly.";
  return base + " - " + spare + " to spare.";
}

// The wall truth: the run of shelves against the wall you have.
function wallTruth(shelves, widthIn, wallFeet) {
  _pos(shelves, "count at least 1 shelf");
  _pos(widthIn, "width must be more than 0 inches");
  _pos(wallFeet, "wall must be more than 0 feet");
  var need = _round1(shelves * widthIn / 12);
  var head = shelves + (shelves === 1 ? " shelf" : " shelves") + " of " + widthIn +
    " inches need " + _fmt(need) + " feet of wall";
  if (need === wallFeet) return head + " - your " + _fmt(wallFeet) + " feet takes them exactly.";
  if (need > wallFeet) {
    return head + " - your " + _fmt(wallFeet) + " feet leaves " + _fmt(_round1(need - wallFeet)) + " short.";
  }
  return head + " - your " + _fmt(wallFeet) + " feet leaves " + _fmt(_round1(wallFeet - need)) + " to spare.";
}
