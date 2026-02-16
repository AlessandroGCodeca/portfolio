// ================================================================
// Alessandro Giovanni Codecà - Portfolio Scripts
// ================================================================

// Dark Mode Logic
function toggleTheme() {
    const body = document.body;
    const currentTheme = body.getAttribute('data-theme');
    const newTheme = currentTheme === 'dark' ? 'light' : 'dark';

    body.setAttribute('data-theme', newTheme);
    localStorage.setItem('theme', newTheme);
    updateThemeIcon(newTheme);
}

function updateThemeIcon(theme) {
    const btn = document.getElementById('themeToggle');
    btn.textContent = theme === 'dark' ? '☀️' : '🌙';
}



// Advanced Typing Animation Logic
const roles = [
    "Business Administration Student",
    "Finance Enthusiast",
    "AI Enthusiast",
    "Lifelong Learner",
    "Problem Solver"
];

let roleIndex = 0;
let charIndex = 0;
let isDeleting = false;
let typeSpeed = 50;

function typeRoles(element) {
    const currentRole = roles[roleIndex];

    if (isDeleting) {
        element.innerHTML = currentRole.substring(0, charIndex - 1);
        charIndex--;
        typeSpeed = 30; // Faster deleting
    } else {
        element.innerHTML = currentRole.substring(0, charIndex + 1);
        charIndex++;
        typeSpeed = 80; // Normal typing
    }

    // Ensure cursor is always there
    if (!element.querySelector('.typing-cursor')) {
        const cursor = document.createElement('span');
        cursor.className = 'typing-cursor';
        element.appendChild(cursor);
    }

    if (!isDeleting && charIndex === currentRole.length) {
        // Finished typing word, pause then delete
        typeSpeed = 2000;
        isDeleting = true;
    } else if (isDeleting && charIndex === 0) {
        // Finished deleting, move to next word
        isDeleting = false;
        roleIndex = (roleIndex + 1) % roles.length;
        typeSpeed = 500;
    }

    setTimeout(() => typeRoles(element), typeSpeed);
}

// Simple typewriter for static text (used for translations mainly)
function typeWriter(text, element, speed = 50) {
    let i = 0;
    element.innerHTML = '';
    element.classList.add('typing-active');
    const cursor = document.createElement('span');
    cursor.className = 'typing-cursor';
    element.appendChild(cursor);

    function type() {
        if (i < text.length) {
            cursor.before(text.charAt(i));
            i++;
            setTimeout(type, speed);
        } else {
            setTimeout(() => cursor.remove(), 2000);
        }
    }
    type();
}

// Dropdown Logic
function toggleLanguageMenu() {
    const menu = document.getElementById('langMenu');
    menu.classList.toggle('show');
}

// Close dropdown when clicking outside
window.onclick = function (event) {
    if (!event.target.matches('.lang-toggle') && !event.target.closest('.lang-toggle')) {
        const dropdowns = document.getElementsByClassName("lang-menu");
        for (let i = 0; i < dropdowns.length; i++) {
            const openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function switchLanguage(lang) {
    const t = translations[lang];

    // Update Dropdown Button UI
    document.getElementById('currentLangFlag').textContent = t.flag;
    document.getElementById('currentLangName').textContent = t.name;

    // Close menu
    document.getElementById('langMenu').classList.remove('show');

    // Update content
    // Handle typing animation for subtitle if language changes
    const subtitleEl = document.querySelector('.subtitle');
    if (subtitleEl.textContent !== t.subtitle + " ") {
        typeWriter(t.subtitle, subtitleEl, 30);
    }

    // Update UI text
    const elements = {
        'profile': t.profile,
        'workExperience': t.workExperience,
        'education': t.education,
        'languages': t.languages,
        'skills': t.skills,
        'certifications': t.certifications,
        'sendMessage': t.sendMessage,
        'navProfile': t.navProfile,
        'navExperience': t.navExperience,
        'navEducation': t.navEducation,
        'contact': t.contact
    };

    for (let key in elements) {
        const el = document.querySelector(`[data-translate="${key}"]`);
        if (el) el.textContent = elements[key];
    }

    document.querySelector('.bio').textContent = t.profileText;

    // Save preference
    localStorage.setItem('preferredLanguage', lang);
}

// Mobile Menu Functions
function toggleMobileMenu() {
    const navLinks = document.getElementById('navLinks');
    const hamburger = document.getElementById('mobileMenuBtn');
    const isExpanded = hamburger.getAttribute('aria-expanded') === 'true';

    navLinks.classList.toggle('mobile-active');
    hamburger.classList.toggle('active');
    hamburger.setAttribute('aria-expanded', !isExpanded);
}

function closeMobileMenu() {
    const navLinks = document.getElementById('navLinks');
    const hamburger = document.getElementById('mobileMenuBtn');

    navLinks.classList.remove('mobile-active');
    hamburger.classList.remove('active');
    hamburger.setAttribute('aria-expanded', 'false');
}

// Copy Email Function
function copyEmail() {
    const email = 'alessandro.codeca@outlook.com';
    navigator.clipboard.writeText(email).then(() => {
        const tooltip = document.getElementById('copyTooltip');
        tooltip.classList.add('show');
        setTimeout(() => {
            tooltip.classList.remove('show');
        }, 2000);
    });
}

// Toast Notification Function
function showToast() {
    const toast = document.getElementById('successToast');
    toast.classList.add('show');
    setTimeout(() => {
        toast.classList.remove('show');
    }, 5000);
}

/* ====================================================================
   SECURITY MODULE (OWASP Best Practices)
   
   Implements client-side security features for static sites:
   - Rate limiting with localStorage tracking
   - Schema-based input validation
   - XSS sanitization
   - Honeypot bot protection
   
   Note: This is defense-in-depth for static sites. Formspree also
   provides server-side spam protection. These measures provide
   additional security and user experience improvements.
   ==================================================================== */
const SecurityModule = {

    // ================================================================
    // CONFIGURATION
    // Adjust these values to tune rate limiting behavior
    // ================================================================
    config: {
        // Rate limit: max submissions per time window
        maxSubmissions: 3,
        // Time window in milliseconds (5 minutes)
        timeWindow: 5 * 60 * 1000,
        // Storage key for rate limit data
        storageKey: 'formRateLimit',
        // Input validation schemas
        validation: {
            name: {
                minLength: 1,
                maxLength: 100,
                // Allow letters, spaces, hyphens, apostrophes, periods (international names)
                pattern: /^[\p{L}\s\-'.]+$/u,
                errorRequired: 'Please enter your name.',
                errorInvalid: 'Name contains invalid characters.',
                errorLength: 'Name must be under 100 characters.'
            },
            email: {
                minLength: 5,
                maxLength: 254,
                // Simplified RFC 5322 email pattern
                pattern: /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$/,
                errorRequired: 'Please enter your email address.',
                errorInvalid: 'Please enter a valid email address.',
                errorLength: 'Email must be under 254 characters.'
            },
            message: {
                minLength: 1,
                maxLength: 5000,
                // Allow most printable characters and newlines
                pattern: null, // Will sanitize instead
                errorRequired: 'Please enter a message.',
                errorLength: 'Message must be under 5000 characters.'
            }
        }
    },

    // ================================================================
    // RATE LIMITING
    // Prevents rapid-fire form submissions (OWASP rate limiting)
    // Uses localStorage to track submission timestamps
    // ================================================================

    /**
     * Get rate limit data from localStorage
     * @returns {Object} Rate limit data with submissions array
     */
    getRateLimitData() {
        try {
            const data = localStorage.getItem(this.config.storageKey);
            return data ? JSON.parse(data) : { submissions: [] };
        } catch (e) {
            console.warn('SecurityModule: localStorage unavailable');
            return { submissions: [] };
        }
    },

    /**
     * Save rate limit data to localStorage
     * @param {Object} data - Rate limit data to save
     */
    setRateLimitData(data) {
        try {
            localStorage.setItem(this.config.storageKey, JSON.stringify(data));
        } catch (e) {
            console.warn('SecurityModule: Could not save rate limit data');
        }
    },

    /**
     * Check if user is rate limited
     * @returns {Object} { limited: boolean, resetIn: milliseconds }
     */
    checkRateLimit() {
        const now = Date.now();
        const data = this.getRateLimitData();

        // Filter out expired submissions (outside time window)
        const recentSubmissions = data.submissions.filter(
            timestamp => now - timestamp < this.config.timeWindow
        );

        // Update stored data with only recent submissions
        this.setRateLimitData({ submissions: recentSubmissions });

        if (recentSubmissions.length >= this.config.maxSubmissions) {
            // Calculate time until oldest submission expires
            const oldestSubmission = Math.min(...recentSubmissions);
            const resetIn = (oldestSubmission + this.config.timeWindow) - now;
            return { limited: true, resetIn: Math.max(0, resetIn) };
        }

        return { limited: false, resetIn: 0 };
    },

    /**
     * Record a new form submission attempt
     */
    recordSubmission() {
        const data = this.getRateLimitData();
        data.submissions.push(Date.now());
        this.setRateLimitData(data);
    },

    /**
     * Format milliseconds as human-readable countdown
     * @param {number} ms - Milliseconds
     * @returns {string} Formatted time string
     */
    formatCountdown(ms) {
        const seconds = Math.ceil(ms / 1000);
        if (seconds < 60) return `${seconds} seconds`;
        const minutes = Math.ceil(seconds / 60);
        return `${minutes} minute${minutes !== 1 ? 's' : ''}`;
    },

    // ================================================================
    // XSS SANITIZATION
    // Escapes HTML entities to prevent script injection
    // (OWASP XSS Prevention Cheat Sheet)
    // ================================================================

    /**
     * Sanitize string by escaping HTML entities
     * @param {string} str - Input string to sanitize
     * @returns {string} Sanitized string
     */
    sanitizeHTML(str) {
        if (typeof str !== 'string') return '';

        const htmlEntities = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;',
            "'": '&#x27;',
            '/': '&#x2F;',
            '`': '&#x60;',
            '=': '&#x3D;'
        };

        return str.replace(/[&<>"'`=/]/g, char => htmlEntities[char]);
    },

    /**
     * Remove potentially dangerous patterns from input
     * @param {string} str - Input string
     * @returns {string} Cleaned string
     */
    cleanInput(str) {
        if (typeof str !== 'string') return '';

        // Remove null bytes
        str = str.replace(/\0/g, '');

        // Trim whitespace
        str = str.trim();

        return str;
    },

    // ================================================================
    // INPUT VALIDATION
    // Schema-based validation with type checks and length limits
    // (OWASP Input Validation Cheat Sheet)
    // ================================================================

    /**
     * Validate a single field against its schema
     * @param {string} fieldName - Name of the field
     * @param {string} value - Value to validate
     * @returns {Object} { valid: boolean, error: string|null }
     */
    validateField(fieldName, value) {
        const schema = this.config.validation[fieldName];
        if (!schema) return { valid: true, error: null };

        // Clean the input first
        const cleaned = this.cleanInput(value);

        // Check required (empty after cleaning)
        if (cleaned.length < schema.minLength) {
            return { valid: false, error: schema.errorRequired };
        }

        // Check max length
        if (cleaned.length > schema.maxLength) {
            return { valid: false, error: schema.errorLength };
        }

        // Check pattern (if defined)
        if (schema.pattern && !schema.pattern.test(cleaned)) {
            return { valid: false, error: schema.errorInvalid };
        }

        return { valid: true, error: null };
    },

    /**
     * Validate all form fields
     * @param {Object} fields - Object with field names as keys
     * @returns {Object} { valid: boolean, errors: {fieldName: error} }
     */
    validateForm(fields) {
        const errors = {};
        let valid = true;

        for (const [fieldName, value] of Object.entries(fields)) {
            const result = this.validateField(fieldName, value);
            if (!result.valid) {
                valid = false;
                errors[fieldName] = result.error;
            }
        }

        return { valid, errors };
    },

    // ================================================================
    // HONEYPOT PROTECTION
    // Hidden field that bots typically fill out
    // (OWASP Bot Detection)
    // ================================================================

    /**
     * Check if honeypot field was filled (indicates bot)
     * @param {string} honeypotValue - Value of honeypot field
     * @returns {boolean} True if likely a bot
     */
    checkHoneypot(honeypotValue) {
        // If honeypot has any value, it's likely a bot
        return honeypotValue && honeypotValue.trim().length > 0;
    }
};

// ================================================================
// FORM SUBMISSION HANDLER
// Integrates all security features with the contact form
// ================================================================
document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('contactForm');
    if (!form) return;

    const submitBtn = document.getElementById('submitBtn');
    const rateLimitWarning = document.getElementById('rateLimitWarning');
    const countdownEl = document.getElementById('rateLimitCountdown');

    let countdownInterval = null;

    /**
     * Show validation error for a field
     */
    function showFieldError(fieldName, message) {
        const group = document.getElementById(fieldName).closest('.form-group');
        const errorEl = document.getElementById(`${fieldName}-error`);

        group.classList.add('has-error');
        errorEl.textContent = message;
        errorEl.classList.add('show');
    }

    /**
     * Clear validation error for a field
     */
    function clearFieldError(fieldName) {
        const group = document.getElementById(fieldName).closest('.form-group');
        const errorEl = document.getElementById(`${fieldName}-error`);

        group.classList.remove('has-error');
        errorEl.textContent = '';
        errorEl.classList.remove('show');
    }

    /**
     * Clear all validation errors
     */
    function clearAllErrors() {
        ['name', 'email', 'message'].forEach(clearFieldError);
    }

    /**
     * Update rate limit UI
     */
    function updateRateLimitUI(limited, resetIn) {
        if (limited) {
            rateLimitWarning.classList.add('show');
            submitBtn.disabled = true;
            submitBtn.style.opacity = '0.5';
            submitBtn.style.cursor = 'not-allowed';

            // Update countdown
            countdownEl.textContent = SecurityModule.formatCountdown(resetIn);

            // Clear any existing interval
            if (countdownInterval) clearInterval(countdownInterval);

            // Start countdown timer
            const endTime = Date.now() + resetIn;
            countdownInterval = setInterval(() => {
                const remaining = endTime - Date.now();
                if (remaining <= 0) {
                    clearInterval(countdownInterval);
                    rateLimitWarning.classList.remove('show');
                    submitBtn.disabled = false;
                    submitBtn.style.opacity = '';
                    submitBtn.style.cursor = '';
                } else {
                    countdownEl.textContent = SecurityModule.formatCountdown(remaining);
                }
            }, 1000);
        } else {
            rateLimitWarning.classList.remove('show');
            submitBtn.disabled = false;
            submitBtn.style.opacity = '';
            submitBtn.style.cursor = '';
        }
    }

    // Check rate limit on page load
    const initialCheck = SecurityModule.checkRateLimit();
    if (initialCheck.limited) {
        updateRateLimitUI(true, initialCheck.resetIn);
    }

    // Real-time validation on input blur
    ['name', 'email', 'message'].forEach(fieldName => {
        const input = document.getElementById(fieldName);
        if (input) {
            input.addEventListener('blur', () => {
                const result = SecurityModule.validateField(fieldName, input.value);
                if (!result.valid) {
                    showFieldError(fieldName, result.error);
                } else {
                    clearFieldError(fieldName);
                }
            });

            // Clear error when user starts typing
            input.addEventListener('input', () => {
                clearFieldError(fieldName);
            });
        }
    });

    // Form submission handler
    form.addEventListener('submit', function (e) {
        // Always prevent default first - we'll submit programmatically if valid
        e.preventDefault();

        clearAllErrors();

        // 1. Check honeypot (bot protection)
        const honeypotValue = document.getElementById('website').value;
        if (SecurityModule.checkHoneypot(honeypotValue)) {
            // Silently reject bot submissions
            // Show fake success to confuse bots
            console.log('SecurityModule: Honeypot triggered');
            showToast();
            form.reset();
            return;
        }

        // 2. Check rate limit
        const rateCheck = SecurityModule.checkRateLimit();
        if (rateCheck.limited) {
            updateRateLimitUI(true, rateCheck.resetIn);
            return;
        }

        // 3. Validate all fields
        const formData = {
            name: document.getElementById('name').value,
            email: document.getElementById('email').value,
            message: document.getElementById('message').value
        };

        const validation = SecurityModule.validateForm(formData);

        if (!validation.valid) {
            // Show all validation errors
            for (const [field, error] of Object.entries(validation.errors)) {
                showFieldError(field, error);
            }
            // Focus first field with error
            const firstErrorField = Object.keys(validation.errors)[0];
            document.getElementById(firstErrorField).focus();
            return;
        }

        // 4. Sanitize inputs before submission
        document.getElementById('name').value = SecurityModule.sanitizeHTML(formData.name);
        document.getElementById('message').value = SecurityModule.sanitizeHTML(formData.message);
        // Note: Email is not HTML-sanitized to preserve valid email format

        // 5. Record submission for rate limiting
        SecurityModule.recordSubmission();

        // 6. Submit the form to Formspree
        // Using fetch for better control over success/error handling
        const submitData = new FormData(form);

        submitBtn.disabled = true;
        submitBtn.textContent = 'Sending...';

        fetch(form.action, {
            method: 'POST',
            body: submitData,
            headers: {
                'Accept': 'application/json'
            }
        })
            .then(response => {
                if (response.ok) {
                    showToast();
                    form.reset();
                } else {
                    throw new Error('Submission failed');
                }
            })
            .catch(error => {
                console.error('Form submission error:', error);
                // Show error toast (reuse existing toast with different message)
                const toast = document.getElementById('successToast');
                toast.querySelector('span:last-child').textContent = 'Failed to send. Please try again.';
                toast.style.background = '#DC2626';
                toast.classList.add('show');
                setTimeout(() => {
                    toast.classList.remove('show');
                    toast.querySelector('span:last-child').textContent = 'Message sent successfully!';
                    toast.style.background = '';
                }, 5000);
            })
            .finally(() => {
                submitBtn.disabled = false;
                submitBtn.textContent = 'Send Message';

                // Check if now rate limited
                const postCheck = SecurityModule.checkRateLimit();
                if (postCheck.limited) {
                    updateRateLimitUI(true, postCheck.resetIn);
                }
            });
    });
});

// Scroll Progress & Back to Top
window.onscroll = function () {
    // Progress Bar
    let winScroll = document.body.scrollTop || document.documentElement.scrollTop;
    let height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
    let scrolled = (winScroll / height) * 100;
    document.getElementById("progressBar").style.width = scrolled + "%";

    // Back to Top Button
    const backToTopBtn = document.querySelector('.back-to-top');
    if (document.body.scrollTop > 300 || document.documentElement.scrollTop > 300) {
        backToTopBtn.classList.add('visible');
    } else {
        backToTopBtn.classList.remove('visible');
    }
};

// Initialization
window.addEventListener('DOMContentLoaded', () => {
    // Theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.body.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    // Language
    const savedLang = localStorage.getItem('preferredLanguage') || 'en';
    if (savedLang !== 'en') {
        switchLanguage(savedLang);
    } else {
        // Start infinite typing animation for default language
        const subtitle = document.querySelector('.subtitle');
        if (subtitle) {
            // Clear initial text to start animation clean
            subtitle.innerHTML = '';
            typeRoles(subtitle);
        }
    }

    // Scroll Animation Observer Setup
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -50px 0px"
    };

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('active');
                observer.unobserve(entry.target);
            }
        });
    }, observerOptions);

    document.querySelectorAll('section, .timeline-item, .sidebar-section').forEach(el => {
        el.classList.add('reveal');
        observer.observe(el);
    });

    // Observe Progress Bars independently
    const barObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const el = entry.target;
                // Animate width
                el.style.width = el.getAttribute('data-width');
                barObserver.unobserve(el);
            }
        });
    }, observerOptions);

    document.querySelectorAll('.progress-fill').forEach(el => {
        // Store original width from inline style
        const targetWidth = el.style.width;
        // Set to 0 initially
        el.style.width = '0%';
        el.setAttribute('data-width', targetWidth);
        barObserver.observe(el);
    });

    // Initialize Particles
    initParticles();

    // Initialize 3D Tilt
    if (window.matchMedia("(min-width: 769px)").matches) {
        initTilt();
    }

    // Init Final Polish
    initMagneticButtons();
    initStaggeredReveals();
});

// Particle Network Logic
function initParticles() {
    const canvas = document.getElementById('particles');
    const ctx = canvas.getContext('2d');
    let width, height;
    let particles = [];

    // Resize handling
    function resize() {
        width = canvas.width = canvas.parentElement.offsetWidth;
        height = canvas.height = canvas.parentElement.offsetHeight;
    }
    window.addEventListener('resize', resize);
    resize();

    // Mouse tracking
    let mouse = { x: null, y: null };
    document.querySelector('header').addEventListener('mousemove', (e) => {
        const rect = canvas.getBoundingClientRect();
        mouse.x = e.clientX - rect.left;
        mouse.y = e.clientY - rect.top;
    });
    document.querySelector('header').addEventListener('mouseleave', () => {
        mouse.x = null;
        mouse.y = null;
    });

    // Particle Class
    class Particle {
        constructor() {
            this.x = Math.random() * width;
            this.y = Math.random() * height;
            this.vx = (Math.random() - 0.5) * 0.5;
            this.vy = (Math.random() - 0.5) * 0.5;
            this.size = Math.random() * 2 + 1;
            this.color = getComputedStyle(document.body).getPropertyValue('--text-light').trim();
        }

        update() {
            this.x += this.vx;
            this.y += this.vy;

            // Bounce edges
            if (this.x < 0 || this.x > width) this.vx *= -1;
            if (this.y < 0 || this.y > height) this.vy *= -1;
        }

        draw() {
            ctx.fillStyle = this.color;
            ctx.beginPath();
            ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
            ctx.fill();
        }
    }

    // Create particles
    for (let i = 0; i < 60; i++) {
        particles.push(new Particle());
    }

    // Animation Loop
    function animate() {
        ctx.clearRect(0, 0, width, height);

        // Update particles
        particles.forEach(p => {
            p.update();
            p.draw();
        });

        // Connect particles
        connectParticles();

        requestAnimationFrame(animate);
    }

    function connectParticles() {
        const maxDist = 120;
        for (let a = 0; a < particles.length; a++) {
            for (let b = a; b < particles.length; b++) {
                const dx = particles[a].x - particles[b].x;
                const dy = particles[a].y - particles[b].y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < maxDist) {
                    ctx.strokeStyle = `rgba(100, 116, 139, ${1 - dist / maxDist})`;
                    ctx.lineWidth = 0.5;
                    ctx.beginPath();
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(particles[b].x, particles[b].y);
                    ctx.stroke();
                }
            }

            // Connect to mouse
            if (mouse.x) {
                const dx = particles[a].x - mouse.x;
                const dy = particles[a].y - mouse.y;
                const dist = Math.sqrt(dx * dx + dy * dy);

                if (dist < 150) {
                    ctx.strokeStyle = `rgba(59, 130, 246, ${1 - dist / 150})`; // Blue connection
                    ctx.lineWidth = 0.8;
                    ctx.beginPath();
                    ctx.moveTo(particles[a].x, particles[a].y);
                    ctx.lineTo(mouse.x, mouse.y);
                    ctx.stroke();
                }
            }
        }
    }

    animate();
}

// 3D Tilt Logic
function initTilt() {
    const cards = document.querySelectorAll('.timeline-item, .sidebar-section, .cert-item');

    cards.forEach(card => {
        card.classList.add('tilt-card');

        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            const x = e.clientX - rect.left; // x position within the element.
            const y = e.clientY - rect.top;  // y position within the element.

            const centerX = rect.width / 2;
            const centerY = rect.height / 2;

            const rotateX = ((y - centerY) / centerY) * -3; // Max rotation deg
            const rotateY = ((x - centerX) / centerX) * 3;

            card.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.01, 1.01, 1.01)`;

            // Add glare effect if desired (simple version)
            // card.style.background = `radial-gradient(circle at ${x}px ${y}px, rgba(255,255,255,0.1), transparent)`;
        });

        card.addEventListener('mouseleave', () => {
            card.style.transform = 'perspective(1000px) rotateX(0) rotateY(0) scale3d(1, 1, 1)';
            // card.style.background = ''; // Reset background
        });
    });
}

// Magnetic Button Logic
function initMagneticButtons() {
    const buttons = document.querySelectorAll('.submit-btn, .social-links a, .lang-toggle, .back-to-top');

    buttons.forEach(btn => {
        btn.classList.add('magnetic');

        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            const x = e.clientX - rect.left - rect.width / 2;
            const y = e.clientY - rect.top - rect.height / 2;

            // Magnetic pull strength
            btn.style.transform = `translate(${x * 0.3}px, ${y * 0.3}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            btn.style.transform = 'translate(0, 0)';
        });
    });
}

// Staggered Reveal Logic
function initStaggeredReveals() {
    const observerOptions = {
        threshold: 0.1,
        rootMargin: "0px 0px -30px 0px"
    };

    const staggerObserver = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const parent = entry.target;
                const children = parent.querySelectorAll('.stagger-hidden');

                children.forEach((child, index) => {
                    setTimeout(() => {
                        child.classList.add('stagger-visible');
                    }, index * 100); // 100ms delay between each item
                });

                staggerObserver.unobserve(parent);
            }
        });
    }, observerOptions);

    // Observe containers (Timeline & Skills)
    document.querySelectorAll('.timeline-group, .skill-category').forEach(group => {
        const children = group.querySelectorAll('.timeline-item, .skill-item');
        children.forEach(child => child.classList.add('stagger-hidden'));
        staggerObserver.observe(group);
    });
}

// Live Time
function updateTime() {
    const timeEl = document.getElementById('localTime');
    if (timeEl) {
        const now = new Date();
        timeEl.textContent = now.toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit', timeZone: 'Europe/Prague' });
    }
}
setInterval(updateTime, 1000);
updateTime();

// Active Navigation Logic
function initActiveNav() {
    const sections = document.querySelectorAll('section');
    const navLinks = document.querySelectorAll('.nav-link');

    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const id = entry.target.getAttribute('id');
                // Optional: skip if ID is null
                if (!id) return;

                navLinks.forEach(link => {
                    link.classList.remove('active');
                    if (link.getAttribute('href') === '#' + id) {
                        link.classList.add('active');
                    }
                });
            }
        });
    }, { threshold: 0.4 }); // Trigger when 40% visible

    sections.forEach(section => observer.observe(section));
}

// Init Interactive Features
window.addEventListener('scroll', () => {
    // Handled by observer mostly, but active nav fallback can act here 
});

initActiveNav();


// Dynamic Greeting
function updateGreeting() {
    const hour = new Date().getHours();
    const greetingEl = document.getElementById('greeting');
    if (greetingEl) {
        if (hour < 12) greetingEl.textContent = 'Good Morning,';
        else if (hour < 18) greetingEl.textContent = 'Good Afternoon,';
        else greetingEl.textContent = 'Good Evening,';
    }
}
updateGreeting();

// Console Easter Egg
console.log(
    "%c Alessandro G. Codecà %c \nStudent & Business Professional",
    "font-family: 'Outfit'; font-size: 24px; font-weight: bold; color: #3B82F6;",
    "font-family: 'Inter'; font-size: 14px; color: #64748B;"
);
console.log(
    "%cFound the code? Let's talk strategy: alessandro.codeca@outlook.com",
    "background: #0F172A; color: #fff; padding: 10px 20px; border-radius: 5px; font-family: 'Courier New';"
);
