window.addEventListener('scroll', () => {
    const navbar = document.getElementById('navbar');

    if(window.scrollY > 50){
        navbar.classList.add('scrolled');
    }
    else{
        navbar.classList.remove('scrolled');
    }
});

function revealSections() {

    const reveals = document.querySelectorAll('.reveal');

    reveals.forEach(section => {

        const windowHeight = window.innerHeight;
        const revealTop = section.getBoundingClientRect().top;

        if(revealTop < windowHeight - 100){
            section.classList.add('active');
        }
    });
}

window.addEventListener('scroll', revealSections);
window.addEventListener('load', revealSections);

window.addEventListener('scroll', () => {

    const navbar =
    document.getElementById('navbar');

    if(window.scrollY > 50){

        navbar.classList.add('scrolled');

    }else{

        navbar.classList.remove('scrolled');
    }
});

function revealSections(){

    const reveals =
    document.querySelectorAll('.reveal');

    reveals.forEach(section => {

        const windowHeight =
        window.innerHeight;

        const revealTop =
        section.getBoundingClientRect().top;

        if(revealTop < windowHeight - 100){

            section.classList.add('active');
        }
    });
}

window.addEventListener(
    'scroll',
    revealSections
);

window.addEventListener(
    'load',
    revealSections
);

document.addEventListener("DOMContentLoaded", function () {

    var dropdown = document.getElementsByClassName("dropdown-btn");

    for (var i = 0; i < dropdown.length; i++) {

        dropdown[i].addEventListener("click", function () {

            this.classList.toggle("active");

            var dropdownContent = this.nextElementSibling;

            if (dropdownContent.style.display === "block") {

                dropdownContent.style.display = "none";

            } else {

                dropdownContent.style.display = "block";
            }
        });
    }

});