

/* Funskjon for søkeknapp */

let slideSearch = document.querySelector(".searchbutton");

function showBar() {
  if (slideSearch.style.display === "block") {
    slideSearch.style.display = "none";
  } else {
    slideSearch.style.display = "block";
  }
}

window.onload = function(){
document.getElementById('loading').className = 'loading active';
setTimeout(function(){
  document.getElementById('loading').style.display='none';
},3000)
}

/* Funksjon for søkeknapp end */


// Made by Angelito - "Message when a button clicked"

var button = document.getElementById("ProductXbox1");
var cartMessage = document.getElementById("cartMessage");

button.addEventListener('click', function() {
    cartMessage.style.display = 'block';
    setTimeout(function() {
        cartMessage.style.display = 'none';
    }, 2000);
});

