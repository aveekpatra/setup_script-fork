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
