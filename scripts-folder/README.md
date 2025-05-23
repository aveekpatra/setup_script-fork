# Scripts Folder - Modular Components

This folder contains the modular breakdown of the Casino Website Generator's functionality. Each script handles a specific aspect of the website generation process.

## 📦 Module Overview

### Core Modules

#### `main_controller.py`

**Main orchestrator module**

- Controls the overall workflow
- Provides interactive menu system
- Supports command-line arguments
- Includes advanced features like full workflow and quick build

**Usage:**

```bash
python scripts-folder/main_controller.py
python scripts-folder/main_controller.py workflow
python scripts-folder/main_controller.py quick
```

#### `country_config.py`

**Country configuration management**

- Handles country selection (Denmark, France, Portugal, UK-IR)
- Copies country-specific footer content
- Copies country-specific offers content
- Validates country support

**Main Functions:**

- `configure_template()` - Main country configuration
- `get_available_countries()` - Get supported countries
- `validate_country_support()` - Check if country is supported

#### `component_importer.py`

**Component template system**

- Extracts templates from component files
- Randomly selects template variants
- Assembles HTML, CSS, and JavaScript
- Manages component processing order

**Main Functions:**

- `import_components()` - Main component import process
- `extract_templates()` - Extract templates using regex
- `insert_html_component()` - Insert HTML components
- `get_component_order()` - Get logical component order

#### `image_downloader.py`

**Image management system**

- Downloads images from Unsplash API (planned)
- Generates images with AI (planned)
- Organizes images by category
- Sets up image directory structure

**Main Functions:**

- `download_images()` - Main image download menu
- `setup_image_directories()` - Create image folder structure
- `validate_image_requirements()` - Check required images
- `get_image_categories()` - Get image categories

#### `error_checker.py`

**Website validation system**

- Checks for empty links
- Validates CSS/JS syntax
- Ensures proper meta tags
- Checks casino compliance requirements
- Validates responsive design

**Main Functions:**

- `error_checking()` - Main validation process
- `check_empty_links()` - Find empty href attributes
- `check_casino_compliance()` - Verify gambling compliance
- `check_responsive_design()` - Check responsive features

#### `cleanup_manager.py`

**Optimization and cleanup**

- Removes temporary files
- Minifies CSS and JavaScript
- Compresses files for production
- Creates production builds
- Generates metadata files

**Main Functions:**

- `cleanup()` - Main cleanup menu
- `basic_cleanup()` - Remove temp files and duplicates
- `full_optimization()` - Minify and compress files
- `production_build()` - Create deployment package

#### `img_processor.py`

**Image processing utilities**

- Resizes images for web optimization
- Optimizes file sizes
- Converts between formats
- Generates responsive image sets
- Fixes image issues in HTML

**Main Functions:**

- `process_images()` - Main image processing menu
- `resize_images()` - Resize to standard dimensions
- `optimize_file_sizes()` - Compress images
- `fix_image_issues()` - Validate and fix image problems

## 🔧 Integration with Main Script

The `starter.py` serves as a **simple entry point** that redirects to the modular system:

1. **Primary Mode**: Imports `main_controller.py` and launches the full modular interface
2. **Fallback Mode**: If modules aren't available, displays helpful error message with troubleshooting steps

This approach:

- ✅ Eliminates code duplication
- ✅ Provides clear error messages
- ✅ Maintains single source of truth for functionality
- ✅ Ensures backward compatibility

## 🚀 Usage Examples

### Interactive Mode

```bash
# Run through the main entry point (recommended)
python starter.py

# Or run the main controller directly
python scripts-folder/main_controller.py
```

### Command Line Mode

```bash
# Individual functions
python scripts-folder/main_controller.py country
python scripts-folder/main_controller.py components
python scripts-folder/main_controller.py check

# Workflows
python scripts-folder/main_controller.py workflow  # Full workflow
python scripts-folder/main_controller.py quick     # Quick build
python scripts-folder/main_controller.py status    # Project status
```

### Individual Module Usage

```python
# Import specific functionality
from country_config import configure_template
from component_importer import import_components
from error_checker import error_checking

# Use functions directly
configure_template()
import_components()
error_checking()
```

## 📋 Module Dependencies

### Standard Library

- `os` - File system operations
- `shutil` - File copying and directory operations
- `re` - Regular expression processing
- `random` - Random template selection
- `sys` - System operations and path management

### Internal Dependencies

- Each module is designed to be independent
- `main_controller.py` imports all other modules
- Modules use relative imports within the scripts-folder

## 🔍 Error Handling

Each module includes:

- **Input Validation**: Validates user input and file existence
- **Graceful Fallbacks**: Handles missing files or directories
- **Error Reporting**: Clear error messages with troubleshooting hints
- **Exception Handling**: Catches and reports unexpected errors

## 📊 Module Status

| Module                  | Status      | Functionality                             |
| ----------------------- | ----------- | ----------------------------------------- |
| `main_controller.py`    | ✅ Complete | Full workflow orchestration               |
| `country_config.py`     | ✅ Complete | Country selection and content copying     |
| `component_importer.py` | ✅ Complete | Template extraction and assembly          |
| `image_downloader.py`   | 🚧 Partial  | Structure ready, API integration pending  |
| `error_checker.py`      | ✅ Complete | Comprehensive website validation          |
| `cleanup_manager.py`    | 🚧 Partial  | Basic cleanup done, optimization pending  |
| `img_processor.py`      | 🚧 Partial  | Framework ready, processing logic pending |

## 🎯 Future Enhancements

### Planned Features

1. **API Integrations**

   - Unsplash API for image downloads
   - OpenAI API for image generation
   - Web validation APIs

2. **Advanced Processing**

   - PIL/Pillow for image manipulation
   - Advanced CSS/JS minification
   - WebP and AVIF image conversion

3. **Enhanced Validation**
   - HTML5 validation
   - Accessibility checking
   - Performance auditing

## 🛠️ Development Guidelines

### Adding New Modules

1. Create module in `scripts-folder/`
2. Follow naming convention: `[feature]_[type].py`
3. Include comprehensive docstrings
4. Add error handling and validation
5. Update `main_controller.py` imports
6. Update this README

### Modifying Existing Modules

1. Maintain function signatures for compatibility
2. Add comprehensive error handling
3. Update documentation
4. Test with existing workflows

This modular structure provides better maintainability, easier testing, and clearer separation of concerns while maintaining the original functionality of the Casino Website Generator.
