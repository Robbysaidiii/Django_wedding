document.addEventListener("DOMContentLoaded", function () {
    const navLinks = document.querySelectorAll(".navbar-nav .nav-link");
    const navbarCollapse = document.querySelector(".navbar-collapse");

    navLinks.forEach(function (link) {
        link.addEventListener("click", function () {
            if (navbarCollapse.classList.contains("show")) {
                new bootstrap.Collapse(navbarCollapse).hide();
            }
        });
    });
});


const music = document.getElementById("bg-music");
const btn = document.getElementById("music-btn");

// coba unmute & play ulang
window.addEventListener("load", () => {
    music.muted = false;

    const playPromise = music.play();
    if (playPromise !== undefined) {
        playPromise
            .then(() => {
                btn.classList.add("playing");
            })
            .catch(() => {
                console.log("Autoplay diblok browser, nunggu klik user");
            });
    }
});

function toggleMusic() {
    if (music.paused) {
        music.muted = false;
        music.play();
        btn.classList.add("playing");
    } else {
        music.pause();
        btn.classList.remove("playing");
    }
}

