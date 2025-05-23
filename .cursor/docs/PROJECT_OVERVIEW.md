# Casino Website Generator - Project Overview

## Project Purpose

This is a **Casino Website Generator Tool** that creates professional casino websites using a template-based system. The tool allows users to:

1. **Configure Country-Specific Content**: Select from predefined countries (Denmark, France, Portugal, UK-IR) to customize footer and offers content
2. **Build Modular Websites**: Combine different pre-designed components (header, hero, offers, etc.) into complete casino websites
3. **Generate Professional Casino Sites**: Create fully-functional, responsive casino websites with modern UI/UX

## Project Structure

```
setup_script-fork/
├── starter.py                    # Main Python script - the core of the project
├── todo.md                      # Feature roadmap and task list
├── .gitignore                   # Git ignore rules
├── web-folder/                  # OUTPUT: Generated casino website files
│   ├── index.html              # Generated main HTML file
│   ├── css/styles.css          # Generated CSS styles
│   ├── scripts/main.js         # Generated JavaScript
│   └── static/                 # Static assets (images, country-specific content)
│       ├── footer/             # Country-specific footer content
│       └── offers/             # Country-specific offers content
├── web-components/             # SOURCE: Component library with templates
│   ├── header/                 # Header component templates (10 variants)
│   ├── footer/                 # Footer component templates (10 variants)
│   ├── hero/                   # Hero section templates (10 variants)
│   ├── offers/                 # Offers section templates
│   ├── details_comparison/     # Comparison section templates
│   ├── why_us/                 # Why Us section templates
│   ├── about/                  # About section templates
│   ├── history/                # History section templates
│   ├── guide/                  # Guide section templates
│   └── faqs/                   # FAQ section templates
├── master/                     # Country-specific templates
│   ├── footer/                 # Country-specific footer content
│   │   ├── Denmark/
│   │   ├── France/
│   │   ├── Portugal/
│   │   ├── UK-IR/
│   │   ├── Croatia/
│   │   └── Argentina/
│   └── offers/                 # Country-specific offers content
│       ├── Denmark/
│       ├── France/
│       ├── Portugal/
│       └── UK-IR/
├── scripts-folder/             # Additional utility scripts (placeholder)
│   ├── checker.py             # (Empty - for error checking)
│   ├── downlaod_image.py      # (Empty - for image downloads)
│   └── img_fix.py             # (Empty - for image processing)
├── AI/                        # AI-related prompts and content
│   └── prompts.md             # AI prompts for content generation
└── .cursor/                   # Cursor IDE configuration
```

## Core Workflow

The project follows this workflow:

1. **User runs `starter.py`** - Main menu with 5 options
2. **Configure Country** - Select target country for localized content
3. **Import Components** - Choose and combine website components
4. **Download Images** - (Planned) Download/generate images
5. **Error Checking** - (Planned) Validate generated website
6. **Clean Up** - (Planned) Final cleanup and optimization

## Component System

### Template Structure

Each component (header, hero, footer, etc.) contains multiple templates:

- **HTML Templates**: 10 different design variants per component
- **CSS Templates**: Corresponding styles for each HTML variant
- **JS Templates**: Interactive functionality for each variant

### Template Naming Convention

Templates are marked with comments:

```html
<!-- Template 1: Template Name -->
<!-- Template 2: Template Name -->
<!-- ... up to Template 10 -->
```

### Component Processing Order

Components are processed in logical order:

1. header
2. hero
3. offers
4. details_comparison
5. why_us
6. about
7. history
8. guide
9. faqs
10. footer

## Key Features

### Country Localization

- Footer content varies by country (legal requirements, language)
- Offers content tailored to local regulations
- Supports: Denmark, France, Portugal, UK-IR, Croatia, Argentina

### Random Template Selection

- Randomly selects one template variant from each component
- Ensures unique website designs on each generation
- Maintains consistent branding across components

### Responsive Design

- All templates use mobile-first responsive design
- CSS variables for consistent theming
- Modern UI/UX patterns for casino websites

### Casino-Specific Features

- Age verification notices
- Responsible gambling messaging
- Bonus and promotion displays
- Game category organization
- VIP/tournament sections

## Technical Implementation

### File Processing

1. **Template Extraction**: Uses regex to extract templates from component files
2. **Random Selection**: Randomly picks one template per component type
3. **HTML Assembly**: Inserts components in logical order into base HTML structure
4. **CSS Compilation**: Combines all component CSS into single stylesheet
5. **JS Compilation**: Combines all component JavaScript into single file

### Generated Output

The final output in `web-folder/` is a complete, production-ready casino website with:

- Semantic HTML5 structure
- Responsive CSS styling
- Interactive JavaScript functionality
- Country-specific legal content
- Casino-specific UI components

## Development Status

### Completed Features ✅

- Main workflow controller
- Country selection and content copying
- Component template system
- Random template selection
- HTML/CSS/JS assembly
- Basic responsive framework

### Planned Features 📋

- Image download system (Unsplash API)
- AI image generation (OpenAI API)
- Comprehensive error checking
- Image compression and optimization
- Enhanced template variations

## File Conventions

### HTML Files

- Use semantic HTML5 elements
- Include proper meta tags for casino sites
- Follow accessibility guidelines
- Include responsible gambling notices

### CSS Files

- Use CSS custom properties (variables)
- Mobile-first responsive design
- Consistent component naming
- Casino-specific styling patterns

### JavaScript Files

- Modern ES6+ features
- Component-based organization
- Accessible interactive elements
- Performance-optimized code

This project represents a sophisticated website generation system specifically designed for the casino industry, with built-in compliance features, professional design templates, and country-specific localization capabilities.
