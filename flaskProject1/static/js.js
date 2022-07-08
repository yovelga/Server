const activePage = window.location.pathname;

/*create an arey of the links in nav, 
compare each to pathname and mark the one that is active
*/
const navLinks = document.querySelectorAll('nav a').forEach(link => {
  if(link.href.includes(`${activePage}`)){
    link.classList.add('active');
  }
});


function recomand(){
    
    if(document.getElementById("age").value<121){
        document.getElementById("book_rec").innerHTML="אנו ממליצים לך על הספר - הזקן בן ה100 שברח מהחלון";
    }


    if(document.getElementById("age").value<80){
        document.getElementById("book_rec").innerHTML=" אנן ממליצים לך על הספר - מסביב לעולם ב80 יום ";
    }
  
    
    if(document.getElementById("age").value<40){
        document.getElementById("book_rec").innerHTML="אנו ממליצים לך על הספר - בתול בן 40";
    }
    
}

// var t=" .הגעתם לאתר הקריאה של ווב, כאן שומרים על פרטיות הלקוחות. ומכבדים אחד את השני, יש להחזיר את הספרים תוך 20 יום"
// function text(){
// document.getElementById("text_p").innerHTML=t;

// }


var i = 0;
var txt = '.הגעתם לאתר הקריאה של ווב, כאן שומרים על פרטיות הלקוחות. ומכבדים אחד את השני, יש להחזיר את הספרים תוך 20 יום';
var speed = 50;
      
function text () {
    if (i < txt.length) {
        document.getElementById("text_p").innerHTML += txt.charAt(i);
        i++;
        setTimeout(text, speed);
        }
      }