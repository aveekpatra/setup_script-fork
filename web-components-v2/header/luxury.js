// Luxury Header Component Script

function initLuxuryHeader() {
  const header = document.querySelector(".luxury-header");
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

  // Active nav link handling with premium animation
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

  // Animate balance on load (luxury feature)
  const balanceAmount = header.querySelector(".balance-amount");
  if (balanceAmount) {
    const targetAmount = balanceAmount.textContent;
    balanceAmount.textContent = "$0.00";

    setTimeout(() => {
      balanceAmount.textContent = targetAmount;
      balanceAmount.style.transition = "all 0.8s ease";
    }, 500);
  }

  console.log("✅ Luxury header initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initLuxuryHeader);
} else {
  initLuxuryHeader();
}
