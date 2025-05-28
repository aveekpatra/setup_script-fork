// Luxury Footer Component Script

function initLuxuryFooter() {
  const footer = document.querySelector(".luxury-footer");
  if (!footer) return;

  const vipIcon = footer.querySelector(".vip-icon");
  const vipButton = footer.querySelector(".vip-button");
  const footerLinks = footer.querySelectorAll(".footer-link");
  const linkSections = footer.querySelectorAll(".link-section");
  const awardItems = footer.querySelectorAll(".award-item");

  // Animate footer sections with luxury timing
  const observerOptions = {
    threshold: 0.1,
    rootMargin: "0px 0px -30px 0px",
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const sections = entry.target.querySelectorAll(".link-section");
        sections.forEach((section, index) => {
          setTimeout(() => {
            section.style.opacity = "1";
            section.style.transform = "translateY(0)";
          }, index * 150);
        });
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  // Animate VIP section
  const vipObserver = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const vipContact = entry.target.querySelector(".vip-contact");
        if (vipContact) {
          setTimeout(() => {
            vipContact.style.opacity = "1";
            vipContact.style.transform = "translateY(0)";
          }, 200);
        }
        vipObserver.unobserve(entry.target);
      }
    });
  }, observerOptions);

  const footerLinksContainer = footer.querySelector(".footer-links");
  const vipSection = footer.querySelector(".footer-vip");

  if (footerLinksContainer) {
    // Initially hide sections
    linkSections.forEach((section) => {
      section.style.opacity = "0";
      section.style.transform = "translateY(30px)";
      section.style.transition = "opacity 0.8s ease, transform 0.8s ease";
    });

    observer.observe(footerLinksContainer);
  }

  if (vipSection) {
    const vipContact = vipSection.querySelector(".vip-contact");
    if (vipContact) {
      vipContact.style.opacity = "0";
      vipContact.style.transform = "translateY(20px)";
      vipContact.style.transition = "opacity 1s ease, transform 1s ease";
    }
    vipObserver.observe(vipSection);
  }

  // Enhanced VIP crown animation
  if (vipIcon) {
    vipIcon.addEventListener("mouseenter", () => {
      vipIcon.style.animation = "crown-glow 0.5s ease-in-out 3";
      vipIcon.style.transform = "scale(1.1) rotate(5deg)";
    });

    vipIcon.addEventListener("mouseleave", () => {
      vipIcon.style.transform = "scale(1) rotate(0deg)";
      setTimeout(() => {
        vipIcon.style.animation =
          "crown-glow 3s ease-in-out infinite alternate";
      }, 300);
    });
  }

  // Premium VIP button effects
  if (vipButton) {
    vipButton.addEventListener("mouseenter", () => {
      vipButton.style.transform = "translateY(-3px) scale(1.05)";
      vipButton.style.boxShadow = `
        ${getComputedStyle(document.documentElement).getPropertyValue(
          "--shadow-large"
        )},
        0 15px 35px rgba(255, 215, 0, 0.5)
      `;
    });

    vipButton.addEventListener("mouseleave", () => {
      vipButton.style.transform = "translateY(0) scale(1)";
      vipButton.style.boxShadow = getComputedStyle(
        document.documentElement
      ).getPropertyValue("--shadow-medium");
    });
  }

  // Luxury footer link interactions
  footerLinks.forEach((link, index) => {
    link.addEventListener("mouseenter", () => {
      link.style.transform = "translateX(8px)";
      // Add sparkle effect
      const sparkle = document.createElement("span");
      sparkle.innerHTML = "✦";
      sparkle.style.position = "absolute";
      sparkle.style.left = "-15px";
      sparkle.style.color = "var(--color-gold)";
      sparkle.style.fontSize = "0.8rem";
      sparkle.style.opacity = "1";
      sparkle.style.transition = "opacity 0.3s ease";
      link.style.position = "relative";
      link.appendChild(sparkle);

      setTimeout(() => {
        if (sparkle.parentNode) {
          sparkle.style.opacity = "0";
          setTimeout(() => {
            if (sparkle.parentNode) sparkle.remove();
          }, 300);
        }
      }, 500);
    });

    link.addEventListener("mouseleave", () => {
      link.style.transform = "translateX(0)";
    });
  });

  // Animate awards on scroll
  if (awardItems.length > 0) {
    const awardsObserver = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          awardItems.forEach((item, index) => {
            setTimeout(() => {
              item.style.opacity = "1";
              item.style.transform = "translateX(0)";
            }, index * 200);
          });
          awardsObserver.unobserve(entry.target);
        }
      });
    }, observerOptions);

    const brandsSection = footer.querySelector(".footer-brand");
    if (brandsSection) {
      awardItems.forEach((item) => {
        item.style.opacity = "0";
        item.style.transform = "translateX(-20px)";
        item.style.transition = "opacity 0.6s ease, transform 0.6s ease";
      });

      awardsObserver.observe(brandsSection);
    }
  }

  console.log("✅ Luxury footer initialized");
}

// Initialize when DOM is ready
if (document.readyState === "loading") {
  document.addEventListener("DOMContentLoaded", initLuxuryFooter);
} else {
  initLuxuryFooter();
}
