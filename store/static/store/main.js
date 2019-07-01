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
