document.addEventListener("DOMContentLoaded", function() {
    const galleryThumbs = new Swiper('.gallery-thumbs', {
      slidesPerView: 4,
      spaceBetween: 10,
      freeMode: true,
      watchSlidesVisibility: true,
      watchSlidesProgress: true,
    });
  
    const galleryTop = new Swiper('.swiper-container', {
    //   spaceBetween: 5, // Уменьшили отступы
      slidesPerView: 1,
      navigation: {
        nextEl: '.swiper-button-next',
        prevEl: '.swiper-button-prev',
      },
      thumbs: {
        swiper: galleryThumbs,
      },
    });
  });
