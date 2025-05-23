# API Reference - Casino Website Generator

## Modular Architecture Overview

The system has been completely refactored from a monolithic `starter.py` into 7 specialized modules:

- **`main_controller.py`** - Main orchestrator and interactive menu
- **`component_importer.py`** - Enhanced component system (primary)
- **`country_config.py`** - Country selection and localization
- **`image_downloader.py`** - Image management and processing
- **`error_checker.py`** - Quality assurance and validation
- **`cleanup_manager.py`** - Optimization and cleanup
- **`img_processor.py`** - Image processing utilities

## Core Functions in `main_controller.py`

### `main()`

**Purpose**: Original main entry point (maintained for compatibility)
**Parameters**: None
**Returns**: None
**Description**: Displays basic menu with 5 options and routes to appropriate module function.

**Menu Options**:

1. Configure Country → `country_config.configure_template()`
2. Import Components → `component_importer.import_components()`
3. Download Images → `image_downloader.download_images()`
4. Error Checking → `error_checker.error_checking()`
5. Clean Up → `cleanup_manager.cleanup()`

---

### `interactive_menu()`

**Purpose**: Enhanced interactive menu system with extended options
**Parameters**: None
**Returns**: None
**Description**: Main interface providing comprehensive project management options.

**Menu Options**:

- **Basic Operations** (1-5): Individual module execution
- **Advanced Options** (6-9): Workflow automation and project management
  - Full Workflow - Complete automation
  - Quick Build - Country + Components only
  - Project Status - Current state analysis
  - Module Information - Documentation display

---

### `run_full_workflow()`

**Purpose**: Complete automated website generation workflow
**Parameters**: None
**Returns**: None
**Description**: Executes all generation steps in sequence with error handling.

**Execution Steps**:

1. Country configuration (`configure_template()`)
2. Component import (`import_components()`)
3. Image processing (`download_images()`)
4. Error checking (`error_checking()`)
5. Final cleanup (`cleanup()`)

---

### `quick_build()`

**Purpose**: Rapid prototyping with essential components only
**Parameters**: None
**Returns**: None
**Description**: Generates basic casino website with country + components only.

---

### `show_project_status()`

**Purpose**: Project state analysis and recommendations
**Parameters**: None
**Returns**: None
**Description**: Analyzes generated files and provides next step recommendations.

## Enhanced Component System (`component_importer.py`)

### `ComponentImporter` Class

**Purpose**: Enhanced component importer with JSON-based configuration
**Description**: Modern component system featuring real files, JSON configuration, and professional theming.

**Key Features**:

- JSON-based component configuration
- Real component file loading (HTML/CSS/JS)
- Advanced theming system
- Professional variant selection
- Casino compliance integration

---

### `import_components()`

**Purpose**: Main component assembly function for enhanced system
**Parameters**: None
**Returns**: None
**Description**: Loads components from JSON configuration and assembles complete website.

**Process Flow**:

1. Validates enhanced component structure exists
2. Gets available components from `web-components-v2/`
3. Loads component configurations from `component.json` files
4. Presents user with component selection interface
5. Randomly selects variants for chosen components
6. Loads actual HTML/CSS/JS files from disk
7. Assembles components into final website structure

**Generated Files**:

- `web-folder/index.html` - Complete HTML document with components
- `web-folder/css/styles.css` - Combined CSS with base styles + components
- `web-folder/js/main.js` - Combined JavaScript with functionality

---

### `ComponentImporter.load_component_config(component_name)`

**Purpose**: Load component configuration from JSON file
**Parameters**:

- `component_name` (string): Name of component directory
  **Returns**: Dict containing component configuration
  **Description**: Loads and parses `component.json` from component directory.

**Configuration Structure**:

```json
{
  "name": "header",
  "description": "Professional casino header with navigation",
  "category": "navigation",
  "version": "1.0.0",
  "variants": [
    {
      "name": "modern",
      "description": "Modern gradient header with smooth animations",
      "html": "modern.html",
      "css": "modern.css",
      "js": "modern.js"
    }
  ],
  "dependencies": [],
  "casino_compliance": {
    "age_verification": true,
    "responsible_gambling": true,
    "legal_notices": true
  }
}
```

---

### `ComponentImporter.get_available_components()`

**Purpose**: Discover available components with JSON configurations
**Parameters**: None
**Returns**: List of component names that have valid `component.json` files
**Description**: Scans `web-components-v2/` directory for components with valid configurations.

---

### `ComponentImporter.create_enhanced_structure()`

**Purpose**: Create enhanced component structure from scratch
**Parameters**: None
**Returns**: None
**Description**: Creates the complete enhanced component system with directories, JSON configurations, and theme files.

**Created Structure**:

- `web-components-v2/` directory with component subdirectories
- `component.json` files for each component
- `themes/` directory with JSON theme definitions
- Sample component configurations for header, hero, footer

---

### `_generate_base_website(importer)`

**Purpose**: Generate base website structure with enhanced CSS/JS framework
**Parameters**:

- `importer` (ComponentImporter): ComponentImporter instance
  **Returns**: None
  **Description**: Creates foundation HTML/CSS/JS files with modern styling framework.

**Generated Base Features**:

- Modern CSS framework with custom properties
- Responsive design utilities
- Professional button styles
- Legal notice integration
- Component initialization system

---

### `_import_single_component(importer, comp_name)`

**Purpose**: Import single component with variant selection
**Parameters**:

- `importer` (ComponentImporter): ComponentImporter instance
- `comp_name` (string): Component name to import
  **Returns**: Boolean success status
  **Description**: Loads component configuration, selects random variant, and integrates files.

**Process Steps**:

1. Load component configuration from JSON
2. Randomly select variant from available options
3. Read HTML file and insert into website
4. Read CSS file and append to stylesheet
5. Read JS file and append to main script

---

### `_insert_component_html(importer, html_content, comp_type)`

**Purpose**: Insert component HTML into appropriate document location
**Parameters**:

- `importer` (ComponentImporter): ComponentImporter instance
- `html_content` (string): Component HTML content
- `comp_type` (string): Component type (header, hero, footer, etc.)
  **Returns**: None
  **Description**: Intelligently inserts components in logical order within HTML structure.

**Insertion Rules**:

- **header**: After `<body>` tag
- **footer**: Before legal notice section
- **others**: Before legal notice section in processing order

## Country Configuration (`country_config.py`)

### `configure_template()`

**Purpose**: Country selection and content copying with enhanced interface
**Parameters**: None
**Returns**: None
**Description**: Interactive country selection with improved user experience.

**Available Countries**:

- Denmark, France, Portugal, UK-IR, Croatia, Argentina

**File Operations**:

- Source: `master/footer/{country}/` → Destination: `web-folder/static/footer/`
- Source: `master/offers/{country}/` → Destination: `web-folder/static/offers/`

## Component Variants and Theming

### Available Header Variants

1. **Modern**: Gradient design with diamond logo and smooth animations

   - Files: `modern.html`, `modern.css`, `modern.js`
   - Features: Diamond spin animation, balance display, gradient backgrounds

2. **Luxury**: Royal black & gold theme with crown logo and shimmer effects

   - Files: `luxury.html`, `luxury.css`, `luxury.js`
   - Features: Crown floating animation, shimmer effects, VIP styling

3. **Neon**: Cyberpunk style with neon glows and scanning effects

   - Files: `neon.html`, `neon.css`, `neon.js`
   - Features: Neon glow effects, scanning animations, color-coded navigation

4. **Minimal**: Clean, elegant design with subtle typography

   - Files: `minimal.html`, `minimal.css`, `minimal.js`
   - Features: Clean styling, dark theme support, subtle animations

5. **Vintage**: Classic 1924 casino theme with playing card suits
   - Files: `vintage.html`, `vintage.css`, `vintage.js`
   - Features: Card flip animations, retro patterns, vintage styling

### Theme System

**Theme Files Location**: `themes/` directory

**Available Themes**:

- `casino-modern.json` - Modern theme with gold accents
- `casino-luxury.json` - Luxury gold and black theme
- `casino-neon.json` - Vibrant neon gaming theme

**Theme Structure**:

```json
{
  "name": "casino-modern",
  "description": "Modern casino theme with gold accents",
  "colors": {
    "primary": "#d4af37",
    "secondary": "#1a1a1a",
    "accent": "#ff6b35",
    "background": "#0f0f0f",
    "surface": "#1e1e1e",
    "text": "#ffffff",
    "text-secondary": "#b0b0b0"
  },
  "typography": {
    "font-primary": "Inter, system-ui, sans-serif",
    "font-display": "Poppins, sans-serif",
    "scale": 1.2
  },
  "spacing": {
    "base": "1rem",
    "scale": 1.5
  },
  "borders": {
    "radius": "8px",
    "width": "1px"
  }
}
```

## File System Operations

### Component File Management

```python
# Load component configuration
config_file = component_dir / "component.json"
with open(config_file, 'r', encoding='utf-8') as f:
    config = json.load(f)

# Load component files
html_file = component_dir / f"{variant_name}.html"
css_file = component_dir / f"{variant_name}.css"
js_file = component_dir / f"{variant_name}.js"

# Read file contents
with open(html_file, 'r', encoding='utf-8') as f:
    html_content = f.read()
```

### Directory Structure Operations

```python
# Create enhanced structure
components_dir.mkdir(exist_ok=True)
themes_dir.mkdir(exist_ok=True)

# Setup web folder
web_folder.mkdir(exist_ok=True)
(web_folder / "css").mkdir(exist_ok=True)
(web_folder / "js").mkdir(exist_ok=True)
(web_folder / "assets").mkdir(exist_ok=True)
```

## Migration Notes

### Key Changes from Old System

1. **Template Extraction Removed**: No longer uses regex to extract templates from component files
2. **Real Files**: Components are actual HTML/CSS/JS files instead of embedded strings
3. **JSON Configuration**: Component metadata stored in structured JSON files
4. **Enhanced Theming**: Professional animations and modern CSS techniques
5. **Modular Architecture**: Split into specialized modules for better maintainability

### Deprecated Functions

The following functions from the old system have been removed:

- `extract_templates()` - No longer needed with real component files
- `extract_template_name()` - Component names from JSON configuration
- `parse_html()` - Direct HTML file reading
- Template regex patterns - Replaced with file system operations

### Modern Replacements

- **Template Strings** → **Real HTML/CSS/JS Files**
- **Regex Extraction** → **JSON Configuration + File Reading**
- **Hardcoded Variants** → **Flexible JSON-Defined Variants**
- **String Templates** → **Professional Component Files with Animations**

This enhanced API provides a robust, maintainable, and scalable foundation for generating professional casino websites with modern web technologies and beautiful designs.
