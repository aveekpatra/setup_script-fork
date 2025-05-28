// Enhanced Casino Website - Base JavaScript

document.addEventListener("DOMContentLoaded", function () {
  console.log("🎰 Enhanced casino website loaded");

  // Initialize all components
  initializeAllComponents();

  // Setup global handlers
  setupGlobalHandlers();

  // Setup theme system
  setupThemeSystem();
});

function initializeAllComponents() {
  console.log("🔧 Initializing enhanced components...");
  // Component initialization functions will be called here
}

function setupGlobalHandlers() {
  // Global keyboard navigation
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape") {
      // Close any open menus
      document.querySelectorAll(".mobile-nav.active").forEach((nav) => {
        nav.classList.remove("active");
      });
    }
  });

  // Smooth scrolling for internal links
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener("click", function (e) {
      e.preventDefault();
      const target = document.querySelector(this.getAttribute("href"));
      if (target) {
        target.scrollIntoView({ behavior: "smooth" });
      }
    });
  });
}

function setupThemeSystem() {
  // Add dynamic theme switching capabilities
  const root = document.documentElement;

  // Theme animation support
  function animateThemeChange() {
    root.style.setProperty("--transition", "all 0.3s ease");
    setTimeout(() => {
      root.style.removeProperty("--transition");
    }, 300);
  }

  // Expose theme utilities globally
  window.casinoTheme = {
    animate: animateThemeChange,
  };
}

// Component scripts will be appended below


// Component Script
// Modern Header Component Script

function initModernHeader() {
  const header = document.querySelector(".modern-header");
  if (!header) return;

  const mobileToggle = header.querySelector(".mobile-toggle");
  const navLinks = header.querySelectorAll(".nav-link");
  const mobileNavLinks = header.querySelectorAll(".mobile-nav-link");

  // Mobile menu toggle
  if (mobileToggle) {
    mobileToggle.addEventListener("click", () => {
      header.classList.toggle("nav-open");
    });
  }

  // Close mobile menu when clicking nav links
  mobileNavLinks.forEach((link) => {
    link.addEventListener("click", () => {
      header.classList.remove("nav-open");
    });
  });

  // Active nav link handling
  navLinks.forEach((link) => {
    link.addEventListener("click", (e) => {
      e.preventDefault();

      // Remove active class from all links
      navLinks.forEach((l) => l.classList.remove("active"));

      // Add active class to clicked link
      link.classList.add("active");
    });
  });

  // Close mobile menu on outside click
  document.addEventListener("click", (e) => {
    if (!header.contains(e.target)) {
      header.classList.remove("nav-open");
    }
  });

  console.log("✅ Modern header initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initModernHeader);
} else {
  initModernHeader();
}


// Component Script
// Jackpot Hero Component Script

function initJackpotHero() {
  const hero = document.querySelector(".jackpot-hero");
  if (!hero) return;

  const jackpotValue = hero.querySelector(".jackpot-value");
  const winnerItems = hero.querySelectorAll(".winner-item");

  // Animate jackpot counter
  if (jackpotValue) {
    const baseValue = 2547832;
    let currentValue = baseValue;

    const updateJackpot = () => {
      // Add random small increment (1-50)
      const increment = Math.floor(Math.random() * 50) + 1;
      currentValue += increment;

      // Format number with commas
      const formattedValue = currentValue.toLocaleString();
      jackpotValue.textContent = formattedValue;
    };

    // Start with initial animation
    let animatedValue = 0;
    const targetValue = baseValue;

    const animateToBase = () => {
      if (animatedValue < targetValue) {
        animatedValue += Math.ceil((targetValue - animatedValue) / 20);
        jackpotValue.textContent = animatedValue.toLocaleString();
        requestAnimationFrame(animateToBase);
      } else {
        // Start the continuous increment
        setInterval(updateJackpot, 2000 + Math.random() * 3000); // Random interval 2-5 seconds
      }
    };

    setTimeout(animateToBase, 500);
  }

  // Animate winner items with staggered entrance
  if (winnerItems.length > 0) {
    const observerOptions = {
      threshold: 0.2,
      rootMargin: "0px 0px -20px 0px",
    };

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const items = entry.target.querySelectorAll(".winner-item");
          items.forEach((item, index) => {
            setTimeout(() => {
              item.style.opacity = "1";
              item.style.transform = "translateY(0)";
            }, index * 150);
          });
          observer.unobserve(entry.target);
        }
      });
    }, observerOptions);

    const winnersContainer = hero.querySelector(".winners-list");
    if (winnersContainer) {
      // Initially hide winner items
      winnerItems.forEach((item) => {
        item.style.opacity = "0";
        item.style.transform = "translateY(30px)";
        item.style.transition = "opacity 0.6s ease, transform 0.6s ease";
      });

      observer.observe(winnersContainer);
    }
  }

  // Add glow effect on jackpot card hover
  const jackpotCard = hero.querySelector(".jackpot-card");
  if (jackpotCard) {
    jackpotCard.addEventListener("mouseenter", () => {
      jackpotCard.style.boxShadow = `
        ${getComputedStyle(document.documentElement).getPropertyValue(
          "--shadow-large"
        )},
        0 0 40px rgba(var(--color-primary-rgb), 0.4)
      `;
    });

    jackpotCard.addEventListener("mouseleave", () => {
      jackpotCard.style.boxShadow = getComputedStyle(
        document.documentElement
      ).getPropertyValue("--shadow-large");
    });
  }

  // Button hover effects
  const buttons = hero.querySelectorAll(".btn");
  buttons.forEach((button) => {
    button.addEventListener("mouseenter", () => {
      button.style.transform = "translateY(-2px)";
    });

    button.addEventListener("mouseleave", () => {
      button.style.transform = "translateY(0)";
    });
  });

  console.log("✅ Jackpot hero initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initJackpotHero);
} else {
  initJackpotHero();
}


// Component Script
// Corporate About Us Component JavaScript

(function () {
  "use strict";

  class CorporateAbout {
    constructor() {
      this.aboutSection = document.querySelector(".about--corporate");
      this.statsElements = document.querySelectorAll(".stat-preview__number");
      this.overviewCards = document.querySelectorAll(".overview-card");
      this.featureItems = document.querySelectorAll(".feature-item");
      this.valueItems = document.querySelectorAll(".value-item");
      this.ctaButtons = document.querySelectorAll(".cta-card .btn");

      this.animationObserver = null;
      this.statsAnimated = false;

      this.init();
    }

    init() {
      if (!this.aboutSection) return;

      this.setupIntersectionObserver();
      this.setupStatsAnimation();
      this.setupCardInteractions();
      this.setupCtaInteractions();
      this.setupAccessibility();
      this.setupScrollAnimations();

      console.log("🎰 Corporate About section initialized");
    }

    setupIntersectionObserver() {
      this.animationObserver = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              this.animateElement(entry.target);
            }
          });
        },
        {
          threshold: 0.2,
          rootMargin: "0px 0px -50px 0px",
        }
      );

      // Observe all animatable elements
      const animatableElements = [
        ...this.overviewCards,
        ...this.featureItems,
        ...this.valueItems,
        document.querySelector(".about__header"),
        document.querySelector(".about__cta"),
      ].filter(Boolean);

      animatableElements.forEach((element) => {
        this.animationObserver.observe(element);
      });
    }

    animateElement(element) {
      element.style.opacity = "0";
      element.style.transform = "translateY(30px)";
      element.style.transition = "opacity 0.6s ease, transform 0.6s ease";

      requestAnimationFrame(() => {
        element.style.opacity = "1";
        element.style.transform = "translateY(0)";
      });

      // Special handling for stats animation
      if (element.classList.contains("stat-preview") && !this.statsAnimated) {
        this.animateStats();
        this.statsAnimated = true;
      }
    }

    setupStatsAnimation() {
      const statsData = [
        {
          element: this.statsElements[0],
          target: 2000000,
          suffix: "M+",
          duration: 2000,
        },
        {
          element: this.statsElements[1],
          target: 500,
          suffix: "+",
          duration: 1500,
        },
      ];

      this.statsData = statsData;
    }

    animateStats() {
      this.statsData.forEach((stat, index) => {
        if (!stat.element) return;

        setTimeout(() => {
          this.animateNumber(
            stat.element,
            stat.target,
            stat.suffix,
            stat.duration
          );
        }, index * 200);
      });
    }

    animateNumber(element, target, suffix, duration) {
      const start = 0;
      const startTime = performance.now();

      const animate = (currentTime) => {
        const elapsed = currentTime - startTime;
        const progress = Math.min(elapsed / duration, 1);

        // Easing function (ease-out)
        const easeProgress = 1 - Math.pow(1 - progress, 3);
        const current = Math.floor(start + (target - start) * easeProgress);

        // Format the number
        let displayValue;
        if (target >= 1000000) {
          displayValue =
            (current / 1000000).toFixed(1) +
            "M" +
            (suffix.replace("M+", "+") || "");
        } else {
          displayValue = current.toLocaleString() + (suffix || "");
        }

        element.textContent = displayValue;

        if (progress < 1) {
          requestAnimationFrame(animate);
        } else {
          // Add final pulse effect
          element.style.transform = "scale(1.1)";
          element.style.color = "var(--color-accent)";

          setTimeout(() => {
            element.style.transform = "scale(1)";
            element.style.color = "var(--color-primary)";
          }, 200);
        }
      };

      requestAnimationFrame(animate);
    }

    setupCardInteractions() {
      // Overview cards hover effects
      this.overviewCards.forEach((card) => {
        card.addEventListener("mouseenter", () => {
          this.enhanceCardHover(card);
        });

        card.addEventListener("mouseleave", () => {
          this.resetCardHover(card);
        });

        // Add focus support for keyboard navigation
        card.addEventListener("focus", () => {
          this.enhanceCardHover(card);
        });

        card.addEventListener("blur", () => {
          this.resetCardHover(card);
        });
      });

      // Feature items interactions
      this.featureItems.forEach((item) => {
        item.addEventListener("mouseenter", () => {
          this.animateFeatureIcon(item);
        });
      });

      // Value items sequential animation on scroll
      this.valueItems.forEach((item, index) => {
        item.addEventListener("mouseenter", () => {
          this.highlightValueItem(item, index);
        });
      });
    }

    enhanceCardHover(card) {
      const icon = card.querySelector(".overview-card__icon");
      if (icon) {
        icon.style.transform = "scale(1.1) rotate(5deg)";
        icon.style.boxShadow = "0 10px 25px rgba(0, 0, 0, 0.2)";
      }

      // Add glow effect
      card.style.boxShadow = `
        var(--shadow-medium),
        0 0 20px var(--color-primary)20
      `;
    }

    resetCardHover(card) {
      const icon = card.querySelector(".overview-card__icon");
      if (icon) {
        icon.style.transform = "scale(1) rotate(0deg)";
        icon.style.boxShadow = "";
      }

      card.style.boxShadow = "var(--shadow-small)";
    }

    animateFeatureIcon(item) {
      const icon = item.querySelector(".feature-item__icon");
      if (icon) {
        icon.style.transform = "scale(1.2) rotate(360deg)";
        icon.style.transition = "transform 0.5s ease";

        setTimeout(() => {
          icon.style.transform = "scale(1) rotate(0deg)";
        }, 500);
      }
    }

    highlightValueItem(item, index) {
      // Temporarily highlight related value items
      this.valueItems.forEach((otherItem, otherIndex) => {
        if (otherIndex !== index) {
          otherItem.style.opacity = "0.6";
        }
      });

      item.addEventListener(
        "mouseleave",
        () => {
          this.valueItems.forEach((otherItem) => {
            otherItem.style.opacity = "1";
          });
        },
        { once: true }
      );
    }

    setupCtaInteractions() {
      this.ctaButtons.forEach((button) => {
        button.addEventListener("click", (e) => {
          this.handleCtaClick(button, e);
        });

        // Enhanced hover effects
        button.addEventListener("mouseenter", () => {
          this.createRippleEffect(button);
        });
      });
    }

    handleCtaClick(button, event) {
      // Create click animation
      this.createClickAnimation(button, event);

      // Handle specific button actions
      const buttonText = button.textContent.trim();

      if (buttonText === "Compare Casinos") {
        this.handleCompareAction();
      } else if (buttonText === "Read Our Reviews") {
        this.handleReviewsAction();
      }
    }

    createRippleEffect(button) {
      const ripple = document.createElement("span");
      const rect = button.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);

      ripple.style.cssText = `
        position: absolute;
        border-radius: 50%;
        background: rgba(255, 255, 255, 0.3);
        width: ${size}px;
        height: ${size}px;
        left: 50%;
        top: 50%;
        transform: translate(-50%, -50%) scale(0);
        animation: ripple 0.6s ease-out;
        pointer-events: none;
      `;

      button.style.position = "relative";
      button.style.overflow = "hidden";
      button.appendChild(ripple);

      setTimeout(() => ripple.remove(), 600);
    }

    createClickAnimation(button, event) {
      button.style.transform = "scale(0.95)";

      setTimeout(() => {
        button.style.transform = "scale(1)";
      }, 150);
    }

    handleCompareAction() {
      // Scroll to comparison section or navigate
      const comparisonSection = document.querySelector(
        "#comparison, .comparison"
      );
      if (comparisonSection) {
        comparisonSection.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      } else {
        // Navigate to comparison page
        console.log("Navigate to casino comparison");
      }
    }

    handleReviewsAction() {
      // Scroll to reviews section or navigate
      const reviewsSection = document.querySelector("#reviews, .reviews");
      if (reviewsSection) {
        reviewsSection.scrollIntoView({
          behavior: "smooth",
          block: "start",
        });
      } else {
        // Navigate to reviews page
        console.log("Navigate to casino reviews");
      }
    }

    setupAccessibility() {
      // Add keyboard navigation support
      const focusableElements = this.aboutSection.querySelectorAll(
        'button, [href], [tabindex]:not([tabindex="-1"])'
      );

      focusableElements.forEach((element) => {
        element.addEventListener("keydown", (e) => {
          if (e.key === "Enter" || e.key === " ") {
            e.preventDefault();
            element.click();
          }
        });
      });

      // Add skip navigation
      this.addSkipNavigation();

      // Support reduced motion preferences
      if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
        this.aboutSection.classList.add("about--reduced-motion");
      }

      // High contrast mode support
      if (window.matchMedia("(prefers-contrast: high)").matches) {
        this.aboutSection.classList.add("about--high-contrast");
      }
    }

    addSkipNavigation() {
      const skipLink = document.createElement("a");
      skipLink.href = "#about-content";
      skipLink.textContent = "Skip to about content";
      skipLink.className = "sr-only skip-link";

      this.aboutSection.insertBefore(skipLink, this.aboutSection.firstChild);

      // Add target for skip link
      const content = this.aboutSection.querySelector(".about__content");
      if (content && !content.id) {
        content.id = "about-content";
      }
    }

    setupScrollAnimations() {
      // Parallax effect for background elements
      window.addEventListener("scroll", () => {
        if (window.matchMedia("(prefers-reduced-motion: reduce)").matches)
          return;

        const scrolled = window.pageYOffset;
        const parallaxElements =
          this.aboutSection.querySelectorAll(".stat-preview");

        parallaxElements.forEach((element, index) => {
          const speed = 0.1 + index * 0.05;
          const yPos = -(scrolled * speed);
          element.style.transform = `translateY(${yPos}px)`;
        });
      });
    }

    // Public API
    refreshAnimations() {
      this.statsAnimated = false;
      if (this.animationObserver) {
        this.animationObserver.disconnect();
        this.setupIntersectionObserver();
      }
    }

    updateStats(newStats) {
      if (newStats.users) {
        this.statsData[0].target = newStats.users;
      }
      if (newStats.casinos) {
        this.statsData[1].target = newStats.casinos;
      }
    }

    destroy() {
      if (this.animationObserver) {
        this.animationObserver.disconnect();
      }
    }
  }

  // Auto-initialize when component is loaded
  document.addEventListener("DOMContentLoaded", () => {
    window.corporateAbout = new CorporateAbout();
  });

  // Export for manual initialization
  window.CorporateAbout = CorporateAbout;

  // Add required CSS animations
  const style = document.createElement("style");
  style.textContent = `
    @keyframes ripple {
      0% {
        transform: translate(-50%, -50%) scale(0);
        opacity: 0.6;
      }
      100% {
        transform: translate(-50%, -50%) scale(1);
        opacity: 0;
      }
    }
    
    .skip-link {
      position: absolute;
      top: -40px;
      left: 6px;
      background: var(--color-primary);
      color: var(--color-background);
      padding: 8px;
      text-decoration: none;
      border-radius: 4px;
      transition: top 0.3s;
      z-index: 1000;
    }
    
    .skip-link:focus {
      top: 6px;
    }
    
    .about--reduced-motion * {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      transition-duration: 0.01ms !important;
    }
    
    .about--high-contrast {
      filter: contrast(2);
    }
  `;
  document.head.appendChild(style);
})();


// Component Script
// Minimal Footer JavaScript
function initFooterMinimal() {
    console.log('Footer minimal variant initialized');
}

// Initialize when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initFooterMinimal);
} else {
    initFooterMinimal();
}