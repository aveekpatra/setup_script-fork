# Cursor AI Rules - Casino Website Generator Project

## ⚠️ CRITICAL PROJECT UNDERSTANDING

### Primary Project Function

This is **NOT** a simple website - this is a **WEBSITE GENERATOR TOOL** that creates casino websites. The main functionality is in `starter.py`, not in building a single website.

### Key Project Facts (NEVER HALLUCINATE THESE)

1. **Main Script**: `starter.py` (720 lines) - the core functionality
2. **Output Directory**: `web-folder/` - where generated websites are placed
3. **Template Library**: `web-components/` - source templates for generation
4. **Country Content**: `master/` - country-specific legal/offers content
5. **Current Countries**: Denmark, France, Portugal, UK-IR, Croatia, Argentina
6. **Template Count**: Each component has exactly 10 template variants

## 🚫 DO NOT HALLUCINATE

### File Structure (Verified Facts Only)

- **`starter.py`**: 720 lines, 5 main functions (configure_template, import_components, download_images, error_checking, cleanup)
- **`web-components/`**: Contains header/, footer/, hero/, offers/, details_comparison/, why_us/, about/, history/, guide/, faqs/
- **`master/footer/`**: Denmark/, France/, Portugal/, UK-IR/, Croatia/, Argentina/
- **`master/offers/`**: Denmark/, France/, Portugal/, UK-IR/
- **`scripts-folder/`**: Contains empty placeholder files (checker.py, downlaod_image.py, img_fix.py)
- **`web-folder/`**: Generated output with index.html, css/, scripts/, static/

### Template System Facts

1. Templates are marked with `<!-- Template X: Name -->` for HTML
2. Templates use `/* Template X: Name */` for CSS
3. Templates use `// Template X: Name` for JavaScript
4. Each component has 10 numbered template variants (1-10)
5. Random selection picks one template per component type

### Processing Order (EXACT)

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

## 🎯 WHEN WORKING WITH THIS PROJECT

### For Code Analysis

- **Always reference actual file paths**: Use the verified directory structure
- **Check template numbering**: Templates are numbered 1-10, not arbitrary
- **Understand the workflow**: This generates websites, doesn't run them
- **Know the current state**: Some features are implemented, others are placeholders

### For Component Work

- **Location**: All components are in `web-components/{component-name}/`
- **File types**: Each component has .html, .css, and .js files
- **Template format**: Use exact comment syntax for template markers
- **Content type**: All content is casino-focused with responsible gambling notices

### For Country Customization

- **Available countries**: Only work with Denmark, France, Portugal, UK-IR (confirmed in code)
- **Content types**: footer/ and offers/ subdirectories in master/
- **Copy mechanism**: Files are copied from master/ to web-folder/static/

### For Python Script Work

- **Main functions**: main(), configure_template(), import_components(), download_images(), error_checking(), cleanup()
- **Regex patterns**: Uses specific regex for template extraction
- **File handling**: Copies, reads, writes, and processes files systematically
- **User interaction**: Uses numbered menu system for choices

## 🔧 DEVELOPMENT GUIDELINES

### When Adding Features

1. **Follow existing patterns**: Use the same template comment syntax
2. **Maintain order**: Respect the component processing order
3. **Keep consistency**: Match the existing code style and structure
4. **Update todos**: Reference todo.md for planned features

### When Debugging

1. **Check file existence**: Verify files exist before referencing them
2. **Validate paths**: Use the correct relative paths from project root
3. **Understand flow**: Template extraction → random selection → assembly
4. **Consider state**: Some placeholder functions exist but aren't implemented

### When Modifying Templates

1. **Use exact syntax**: Follow the `<!-- Template X: Name -->` format precisely
2. **Include all three**: Ensure HTML, CSS, and JS variants exist
3. **Test regex compatibility**: Templates must be extractable by existing regex
4. **Maintain numbering**: Keep templates numbered 1-10

## 📋 CURRENT PROJECT STATUS

### ✅ Implemented Features

- Main menu system in starter.py
- Country selection and file copying
- Component template extraction system
- Random template selection algorithm
- HTML/CSS/JS assembly and combination
- Basic responsive CSS framework
- Template comment parsing with regex

### 🚧 Placeholder Features (Empty Files)

- `scripts-folder/checker.py` - Error checking (0 lines)
- `scripts-folder/downlaod_image.py` - Image download (0 lines)
- `scripts-folder/img_fix.py` - Image processing (0 lines)
- `download_images()` function in starter.py (placeholder)
- `error_checking()` function in starter.py (placeholder)
- `cleanup()` function in starter.py (placeholder)

### 📝 Known File Issues

- Some component directories may be empty (like offers/)
- Placeholder scripts exist but have no implementation
- Country support varies between footer/ and offers/

## 🎲 CASINO-SPECIFIC REQUIREMENTS

### Legal Compliance

- Age verification notices (18+ or 21+)
- Responsible gambling messages
- Terms and conditions links
- Affiliate content labeling
- Country-specific legal requirements

### Content Standards

- Professional casino terminology
- Bonus and promotion focus
- Game categorization (slots, table games, live casino)
- VIP and tournament features
- Mobile-responsive design priority

### Technical Requirements

- Semantic HTML5 structure
- CSS custom properties for theming
- Mobile-first responsive approach
- Modern ES6+ JavaScript
- Performance optimization focus

## 🚨 ERROR PREVENTION

### Before Making Changes

1. **Verify file existence**: Check files exist before referencing
2. **Understand scope**: Know if you're working on generator or generated output
3. **Check dependencies**: Ensure required directories/files are present
4. **Validate syntax**: Use exact template comment formats

### Common Mistakes to Avoid

1. **Don't confuse `web-folder/` (output) with `web-components/` (source)**
2. **Don't assume all component directories have files**
3. **Don't change template numbering or comment syntax**
4. **Don't implement placeholder features without understanding the intended scope**
5. **Don't add countries not supported in the existing master/ structure**

This project is a sophisticated tool for generating casino websites, not a single website itself. Always consider the generation workflow when making modifications.
