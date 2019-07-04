/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("nav_bar");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}

function Scroll_()
{
    document.getElementById('main').scrollIntoView();
}

function show(z) {
  // var x = document.getElementById("useless");
  //   x.style.display = "none";
  var x = document.getElementById("random");
    x.style.display = "none";
  var x = document.getElementById("subscription");
    x.style.display = "none";
  var x = document.getElementById("content");
    x.style.display = "none";
  var x = document.getElementById(z);
    x.style.display = "block";
  var element = document.getElementById("random_link");
  element.classList.remove("Active");
  var element = document.getElementById("subscription_link");
  element.classList.remove("Active");
  var element = document.getElementById("content_link");
  element.classList.remove("Active");
  var element = document.getElementById(z+"_link");
  element.classList.add("Active");
}

function expandcontent() {
  var w = document.getElementById("desc");
  var y = document.getElementById("expanded_desc");
  var z = document.getElementById("toggle_desc");
  if (z.textContent == '▼') {
    w.style.display = "none";
    y.style.display = "block";
    z.textContent = "▲ ";
  }
  else {
    w.style.display = "block";
    y.style.display = "none";
    z.textContent = "▼";
  }
}

function toggle_comment() {
  var y = document.getElementById("fade_Screen");
  var x = document.getElementById("create_comment_window");
  var z = document.getElementById("togglecomment");
  if (x.style.display == "none") {
    x.style.display = "block";
    y.style.display = "block";
  }
  else {
    x.style.display ="none";
    y.style.display= "none";
  }
}

function get_order() {
  var x = document.getElementById("sorter").value;
  var a = document.getElementById("price")
  var b = document.getElementById("-date_posted")
  var d = document.getElementById("n_rating")
  var e = document.getElementById("n_subs")
  var y = document.getElementById(x)
  a.style.display = "none";
  b.style.display = "none";
  d.style.display = "none";
  e.style.display = "none";
  y.style.display= "block";
}