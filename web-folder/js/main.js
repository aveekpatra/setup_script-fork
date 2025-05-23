// Enhanced Casino Website - Base JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('🎰 Enhanced casino website loaded');
    
    // Initialize all components
    initializeAllComponents();
    
    // Setup global handlers
    setupGlobalHandlers();
    
    // Setup theme system
    setupThemeSystem();
});

function initializeAllComponents() {
    console.log('🔧 Initializing enhanced components...');
    // Component initialization functions will be called here
}

function setupGlobalHandlers() {
    // Global keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            // Close any open menus
            document.querySelectorAll('.mobile-nav.active').forEach(nav => {
                nav.classList.remove('active');
            });
        }
    });
    
    // Smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

function setupThemeSystem() {
    // Add dynamic theme switching capabilities
    const root = document.documentElement;
    
    // Theme animation support
    function animateThemeChange() {
        root.style.setProperty('--transition', 'all 0.3s ease');
        setTimeout(() => {
            root.style.removeProperty('--transition');
        }, 300);
    }
    
    // Expose theme utilities globally
    window.casinoTheme = {
        animate: animateThemeChange
    };
}

// Component scripts will be appended below


// Component Script
// Modern Header JavaScript
function initHeaderModern() {
    const mobileToggle = document.querySelector('.mobile-menu-toggle');
    const mainNav = document.querySelector('.main-nav');
    
    if (mobileToggle && mainNav) {
        mobileToggle.addEventListener('click', function() {
            mainNav.classList.toggle('active');
        });
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeaderModern);
} else {
    initHeaderModern();
}

// Component Script
// Welcome Hero JavaScript
function initHeroWelcome() {
    // Add interactive animations
    const heroTitle = document.querySelector('.hero-title');
    if (heroTitle) {
        heroTitle.addEventListener('mouseover', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        heroTitle.addEventListener('mouseout', function() {
            this.style.transform = 'scale(1)';
        });
    }
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initHeroWelcome);
} else {
    initHeroWelcome();
}

// Component Script
// Comprehensive Footer JavaScript
function initFooterComprehensive() {
    console.log('Footer comprehensive variant initialized');
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFooterComprehensive);
} else {
    initFooterComprehensive();
}