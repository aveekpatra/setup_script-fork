// Modern Casino Hero JavaScript

document.addEventListener("DOMContentLoaded", function () {
  // Initialize all hero functionalities
  initTypingEffect();
  initJackpotCounter();
  initCountdownTimer();
  initGameCategoryInteraction();
  initParticleAnimations();
  initScrollAnimations();
  initHeroTemplateSystem();
});

/**
 * Typing Effect for Hero 2
 */
function initTypingEffect() {
  const typingElement = document.querySelector(".typing-text");
  if (!typingElement) return;

  const words = typingElement.dataset.words.split(",");
  let currentWord = 0;
  let currentChar = 0;
  let isDeleting = false;

  function typeEffect() {
    const currentText = words[currentWord];

    if (isDeleting) {
      typingElement.textContent = currentText.substring(0, currentChar - 1);
      currentChar--;
    } else {
      typingElement.textContent = currentText.substring(0, currentChar + 1);
      currentChar++;
    }

    if (!isDeleting && currentChar === currentText.length) {
      setTimeout(() => (isDeleting = true), 1500);
    } else if (isDeleting && currentChar === 0) {
      isDeleting = false;
      currentWord = (currentWord + 1) % words.length;
    }

    const typingSpeed = isDeleting ? 50 : 100;
    setTimeout(typeEffect, typingSpeed);
  }

  typeEffect();
}

/**
 * Jackpot Counter Animation for Hero 6
 */
function initJackpotCounter() {
  const jackpotAmount = document.querySelector(".jackpot-amount");
  if (!jackpotAmount) return;

  let currentAmount = parseInt(jackpotAmount.dataset.target);

  // Animate jackpot increasing
  setInterval(() => {
    const increase = Math.floor(Math.random() * 100) + 50;
    currentAmount += increase;

    // Add animation class
    jackpotAmount.classList.add("jackpot-increase");
    jackpotAmount.textContent = "$" + currentAmount.toLocaleString();

    // Remove animation class after animation
    setTimeout(() => {
      jackpotAmount.classList.remove("jackpot-increase");
    }, 500);

    // Update data attribute
    jackpotAmount.dataset.target = currentAmount;
  }, 3000);
}

/**
 * Countdown Timer for Hero 6
 */
function initCountdownTimer() {
  const hoursElement = document.getElementById("hours");
  const minutesElement = document.getElementById("minutes");
  const secondsElement = document.getElementById("seconds");

  if (!hoursElement || !minutesElement || !secondsElement) return;

  function updateCountdown() {
    let h = parseInt(hoursElement.textContent);
    let m = parseInt(minutesElement.textContent);
    let s = parseInt(secondsElement.textContent);

    s--;
    if (s < 0) {
      s = 59;
      m--;
      if (m < 0) {
        m = 59;
        h--;
        if (h < 0) {
          h = 23; // Reset to 24 hours
          m = 59;
          s = 59;
        }
      }
    }

    hoursElement.textContent = h.toString().padStart(2, "0");
    minutesElement.textContent = m.toString().padStart(2, "0");
    secondsElement.textContent = s.toString().padStart(2, "0");

    // Add pulse effect on seconds change
    secondsElement.parentElement.classList.add("timer-pulse");
    setTimeout(() => {
      secondsElement.parentElement.classList.remove("timer-pulse");
    }, 200);
  }

  setInterval(updateCountdown, 1000);
}

/**
 * Game Category Interaction for Hero 4
 */
function initGameCategoryInteraction() {
  const gameCategories = document.querySelectorAll(".game-category");
  if (gameCategories.length === 0) return;

  gameCategories.forEach((category) => {
    category.addEventListener("click", function () {
      // Remove active class from all categories
      gameCategories.forEach((cat) => cat.classList.remove("active"));

      // Add active class to clicked category
      this.classList.add("active");

      // Trigger mini-game animation
      const miniGames = this.querySelectorAll(".mini-game");
      miniGames.forEach((game, index) => {
        setTimeout(() => {
          game.style.transform = "scale(1.2)";
          setTimeout(() => {
            game.style.transform = "scale(1)";
          }, 150);
        }, index * 100);
      });

      // Update button text based on selected category
      const selectedCategory = this.querySelector("h3").textContent;
      const actionButton = document.querySelector(".hero-4 .btn-primary");
      if (actionButton) {
        actionButton.textContent = `Play ${selectedCategory}`;
      }
    });

    // Hover effects
    category.addEventListener("mouseenter", function () {
      const icon = this.querySelector(".category-icon");
      if (icon) {
        icon.style.transform = "scale(1.1) rotate(5deg)";
      }
    });

    category.addEventListener("mouseleave", function () {
      const icon = this.querySelector(".category-icon");
      if (icon) {
        icon.style.transform = "scale(1) rotate(0deg)";
      }
    });
  });
}

/**
 * Particle Animations for Hero 1
 */
function initParticleAnimations() {
  const particleContainers = document.querySelectorAll(
    ".particles-bg, .money-rain"
  );

  particleContainers.forEach((container) => {
    // Add more dynamic particles
    if (container.classList.contains("particles-bg")) {
      createFloatingParticles(container);
    } else if (container.classList.contains("money-rain")) {
      enhanceMoneyRain(container);
    }
  });
}

function createFloatingParticles(container) {
  // Create additional floating elements
  for (let i = 0; i < 10; i++) {
    const particle = document.createElement("div");
    particle.className = "dynamic-particle";
    particle.style.cssText = `
            position: absolute;
            width: ${Math.random() * 6 + 2}px;
            height: ${Math.random() * 6 + 2}px;
            background: rgba(255, 255, 255, ${Math.random() * 0.5 + 0.2});
            border-radius: 50%;
            top: ${Math.random() * 100}%;
            left: ${Math.random() * 100}%;
            animation: dynamicFloat ${
              Math.random() * 10 + 5
            }s ease-in-out infinite;
            animation-delay: ${Math.random() * 5}s;
        `;
    container.appendChild(particle);
  }

  // Add CSS animation if not exists
  if (!document.getElementById("dynamic-particles-style")) {
    const style = document.createElement("style");
    style.id = "dynamic-particles-style";
    style.textContent = `
            @keyframes dynamicFloat {
                0%, 100% { 
                    transform: translateY(0px) translateX(0px) rotate(0deg);
                    opacity: 0.3;
                }
                25% { 
                    transform: translateY(-20px) translateX(10px) rotate(90deg);
                    opacity: 1;
                }
                50% { 
                    transform: translateY(-10px) translateX(-15px) rotate(180deg);
                    opacity: 0.7;
                }
                75% { 
                    transform: translateY(-30px) translateX(5px) rotate(270deg);
                    opacity: 0.9;
                }
            }
            .timer-pulse {
                animation: timerPulse 0.3s ease-out;
            }
            @keyframes timerPulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.05); }
                100% { transform: scale(1); }
            }
            .jackpot-increase {
                animation: jackpotBounce 0.5s ease-out;
            }
            @keyframes jackpotBounce {
                0% { transform: scale(1); }
                50% { transform: scale(1.1); }
                100% { transform: scale(1); }
            }
        `;
    document.head.appendChild(style);
  }
}

function enhanceMoneyRain(container) {
  // Add more money bills dynamically
  setInterval(() => {
    const bill = document.createElement("div");
    bill.className = "dynamic-money-bill";
    bill.style.cssText = `
            position: absolute;
            width: ${Math.random() * 15 + 15}px;
            height: ${Math.random() * 20 + 30}px;
            background: linear-gradient(135deg, #228B22, #32CD32);
            border-radius: 2px;
            left: ${Math.random() * 100}%;
            top: -50px;
            animation: dynamicMoneyFall ${
              Math.random() * 2 + 3
            }s linear forwards;
            box-shadow: 0 2px 5px rgba(0,0,0,0.3);
        `;
    container.appendChild(bill);

    // Remove after animation
    setTimeout(() => {
      if (bill.parentNode) {
        bill.parentNode.removeChild(bill);
      }
    }, 5000);
  }, 1000);

  // Add CSS for dynamic money fall
  if (!document.getElementById("dynamic-money-style")) {
    const style = document.createElement("style");
    style.id = "dynamic-money-style";
    style.textContent = `
            @keyframes dynamicMoneyFall {
                0% {
                    transform: translateY(-50px) rotate(0deg);
                    opacity: 1;
                }
                100% {
                    transform: translateY(calc(100vh + 100px)) rotate(${
                      Math.random() * 720 - 360
                    }deg);
                    opacity: 0;
                }
            }
        `;
    document.head.appendChild(style);
  }
}

/**
 * Scroll Animations
 */
function initScrollAnimations() {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const hero = entry.target;

        // Trigger entrance animations
        const animatedElements = hero.querySelectorAll(
          ".hero-title, .hero-description, .hero-actions, .hero-stats"
        );
        animatedElements.forEach((element, index) => {
          setTimeout(() => {
            element.style.opacity = "1";
            element.style.transform = "translateY(0)";
          }, index * 200);
        });

        // Special animations for specific heroes
        if (hero.classList.contains("hero-5")) {
          setTimeout(() => {
            const neonElements = hero.querySelectorAll(
              ".neon-text, .neon-border"
            );
            neonElements.forEach((el) => {
              el.style.animation = "neonFlicker 3s ease-in-out infinite";
            });
          }, 500);
        }

        if (hero.classList.contains("hero-9")) {
          setTimeout(() => {
            const competitionElements = hero.querySelectorAll(
              ".trophy-icon, .medal-icon, .star-icon"
            );
            competitionElements.forEach((el, index) => {
              setTimeout(() => {
                el.style.opacity = "1";
                el.style.transform = "scale(1.2)";
                setTimeout(() => {
                  el.style.transform = "scale(1)";
                }, 300);
              }, index * 200);
            });
          }, 800);
        }
      }
    });
  }, observerOptions);

  // Observe all hero sections
  document.querySelectorAll(".modern-hero").forEach((hero) => {
    // Set initial state for animated elements
    const animatedElements = hero.querySelectorAll(
      ".hero-title, .hero-description, .hero-actions, .hero-stats"
    );
    animatedElements.forEach((element) => {
      element.style.opacity = "0";
      element.style.transform = "translateY(30px)";
      element.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    });

    observer.observe(hero);
  });
}

/**
 * Hero Template System
 */
function initHeroTemplateSystem() {
  // Global template switcher function
  window.showHeroTemplate = function (templateNumber) {
    // Hide all heroes
    const allHeroes = document.querySelectorAll(".modern-hero");
    allHeroes.forEach((hero) => {
      hero.style.display = "none";
    });

    // Show selected hero
    const selectedHero = document.getElementById(`hero-${templateNumber}`);
    if (selectedHero) {
      selectedHero.style.display = "block";

      // Trigger entrance animation
      setTimeout(() => {
        const animatedElements = selectedHero.querySelectorAll(
          ".hero-title, .hero-description, .hero-actions"
        );
        animatedElements.forEach((element, index) => {
          element.style.opacity = "0";
          element.style.transform = "translateY(30px)";

          setTimeout(() => {
            element.style.opacity = "1";
            element.style.transform = "translateY(0)";
          }, index * 150);
        });
      }, 100);

      // Update URL hash
      window.location.hash = `hero-${templateNumber}`;

      // Reinitialize specific hero functionalities
      setTimeout(() => {
        if (templateNumber === 2) initTypingEffect();
        if (templateNumber === 4) initGameCategoryInteraction();
        if (templateNumber === 6) {
          initJackpotCounter();
          initCountdownTimer();
        }
      }, 200);
    }

    // Update active button
    const buttons = document.querySelectorAll(".template-switcher button");
    buttons.forEach((btn) => btn.classList.remove("active"));
    const activeButton = document.querySelector(
      `[onclick="showHeroTemplate(${templateNumber})"]`
    );
    if (activeButton) {
      activeButton.classList.add("active");
    }
  };

  // Set active hero from URL hash on load
  const hash = window.location.hash;
  if (hash && hash.startsWith("#hero-")) {
    const heroNumber = parseInt(hash.replace("#hero-", ""));
    if (heroNumber >= 1 && heroNumber <= 10) {
      showHeroTemplate(heroNumber);
    }
  }
}

/**
 * Button Interaction Enhancements
 */
function initButtonEnhancements() {
  // Add ripple effect to all CTA buttons
  const buttons = document.querySelectorAll(
    ".btn-primary, .btn-secondary, .btn-luxury, .btn-neon, .btn-glass, .btn-mobile, .btn-tournament, .btn-jackpot, .btn-minimal"
  );

  buttons.forEach((button) => {
    button.addEventListener("click", function (e) {
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
                background: rgba(255,255,255,0.4);
                border-radius: 50%;
                transform: scale(0);
                animation: rippleEffect 0.6s ease-out;
                pointer-events: none;
                z-index: 1;
            `;

      this.style.position = "relative";
      this.style.overflow = "hidden";
      this.appendChild(ripple);

      setTimeout(() => {
        ripple.remove();
      }, 600);
    });
  });

  // Add ripple animation CSS
  if (!document.getElementById("ripple-style")) {
    const style = document.createElement("style");
    style.id = "ripple-style";
    style.textContent = `
            @keyframes rippleEffect {
                to {
                    transform: scale(2);
                    opacity: 0;
                }
            }
        `;
    document.head.appendChild(style);
  }
}

// Initialize button enhancements
document.addEventListener("DOMContentLoaded", initButtonEnhancements);

/**
 * Mobile Optimizations
 */
function initMobileOptimizations() {
  if (window.innerWidth <= 768) {
    // Reduce particle count on mobile
    const particles = document.querySelectorAll(".particle, .dynamic-particle");
    particles.forEach((particle, index) => {
      if (index % 2 === 0) {
        particle.style.display = "none";
      }
    });

    // Simplify animations on mobile
    const animatedElements = document.querySelectorAll(
      ".neon-text, .glass-text, .tournament-text"
    );
    animatedElements.forEach((element) => {
      element.style.animation = "none";
    });
  }
}

// Initialize mobile optimizations
document.addEventListener("DOMContentLoaded", initMobileOptimizations);
window.addEventListener("resize", initMobileOptimizations);

/**
 * Accessibility Enhancements
 */
function initAccessibilityEnhancements() {
  // Add keyboard navigation for template switcher
  const switcherButtons = document.querySelectorAll(
    ".template-switcher button"
  );
  switcherButtons.forEach((button, index) => {
    button.addEventListener("keydown", function (e) {
      if (e.key === "ArrowRight" || e.key === "ArrowDown") {
        e.preventDefault();
        const nextIndex = (index + 1) % switcherButtons.length;
        switcherButtons[nextIndex].focus();
      } else if (e.key === "ArrowLeft" || e.key === "ArrowUp") {
        e.preventDefault();
        const prevIndex =
          (index - 1 + switcherButtons.length) % switcherButtons.length;
        switcherButtons[prevIndex].focus();
      }
    });
  });

  // Add ARIA labels and descriptions
  const heroes = document.querySelectorAll(".modern-hero");
  heroes.forEach((hero, index) => {
    hero.setAttribute("role", "region");
    hero.setAttribute("aria-label", `Hero section ${index + 1}`);
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

// Initialize accessibility enhancements
document.addEventListener("DOMContentLoaded", initAccessibilityEnhancements);
