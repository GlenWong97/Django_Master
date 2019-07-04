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
  var x = document.getElementsByClassName("random");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  var x = document.getElementsByClassName("subscription");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  }
  var x = document.getElementsByClassName("content");
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "none";
  } 
  var x = document.getElementsByClassName(z);
  for (i = 0; i < x.length; i++) {
    x[i].style.display = "block";
  }
  document.getElementById("random_link").classList.remove("Active");
  document.getElementById("subscription_link").classList.remove("Active");
  document.getElementById("content_link").classList.remove("Active");
  document.getElementById(z+"_link").classList.add("Active");
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
  var a = document.getElementsByClassName("price")
  var b = document.getElementsByClassName("-date_posted")
  var d = document.getElementsByClassName("-n_rating")
  var e = document.getElementsByClassName("-n_subs")
  var y = document.getElementsByClassName(x)
  for (i = 0; i < a.length; i++) {
    a[i].style.display = "none";
  }
  for (i = 0; i < b.length; i++) {
    b[i].style.display = "none";
  }
  for (i = 0; i < d.length; i++) {
    d[i].style.display = "none";
  }
  for (i = 0; i < e.length; i++) {
    e[i].style.display = "none";
  }
  for (i = 0; i < y.length; i++) {
    y[i].style.display = "block";
  }
}