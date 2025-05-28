# Base Templates Directory

This directory contains the base templates and boilerplate code used by the Enhanced Component Importer system.

## Structure

```
base/
├── templates/
│   └── index.html          # Base HTML template
├── css/
│   ├── base-styles.css     # Common CSS styles
│   ├── theme-variables.css # Theme variable template (with placeholders)
│   └── fallback-theme.css  # Default fallback theme
├── js/
│   └── main.js            # Base JavaScript functionality
└── README.md              # This file
```

## Purpose

Instead of hardcoding HTML, CSS, and JavaScript boilerplate directly in the Python script, this system:

1. **Separates concerns**: Keeps template code in separate files for better maintainability
2. **Enables easier customization**: Developers can modify templates without touching Python code
3. **Improves reusability**: Templates can be reused across different parts of the system
4. **Better version control**: Changes to templates are tracked separately from logic changes

## Template System

### HTML Template (`templates/index.html`)

- Base HTML structure with proper meta tags and font loading
- Placeholder comments for component insertion
- Legal notice and basic page structure

### CSS Templates

- **`base-styles.css`**: Common styles, utilities, and responsive design
- **`theme-variables.css`**: Template with placeholders for dynamic theme generation
- **`fallback-theme.css`**: Default theme when no custom theme is specified

### JavaScript Template (`js/main.js`)

- Base functionality for component initialization
- Global event handlers and theme system
- Smooth scrolling and accessibility features

## Usage

The `ComponentImporter` class automatically loads these templates and:

1. Copies the HTML template as the base structure
2. Generates CSS by combining theme variables with base styles
3. Uses the JavaScript template as the foundation for component scripts

## Customization

To customize the base templates:

1. Edit the appropriate template file
2. The changes will be automatically applied to all new website generations
3. No Python code changes required for basic template modifications
