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