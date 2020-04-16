function load()
{
  var loader = '<div class="loadingio-spinner-spinner-0dpf02320gal"><div class="ldio-pmy181v3w7"><div></div><div></div><div></div><div></div><div></div><div></div><div></div><div></div></div></div>';
  var button = document.getElementById("submit");
  button.innerHTML = loader;
}
function stopLoading()
{
  var button = document.getElementById("submit");
  button.innerHTML = "Submit";
}
