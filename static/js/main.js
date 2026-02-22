/* SAM EMPIRE — Main JS — V4 */
document.addEventListener('DOMContentLoaded', () => {

    // === PRELOADER ===
    const preloader = document.getElementById('preloader');
    window.addEventListener('load', () => {
        setTimeout(() => { preloader.classList.add('loaded'); setTimeout(() => preloader.remove(), 600); }, 800);
    });

    // === NAVBAR ===
    const navbar = document.querySelector('.navbar');
    const scrollTopBtn = document.querySelector('.scroll-top');
    window.addEventListener('scroll', () => {
        navbar.classList.toggle('scrolled', window.scrollY > 50);
        scrollTopBtn.classList.toggle('visible', window.scrollY > 400);
    });
    scrollTopBtn.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

    // === MOBILE MENU ===
    const burger = document.querySelector('.nav-burger');
    const navLinks = document.querySelector('.nav-links');
    burger.addEventListener('click', () => {
        burger.classList.toggle('active');
        navLinks.classList.toggle('active');
        document.body.style.overflow = navLinks.classList.contains('active') ? 'hidden' : '';
    });
    navLinks.querySelectorAll('a').forEach(l => l.addEventListener('click', () => {
        burger.classList.remove('active');
        navLinks.classList.remove('active');
        document.body.style.overflow = '';
    }));

    // === ACTIVE NAV ===
    const sections = document.querySelectorAll('section[id]');
    window.addEventListener('scroll', () => {
        const y = window.scrollY + 100;
        sections.forEach(s => {
            const link = document.querySelector(`.nav-links a[href="#${s.id}"]`);
            if (link) link.classList.toggle('active', y >= s.offsetTop && y < s.offsetTop + s.offsetHeight);
        });
    });

    // === REVEAL ON SCROLL ===
    const revealEls = document.querySelectorAll('.reveal');
    const doReveal = () => revealEls.forEach(el => {
        if (el.getBoundingClientRect().top < window.innerHeight - 80) el.classList.add('active');
    });
    window.addEventListener('scroll', doReveal);
    doReveal();

    // === SERVICE CARDS STAGGER ===
    const serviceCards = document.querySelectorAll('.service-card');
    if (serviceCards.length) {
        const obs = new IntersectionObserver(entries => {
            entries.forEach(e => {
                if (e.isIntersecting) {
                    e.target.parentElement.querySelectorAll('.service-card').forEach((c, i) => {
                        setTimeout(() => c.classList.add('animated'), i * 150);
                    });
                    obs.unobserve(e.target);
                }
            });
        }, { threshold: 0.2 });
        obs.observe(serviceCards[0]);
    }

    // === COUNTER ANIMATION ===
    const counters = document.querySelectorAll('.hero-stat-number[data-count]');
    let counted = false;
    const animateCounters = () => {
        if (counted) return;
        counted = true;
        counters.forEach(c => {
            const target = +c.dataset.count;
            const suffix = c.dataset.suffix || '';
            let cur = 0;
            const step = target / 125;
            const tick = () => { cur += step; if (cur < target) { c.textContent = Math.floor(cur) + suffix; requestAnimationFrame(tick); } else c.textContent = target + suffix; };
            tick();
        });
    };
    const heroStats = document.querySelector('.hero-stats');
    if (heroStats) {
        new IntersectionObserver(e => { if (e[0].isIntersecting) animateCounters(); }, { threshold: 0.5 }).observe(heroStats);
    }

    // === AUTO DISMISS ALERTS ===
    document.querySelectorAll('.alert').forEach(a => {
        setTimeout(() => { a.style.opacity = '0'; a.style.transform = 'translateX(100px)'; setTimeout(() => a.remove(), 400); }, 5000);
    });

    // === SMOOTH SCROLL ===
    document.querySelectorAll('a[href^="#"]').forEach(a => {
        a.addEventListener('click', e => {
            e.preventDefault();
            const t = document.querySelector(a.getAttribute('href'));
            if (t) t.scrollIntoView({ behavior: 'smooth' });
        });
    });

    // =============================================
    // === TEAM CARD-STACK CAROUSEL ===
    // =============================================
    const cards = document.querySelectorAll('.team-card-stack');
    const prevBtn = document.querySelector('.team-nav-prev');
    const nextBtn = document.querySelector('.team-nav-next');
    const modal = document.getElementById('teamModal');
    let activeIndex = 0;

    function positionCards() {
        const total = cards.length;
        cards.forEach((card, i) => {
            card.classList.remove('active');
            let offset = i - activeIndex;
            // Wrap around
            if (offset > Math.floor(total / 2)) offset -= total;
            if (offset < -Math.floor(total / 2)) offset += total;

            const absOffset = Math.abs(offset);
            const translateX = offset * 160;
            const translateZ = -absOffset * 80;
            const rotateY = offset * -8;
            const scale = 1 - absOffset * 0.12;
            const zIndex = total - absOffset;
            const opacity = absOffset > 2 ? 0 : 1 - absOffset * 0.25;

            card.style.transform = `translateX(calc(-50% + ${translateX}px)) translateZ(${translateZ}px) rotateY(${rotateY}deg) scale(${scale})`;
            card.style.zIndex = zIndex;
            card.style.opacity = opacity;
            card.style.left = '50%';
            card.style.top = '50%';
            card.style.marginTop = '-200px';
            card.style.pointerEvents = absOffset === 0 ? 'auto' : 'none';

            if (offset === 0) card.classList.add('active');
        });
    }

    function goNext() {
        activeIndex = (activeIndex + 1) % cards.length;
        positionCards();
    }
    function goPrev() {
        activeIndex = (activeIndex - 1 + cards.length) % cards.length;
        positionCards();
    }

    if (prevBtn && nextBtn) {
        prevBtn.addEventListener('click', goPrev);
        nextBtn.addEventListener('click', goNext);
        positionCards();
    }

    // Open modal on + click
    cards.forEach(card => {
        const plusBtn = card.querySelector('.tc-plus');
        if (plusBtn) {
            plusBtn.addEventListener('click', (e) => {
                e.stopPropagation();
                const modalPhoto = document.getElementById('modalPhoto');
                // Show photo if available, otherwise emoji
                if (card.dataset.photo && card.dataset.photo !== '') {
                    modalPhoto.innerHTML = '<img src="' + card.dataset.photo + '" alt="' + card.dataset.name + '" style="width:120px;height:120px;object-fit:cover;border-radius:50%;border:3px solid var(--primary-blue);" onerror="this.outerHTML=\'' + card.dataset.avatar + '\'">';
                } else {
                    modalPhoto.textContent = card.dataset.avatar;
                }
                document.getElementById('modalName').textContent = card.dataset.name;
                document.getElementById('modalRole').textContent = card.dataset.role;
                document.getElementById('modalBio').textContent = card.dataset.bio;
                // Update social links from data attributes
                const linkedinLink = modal.querySelector('[title="LinkedIn"]');
                const facebookLink = modal.querySelector('[title="Facebook"]');
                if (linkedinLink) linkedinLink.href = card.dataset.linkedin || '#';
                if (facebookLink) facebookLink.href = card.dataset.facebook || '#';
                modal.classList.add('active');
                document.body.style.overflow = 'hidden';
            });
        }
        // Clicking card itself also navigates
        card.addEventListener('click', () => {
            const idx = Array.from(cards).indexOf(card);
            if (idx !== activeIndex) {
                activeIndex = idx;
                positionCards();
            }
        });
    });

    // Close modal
    const closeModal = () => { modal.classList.remove('active'); document.body.style.overflow = ''; };
    document.querySelector('.team-modal-close')?.addEventListener('click', closeModal);
    modal?.addEventListener('click', (e) => { if (e.target === modal) closeModal(); });

    // Keyboard nav for carousel
    document.addEventListener('keydown', (e) => {
        if (e.key === 'ArrowLeft') goPrev();
        if (e.key === 'ArrowRight') goNext();
        if (e.key === 'Escape') closeModal();
    });

    // Touch swipe for carousel
    let touchStartX = 0;
    const wrapper = document.querySelector('.team-cards-wrapper');
    if (wrapper) {
        wrapper.addEventListener('touchstart', e => { touchStartX = e.touches[0].clientX; }, { passive: true });
        wrapper.addEventListener('touchend', e => {
            const diff = touchStartX - e.changedTouches[0].clientX;
            if (Math.abs(diff) > 50) { diff > 0 ? goNext() : goPrev(); }
        }, { passive: true });
    }

    // Auto-rotate carousel every 4s
    let autoRotate = setInterval(goNext, 4000);
    const carouselSection = document.querySelector('.team-carousel');
    if (carouselSection) {
        carouselSection.addEventListener('mouseenter', () => clearInterval(autoRotate));
        carouselSection.addEventListener('mouseleave', () => { autoRotate = setInterval(goNext, 4000); });
    }
});
