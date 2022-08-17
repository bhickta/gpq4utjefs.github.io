document.oncontextmenu = new Function("return false");
const disableselect = (e) => {
  return false
}
document.onselectstart = disableselect
document.onmousedown = disableselect