// Minimal Footer Component Script

function initMinimalFooter() {
  const footer = document.querySelector(".minimal-footer");
  if (!footer) return;

  const footerLinks = footer.querySelectorAll(".footer-link");

  // Simple fade-in animation on scroll
  const observerOptions = {
    threshold: 0.5,
    rootMargin: "0px 0px -20px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.style.opacity = "1";
        entry.target.style.transform = "translateY(0)";
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Initially hide footer for animation
  footer.style.opacity = "0";
  footer.style.transform = "translateY(20px)";
  footer.style.transition = "opacity 0.8s ease, transform 0.8s ease";

  observer.observe(footer);

  // Simple link interactions
  footerLinks.forEach((link) => {
    link.addEventListener("mouseenter", () => {
      link.style.transform = "translateY(-1px)";
    });

    link.addEventListener("mouseleave", () => {
      link.style.transform = "translateY(0)";
    });
  });

  console.log("✅ Minimal footer initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initMinimalFooter);
} else {
  initMinimalFooter();
}
