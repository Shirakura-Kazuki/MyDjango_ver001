let slideIndex = 0;
let slides, dots;

document.addEventListener("DOMContentLoaded", function () {
    slides = document.getElementsByClassName("slide");
    dots = document.getElementsByClassName("dot");

    showSlides(slideIndex);

    // 3秒ごとに自動スライド
    setInterval(nextSlide, 3000);
});

// スライドの表示を更新する関数
function showSlides(n) {
    if (!slides || slides.length === 0) return;

    if (n >= slides.length) {
        slideIndex = 0;
    } else if (n < 0) {
        slideIndex = slides.length - 1;
    } else {
        slideIndex = n;
    }

    // すべてのスライドを非表示にする
    for (let i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }

    // すべてのドットのアクティブを解除
    if (dots) {
        for (let i = 0; i < dots.length; i++) {
            dots[i].classList.remove("active");
        }
    }

    // 現在のスライドとドットを表示
    slides[slideIndex].style.display = "block";
    if (dots && dots[slideIndex]) {
        dots[slideIndex].classList.add("active");
    }
}

// 次のスライドに移動
function nextSlide() {
    showSlides(slideIndex + 1);
}

// 前のスライドに移動
function prevSlide() {
    showSlides(slideIndex - 1);
}

// ドットをクリックしたときのスライド変更
function setSlide(n) {
    showSlides(n);
}





