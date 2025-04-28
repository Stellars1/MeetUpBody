// Sayfa Geçiş Animasyonları
document.addEventListener('DOMContentLoaded', function() {
    const content = document.querySelector('.container');
    content.classList.add('fade-in');
});

// Loading Spinner
function showLoading() {
    const spinner = document.createElement('div');
    spinner.className = 'loading-spinner';
    document.body.appendChild(spinner);
}

function hideLoading() {
    const spinner = document.querySelector('.loading-spinner');
    if (spinner) {
        spinner.remove();
    }
}

// Smooth Scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});

// Hover Efektleri
document.querySelectorAll('.card').forEach(card => {
    card.addEventListener('mouseenter', function() {
        this.classList.add('shadow');
    });
    
    card.addEventListener('mouseleave', function() {
        this.classList.remove('shadow');
    });
}); 