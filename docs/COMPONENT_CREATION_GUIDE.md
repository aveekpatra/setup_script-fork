# Component Creation Guide for web-components-v2

## Overview

The `web-components-v2` directory contains modular, reusable components for the Casino Website Generator. Each component supports multiple variants (themes/styles) and integrates seamlessly with the dynamic theming system.

## Directory Structure

```
web-components-v2/
├── header/
│   ├── component.json          # Component configuration
│   ├── modern.html             # HTML for modern variant
│   ├── modern.css              # CSS for modern variant
│   ├── modern.js               # JavaScript for modern variant
│   ├── luxury.html             # HTML for luxury variant
│   ├── luxury.css              # CSS for luxury variant
│   ├── luxury.js               # JavaScript for luxury variant
│   └── ...                     # Additional variants
├── hero/
│   ├── component.json
│   ├── jackpot.html
│   ├── jackpot.css
│   ├── jackpot.js
│   └── ...
└── footer/
    ├── component.json
    ├── comprehensive.html
    ├── comprehensive.css
    ├── comprehensive.js
    └── ...
```

## Component Configuration (component.json)

Every component directory must contain a `component.json` file that defines the component's metadata and variants.

### Basic Structure

```json
{
  "name": "component-name",
  "description": "Brief description of the component's purpose",
  "category": "navigation|content|layout|feature",
  "version": "1.0.0",
  "variants": [
    {
      "name": "variant-name",
      "description": "Description of this specific variant",
      "theme": "modern|luxury|neon|minimal|vintage",
      "html": "variant-name.html",
      "css": "variant-name.css",
      "js": "variant-name.js"
    }
  ],
  "dependencies": [],
  "casino_compliance": {
    "age_verification": true,
    "responsible_gambling": true,
    "legal_notices": true
  }
}
```

### Complete Example

```json
{
  "name": "header",
  "description": "Professional casino header with navigation",
  "category": "navigation",
  "version": "1.0.0",
  "variants": [
    {
      "name": "modern",
      "description": "Modern gradient header with smooth animations",
      "theme": "modern",
      "html": "modern.html",
      "css": "modern.css",
      "js": "modern.js"
    },
    {
      "name": "luxury",
      "description": "Luxury gold header with premium styling",
      "theme": "luxury",
      "html": "luxury.html",
      "css": "luxury.css",
      "js": "luxury.js"
    },
    {
      "name": "neon",
      "description": "Vibrant neon gaming header with glow effects",
      "theme": "neon",
      "html": "neon.html",
      "css": "neon.css",
      "js": "neon.js"
    }
  ],
  "dependencies": [],
  "casino_compliance": {
    "age_verification": true,
    "responsible_gambling": true,
    "legal_notices": true
  }
}
```

## HTML Files

### Structure Requirements

- Use semantic HTML5 elements
- Include proper ARIA attributes for accessibility
- Use CSS custom properties (CSS variables) for theming
- Follow BEM naming convention for CSS classes

### Example Header HTML (modern.html)

```html
<header class="header header--modern" role="banner">
  <div class="container">
    <div class="header__content">
      <!-- Logo -->
      <div class="header__logo">
        <a href="#" class="logo" aria-label="Casino Home">
          <span class="logo__icon">🎰</span>
          <span class="logo__text">Elite Casino</span>
        </a>
      </div>

      <!-- Navigation -->
      <nav class="header__nav" role="navigation" aria-label="Main navigation">
        <ul class="nav-list">
          <li class="nav-item">
            <a href="#games" class="nav-link">Games</a>
          </li>
          <li class="nav-item">
            <a href="#promotions" class="nav-link">Promotions</a>
          </li>
          <li class="nav-item">
            <a href="#vip" class="nav-link">VIP Club</a>
          </li>
          <li class="nav-item">
            <a href="#support" class="nav-link">Support</a>
          </li>
        </ul>
      </nav>

      <!-- User Actions -->
      <div class="header__actions">
        <button class="btn btn-secondary" aria-label="Login">Login</button>
        <button class="btn btn-primary" aria-label="Sign Up">Sign Up</button>
      </div>

      <!-- Mobile Menu Toggle -->
      <button
        class="mobile-toggle"
        aria-label="Toggle mobile menu"
        aria-expanded="false"
      >
        <span class="mobile-toggle__line"></span>
        <span class="mobile-toggle__line"></span>
        <span class="mobile-toggle__line"></span>
      </button>
    </div>
  </div>
</header>
```

### Example Hero HTML (jackpot.html)

```html
<section class="hero hero--jackpot" role="banner">
  <div class="container">
    <div class="hero__content">
      <div class="hero__text">
        <h1 class="hero__title">
          <span class="hero__title-small">Win Big Today</span>
          <span class="hero__title-main">MEGA JACKPOT</span>
          <span class="hero__title-amount" data-jackpot="12500000"
            >$12,500,000</span
          >
        </h1>

        <p class="hero__description">
          Join thousands of winners and claim your share of our progressive
          jackpots. Your fortune awaits!
        </p>

        <div class="hero__actions">
          <button class="btn btn-primary btn-large">Play Now</button>
          <button class="btn btn-secondary btn-large">Learn More</button>
        </div>
      </div>

      <div class="hero__visual">
        <div class="jackpot-display">
          <div class="jackpot-display__coins"></div>
          <div class="jackpot-display__glow"></div>
        </div>
      </div>
    </div>
  </div>
</section>
```

## CSS Files

### Theme Integration

Always use CSS custom properties to ensure compatibility with the dynamic theming system.

### Available CSS Variables

```css
/* Colors */
--color-primary
--color-secondary
--color-accent
--color-background
--color-surface
--color-surface-elevated
--color-text
--color-text-secondary
--color-border
--color-hover
--color-active
--color-focus

/* Status Colors */
--color-success
--color-warning
--color-error

/* Casino Colors */
--color-gold
--color-silver
--color-bronze

/* Typography */
--font-primary
--font-display

/* Layout */
--spacing-base
--border-radius
--border-width

/* Effects */
--shadow-small
--shadow-medium
--shadow-large
--transition
--transition-fast
--transition-slow
```

### Example Header CSS (modern.css)

```css
/* Modern Header Component */

.header--modern {
  background: linear-gradient(
    135deg,
    var(--color-surface),
    var(--color-surface-elevated)
  );
  backdrop-filter: blur(20px);
  border-bottom: var(--border-width) solid var(--color-border);
  position: sticky;
  top: 0;
  z-index: 100;
  transition: var(--transition);
}

.header__content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding: 1rem 0;
  min-height: 4rem;
}

/* Logo Styles */
.header__logo .logo {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: var(--color-text);
  text-decoration: none;
  font-family: var(--font-display);
  font-weight: 700;
  font-size: 1.5rem;
  transition: var(--transition);
}

.logo__icon {
  font-size: 2rem;
  filter: drop-shadow(0 0 10px var(--color-primary));
}

.logo:hover {
  color: var(--color-primary);
  transform: scale(1.05);
}

/* Navigation Styles */
.header__nav {
  display: flex;
  align-items: center;
}

.nav-list {
  display: flex;
  list-style: none;
  gap: 2rem;
  margin: 0;
  padding: 0;
}

.nav-link {
  color: var(--color-text);
  text-decoration: none;
  font-weight: 500;
  position: relative;
  transition: var(--transition);
  padding: 0.5rem 0;
}

.nav-link::after {
  content: "";
  position: absolute;
  bottom: 0;
  left: 0;
  width: 0;
  height: 2px;
  background: linear-gradient(90deg, var(--color-primary), var(--color-accent));
  transition: width 0.3s ease;
}

.nav-link:hover {
  color: var(--color-primary);
}

.nav-link:hover::after {
  width: 100%;
}

/* Actions */
.header__actions {
  display: flex;
  gap: 1rem;
  align-items: center;
}

/* Mobile Toggle */
.mobile-toggle {
  display: none;
  flex-direction: column;
  background: none;
  border: none;
  cursor: pointer;
  padding: 0.5rem;
  gap: 3px;
}

.mobile-toggle__line {
  width: 24px;
  height: 3px;
  background: var(--color-text);
  transition: var(--transition);
  border-radius: 2px;
}

.mobile-toggle:hover .mobile-toggle__line {
  background: var(--color-primary);
}

/* Responsive Design */
@media (max-width: 768px) {
  .header__nav {
    display: none;
  }

  .mobile-toggle {
    display: flex;
  }

  .header__actions .btn {
    padding: 0.5rem 1rem;
    font-size: 0.875rem;
  }
}

@media (max-width: 480px) {
  .header__content {
    padding: 0.75rem 0;
  }

  .logo__text {
    display: none;
  }

  .header__actions {
    gap: 0.5rem;
  }
}
```

### Example Hero CSS (jackpot.css)

```css
/* Jackpot Hero Component */

.hero--jackpot {
  background: radial-gradient(
    ellipse at center,
    var(--color-surface-elevated),
    var(--color-background)
  );
  position: relative;
  padding: 4rem 0;
  overflow: hidden;
}

.hero--jackpot::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    45deg,
    transparent 30%,
    var(--color-primary) 10 50%,
    transparent 70%
  );
  opacity: 0.1;
  pointer-events: none;
}

.hero__content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
  position: relative;
  z-index: 2;
}

/* Text Content */
.hero__title {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

.hero__title-small {
  font-size: 1.25rem;
  font-weight: 500;
  color: var(--color-text-secondary);
  text-transform: uppercase;
  letter-spacing: 2px;
}

.hero__title-main {
  font-size: 4rem;
  font-weight: 800;
  font-family: var(--font-display);
  color: var(--color-text);
  text-shadow: 0 0 20px var(--color-primary);
  line-height: 0.9;
}

.hero__title-amount {
  font-size: 3rem;
  font-weight: 700;
  color: var(--color-gold);
  text-shadow: 0 0 30px var(--color-gold);
  animation: jackpotPulse 2s ease-in-out infinite;
}

@keyframes jackpotPulse {
  0%,
  100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.05);
  }
}

.hero__description {
  font-size: 1.25rem;
  line-height: 1.6;
  color: var(--color-text-secondary);
  margin-bottom: 2rem;
  max-width: 500px;
}

.hero__actions {
  display: flex;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-large {
  padding: 1rem 2rem;
  font-size: 1.125rem;
  font-weight: 600;
}

/* Visual Elements */
.hero__visual {
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.jackpot-display {
  position: relative;
  width: 300px;
  height: 300px;
  display: flex;
  align-items: center;
  justify-content: center;
}

.jackpot-display__glow {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 250px;
  height: 250px;
  border-radius: 50%;
  background: radial-gradient(circle, var(--color-gold) 20, transparent 70%);
  animation: glowPulse 3s ease-in-out infinite;
}

@keyframes glowPulse {
  0%,
  100% {
    opacity: 0.5;
    transform: translate(-50%, -50%) scale(1);
  }
  50% {
    opacity: 0.8;
    transform: translate(-50%, -50%) scale(1.1);
  }
}

.jackpot-display__coins {
  position: relative;
  z-index: 2;
  font-size: 6rem;
  filter: drop-shadow(0 0 20px var(--color-gold));
}

.jackpot-display__coins::before {
  content: "🪙";
  animation: coinFloat 4s ease-in-out infinite;
}

@keyframes coinFloat {
  0%,
  100% {
    transform: translateY(0) rotate(0deg);
  }
  25% {
    transform: translateY(-10px) rotate(90deg);
  }
  50% {
    transform: translateY(0) rotate(180deg);
  }
  75% {
    transform: translateY(-5px) rotate(270deg);
  }
}

/* Responsive Design */
@media (max-width: 768px) {
  .hero__content {
    grid-template-columns: 1fr;
    text-align: center;
    gap: 2rem;
  }

  .hero__title-main {
    font-size: 2.5rem;
  }

  .hero__title-amount {
    font-size: 2rem;
  }

  .jackpot-display {
    width: 200px;
    height: 200px;
  }

  .jackpot-display__glow {
    width: 150px;
    height: 150px;
  }

  .jackpot-display__coins {
    font-size: 4rem;
  }
}
```

## JavaScript Files

### Structure and Requirements

- Use modern ES6+ JavaScript
- Include proper error handling
- Follow casino compliance requirements
- Integrate with global theme system

### Example Header JS (modern.js)

```javascript
// Modern Header Component JavaScript

(function () {
  "use strict";

  class ModernHeader {
    constructor() {
      this.header = document.querySelector(".header--modern");
      this.mobileToggle = document.querySelector(".mobile-toggle");
      this.nav = document.querySelector(".header__nav");
      this.scrollThreshold = 100;

      this.init();
    }

    init() {
      if (!this.header) return;

      this.setupScrollEffects();
      this.setupMobileMenu();
      this.setupNavigation();
      this.setupAccessibility();

      console.log("🎰 Modern header initialized");
    }

    setupScrollEffects() {
      let isScrolled = false;

      const handleScroll = () => {
        const scrolled = window.scrollY > this.scrollThreshold;

        if (scrolled !== isScrolled) {
          isScrolled = scrolled;
          this.header.classList.toggle("header--scrolled", scrolled);

          // Enhance backdrop blur when scrolled
          this.header.style.setProperty(
            "backdrop-filter",
            scrolled ? "blur(30px)" : "blur(20px)"
          );
        }
      };

      window.addEventListener("scroll", handleScroll, { passive: true });
      handleScroll(); // Initial check
    }

    setupMobileMenu() {
      if (!this.mobileToggle) return;

      this.mobileToggle.addEventListener("click", () => {
        const isExpanded =
          this.mobileToggle.getAttribute("aria-expanded") === "true";

        this.mobileToggle.setAttribute("aria-expanded", !isExpanded);
        this.nav?.classList.toggle("nav--mobile-open", !isExpanded);

        // Lock body scroll when mobile menu is open
        document.body.style.overflow = !isExpanded ? "hidden" : "";
      });

      // Close mobile menu on escape key
      document.addEventListener("keydown", (e) => {
        if (
          e.key === "Escape" &&
          this.nav?.classList.contains("nav--mobile-open")
        ) {
          this.closeMobileMenu();
        }
      });

      // Close mobile menu on resize to desktop
      window.addEventListener("resize", () => {
        if (window.innerWidth > 768) {
          this.closeMobileMenu();
        }
      });
    }

    closeMobileMenu() {
      this.mobileToggle?.setAttribute("aria-expanded", "false");
      this.nav?.classList.remove("nav--mobile-open");
      document.body.style.overflow = "";
    }

    setupNavigation() {
      const navLinks = this.header.querySelectorAll(".nav-link");

      navLinks.forEach((link) => {
        // Smooth scroll for anchor links
        if (link.getAttribute("href")?.startsWith("#")) {
          link.addEventListener("click", (e) => {
            e.preventDefault();
            const target = document.querySelector(link.getAttribute("href"));

            if (target) {
              target.scrollIntoView({
                behavior: "smooth",
                block: "start",
              });

              // Close mobile menu if open
              this.closeMobileMenu();
            }
          });
        }

        // Add active state management
        link.addEventListener("mouseenter", () => {
          link.style.setProperty("--nav-hover-scale", "1.05");
        });

        link.addEventListener("mouseleave", () => {
          link.style.removeProperty("--nav-hover-scale");
        });
      });
    }

    setupAccessibility() {
      // Keyboard navigation support
      const focusableElements = this.header.querySelectorAll(
        'a, button, [tabindex]:not([tabindex="-1"])'
      );

      focusableElements.forEach((element, index) => {
        element.addEventListener("keydown", (e) => {
          if (e.key === "Tab") {
            // Add custom tab behavior if needed
          }
        });
      });

      // High contrast mode detection
      if (window.matchMedia("(prefers-contrast: high)").matches) {
        this.header.classList.add("header--high-contrast");
      }

      // Reduced motion support
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        this.header.classList.add("header--reduced-motion");
      }
    }

    // Public API
    updateTheme(theme) {
      this.header.setAttribute("data-theme", theme.mode);

      // Animate theme change
      if (window.casinoTheme?.animate) {
        window.casinoTheme.animate();
      }
    }
  }

  // Auto-initialize when component is loaded
  document.addEventListener("DOMContentLoaded", () => {
    window.modernHeader = new ModernHeader();
  });

  // Export for manual initialization
  window.ModernHeader = ModernHeader;
})();
```

### Example Hero JS (jackpot.js)

```javascript
// Jackpot Hero Component JavaScript

(function () {
  "use strict";

  class JackpotHero {
    constructor() {
      this.hero = document.querySelector(".hero--jackpot");
      this.jackpotAmount = document.querySelector("[data-jackpot]");
      this.baseAmount = 12500000; // Starting jackpot amount
      this.increment = 100; // Amount to increment by
      this.updateInterval = 5000; // Update every 5 seconds

      this.init();
    }

    init() {
      if (!this.hero) return;

      this.setupJackpotCounter();
      this.setupAnimations();
      this.setupInteractions();
      this.setupAccessibility();

      console.log("🎰 Jackpot hero initialized");
    }

    setupJackpotCounter() {
      if (!this.jackpotAmount) return;

      let currentAmount = this.baseAmount;

      const updateJackpot = () => {
        // Simulate jackpot growth
        currentAmount += Math.floor(Math.random() * this.increment * 2);

        // Format with commas and currency
        const formatted = new Intl.NumberFormat("en-US", {
          style: "currency",
          currency: "USD",
          minimumFractionDigits: 0,
        }).format(currentAmount);

        this.animateNumberChange(this.jackpotAmount, formatted);

        // Update data attribute
        this.jackpotAmount.setAttribute("data-jackpot", currentAmount);
      };

      // Initial update
      updateJackpot();

      // Set up interval for continuous updates
      setInterval(updateJackpot, this.updateInterval);
    }

    animateNumberChange(element, newValue) {
      element.style.transform = "scale(1.1)";
      element.style.textShadow = "0 0 40px var(--color-gold)";

      setTimeout(() => {
        element.textContent = newValue;
      }, 150);

      setTimeout(() => {
        element.style.transform = "scale(1)";
        element.style.textShadow = "0 0 30px var(--color-gold)";
      }, 300);
    }

    setupAnimations() {
      // Intersection Observer for scroll-triggered animations
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("hero--animated");
              this.startParticleEffects();
            }
          });
        },
        { threshold: 0.1 }
      );

      observer.observe(this.hero);

      // Enhanced coin animation on hover
      const coinDisplay = this.hero.querySelector(".jackpot-display__coins");
      if (coinDisplay) {
        coinDisplay.addEventListener("mouseenter", () => {
          coinDisplay.style.animation = "coinFloat 1s ease-in-out infinite";
        });

        coinDisplay.addEventListener("mouseleave", () => {
          coinDisplay.style.animation = "coinFloat 4s ease-in-out infinite";
        });
      }
    }

    startParticleEffects() {
      // Create floating particles effect
      const particlesContainer = document.createElement("div");
      particlesContainer.className = "hero-particles";
      particlesContainer.style.cssText = `
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        pointer-events: none;
        z-index: 1;
      `;

      this.hero.appendChild(particlesContainer);

      // Generate particles
      for (let i = 0; i < 20; i++) {
        setTimeout(() => {
          this.createParticle(particlesContainer);
        }, i * 200);
      }
    }

    createParticle(container) {
      const particle = document.createElement("div");
      particle.textContent = ["💰", "🪙", "💎", "⭐"][
        Math.floor(Math.random() * 4)
      ];
      particle.style.cssText = `
        position: absolute;
        font-size: ${Math.random() * 20 + 10}px;
        left: ${Math.random() * 100}%;
        top: 100%;
        opacity: 0.7;
        pointer-events: none;
        animation: floatUp ${3 + Math.random() * 2}s ease-out forwards;
      `;

      container.appendChild(particle);

      // Remove particle after animation
      setTimeout(() => {
        particle.remove();
      }, 5000);
    }

    setupInteractions() {
      const playButton = this.hero.querySelector(".btn-primary");
      const learnButton = this.hero.querySelector(".btn-secondary");

      // Enhanced button interactions
      [playButton, learnButton].forEach((button) => {
        if (!button) return;

        button.addEventListener("click", (e) => {
          // Casino compliance check
          if (!this.checkCasinoCompliance()) {
            e.preventDefault();
            this.showComplianceMessage();
            return;
          }

          // Create ripple effect
          this.createRippleEffect(button, e);
        });

        // Add hover sound effect (if audio is enabled)
        button.addEventListener("mouseenter", () => {
          this.playHoverSound();
        });
      });
    }

    createRippleEffect(button, event) {
      const ripple = document.createElement("span");
      const rect = button.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = event.clientX - rect.left - size / 2;
      const y = event.clientY - rect.top - size / 2;

      ripple.style.cssText = `
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        width: ${size}px;
        height: ${size}px;
        left: ${x}px;
        top: ${y}px;
        animation: ripple 0.6s ease-out;
        pointer-events: none;
      `;

      button.style.position = "relative";
      button.style.overflow = "hidden";
      button.appendChild(ripple);

      setTimeout(() => ripple.remove(), 600);
    }

    checkCasinoCompliance() {
      // Basic age verification (implement proper verification in production)
      return localStorage.getItem("ageVerified") === "true";
    }

    showComplianceMessage() {
      alert("You must be 18+ to play. Please verify your age.");
    }

    playHoverSound() {
      // Placeholder for sound effects
      if (window.casinoSounds?.enabled) {
        // window.casinoSounds.play('hover');
      }
    }

    setupAccessibility() {
      // Add skip link for screen readers
      const skipLink = document.createElement("a");
      skipLink.href = "#main-content";
      skipLink.textContent = "Skip to main content";
      skipLink.className = "sr-only";
      this.hero.insertBefore(skipLink, this.hero.firstChild);

      // Respect reduced motion preferences
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        this.hero.classList.add("hero--reduced-motion");
      }

      // High contrast mode support
      if (window.matchMedia("(prefers-contrast: high)").matches) {
        this.hero.classList.add("hero--high-contrast");
      }
    }

    // Public API
    updateJackpot(amount) {
      this.baseAmount = amount;
      this.jackpotAmount.setAttribute("data-jackpot", amount);
    }

    pauseAnimations() {
      this.hero.style.animationPlayState = "paused";
    }

    resumeAnimations() {
      this.hero.style.animationPlayState = "running";
    }
  }

  // Auto-initialize when component is loaded
  document.addEventListener("DOMContentLoaded", () => {
    window.jackpotHero = new JackpotHero();
  });

  // Export for manual initialization
  window.JackpotHero = JackpotHero;

  // Add required CSS animations
  const style = document.createElement("style");
  style.textContent = `
    @keyframes floatUp {
      0% {
        transform: translateY(0) rotate(0deg);
        opacity: 0.7;
      }
      50% {
        opacity: 1;
      }
      100% {
        transform: translateY(-200px) rotate(360deg);
        opacity: 0;
      }
    }
    
    @keyframes ripple {
      0% {
        transform: scale(0);
        opacity: 0.6;
      }
      100% {
        transform: scale(1);
        opacity: 0;
      }
    }
    
    .sr-only {
      position: absolute !important;
      width: 1px !important;
      height: 1px !important;
      padding: 0 !important;
      margin: -1px !important;
      overflow: hidden !important;
      clip: rect(0, 0, 0, 0) !important;
      white-space: nowrap !important;
      border: 0 !important;
    }
  `;
  document.head.appendChild(style);
})();
```

## Best Practices

### 1. CSS Custom Properties

- Always use CSS variables for colors, spacing, and typography
- This ensures compatibility with the dynamic theming system
- Use semantic names: `--color-primary` instead of `--blue`

### 2. Responsive Design

- Mobile-first approach with min-width media queries
- Use CSS Grid and Flexbox for layouts
- Test on multiple screen sizes (320px, 768px, 1024px, 1440px+)

### 3. Accessibility

- Include proper ARIA labels and roles
- Ensure keyboard navigation works
- Maintain color contrast ratios (4.5:1 minimum)
- Support screen readers with semantic HTML

### 4. Performance

- Optimize images and use modern formats (WebP, AVIF)
- Minimize JavaScript and use event delegation
- Use CSS transforms for animations (GPU accelerated)
- Implement lazy loading for non-critical content

### 5. Casino Compliance

- Include age verification checks
- Add responsible gambling notices
- Implement legal compliance features
- Follow gaming authority requirements

### 6. Code Organization

- Use BEM methodology for CSS classes
- Keep JavaScript modular and encapsulated
- Include error handling and fallbacks
- Document complex functionality

## Testing Your Components

### 1. Manual Testing

```bash
# Run the component importer
python3 starter.py

# Select option 2 (Import Components)
# Choose your component to test
# Verify theme integration works
```

### 2. Browser Testing

- Test in Chrome, Firefox, Safari, Edge
- Check mobile and tablet viewports
- Verify animations and interactions
- Test keyboard navigation

### 3. Accessibility Testing

- Use browser dev tools accessibility panel
- Test with screen reader (NVDA, JAWS, VoiceOver)
- Verify keyboard-only navigation
- Check color contrast ratios

## Component Categories

### Navigation Components

- `header` - Main site navigation
- `footer` - Site footer with links
- `sidebar` - Side navigation menus

### Content Components

- `hero` - Main banner/hero sections
- `features` - Feature showcases
- `testimonials` - Customer reviews
- `about` - About sections

### Gaming Components

- `games` - Game listings
- `promotions` - Bonus offers
- `tournaments` - Competition displays
- `leaderboards` - Player rankings

### Layout Components

- `container` - Content wrappers
- `grid` - Layout grids
- `modal` - Popup dialogs
- `tabs` - Tabbed content

## Variant Naming Conventions

### Style-based Variants

- `modern` - Clean, contemporary design
- `luxury` - Premium, elegant styling
- `neon` - Bright, gaming-focused
- `minimal` - Simple, clean design
- `vintage` - Classic, retro styling

### Function-based Variants

- `basic` - Essential functionality
- `advanced` - Extended features
- `premium` - Full-featured version
- `compact` - Space-saving version

### Content-based Variants

- `welcome` - New user focused
- `vip` - High-value player focused
- `tournament` - Competition focused
- `jackpot` - Prize focused

## Troubleshooting

### Common Issues

1. **Component not appearing**: Check HTML file exists and is valid
2. **Styling not applied**: Verify CSS file exists and uses CSS variables correctly
3. **JavaScript errors**: Check browser console for syntax errors
4. **Theme not working**: Ensure CSS variables are used instead of hardcoded colors

### Debug Steps

1. Check `component.json` is valid JSON
2. Verify all referenced files exist
3. Test HTML markup independently
4. Validate CSS with browser dev tools
5. Check JavaScript console for errors

### Getting Help

1. Check the console output when running the importer
2. Verify file naming matches component.json references
3. Test individual files in isolation
4. Review existing working components for reference

---

_This guide covers the complete process of creating components for the web-components-v2 system. Follow these patterns and practices to ensure your components integrate seamlessly with the dynamic theming system and provide an excellent user experience._
