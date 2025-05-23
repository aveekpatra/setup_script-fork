# Casino Website Generator

A sophisticated Python tool for generating professional casino websites using a modular template system with country-specific localization and responsive design.

## 🎯 Project Overview

This is **NOT** a simple website project - it's a **website generator tool** that creates complete casino websites by combining modular components and country-specific content. The system uses template-based architecture to ensure design diversity while maintaining professional standards and legal compliance.

### Key Features

- **🌍 Country Localization**: Support for Denmark, France, Portugal, UK-IR with legal compliance
- **🎨 Template Variety**: 10 design variants per component for unique website generation
- **🎰 Casino-Focused**: Built-in responsible gambling notices and casino-specific features
- **📱 Responsive Design**: Mobile-first approach with modern UI/UX patterns
- **🔧 Modular System**: Component-based architecture for easy customization

## 🚀 Quick Start

1. **Run the generator**:

   ```bash
   python3 starter.py
   ```

2. **Follow the menu**:

   - Configure Country (select target market)
   - Import Components (generate website)
   - View output in `web-folder/`

3. **Generated website structure**:
   ```
   web-folder/
   ├── index.html          # Complete casino website
   ├── css/styles.css      # Combined responsive styles
   ├── scripts/main.js     # Interactive functionality
   └── static/             # Country-specific content
   ```

## 📁 Project Structure

```
setup_script-fork/
├── starter.py              # 🔥 MAIN SCRIPT (720 lines)
├── web-components/         # 📦 Template library (10 variants each)
│   ├── header/            # Navigation & branding
│   ├── hero/              # Main promotional sections
│   ├── footer/            # Legal & contact info
│   └── [8 more components]
├── master/                # 🌍 Country-specific content
│   ├── footer/            # Legal requirements by country
│   └── offers/            # Localized promotions
├── web-folder/            # 🎯 GENERATED OUTPUT
└── .cursor/docs/          # 📚 Complete documentation
```

## 🎲 Component System

### Available Components

1. **header** - Site navigation and branding
2. **hero** - Main promotional area
3. **offers** - Casino promotions
4. **details_comparison** - Casino comparison tables
5. **why_us** - Value propositions
6. **about** - Company information
7. **history** - Company background
8. **guide** - Gaming guides
9. **faqs** - Frequently asked questions
10. **footer** - Legal and contact information

### Template Structure

Each component contains **exactly 10 template variants**:

- `component.html` - HTML templates marked with `<!-- Template X: Name -->`
- `component.css` - CSS templates marked with `/* Template X: Name */`
- `component.js` - JavaScript templates marked with `// Template X: Name`

## 🌍 Supported Countries

| Country   | Footer Content | Offers Content | Legal Compliance       |
| --------- | -------------- | -------------- | ---------------------- |
| Denmark   | ✅             | ✅             | Danish gambling laws   |
| France    | ✅             | ✅             | ARJEL compliance       |
| Portugal  | ✅             | ✅             | Portuguese regulations |
| UK-IR     | ✅             | ✅             | UK Gambling Commission |
| Croatia   | ✅             | ❌             | Basic support          |
| Argentina | ✅             | ❌             | Basic support          |

## 🔧 Development Status

### ✅ Implemented Features

- [x] Main workflow controller (`starter.py`)
- [x] Country selection and content copying
- [x] Component template extraction system
- [x] Random template selection algorithm
- [x] HTML/CSS/JS assembly and combination
- [x] Responsive CSS framework
- [x] Template comment parsing with regex

### 🚧 Planned Features

- [ ] Image download system (Unsplash API)
- [ ] AI image generation (OpenAI API)
- [ ] Comprehensive error checking
- [ ] Image compression and optimization
- [ ] Enhanced template variations

## 📚 Documentation

Comprehensive documentation is available in `.cursor/docs/`:

- **[PROJECT_OVERVIEW.md](.cursor/docs/PROJECT_OVERVIEW.md)** - Complete project understanding
- **[CURSOR_RULES.md](.cursor/docs/CURSOR_RULES.md)** - Critical rules to prevent hallucination
- **[COMPONENT_SYSTEM.md](.cursor/docs/COMPONENT_SYSTEM.md)** - Template system details
- **[DEVELOPMENT_WORKFLOW.md](.cursor/docs/DEVELOPMENT_WORKFLOW.md)** - Development guidelines
- **[API_REFERENCE.md](.cursor/docs/API_REFERENCE.md)** - Function documentation

## ⚠️ Important Notes

### For Developers

- This is a **generator tool**, not a single website
- Main functionality is in `starter.py` (720 lines)
- Templates must follow exact comment syntax for regex extraction
- Component processing order is fixed and critical
- Some features are placeholders (see `todo.md`)

### For AI Assistants

- **NEVER hallucinate** file structures or functions
- Always verify file existence before referencing
- Understand the difference between source (`web-components/`) and output (`web-folder/`)
- Follow the exact template numbering system (1-10)
- Respect the component processing order

## 🎰 Casino Compliance

All generated websites include:

- **Age verification** notices (18+ or 21+)
- **Responsible gambling** messaging and resources
- **Legal compliance** elements for target countries
- **Professional terminology** and industry standards
- **Accessibility** features and semantic HTML

## 🛠️ Technical Requirements

- **Python 3.x** with standard libraries (`os`, `shutil`, `re`, `random`)
- **Modern browsers** for generated websites
- **Local server** recommended for testing (optional)

## 📝 License

This project is designed for generating professional casino websites with built-in compliance features. Please ensure all generated content meets local gambling regulations and licensing requirements.

---

**🎯 Remember**: This is a sophisticated website generation system, not a simple website. Always consider the generation workflow when making modifications or additions.
