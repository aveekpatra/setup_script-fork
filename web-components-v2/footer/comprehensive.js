// Comprehensive Footer Component Script

function initComprehensiveFooter() {
  const footer = document.querySelector(".comprehensive-footer");
  if (!footer) return;

  const newsletterForm = footer.querySelector(".newsletter-form");
  const newsletterInput = footer.querySelector(".newsletter-input");
  const socialLinks = footer.querySelectorAll(".social-link");
  const footerLinks = footer.querySelectorAll(".footer-link");
  const linkSections = footer.querySelectorAll(".link-section");
  const complianceBadges = footer.querySelectorAll(".compliance-badge");

  // Newsletter form handling
  if (newsletterForm && newsletterInput) {
    newsletterForm.addEventListener("submit", (e) => {
      e.preventDefault();
      const email = newsletterInput.value.trim();

      if (email && isValidEmail(email)) {
        // Simulate subscription success
        showNewsletterSuccess(newsletterForm);
      } else {
        showNewsletterError(newsletterInput);
      }
    });

    // Real-time email validation
    newsletterInput.addEventListener("input", () => {
      const email = newsletterInput.value.trim();
      if (email && isValidEmail(email)) {
        newsletterInput.style.borderColor = "var(--color-success)";
      } else if (email) {
        newsletterInput.style.borderColor = "var(--color-error)";
      } else {
        newsletterInput.style.borderColor = "var(--color-border)";
      }
    });
  }

  // Animate footer sections on scroll
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -30px 0px",
  };

  // Newsletter animation
  const newsletterObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const content = entry.target.querySelector(".newsletter-content");
        if (content) {
          setTimeout(() => {
            content.style.opacity = "1";
            content.style.transform = "translateY(0)";
          }, 100);
        }
        newsletterObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Footer links animation
  const linksObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const sections = entry.target.querySelectorAll(".link-section");
        sections.forEach((section, index) => {
          setTimeout(() => {
            section.style.opacity = "1";
            section.style.transform = "translateY(0)";
          }, index * 100);
        });
        linksObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Compliance badges animation
  const badgesObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const badges = entry.target.querySelectorAll(".compliance-badge");
        badges.forEach((badge, index) => {
          setTimeout(() => {
            badge.style.opacity = "1";
            badge.style.transform = "translateY(0)";
          }, index * 150);
        });
        badgesObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Initialize animations
  const newsletterSection = footer.querySelector(".footer-newsletter");
  const footerLinksContainer = footer.querySelector(".footer-links");
  const complianceSection = footer.querySelector(".compliance-logos");

  if (newsletterSection) {
    const content = newsletterSection.querySelector(".newsletter-content");
    if (content) {
      content.style.opacity = "0";
      content.style.transform = "translateY(30px)";
      content.style.transition = "opacity 0.8s ease, transform 0.8s ease";
    }
    newsletterObserver.observe(newsletterSection);
  }

  if (footerLinksContainer) {
    linkSections.forEach((section) => {
      section.style.opacity = "0";
      section.style.transform = "translateY(20px)";
      section.style.transition = "opacity 0.6s ease, transform 0.6s ease";
    });
    linksObserver.observe(footerLinksContainer);
  }

  if (complianceSection) {
    complianceBadges.forEach((badge) => {
      badge.style.opacity = "0";
      badge.style.transform = "translateY(10px)";
      badge.style.transition = "opacity 0.5s ease, transform 0.5s ease";
    });
    badgesObserver.observe(complianceSection);
  }

  // Enhanced social link interactions
  socialLinks.forEach((link) => {
    link.addEventListener("mouseenter", () => {
      link.style.transform = "translateY(-3px) scale(1.1)";
    });

    link.addEventListener("mouseleave", () => {
      link.style.transform = "translateY(0) scale(1)";
    });
  });

  // Footer link hover effects
  footerLinks.forEach((link) => {
    link.addEventListener("mouseenter", () => {
      link.style.transform = "translateX(3px)";
    });

    link.addEventListener("mouseleave", () => {
      link.style.transform = "translateX(0)";
    });
  });

  // Compliance badge hover effects
  complianceBadges.forEach((badge) => {
    badge.addEventListener("mouseenter", () => {
      badge.style.transform = "translateY(-2px)";
      badge.style.boxShadow = "var(--shadow-small)";
    });

    badge.addEventListener("mouseleave", () => {
      badge.style.transform = "translateY(0)";
      badge.style.boxShadow = "none";
    });
  });

  console.log("✅ Comprehensive footer initialized");
}

// Helper functions
function isValidEmail(email) {
  const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return emailRegex.test(email);
}

function showNewsletterSuccess(form) {
  const button = form.querySelector(".newsletter-button");
  const originalText = button.textContent;

  button.textContent = "✓ Subscribed!";
  button.style.background = "var(--color-success)";
  button.disabled = true;

  setTimeout(() => {
    button.textContent = originalText;
    button.style.background = "var(--color-primary)";
    button.disabled = false;
    form.reset();
  }, 3000);
}

function showNewsletterError(input) {
  input.style.borderColor = "var(--color-error)";
  input.style.animation = "shake 0.5s ease-in-out";

  setTimeout(() => {
    input.style.animation = "";
    input.style.borderColor = "var(--color-border)";
  }, 500);
}

// Add shake animation for error states
const style = document.createElement("style");
style.textContent = `
  @keyframes shake {
    0%, 100% { transform: translateX(0); }
    10%, 30%, 50%, 70%, 90% { transform: translateX(-5px); }
    20%, 40%, 60%, 80% { transform: translateX(5px); }
  }
`;
document.head.appendChild(style);

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initComprehensiveFooter);
} else {
  initComprehensiveFooter();
}
