# API Reference - Casino Website Generator Production System

## System Overview

The Casino Website Generator Production System is powered by a **sophisticated modular architecture** orchestrated by `main_controller.py` (297 lines). The system provides comprehensive workflow automation, country-specific localization, advanced component processing, and professional validation through specialized modules.

## Primary Module: `main_controller.py`

### Main Entry Functions

#### `main()`

**Purpose**: Primary function called by starter.py for basic menu functionality
**Parameters**: None
**Returns**: None
**Description**: Displays basic menu with 5 core operations and handles user selection

**Menu Options**:

1. Configure Country → `country_config.configure_template()`
2. Import Components → `component_importer.import_components()`
3. Download Images → `image_downloader.download_images()`
4. Error Checking → `error_checker.error_checking()`
5. Clean Up → `cleanup_manager.cleanup()`

#### `interactive_menu()`

**Purpose**: Extended interactive menu with comprehensive workflow options
**Parameters**: None
**Returns**: None
**Description**: Full-featured menu system with advanced workflows and project management

**Extended Menu Structure**:

```
CASINO WEBSITE GENERATOR - MAIN MENU
Basic Operations:
  1. Configure Country        → Country localization
  2. Import Components        → Advanced component system
  3. Download Images         → Image management
  4. Error Checking          → Comprehensive validation
  5. Clean Up                → Optimization and cleanup

Advanced Options:
  6. Full Workflow           → Complete automated generation
  7. Quick Build             → Essential steps only
  8. Show Project Status     → Real-time monitoring
  9. Module Information      → Built-in help system
  0. Exit
```

#### `run_full_workflow()`

**Purpose**: Execute complete end-to-end website generation workflow
**Parameters**: None
**Returns**: None
**Description**: Automated workflow running all modules in sequence with error handling

**Workflow Sequence**:

1. **Country Configuration**: Select and configure country-specific content
2. **Component Import**: Import and assemble components with Mix-and-Match
3. **Image Processing**: Download and process images
4. **Error Validation**: Comprehensive website validation
5. **Cleanup & Optimization**: Final optimization and production build

#### `quick_build()`

**Purpose**: Quick development build with essential components only
**Parameters**: None
**Returns**: None
**Description**: Streamlined build process for rapid development iteration

**Quick Process**:

- Country configuration
- Component import
- Skip image processing, validation, and optimization
- Generate basic functional website

#### `show_project_status()`

**Purpose**: Display current project status and generated file information
**Parameters**: None
**Returns**: None
**Description**: Real-time monitoring of project state and file generation status

**Status Information**:

- Project directory paths
- Generated file status (HTML, CSS, JS, static content)
- File existence validation
- Recommended next steps based on current state

#### `show_module_info()`

**Purpose**: Display comprehensive information about all available modules
**Parameters**: None
**Returns**: None
**Description**: Built-in documentation system with module descriptions and features

**Module Information Includes**:

- Module descriptions and main functions
- Feature lists and capabilities
- Usage examples and integration points

---

## Specialized Module APIs

### Country Configuration: `country_config.py` (132 lines)

#### `configure_template()`

**Purpose**: Interactive country selection and content localization
**Parameters**: None
**Returns**: None
**Description**: Handles country selection and copies country-specific content

**Supported Countries**: Denmark, France, Portugal, UK-IR

**File Operations**:

- Source: `master/footer/{country}/` → Destination: `web-folder/static/footer/`
- Source: `master/offers/{country}/` → Destination: `web-folder/static/offers/`

**Process Flow**:

1. Display numbered country list (1-4)
2. Validate user selection
3. Copy footer content with cleanup
4. Copy offers content with cleanup
5. Report operation status

#### `get_available_countries()`

**Purpose**: Return list of supported countries
**Parameters**: None
**Returns**: List[str] - ["Denmark", "France", "Portugal", "UK-IR"]

#### `validate_country_support(country: str)`

**Purpose**: Validate if country is supported
**Parameters**: `country` (str) - Country name to check
**Returns**: bool - True if supported, False otherwise

### Component Import: `component_importer.py` (1258 lines)

#### `import_components()`

**Purpose**: Main entry point for the enhanced Mix-and-Match component system with external templates
**Parameters**: None
**Returns**: None
**Description**: Interactive component generation with custom theming, intelligent mixing, and external template system

**Core Features**:

- **🎨 Custom Theme Generation**: Generate themes from any hex color with light/dark mode
- **🎲 Mix-and-Match System**: Smart, Wild, and Single random component combinations
- **🔧 JSON Configuration**: Structured component definitions with validation
- **✨ Advanced Color Science**: HSL manipulation, triadic colors, contrast validation
- **📋 External Templates**: Separated HTML, CSS, and JavaScript template system

**Process Flow**:

1. **Template Validation**: Validates all base templates exist in `base/` directory
2. **Structure Validation**: Validates component structure and creates if missing
3. **Component Discovery**: Scans `web-components-v2/` for available components
4. **User Selection**: Interactive component selection with presets
5. **Mixing Mode**: Choose between Single Random, Smart Mix, or Wild Mix
6. **Custom Theme**: Generate theme from any hex color with light/dark mode
7. **Component Assembly**: Process and combine selected components with external templates
8. **Website Generation**: Create complete responsive casino website using template system

#### ComponentImporter Class

**Constructor**: `ComponentImporter()`

**Properties**:

- `current_dir`: Path to project root directory
- `components_dir`: Path to `web-components-v2/` directory
- `web_folder`: Path to `web-folder/` output directory
- `themes_dir`: Path to `themes/` directory
- `base_dir`: Path to `base/` external templates directory (NEW)
- `custom_theme`: Generated theme dictionary
- `component_order`: Processing order for components
- `theme_compatibility`: Theme compatibility matrix for Smart Mix

#### Template System Methods (NEW)

##### `load_template(template_path: str) -> str`

**Purpose**: Load template content from base directory
**Parameters**:

- `template_path` (str): Relative path to template file within `base/` directory
  **Returns**: str - Template content as string
  **Raises**: Prints warning if template not found
  **Description**: Safely loads external template files with error handling

**Usage Examples**:

```python
importer = ComponentImporter()

# Load HTML template
html_content = importer.load_template("templates/index.html")

# Load CSS template
css_template = importer.load_template("css/theme-variables.css")

# Load JavaScript template
js_content = importer.load_template("js/main.js")
```

##### `validate_base_templates() -> bool`

**Purpose**: Validate that all required base templates exist
**Parameters**: None
**Returns**: bool - True if all templates exist, False otherwise
**Description**: Checks for existence of all required template files before processing

**Required Templates**:

- `templates/index.html`
- `css/base-styles.css`
- `css/theme-variables.css`
- `css/fallback-theme.css`
- `js/main.js`

**Usage**:

```python
importer = ComponentImporter()
if importer.validate_base_templates():
    print("✅ All templates found")
    # Proceed with generation
else:
    print("❌ Missing templates")
    # Handle missing templates
```

##### `generate_theme_css(theme: Dict[str, Any]) -> str`

**Purpose**: Generate CSS content with theme variables from template
**Parameters**:

- `theme` (Dict[str, Any]): Theme dictionary containing colors, typography, spacing, etc.
  **Returns**: str - Complete CSS content with theme variables replaced
  **Description**: Takes theme variable template and replaces placeholders with actual theme values

**Template Placeholders Replaced**:

- `{THEME_MODE}`: Theme mode (Light/Dark)
- `{COLOR_PRIMARY}`: Primary color hex value
- `{COLOR_PRIMARY_RGB}`: Primary color RGB values
- `{COLOR_SECONDARY}`: Secondary color hex value
- `{COLOR_ACCENT}`: Accent color hex value
- `{COLOR_BACKGROUND}`: Background color hex value
- `{COLOR_SURFACE}`: Surface color hex value
- `{COLOR_SURFACE_ELEVATED}`: Elevated surface color hex value
- `{COLOR_TEXT}`: Primary text color hex value
- `{COLOR_TEXT_SECONDARY}`: Secondary text color hex value
- `{COLOR_BORDER}`: Border color hex value
- `{COLOR_HOVER}`: Hover state color hex value
- `{COLOR_ACTIVE}`: Active state color hex value
- `{COLOR_FOCUS}`: Focus state color hex value
- `{COLOR_SUCCESS}`: Success color hex value
- `{COLOR_WARNING}`: Warning color hex value
- `{COLOR_ERROR}`: Error color hex value
- `{COLOR_GOLD}`: Casino gold color hex value
- `{COLOR_SILVER}`: Casino silver color hex value
- `{COLOR_BRONZE}`: Casino bronze color hex value
- `{FONT_PRIMARY}`: Primary font family
- `{FONT_DISPLAY}`: Display font family
- `{SPACING_BASE}`: Base spacing unit
- `{BORDER_RADIUS}`: Border radius value
- `{BORDER_WIDTH}`: Border width value
- `{SHADOW_SMALL}`: Small shadow definition
- `{SHADOW_MEDIUM}`: Medium shadow definition
- `{SHADOW_LARGE}`: Large shadow definition

**Usage**:

```python
importer = ComponentImporter()
custom_theme = importer.generate_custom_theme("#ff6b35", "dark")
css_content = importer.generate_theme_css(custom_theme)
```

#### Core Component Methods

### Image Management: `image_downloader.py` (323 lines)

#### `download_images()`

**Purpose**: Main image management system with multiple download options
**Parameters**: None
**Returns**: None
**Description**: Interactive menu for image download and organization

**Available Options**:

1. **Download from Unsplash**: Casino-themed images (planned)
2. **Generate with AI**: Custom graphics with OpenAI API (planned)
3. **Download Casino Stock**: Curated collections (planned)
4. **Process Existing**: Optimize existing images (planned)

#### `get_image_categories()`

**Purpose**: Get categorized image requirements for casino websites
**Parameters**: None
**Returns**: Dict[str, List[str]] - Categories mapped to specific image types

**Image Categories**:

```python
{
    "header": ["casino logo", "luxury casino background"],
    "hero": ["casino banner", "jackpot winner", "poker table"],
    "games": ["poker cards", "roulette wheel", "slot machine"],
    "promotions": ["casino bonus", "golden coins", "jackpot"],
    "footer": ["casino decoration", "luxury pattern"]
}
```

### Error Validation: `error_checker.py` (600 lines)

#### `error_checking()`

**Purpose**: Comprehensive website validation and compliance checking
**Parameters**: None
**Returns**: None
**Description**: Performs multiple validation checks and displays detailed results

**Validation Categories**:

- **Empty Links**: Find '#' links and broken references
- **CSS Files**: Validate file existence and references
- **Meta Tags**: Check required HTML meta tags
- **Logos/Favicons**: Asset presence validation
- **HTML/CSS/JS Syntax**: Basic syntax validation
- **Casino Compliance**: Industry-specific requirements
- **Responsive Design**: Mobile compatibility checks

**Casino Compliance Checks**:

- Age verification (18+ notices)
- Responsible gambling links (BeGambleAware.org)
- Legal notices and disclaimers
- Terms & conditions links

### Cleanup & Optimization: `cleanup_manager.py` (584 lines)

#### `cleanup()`

**Purpose**: Website optimization and production build system
**Parameters**: None
**Returns**: None
**Description**: Interactive menu for cleanup and optimization options

**Optimization Levels**:

1. **Basic Cleanup**: Remove temp files, empty directories, cache files, duplicates
2. **Full Optimization**: Minify CSS/JS, optimize images, compress files
3. **Production Build**: Create deployment packages in `dist/`
4. **Clean Everything**: Reset to initial state (with confirmation)

**Production Build Features**:

- Combined and minified assets
- Optimized file structure
- Deployment-ready packages
- Sitemap and robots.txt generation

### Image Processing: `img_processor.py` (552 lines)

#### `process_images()`

**Purpose**: Advanced image processing and optimization system
**Parameters**: None
**Returns**: None
**Description**: Interactive menu for image processing operations

**Processing Options**:

1. **Resize Images**: Standard casino website dimensions
2. **Optimize File Sizes**: Compression without quality loss
3. **Convert Formats**: WebP, AVIF for modern browsers
4. **Generate Responsive Sets**: Multiple sizes for different devices
5. **Fix Image Issues**: Validate and fix image problems
6. **Batch Process All**: Complete image processing workflow

**Standard Image Dimensions**:

```python
{
    "hero_banner": (1920, 800),
    "header_logo": (200, 60),
    "game_thumbnail": (300, 200),
    "promotional_banner": (800, 400),
    "footer_decoration": (100, 50)
}
```

---

## Entry Point System

### `starter.py` - Smart Launcher

**Purpose**: Simple, reliable entry point with comprehensive error handling
**Functionality**: Redirects to main_controller with fallback guidance

```python
def main():
    try:
        from main_controller import main as main_controller
        main_controller()
    except ImportError as e:
        # Display helpful error message with module troubleshooting
        # List required modules and provide fix suggestions
```

**Error Handling Features**:

- Lists all required modules
- Provides troubleshooting steps
- Suggests alternative execution methods
- Maintains user-friendly experience

---

## Command Line Interface

### Main Controller Commands

```bash
# Interactive modes
python starter.py                                    # Primary entry point
python scripts-folder/main_controller.py            # Direct access

# Direct workflow commands
python scripts-folder/main_controller.py workflow   # Full automated workflow
python scripts-folder/main_controller.py quick      # Quick development build
python scripts-folder/main_controller.py status     # Project status monitoring

# Individual module commands
python scripts-folder/main_controller.py country    # Country configuration
python scripts-folder/main_controller.py components # Component import
python scripts-folder/main_controller.py images     # Image management
python scripts-folder/main_controller.py check      # Error validation
python scripts-folder/main_controller.py cleanup    # Cleanup & optimization
```

### Individual Module Execution

```bash
# Direct module execution
python scripts-folder/country_config.py      # Country configuration only
python scripts-folder/component_importer.py  # Component import only
python scripts-folder/error_checker.py       # Error checking only
python scripts-folder/cleanup_manager.py     # Cleanup only
```

---

## Advanced Integration

### Programmatic Usage

```python
# Import main controller functions
from scripts_folder.main_controller import run_full_workflow, quick_build

# Execute complete workflows
run_full_workflow()        # Full automated generation
quick_build()             # Development build

# Import individual modules
from scripts_folder.country_config import configure_template
from scripts_folder.component_importer import import_components
from scripts_folder.error_checker import error_checking

# Execute specific functions
configure_template()      # Configure country
import_components()       # Import components
error_checking()         # Validate website
```

### Custom Workflow Creation

```python
def custom_casino_workflow():
    """Create custom workflow for specific requirements."""
    from scripts_folder.country_config import configure_template
    from scripts_folder.component_importer import import_components
    from scripts_folder.cleanup_manager import basic_cleanup

    print("🎰 Starting custom casino workflow...")

    # Essential steps only
    configure_template()
    import_components()
    basic_cleanup()

    print("✅ Custom workflow completed!")
```

---

**🎯 Production API**: This comprehensive API provides full programmatic access to the Casino Website Generator's modular architecture, enabling both interactive use and advanced automation for professional casino website development.
