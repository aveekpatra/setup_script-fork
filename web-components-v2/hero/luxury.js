// Luxury Hero Component Script

function initLuxuryHero() {
  const hero = document.querySelector(".luxury-hero");
  if (!hero) return;

  const statValues = hero.querySelectorAll(".stat-value");
  const benefitItems = hero.querySelectorAll(".benefit-item");
  const vipCard = hero.querySelector(".vip-card");

  // Animate stats on scroll
  const animateStats = () => {
    const statsData = [
      {
        element: statValues[0],
        target: "$50M+",
        start: 0,
        end: 50,
        prefix: "$",
        suffix: "M+",
      },
      {
        element: statValues[1],
        target: "2,500+",
        start: 0,
        end: 2500,
        prefix: "",
        suffix: "+",
      },
      {
        element: statValues[2],
        target: "24/7",
        start: 0,
        end: 24,
        prefix: "",
        suffix: "/7",
      },
      {
        element: statValues[3],
        target: "100%",
        start: 0,
        end: 100,
        prefix: "",
        suffix: "%",
      },
    ];

    statsData.forEach((stat, index) => {
      if (!stat.element) return;

      let current = stat.start;
      const increment = Math.ceil(stat.end / 30);

      const animateStat = () => {
        if (current < stat.end) {
          current += increment;
          if (current > stat.end) current = stat.end;

          if (index === 1) {
            stat.element.textContent = `${current.toLocaleString()}${
              stat.suffix
            }`;
          } else {
            stat.element.textContent = `${stat.prefix}${current}${stat.suffix}`;
          }

          requestAnimationFrame(animateStat);
        }
      };

      setTimeout(animateStat, index * 200);
    });
  };

  // Observe stats section for animation trigger
  const observerOptions = {
    threshold: 0.3,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        animateStats();
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const statsContainer = hero.querySelector(".hero-stats");
  if (statsContainer) {
    observer.observe(statsContainer);
  }

  // Animate benefit items with staggered entrance
  if (benefitItems.length > 0) {
    const benefitsObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          const items = entry.target.querySelectorAll(".benefit-item");
          items.forEach((item, index) => {
            setTimeout(() => {
              item.style.opacity = "1";
              item.style.transform = "translateX(0)";
            }, index * 150);
          });
          benefitsObserver.unobserve(entry.target);
        }
      });
    }, observerOptions);

    const benefitsContainer = hero.querySelector(".vip-benefits");
    if (benefitsContainer) {
      // Initially hide benefit items
      benefitItems.forEach((item) => {
        item.style.opacity = "0";
        item.style.transform = "translateX(-20px)";
        item.style.transition = "opacity 0.6s ease, transform 0.6s ease";
      });

      benefitsObserver.observe(benefitsContainer);
    }
  }

  // Enhanced VIP card interactions
  if (vipCard) {
    vipCard.addEventListener("mouseenter", () => {
      vipCard.style.transform = "translateY(-5px) scale(1.02)";
      vipCard.style.boxShadow = `
        ${getComputedStyle(document.documentElement).getPropertyValue(
          "--shadow-large"
        )},
        0 20px 40px rgba(255, 215, 0, 0.3)
      `;
    });

    vipCard.addEventListener("mouseleave", () => {
      vipCard.style.transform = "translateY(0) scale(1)";
      vipCard.style.boxShadow = getComputedStyle(
        document.documentElement
      ).getPropertyValue("--shadow-large");
    });
  }

  // Premium button effects
  const buttons = hero.querySelectorAll(".btn");
  buttons.forEach((button) => {
    button.addEventListener("mouseenter", () => {
      if (button.classList.contains("btn-primary")) {
        button.style.transform = "translateY(-3px)";
      } else {
        button.style.transform = "translateY(-2px)";
      }
    });

    button.addEventListener("mouseleave", () => {
      button.style.transform = "translateY(0)";
    });
  });

  // Crown animation enhancement
  const crown = hero.querySelector(".hero-crown");
  if (crown) {
    crown.addEventListener("mouseenter", () => {
      crown.style.animation = "crown-glow 0.5s ease-in-out 3";
    });

    crown.addEventListener("animationend", (e) => {
      if (e.animationName === "crown-glow" && e.target === crown) {
        crown.style.animation = "crown-glow 3s ease-in-out infinite alternate";
      }
    });
  }

  console.log("✅ Luxury hero initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initLuxuryHero);
} else {
  initLuxuryHero();
}
