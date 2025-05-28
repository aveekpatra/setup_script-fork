// Modern Footer Component Script

function initModernFooter() {
  const footer = document.querySelector(".modern-footer");
  if (!footer) return;

  const socialLinks = footer.querySelectorAll(".social-link");
  const footerLinks = footer.querySelectorAll(".footer-link");
  const linkSections = footer.querySelectorAll(".link-section");

  // Animate footer sections on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -50px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const sections = entry.target.querySelectorAll(".link-section");
        sections.forEach((section, index) => {
          setTimeout(() => {
            section.style.opacity = "1";
            section.style.transform = "translateY(0)";
          }, index * 100);
        });
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const footerLinksContainer = footer.querySelector(".footer-links");
  if (footerLinksContainer) {
    // Initially hide sections
    linkSections.forEach((section) => {
      section.style.opacity = "0";
      section.style.transform = "translateY(20px)";
      section.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    });

    observer.observe(footerLinksContainer);
  }

  // Enhanced social link interactions
  socialLinks.forEach((link) => {
    link.addEventListener("mouseenter", () => {
      link.style.transform = "translateY(-2px) scale(1.1)";
    });

    link.addEventListener("mouseleave", () => {
      link.style.transform = "translateY(0) scale(1)";
    });
  });

  // Footer link hover effects with stagger
  footerLinks.forEach((link, index) => {
    link.addEventListener("mouseenter", () => {
      link.style.transform = "translateX(4px)";
    });

    link.addEventListener("mouseleave", () => {
      link.style.transform = "translateX(0)";
    });
  });

  console.log("✅ Modern footer initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initModernFooter);
} else {
  initModernFooter();
}
