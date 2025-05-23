/**
 * Modern Casino Footer JavaScript
 * Interactive functionality for all footer templates
 */

document.addEventListener("DOMContentLoaded", function () {
  // Initialize all footer functionalities
  initFooterTemplateSwitcher();
  initNewsletterForms();
  initAccordionFunctionality();
  initScrollAnimations();
  initInteractiveElements();
  initResponsiveFeatures();
  initAccessibilityEnhancements();

  console.log("Modern Casino Footer loaded successfully");
});

/**
 * Footer Template Switcher Functionality
 */
function initFooterTemplateSwitcher() {
  const footers = document.querySelectorAll(".modern-footer");
  const switcherButtons = document.querySelectorAll(
    ".template-switcher button"
  );

  if (!footers.length || !switcherButtons.length) return;

  switcherButtons.forEach((button, index) => {
    button.addEventListener("click", function () {
      showFooterTemplate(index + 1);

      // Update active button
      switcherButtons.forEach((btn) => btn.classList.remove("active"));
      this.classList.add("active");
    });

    // Add keyboard navigation
    button.addEventListener("keydown", function (e) {
      if (e.key === "ArrowLeft" || e.key === "ArrowRight") {
        e.preventDefault();
        const direction = e.key === "ArrowLeft" ? -1 : 1;
        const currentIndex = Array.from(switcherButtons).indexOf(this);
        const nextIndex =
          (currentIndex + direction + switcherButtons.length) %
          switcherButtons.length;
        switcherButtons[nextIndex].focus();
        switcherButtons[nextIndex].click();
      }
    });
  });
}

/**
 * Show specific footer template
 */
function showFooterTemplate(templateNumber) {
  const footers = document.querySelectorAll(".modern-footer");
  const targetFooter = document.querySelector(`#footer-${templateNumber}`);

  if (!targetFooter) return;

  // Hide all footers
  footers.forEach((footer) => {
    footer.style.display = "none";
    footer.classList.remove("active");
  });

  // Show target footer with animation
  targetFooter.style.display = "block";
  targetFooter.classList.add("active");

  // Trigger any specific initialization for the footer
  initFooterSpecificFeatures(templateNumber);

  // Scroll to footer if not in view
  setTimeout(() => {
    targetFooter.scrollIntoView({
      behavior: "smooth",
      block: "nearest",
    });
  }, 100);
}

/**
 * Newsletter Form Functionality
 */
function initNewsletterForms() {
  const newsletterForms = document.querySelectorAll(".newsletter-form");

  newsletterForms.forEach((form) => {
    const submitBtn = form.querySelector('button[type="submit"], button');
    const emailInput = form.querySelector('input[type="email"]');

    if (!submitBtn || !emailInput) return;

    // Handle form submission
    submitBtn.addEventListener("click", function (e) {
      e.preventDefault();

      const email = emailInput.value.trim();

      if (!isValidEmail(email)) {
        showFormMessage(form, "Please enter a valid email address", "error");
        emailInput.focus();
        return;
      }

      // Simulate newsletter subscription
      submitBtn.disabled = true;
      submitBtn.textContent = "Subscribing...";

      setTimeout(() => {
        showFormMessage(
          form,
          "Successfully subscribed! Check your email for confirmation.",
          "success"
        );
        emailInput.value = "";
        submitBtn.disabled = false;
        submitBtn.textContent = "Subscribe";
      }, 2000);
    });

    // Real-time email validation
    emailInput.addEventListener("input", function () {
      const email = this.value.trim();
      if (email && !isValidEmail(email)) {
        this.style.borderColor = "#ef4444";
      } else {
        this.style.borderColor = "";
      }
    });

    // Enter key submission
    emailInput.addEventListener("keypress", function (e) {
      if (e.key === "Enter") {
        e.preventDefault();
        submitBtn.click();
      }
    });
  });
}

/**
 * Accordion Functionality for Mobile Footer
 */
function initAccordionFunctionality() {
  const accordionHeaders = document.querySelectorAll(".accordion-header");

  accordionHeaders.forEach((header) => {
    header.addEventListener("click", function () {
      const accordionItem = this.parentElement;
      const content = accordionItem.querySelector(".accordion-content");
      const icon = this.querySelector("i");

      if (!content) return;

      const isActive = content.classList.contains("active");

      // Close all other accordions in the same footer
      const footer = this.closest(".modern-footer");
      if (footer) {
        footer
          .querySelectorAll(".accordion-content.active")
          .forEach((activeContent) => {
            if (activeContent !== content) {
              activeContent.classList.remove("active");
              activeContent.parentElement
                .querySelector(".accordion-header")
                .classList.remove("active");
            }
          });
      }

      // Toggle current accordion
      if (isActive) {
        content.classList.remove("active");
        this.classList.remove("active");
      } else {
        content.classList.add("active");
        this.classList.add("active");
      }

      // Animate icon if present
      if (icon) {
        icon.style.transform = isActive ? "rotate(0deg)" : "rotate(180deg)";
      }
    });

    // Keyboard accessibility
    header.addEventListener("keydown", function (e) {
      if (e.key === "Enter" || e.key === " ") {
        e.preventDefault();
        this.click();
      }
    });
  });
}

/**
 * Scroll Animations
 */
function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver(function (entries) {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("animate-in");

        // Animate child elements with stagger
        const children = entry.target.querySelectorAll(
          ".stat-item, .social-link, .crypto-item, .game-category, .link-group, .contact-method"
        );
        children.forEach((child, index) => {
          setTimeout(() => {
            child.style.animation = `slideInUp 0.6s ease-out ${
              index * 0.1
            }s both`;
          }, 100);
        });
      }
    });
  }, observerOptions);

  // Observe footer sections
  const footerSections = document.querySelectorAll(
    ".modern-footer .footer-content, .footer-gaming-stats, .crypto-showcase, .tournament-banner, .vip-section"
  );
  footerSections.forEach((section) => observer.observe(section));

  // Add CSS animations if not present
  if (!document.getElementById("footer-animations")) {
    const style = document.createElement("style");
    style.id = "footer-animations";
    style.textContent = `
            @keyframes slideInUp {
                from {
                    opacity: 0;
                    transform: translateY(30px);
                }
                to {
                    opacity: 1;
                    transform: translateY(0);
                }
            }
            
            .animate-in {
                animation: slideInUp 0.6s ease-out;
            }
        `;
    document.head.appendChild(style);
  }
}

/**
 * Interactive Elements
 */
function initInteractiveElements() {
  // Social link hover effects
  const socialLinks = document.querySelectorAll(
    ".social-links a, .footer-social a, .social-minimal a, .social-crypto a"
  );
  socialLinks.forEach((link) => {
    link.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-3px) scale(1.05)";
    });

    link.addEventListener("mouseleave", function () {
      this.style.transform = "";
    });
  });

  // CTA Button effects
  const ctaButtons = document.querySelectorAll(
    ".cta-button, .vip-button, .tournament-btn, .download-btn"
  );
  ctaButtons.forEach((button) => {
    button.addEventListener("click", function (e) {
      // Ripple effect
      const ripple = document.createElement("span");
      const rect = this.getBoundingClientRect();
      const size = Math.max(rect.width, rect.height);
      const x = e.clientX - rect.left - size / 2;
      const y = e.clientY - rect.top - size / 2;

      ripple.style.cssText = `
                position: absolute;
                width: ${size}px;
                height: ${size}px;
                left: ${x}px;
                top: ${y}px;
                background: rgba(255,255,255,0.3);
                border-radius: 50%;
                transform: scale(0);
                animation: ripple 0.6s ease-out;
                pointer-events: none;
            `;

      this.style.position = "relative";
      this.style.overflow = "hidden";
      this.appendChild(ripple);

      setTimeout(() => ripple.remove(), 600);
    });
  });

  // Crypto item hover effects
  const cryptoItems = document.querySelectorAll(".crypto-item");
  cryptoItems.forEach((item) => {
    item.addEventListener("mouseenter", function () {
      this.style.transform = "translateY(-8px) scale(1.02)";
    });

    item.addEventListener("mouseleave", function () {
      this.style.transform = "";
    });
  });

  // Stats counter animation
  initStatsCounters();
}

/**
 * Stats Counter Animation
 */
function initStatsCounters() {
  const statNumbers = document.querySelectorAll(".stat-number");

  const animateCounter = (element, target, duration = 2000) => {
    const start = 0;
    const increment = target / (duration / 16);
    let current = start;

    const timer = setInterval(() => {
      current += increment;
      if (current >= target) {
        current = target;
        clearInterval(timer);
      }

      // Format the number
      let displayValue = Math.floor(current).toLocaleString();
      if (element.textContent.includes("M+")) {
        displayValue = (current / 1000000).toFixed(1) + "M+";
      } else if (element.textContent.includes("$")) {
        displayValue = "$" + displayValue;
      } else if (element.textContent.includes("%")) {
        displayValue = current.toFixed(1) + "%";
      } else if (element.textContent.includes("ms")) {
        displayValue = Math.floor(current) + "ms";
      } else if (element.textContent.includes("h")) {
        displayValue = Math.floor(current) + "h";
      } else if (element.textContent.includes("+")) {
        displayValue = displayValue + "+";
      }

      element.textContent = displayValue;
    }, 16);
  };

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (
          entry.isIntersecting &&
          !entry.target.hasAttribute("data-animated")
        ) {
          entry.target.setAttribute("data-animated", "true");

          const text = entry.target.textContent;
          let targetValue = parseFloat(text.replace(/[^\d.]/g, ""));

          if (text.includes("M+")) {
            targetValue = targetValue * 1000000;
          } else if (text.includes("K+")) {
            targetValue = targetValue * 1000;
          }

          animateCounter(entry.target, targetValue);
        }
      });
    },
    { threshold: 0.5 }
  );

  statNumbers.forEach((stat) => observer.observe(stat));
}

/**
 * Footer-specific features initialization
 */
function initFooterSpecificFeatures(templateNumber) {
  switch (templateNumber) {
    case 4: // Neon footer
      initNeonEffects();
      break;
    case 6: // Mobile footer
      initMobileAppDemo();
      break;
    case 8: // Crypto footer
      initCryptoAnimations();
      break;
    case 9: // Tournament footer
      initTournamentFeatures();
      break;
  }
}

/**
 * Neon Effects for Footer 4
 */
function initNeonEffects() {
  const neonElements = document.querySelectorAll(
    ".footer-4 .stat-number, .footer-4 .footer-logo span, .footer-4 .game-category h4"
  );

  neonElements.forEach((element) => {
    element.addEventListener("mouseenter", function () {
      this.style.textShadow = "0 0 20px currentColor, 0 0 30px currentColor";
    });

    element.addEventListener("mouseleave", function () {
      this.style.textShadow = "";
    });
  });
}

/**
 * Mobile App Demo for Footer 6
 */
function initMobileAppDemo() {
  const phoneScreen = document.querySelector(".footer-6 .phone-screen");
  if (!phoneScreen) return;

  // Add interactive elements to phone mockup
  phoneScreen.addEventListener("click", function () {
    this.style.transform = "scale(1.05)";
    setTimeout(() => {
      this.style.transform = "";
    }, 200);
  });
}

/**
 * Crypto Animations for Footer 8
 */
function initCryptoAnimations() {
  const cryptoGrid = document.querySelector(".footer-8 .crypto-grid");
  if (!cryptoGrid) return;

  // Add hover effect to pause animation
  cryptoGrid.addEventListener("mouseenter", function () {
    this.style.animationPlayState = "paused";
  });

  cryptoGrid.addEventListener("mouseleave", function () {
    this.style.animationPlayState = "running";
  });
}

/**
 * Tournament Features for Footer 9
 */
function initTournamentFeatures() {
  const tournamentStats = document.querySelectorAll(
    ".footer-9 .tournament-stat .stat-number"
  );

  // Simulate live updating stats
  setInterval(() => {
    tournamentStats.forEach((stat) => {
      if (stat.textContent.includes(",")) {
        const currentValue = parseInt(stat.textContent.replace(/,/g, ""));
        const newValue = currentValue + Math.floor(Math.random() * 5);
        stat.textContent = newValue.toLocaleString();
      }
    });
  }, 5000);
}

/**
 * Responsive Features
 */
function initResponsiveFeatures() {
  const handleResize = () => {
    const footers = document.querySelectorAll(".modern-footer");
    const isMobile = window.innerWidth <= 768;

    footers.forEach((footer) => {
      // Adjust layout for mobile
      const grids = footer.querySelectorAll('[class*="grid"]');
      grids.forEach((grid) => {
        if (isMobile) {
          grid.style.gridTemplateColumns = "1fr";
        } else {
          grid.style.gridTemplateColumns = "";
        }
      });

      // Hide/show elements based on screen size
      const mobileOnly = footer.querySelectorAll(".mobile-only");
      const desktopOnly = footer.querySelectorAll(".desktop-only");

      mobileOnly.forEach(
        (el) => (el.style.display = isMobile ? "block" : "none")
      );
      desktopOnly.forEach(
        (el) => (el.style.display = isMobile ? "none" : "block")
      );
    });
  };

  window.addEventListener("resize", debounce(handleResize, 250));
  handleResize(); // Initial call
}

/**
 * Accessibility Enhancements
 */
function initAccessibilityEnhancements() {
  // Add ARIA labels to interactive elements
  const socialLinks = document.querySelectorAll(
    ".social-links a, .footer-social a"
  );
  socialLinks.forEach((link) => {
    if (!link.getAttribute("aria-label")) {
      const icon = link.querySelector("i");
      if (icon) {
        const platform = extractSocialPlatform(icon.className);
        link.setAttribute("aria-label", `Follow us on ${platform}`);
      }
    }
  });

  // Add keyboard navigation for accordion
  const accordionHeaders = document.querySelectorAll(".accordion-header");
  accordionHeaders.forEach((header) => {
    header.setAttribute("role", "button");
    header.setAttribute("aria-expanded", "false");
    header.setAttribute("tabindex", "0");
  });

  // Add focus indicators
  const focusableElements = document.querySelectorAll(
    "a, button, input, [tabindex]"
  );
  focusableElements.forEach((element) => {
    element.addEventListener("focus", function () {
      this.style.outline = "2px solid #3b82f6";
      this.style.outlineOffset = "2px";
    });

    element.addEventListener("blur", function () {
      this.style.outline = "";
      this.style.outlineOffset = "";
    });
  });

  // Reduce motion for users who prefer it
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
    const style = document.createElement("style");
    style.textContent = `
            *, *::before, *::after {
                animation-duration: 0.01ms !important;
                animation-iteration-count: 1 !important;
                transition-duration: 0.01ms !important;
            }
        `;
    document.head.appendChild(style);
  }
}

/**
 * Utility Functions
 */
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function showFormMessage(form, message, type) {
  // Remove existing messages
  const existingMessage = form.querySelector(".form-message");
  if (existingMessage) {
    existingMessage.remove();
  }

  // Create new message
  const messageEl = document.createElement("div");
  messageEl.className = `form-message ${type}`;
  messageEl.textContent = message;
  messageEl.style.cssText = `
        margin-top: 1rem;
        padding: 0.5rem 1rem;
        border-radius: 6px;
        font-size: 0.9rem;
        background: ${type === "success" ? "#10b981" : "#ef4444"};
        color: white;
        animation: slideInUp 0.3s ease-out;
    `;

  form.appendChild(messageEl);

  // Auto-remove after 5 seconds
  setTimeout(() => {
    if (messageEl.parentNode) {
      messageEl.style.animation = "slideOutUp 0.3s ease-out";
      setTimeout(() => messageEl.remove(), 300);
    }
  }, 5000);
}

function extractSocialPlatform(className) {
  if (className.includes("facebook")) return "Facebook";
  if (className.includes("twitter")) return "Twitter";
  if (className.includes("instagram")) return "Instagram";
  if (className.includes("youtube")) return "YouTube";
  if (className.includes("discord")) return "Discord";
  if (className.includes("telegram")) return "Telegram";
  if (className.includes("reddit")) return "Reddit";
  if (className.includes("github")) return "GitHub";
  if (className.includes("twitch")) return "Twitch";
  return "Social Media";
}

function debounce(func, wait) {
  let timeout;
  return function executedFunction(...args) {
    const later = () => {
      clearTimeout(timeout);
      func(...args);
    };
    clearTimeout(timeout);
    timeout = setTimeout(later, wait);
  };
}

// Export for external use
window.showFooterTemplate = showFooterTemplate;

// Initialize on page load
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", function () {
    // Re-initialize if DOM was not ready
    setTimeout(() => {
      initFooterTemplateSwitcher();
      initNewsletterForms();
      initAccordionFunctionality();
    }, 100);
  });
}
