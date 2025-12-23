document.addEventListener('DOMContentLoaded', function () { /* на глпвной странице всплывает надпись!! */

    const title = document.querySelector('.hero-title');

    if (title) {
        title.style.opacity = '0';

        setTimeout(() => {
            title.style.transition = 'opacity 3.8s';
            title.style.opacity = '1';
        }, 200);
    }
});
