/**
 * Professional Casino Header JavaScript
 * Essential functionality for header templates with consistent theming
 */

document.addEventListener("DOMContentLoaded", function () {
  // Initialize essential header functionalities
  initHeaderTemplateSwitcher();
  initMobileMenuToggle();
  initSearchFunctionality();
  initScrollEffects();
  initAccessibilityFeatures();
  initPerformanceOptimizations();

  console.log("Professional Casino Headers loaded successfully");
});

/**
 * Header Template Switcher Functionality
 */
function initHeaderTemplateSwitcher() {
  const headers = document.querySelectorAll(".modern-header");
  const switcherButtons = document.querySelectorAll(
    "button[onclick*='showHeaderTemplate']"
  );

  if (!headers.length) return;

  // Enhanced template switching with smooth transitions
  window.showHeaderTemplate = function (templateNumber) {
    headers.forEach((header, index) => {
      if (index + 1 === templateNumber) {
        header.style.display = "block";
        header.style.opacity = "0";
        header.style.transform = "translateY(-10px)";

        // Smooth fade in
        requestAnimationFrame(() => {
          header.style.transition = "all 0.3s ease";
          header.style.opacity = "1";
          header.style.transform = "translateY(0)";
        });

        // Re-initialize Lucide icons for the new template
        if (typeof lucide !== "undefined") {
          setTimeout(() => {
            lucide.createIcons();
          }, 100);
        }
      } else {
        header.style.display = "none";
      }
    });

    // Update active button
    switcherButtons.forEach((btn, index) => {
      btn.classList.toggle("active", index + 1 === templateNumber);
    });

    // Trigger template change event
    window.dispatchEvent(
      new CustomEvent("headerTemplateChanged", {
        detail: { templateNumber },
      })
    );
  };

  // Add keyboard navigation
  switcherButtons.forEach((button, index) => {
    button.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft" || e.key === "ArrowRight") {
        e.preventDefault();
        const direction = e.key === "ArrowLeft" ? -1 : 1;
        const nextIndex =
          (index + direction + switcherButtons.length) % switcherButtons.length;
        switcherButtons[nextIndex].focus();
        switcherButtons[nextIndex].click();
      }
    });
  });
}

/**
 * Mobile Menu Toggle Functionality
 */
function initMobileMenuToggle() {
  const mobileToggles = document.querySelectorAll(".mobile-menu-toggle");

  mobileToggles.forEach((toggle) => {
    toggle.addEventListener("click", function () {
      const header = this.closest(".modern-header");
      const nav = header.querySelector(".main-nav");

      if (!nav) return;

      const isOpen = nav.classList.contains("mobile-open");

      // Toggle mobile menu
      nav.classList.toggle("mobile-open", !isOpen);
      toggle.classList.toggle("active", !isOpen);

      // Animate hamburger lines
      const spans = toggle.querySelectorAll("span");
      if (spans.length === 3) {
        if (!isOpen) {
          spans[0].style.transform = "rotate(45deg) translateY(8px)";
          spans[1].style.opacity = "0";
          spans[2].style.transform = "rotate(-45deg) translateY(-8px)";
        } else {
          spans[0].style.transform = "";
          spans[1].style.opacity = "";
          spans[2].style.transform = "";
        }
      }

      // Add mobile menu styles if not present
      if (!document.getElementById("mobile-menu-styles")) {
        const style = document.createElement("style");
        style.id = "mobile-menu-styles";
        style.textContent = `
          @media (max-width: 768px) {
            .main-nav {
              position: absolute;
              top: 100%;
              left: 0;
              right: 0;
              background: var(--bg-primary);
              border-top: 1px solid var(--border-light);
              box-shadow: 0 4px 6px var(--shadow-medium);
              transform: translateY(-100%);
              opacity: 0;
              visibility: hidden;
              transition: all var(--transition-base);
              z-index: var(--z-dropdown);
            }
            
            .main-nav.mobile-open {
              transform: translateY(0);
              opacity: 1;
              visibility: visible;
            }
            
            .main-nav .nav-list {
              flex-direction: column;
              padding: var(--space-4);
              gap: var(--space-2);
            }
            
            .main-nav .nav-link {
              padding: var(--space-3) var(--space-4);
              border-radius: var(--radius-md);
              display: block;
            }
            
            .main-nav .nav-link:hover {
              background: var(--bg-tertiary);
            }

            /* Icon navigation mobile adjustments */
            .header-9 .nav-link {
              flex-direction: row;
              justify-content: flex-start;
              gap: var(--space-3);
              min-width: auto;
              text-align: left;
            }

            .header-9 .nav-link i {
              font-size: var(--font-size-base);
              margin-bottom: 0;
            }

            /* Hide dropdown icons on mobile */
            .dropdown-icon {
              display: none;
            }
          }
        `;
        document.head.appendChild(style);
      }
    });
  });
}

/**
 * Search Functionality
 */
function initSearchFunctionality() {
  const searchBoxes = document.querySelectorAll(".search-box");

  searchBoxes.forEach((searchBox) => {
    const input = searchBox.querySelector("input");
    const searchButton = searchBox.querySelector(".search-button");

    if (!input) return;

    // Search input handling
    input.addEventListener(
      "input",
      debounce(function () {
        const query = this.value.trim();

        if (query.length > 2) {
          console.log("Searching for:", query);

          // Dispatch search event for external handling
          window.dispatchEvent(
            new CustomEvent("casinoHeaderSearch", {
              detail: { query },
            })
          );
        }
      }, 300)
    );

    // Search button click
    if (searchButton) {
      searchButton.addEventListener("click", function () {
        const query = input.value.trim();
        if (query) {
          window.dispatchEvent(
            new CustomEvent("casinoHeaderSearchSubmit", {
              detail: { query },
            })
          );
        }
      });
    }

    // Enter key handling
    input.addEventListener("keydown", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        const query = this.value.trim();
        if (query) {
          window.dispatchEvent(
            new CustomEvent("casinoHeaderSearchSubmit", {
              detail: { query },
            })
          );
        }
      }
    });
  });
}

/**
 * Scroll Effects
 */
function initScrollEffects() {
  let lastScrollY = window.scrollY;
  let ticking = false;

  function updateScrollEffects() {
    const scrollY = window.scrollY;
    const scrollDirection = scrollY > lastScrollY ? "down" : "up";
    const scrollDistance = Math.abs(scrollY - lastScrollY);

    document.querySelectorAll(".modern-header").forEach((header) => {
      if (header.style.display === "none") return;

      // Add/remove scrolled class for visual feedback
      header.classList.toggle("scrolled", scrollY > 10);

      // Auto-hide functionality for headers that support it
      if (header.classList.contains("header-auto-hide")) {
        if (scrollDirection === "down" && scrollDistance > 5 && scrollY > 100) {
          header.style.transform = "translateY(-100%)";
        } else if (scrollDirection === "up" && scrollDistance > 5) {
          header.style.transform = "translateY(0)";
        }
      }
    });

    lastScrollY = scrollY;
    ticking = false;
  }

  function requestTick() {
    if (!ticking) {
      requestAnimationFrame(updateScrollEffects);
      ticking = true;
    }
  }

  window.addEventListener("scroll", requestTick, { passive: true });

  // Add scroll styles
  if (!document.getElementById("scroll-styles")) {
    const style = document.createElement("style");
    style.id = "scroll-styles";
    style.textContent = `
      .modern-header {
        transition: transform var(--transition-base), box-shadow var(--transition-base);
      }
      
      .modern-header.scrolled {
        box-shadow: 0 4px 20px var(--shadow-medium);
      }
      
      .modern-header.header-auto-hide {
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        z-index: var(--z-sticky);
      }
    `;
    document.head.appendChild(style);
  }
}

/**
 * Accessibility Features
 */
function initAccessibilityFeatures() {
  // Enhanced focus indicators
  const focusableElements = document.querySelectorAll(
    'a, button, input, [tabindex]:not([tabindex="-1"])'
  );

  focusableElements.forEach((element) => {
    element.addEventListener("focus", function () {
      this.style.outline = "2px solid var(--brand-primary)";
      this.style.outlineOffset = "2px";
    });

    element.addEventListener("blur", function () {
      this.style.outline = "";
      this.style.outlineOffset = "";
    });
  });

  // Add ARIA labels where missing
  const logos = document.querySelectorAll(".logo-link");
  logos.forEach((logo) => {
    if (!logo.getAttribute("aria-label")) {
      logo.setAttribute("aria-label", "CasinoPro Homepage");
    }
  });

  // Add skip navigation link
  if (!document.querySelector(".skip-nav")) {
    const skipNav = document.createElement("a");
    skipNav.className = "skip-nav";
    skipNav.href = "#main-content";
    skipNav.textContent = "Skip to main content";
    skipNav.style.cssText = `
      position: absolute;
      top: -40px;
      left: 6px;
      background: var(--brand-primary);
      color: white;
      padding: 8px;
      border-radius: 4px;
      text-decoration: none;
      transition: top 0.3s;
      z-index: 100000;
      font-weight: 600;
    `;

    skipNav.addEventListener("focus", function () {
      this.style.top = "6px";
    });

    skipNav.addEventListener("blur", function () {
      this.style.top = "-40px";
    });

    document.body.insertBefore(skipNav, document.body.firstChild);
  }

  // Mega menu keyboard navigation
  const megaMenuLinks = document.querySelectorAll(".has-dropdown");
  megaMenuLinks.forEach((link) => {
    link.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        // Trigger dropdown toggle (placeholder for actual mega menu functionality)
        console.log("Mega menu triggered:", this.textContent);

        // Animate dropdown icon
        const dropdownIcon = this.querySelector(".dropdown-icon");
        if (dropdownIcon) {
          dropdownIcon.style.transform =
            dropdownIcon.style.transform === "rotate(180deg)"
              ? "rotate(0deg)"
              : "rotate(180deg)";
        }
      }
    });

    // Mouse hover effect for dropdown icon
    link.addEventListener("mouseenter", function () {
      const dropdownIcon = this.querySelector(".dropdown-icon");
      if (dropdownIcon) {
        dropdownIcon.style.transform = "rotate(180deg)";
      }
    });

    link.addEventListener("mouseleave", function () {
      const dropdownIcon = this.querySelector(".dropdown-icon");
      if (dropdownIcon) {
        dropdownIcon.style.transform = "rotate(0deg)";
      }
    });
  });
}

/**
 * Performance Optimizations
 */
function initPerformanceOptimizations() {
  // Lazy load non-critical animations
  const animatedElements = document.querySelectorAll(".logo-icon, .cta-button");

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add("animate-ready");
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.1 }
  );

  animatedElements.forEach((el) => observer.observe(el));

  // Preconnect to external domains
  const preconnectDomains = [
    "https://unpkg.com",
    "https://fonts.googleapis.com",
  ];

  preconnectDomains.forEach((domain) => {
    const link = document.createElement("link");
    link.rel = "preconnect";
    link.href = domain;
    document.head.appendChild(link);
  });

  // Optimize images with loading attributes
  const images = document.querySelectorAll("img");
  images.forEach((img) => {
    if (!img.getAttribute("loading")) {
      img.setAttribute("loading", "lazy");
    }
  });
}

/**
 * Sidebar Toggle Functionality (for Template 8)
 */
function initSidebarToggle() {
  const sidebarToggles = document.querySelectorAll(".sidebar-toggle");

  sidebarToggles.forEach((toggle) => {
    toggle.addEventListener("click", function () {
      // Dispatch event for external sidebar handling
      window.dispatchEvent(
        new CustomEvent("casinoSidebarToggle", {
          detail: { action: "toggle" },
        })
      );

      // Visual feedback
      this.classList.toggle("active");
      console.log("Sidebar toggle triggered");
    });
  });
}

/**
 * Notification Button Functionality (for Template 9)
 */
function initNotificationButton() {
  const notificationBtns = document.querySelectorAll(".notification-btn");

  notificationBtns.forEach((btn) => {
    btn.addEventListener("click", function () {
      // Dispatch event for external notification handling
      window.dispatchEvent(
        new CustomEvent("casinoNotificationClick", {
          detail: { timestamp: Date.now() },
        })
      );

      // Hide notification badge
      const badge = this.querySelector(".notification-badge");
      if (badge) {
        badge.style.display = "none";
      }

      console.log("Notification button clicked");
    });
  });
}

/**
 * Lucide Icons Helper Functions
 */
function initLucideIcons() {
  // Initialize Lucide icons when available
  if (typeof lucide !== "undefined") {
    lucide.createIcons();

    // Re-initialize icons when templates change
    document.addEventListener("headerTemplateChanged", function () {
      setTimeout(() => {
        lucide.createIcons();
      }, 100);
    });
  }
}

/**
 * Utility Functions
 */
function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func.apply(this, args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

/**
 * Public API for external theme management
 */
window.CasinoHeader = {
  // Switch to a specific template
  switchTemplate: function (templateNumber) {
    if (window.showHeaderTemplate) {
      window.showHeaderTemplate(templateNumber);
    }
  },

  // Update brand colors (for Python script integration)
  updateBrandColors: function (colors) {
    const root = document.documentElement;

    if (colors.primary) {
      root.style.setProperty("--brand-primary", colors.primary);
      root.style.setProperty(
        "--brand-primary-light",
        colors.primaryLight || colors.primary
      );
      root.style.setProperty(
        "--brand-primary-dark",
        colors.primaryDark || colors.primary
      );
    }

    if (colors.secondary) {
      root.style.setProperty("--brand-secondary", colors.secondary);
      root.style.setProperty(
        "--brand-secondary-light",
        colors.secondaryLight || colors.secondary
      );
      root.style.setProperty(
        "--brand-secondary-dark",
        colors.secondaryDark || colors.secondary
      );
    }

    if (colors.accent) {
      root.style.setProperty("--brand-accent", colors.accent);
      root.style.setProperty(
        "--brand-accent-light",
        colors.accentLight || colors.accent
      );
      root.style.setProperty(
        "--brand-accent-dark",
        colors.accentDark || colors.accent
      );
    }

    console.log("Brand colors updated:", colors);
  },

  // Get current active template
  getActiveTemplate: function () {
    const headers = document.querySelectorAll(".modern-header");
    for (let i = 0; i < headers.length; i++) {
      if (headers[i].style.display !== "none") {
        return i + 1;
      }
    }
    return 1; // Default to first template
  },

  // Initialize additional features
  init: function () {
    initSidebarToggle();
    initNotificationButton();
    initLucideIcons();
  },
};

// Auto-initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", function () {
    setTimeout(() => {
      window.CasinoHeader.init();
    }, 100);
  });
} else {
  window.CasinoHeader.init();
}

// Export main functions for template switching
window.showHeaderTemplate = showHeaderTemplate;
