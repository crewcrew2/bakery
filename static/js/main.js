document.addEventListener('DOMContentLoaded', function () { /* на глпвной странице всплывает надпись!! */
console.log("test commit");
    const title = document.querySelector('.hero-title');

    if (title) {
        title.style.opacity = '0';

        setTimeout(() => {
            title.style.transition = 'opacity 3.8s';
            title.style.opacity = '1';
        }, 200);
    }
});


if (document.querySelector('.about-page')) {
    const aboutImage = document.querySelector('.about-image img');

    if (aboutImage) {
        
        aboutImage.style.transition = 'transform 0.3s ease';

        aboutImage.addEventListener('mouseenter', () => {
            aboutImage.style.transform = 'scale(1.15)';   
        });

        aboutImage.addEventListener('mouseleave', () => {
            aboutImage.style.transform = 'scale(1)'; 
        });
    }
}