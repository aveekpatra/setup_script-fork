// Minimal Hero Component Script

function initMinimalHero() {
  const hero = document.querySelector(".minimal-hero");
  if (!hero) return;

  const button = hero.querySelector(".btn");
  const title = hero.querySelector(".hero-title");

  // Simple button interaction
  if (button) {
    button.addEventListener("mouseenter", () => {
      button.style.transform = "translateY(-2px)";
    });

    button.addEventListener("mouseleave", () => {
      button.style.transform = "translateY(0)";
    });

    button.addEventListener("mousedown", () => {
      button.style.transform = "translateY(0)";
    });

    button.addEventListener("mouseup", () => {
      button.style.transform = "translateY(-2px)";
    });
  }

  // Subtle title animation on load
  if (title) {
    title.style.opacity = "0";
    title.style.transform = "translateY(20px)";

    setTimeout(() => {
      title.style.transition = "opacity 1s ease, transform 1s ease";
      title.style.opacity = "1";
      title.style.transform = "translateY(0)";
    }, 200);
  }

  console.log("✅ Minimal hero initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initMinimalHero);
} else {
  initMinimalHero();
}
