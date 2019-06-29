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
  var x = document.getElementById("random");
    x.style.display = "none";
  var x = document.getElementById("subscription");
    x.style.display = "none";
  var x = document.getElementById("content");
    x.style.display = "none";
  var x = document.getElementById(z);
    x.style.display = "block";
  // document.getElementById(z+"_link").style.background = "white";
  // document.getElementById("random_link").style.background = rgb(200, 200, 200);
  // document.getElementById("subscription_link").style.background = rgb(200, 200, 200);
  // document.getElementById("content_link").style.background = rgb(200, 200, 200);
}