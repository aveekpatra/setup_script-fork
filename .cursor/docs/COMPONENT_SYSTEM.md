# Component System Documentation

## Overview

The component system is the core of the casino website generator. Each component represents a section of a casino website (header, hero, footer, etc.) and contains multiple template variants to ensure design diversity.

## Component Directory Structure

```
web-components/
├── header/             # Navigation and branding
│   ├── header.html    # 10 HTML template variants
│   ├── header.css     # 10 CSS template variants
│   └── header.js      # 10 JS template variants
├── footer/             # Footer sections
│   ├── footer.html    # 10 HTML template variants
│   ├── footer.css     # 10 CSS template variants
│   └── footer.js      # 10 JS template variants
├── hero/               # Main hero sections
│   ├── hero.html      # 10 HTML template variants
│   ├── hero.css       # 10 CSS template variants
│   └── hero.js        # 10 JS template variants
├── offers/             # Casino offers/promotions (may be empty)
├── details_comparison/ # Casino comparison tables
├── why_us/            # Why choose us sections
├── about/             # About us content
├── history/           # Company history
├── guide/             # Gaming guides
└── faqs/              # FAQ sections with accordions
```

## Template Structure

### Template Marking System

Each template within a component file is marked with specific comment syntax:

**HTML Templates:**

```html
<!-- Template 1: Standard Professional Header -->
<header class="modern-header header-1">
  <!-- Template content here -->
</header>

<!-- Template 2: Two-Row Header with Top Bar -->
<header class="modern-header header-2">
  <!-- Template content here -->
</header>
```

**CSS Templates:**

```css
/* Template 1: Standard Professional Header */
.header-1 {
  /* Template styles here */
}

/* Template 2: Two-Row Header with Top Bar */
.header-2 {
  /* Template styles here */
}
```

**JavaScript Templates:**

```javascript
// Template 1: Standard Professional Header
function initHeader1() {
  // Template functionality here
}

// Template 2: Two-Row Header with Top Bar
function initHeader2() {
  // Template functionality here
}
```

### Template Numbering

- Each component contains exactly **10 template variants**
- Templates are numbered sequentially: **Template 1** through **Template 10**
- Numbering must be consistent across HTML, CSS, and JS files
- Template names should be descriptive and unique

## Component Processing

### Processing Order

Components are processed in this exact order:

1. **header** - Site navigation and branding
2. **hero** - Main hero/banner section
3. **offers** - Casino offers and promotions
4. **details_comparison** - Detailed casino comparisons
5. **why_us** - Why choose us content
6. **about** - About us information
7. **history** - Company/site history
8. **guide** - Gaming guides and tutorials
9. **faqs** - Frequently asked questions
10. **footer** - Footer with legal info

### Selection Algorithm

1. **Extract all templates** from each component file using regex
2. **Group templates by name** across HTML/CSS/JS files
3. **Randomly select one template group** per component
4. **Combine selected templates** into final website

### HTML Assembly Rules

- **Headers**: Inserted immediately after `<body>` tag
- **Heroes**: Inserted after header section
- **Other components**: Inserted in processing order after hero
- **Footers**: Inserted before closing `</body>` tag
- **CSS/JS**: Combined into single files respectively

## Template Content Standards

### Casino-Specific Requirements

All templates must include:

- **Age verification** notices (18+ or 21+)
- **Responsible gambling** messaging
- **Professional casino terminology**
- **Bonus/promotion highlights**
- **Game category organization**
- **Mobile-responsive design**

### Legal Compliance Elements

- Terms and conditions links
- Privacy policy references
- Licensing information displays
- Affiliate disclosure notices
- Responsible gambling resources

### Technical Standards

- **Semantic HTML5** structure
- **CSS custom properties** for theming
- **Mobile-first** responsive design
- **Modern ES6+** JavaScript
- **Accessibility** compliance
- **Performance** optimization

## Component Types

### Header Components

**Purpose**: Site navigation, branding, user account access
**Variants**: Standard, two-row, centered, compact, with search, with promo banner, mega menu, sidebar toggle, icon nav, minimal
**Key Features**: Logo, navigation menu, CTA buttons, mobile menu toggle

### Hero Components

**Purpose**: Main promotional area, key messaging, primary CTAs
**Variants**: Classic casino, split screen, luxury, game categories, neon, jackpot, glassmorphic, mobile-first, tournament, minimal
**Key Features**: Headlines, promotional content, primary action buttons, visual elements

### Footer Components

**Purpose**: Legal information, links, contact details
**Variants**: Modern minimalist, dark professional, gradient gold, neon gaming, luxury VIP, mobile-first, glass morphism, crypto, tournament, minimalist pure
**Key Features**: Legal notices, game categories, contact info, responsible gambling links

### Content Components

**Purpose**: Informational sections, comparisons, guides
**Common Features**:

- Casino comparison tables
- Game guides and tutorials
- FAQ sections with accordions
- About us content
- Company history
- Why choose us arguments

## File Extraction Process

### Regex Patterns Used

The system uses specific regex patterns to extract templates:

**HTML Pattern:**

```regex
<!-- Template \d+: [^>]+ -->([\s\S]*?)(?=<!-- Template \d+:|$)
```

**CSS Pattern:**

```regex
/\* Template \d+: [^*]+ \*/([\s\S]*?)(?=/\* Template \d+:|$)
```

**JavaScript Pattern:**

```regex
// Template \d+: [^\n]+ \n([\s\S]*?)(?=// Template \d+:|$)
```

### Template Name Extraction

Template names are extracted from the comment headers:

- **HTML**: `<!-- Template \d+: ([^>]+) -->`
- **CSS**: `/\* Template \d+: ([^*]+) \*/`
- **JavaScript**: `// Template \d+: ([^\n]+)`

## Development Guidelines

### Adding New Templates

1. **Follow numbering convention**: Use Template 1-10
2. **Match comment syntax**: Use exact comment formats
3. **Maintain consistency**: Keep similar structure across templates
4. **Include all file types**: Ensure HTML, CSS, and JS variants exist
5. **Test regex compatibility**: Verify templates are extractable

### Modifying Existing Templates

1. **Preserve template markers**: Don't change comment syntax
2. **Maintain numbering**: Keep existing template numbers
3. **Update consistently**: Modify corresponding HTML/CSS/JS together
4. **Test functionality**: Ensure modifications work with extraction system

### Component Naming Conventions

- **CSS Classes**: Use component-specific prefixes (e.g., `.header-1`, `.hero-2`)
- **JavaScript Functions**: Use descriptive names (e.g., `initHeader1()`, `setupHero2()`)
- **HTML IDs**: Use template-specific IDs (e.g., `id="header-1"`, `id="hero-2"`)

## Quality Assurance

### Template Validation

- Verify all 10 templates exist per component
- Check comment syntax matches regex patterns
- Ensure responsive design works across templates
- Test casino-specific features (age verification, responsible gambling)
- Validate HTML semantics and accessibility

### Content Review

- Casino terminology accuracy
- Legal compliance requirements
- Responsive design consistency
- Performance optimization
- Cross-browser compatibility

This component system provides the foundation for generating diverse, professional casino websites while maintaining consistency in branding, legal compliance, and user experience.
