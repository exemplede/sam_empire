/* ============================================================
   SAM EMPIRE - Main JavaScript
   ============================================================ */

document.addEventListener('DOMContentLoaded', () => {

    // --- Preloader ---
    const preloader = document.getElementById('preloader');
    window.addEventListener('load', () => {
        setTimeout(() => {
            preloader.classList.add('loaded');
            setTimeout(() => preloader.remove(), 600);
        }, 800);
    });

    // --- Navbar Scroll ---
    const navbar = document.querySelector('.navbar');
    const scrollTop = document.querySelector('.scroll-top');
    
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY;
        
        if (scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
        
        if (scrollY > 400) {
            scrollTop.classList.add('visible');
        } else {
            scrollTop.classList.remove('visible');
        }
    });

    // --- Scroll to Top ---
    scrollTop.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });

    // --- Mobile Menu ---
    const burger = document.querySelector('.nav-burger');
    const navLinks = document.querySelector('.nav-links');
    
    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        navLinks.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });
    
    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            burger.classList.remove('active');
            navLinks.classList.remove('active');
            document.body.style.overflow = '';
        });
    });

    // --- Active Nav Link ---
    const sections = document.querySelectorAll('section[id]');
    
    window.addEventListener('scroll', () => {
        const scrollY = window.scrollY + 100;
        
        sections.forEach(section => {
            const sectionTop = section.offsetTop;
            const sectionHeight = section.offsetHeight;
            const sectionId = section.getAttribute('id');
            const navLink = document.querySelector(`.nav-links a[href="#${sectionId}"]`);
            
            if (navLink) {
                if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
                    navLink.classList.add('active');
                } else {
                    navLink.classList.remove('active');
                }
            }
        });
    });

    // --- Scroll Reveal ---
    const revealElements = document.querySelectorAll('.reveal');
    
    const revealOnScroll = () => {
        revealElements.forEach(el => {
            const elementTop = el.getBoundingClientRect().top;
            const windowHeight = window.innerHeight;
            
            if (elementTop < windowHeight - 80) {
                el.classList.add('active');
            }
        });
    };
    
    window.addEventListener('scroll', revealOnScroll);
    revealOnScroll();

    // --- Counter Animation ---
    const counters = document.querySelectorAll('.hero-stat-number[data-count]');
    let counted = false;
    
    const animateCounters = () => {
        if (counted) return;
        
        counters.forEach(counter => {
            const target = parseInt(counter.getAttribute('data-count'));
            const suffix = counter.getAttribute('data-suffix') || '';
            const duration = 2000;
            const step = target / (duration / 16);
            let current = 0;
            
            const updateCounter = () => {
                current += step;
                if (current < target) {
                    counter.textContent = Math.floor(current) + suffix;
                    requestAnimationFrame(updateCounter);
                } else {
                    counter.textContent = target + suffix;
                }
            };
            
            updateCounter();
        });
        
        counted = true;
    };
    
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        const observer = new IntersectionObserver((entries) => {
            if (entries[0].isIntersecting) {
                animateCounters();
            }
        }, { threshold: 0.5 });
        observer.observe(heroStats);
    }

    // --- Auto-dismiss alerts ---
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            alert.style.opacity = '0';
            alert.style.transform = 'translateX(100px)';
            setTimeout(() => alert.remove(), 400);
        }, 5000);
    });

    // --- Smooth Scroll for anchor links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });

});
