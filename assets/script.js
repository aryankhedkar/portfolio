// Mobile nav toggling
const hamburger = document.getElementById('hamburger');
const mobileNav = document.getElementById('mobileNav');

function toggleMobileNav() {
  mobileNav.classList.toggle('open');
}
hamburger.addEventListener('click', toggleMobileNav);

// Close nav when link clicked
document.querySelectorAll('a[data-toggle-nav="true"]').forEach(link => {
  link.addEventListener('click', () => {
    mobileNav.classList.remove('open');
  });
});

// Scroll down button
const scrollDownBtn = document.getElementById('scrollDownBtn');
if (scrollDownBtn) {
  scrollDownBtn.addEventListener('click', () => {
    document.getElementById('About').scrollIntoView({ behavior: 'smooth' });
  });
}

// Back to top button
const backToTopBtn = document.getElementById('backToTop');
window.addEventListener('scroll', () => {
  if (window.scrollY > 300) {
    backToTopBtn.classList.add('show');
  } else {
    backToTopBtn.classList.remove('show');
  }
});
backToTopBtn.addEventListener('click', () => {
  window.scrollTo({ top: 0, behavior: 'smooth' });
});

// Testimonials carousel
let currentSlide = 1;
const totalSlides = 3;

function showSlide(n) {
  currentSlide = n;
  for (let i = 1; i <= totalSlides; i++) {
    document.getElementById('slide' + i).classList.remove('active');
  }
  document.getElementById('slide' + currentSlide).classList.add('active');
}

// Hook up testimonial nav buttons
document.querySelectorAll('.testimonial-nav button').forEach(btn => {
  btn.addEventListener('click', () => {
    const slideNum = btn.getAttribute('data-slide-num');
    showSlide(parseInt(slideNum, 10));
  });
});

// Initialize
showSlide(1);
