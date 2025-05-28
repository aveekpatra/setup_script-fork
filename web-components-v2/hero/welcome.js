// Welcome Hero Component Script

function initWelcomeHero() {
  const hero = document.querySelector(".welcome-hero");
  if (!hero) return;

  const bonusPercent = hero.querySelector(".bonus-percent");
  const bonusSpins = hero.querySelector(".bonus-spins");
  const featureItems = hero.querySelectorAll(".feature-item");

  // Animate bonus values on load
  if (bonusPercent && bonusSpins) {
    const targetPercent = 200;
    const targetSpins = 100;
    let currentPercent = 0;
    let currentSpins = 0;

    const animateBonus = () => {
      if (currentPercent < targetPercent) {
        currentPercent += Math.ceil((targetPercent - currentPercent) / 15);
        bonusPercent.textContent = `${currentPercent}%`;
      }

      if (currentSpins < targetSpins) {
        currentSpins += Math.ceil((targetSpins - currentSpins) / 12);
        bonusSpins.textContent = `${currentSpins} Spins`;
      }

      if (currentPercent < targetPercent || currentSpins < targetSpins) {
        requestAnimationFrame(animateBonus);
      }
    };

    // Start animation after a brief delay
    setTimeout(animateBonus, 500);
  }

  // Animate feature items on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const items = entry.target.querySelectorAll(".feature-item");
        items.forEach((item, index) => {
          setTimeout(() => {
            item.style.opacity = "1";
            item.style.transform = "translateY(0)";
          }, index * 100);
        });
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const featuresContainer = hero.querySelector(".hero-features");
  if (featuresContainer) {
    // Initially hide feature items
    featureItems.forEach((item) => {
      item.style.opacity = "0";
      item.style.transform = "translateY(20px)";
      item.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    });

    observer.observe(featuresContainer);
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

  console.log("✅ Welcome hero initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initWelcomeHero);
} else {
  initWelcomeHero();
}
