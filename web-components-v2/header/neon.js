// Neon Header Component Script

function initNeonHeader() {
  const header = document.querySelector(".neon-header");
  if (!header) return;

  const mobileToggle = header.querySelector(".mobile-toggle");
  const navLinks = header.querySelectorAll(".nav-link");
  const mobileNavLinks = header.querySelectorAll(".mobile-nav-link");
  const energyFill = header.querySelector(".energy-fill");
  const energyValue = header.querySelector(".energy-value");

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

  // Active nav link handling with neon effects
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

  // Animate energy bar on load
  if (energyFill && energyValue) {
    let currentEnergy = 0;
    const targetEnergy = 87;

    const animateEnergy = () => {
      if (currentEnergy < targetEnergy) {
        currentEnergy += Math.ceil((targetEnergy - currentEnergy) / 10);
        energyFill.style.setProperty("--energy-width", `${currentEnergy}%`);
        energyValue.textContent = `${currentEnergy}%`;
        requestAnimationFrame(animateEnergy);
      }
    };

    setTimeout(animateEnergy, 300);
  }

  // Cyberpunk glitch effect on logo hover
  const logoIcon = header.querySelector(".logo-icon");
  if (logoIcon) {
    logoIcon.addEventListener("mouseenter", () => {
      logoIcon.style.animation = "pulse-glow 0.1s ease-in-out 3";
    });

    logoIcon.addEventListener("animationend", () => {
      logoIcon.style.animation = "pulse-glow 2s ease-in-out infinite alternate";
    });
  }

  console.log("✅ Neon header initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initNeonHeader);
} else {
  initNeonHeader();
}
