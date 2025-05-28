// Minimal Header Component Script

function initMinimalHeader() {
  const header = document.querySelector(".minimal-header");
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

  console.log("✅ Minimal header initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initMinimalHeader);
} else {
  initMinimalHeader();
}
