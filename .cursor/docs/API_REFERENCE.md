# API Reference - Casino Website Generator

## Core Functions in `starter.py`

### `main()`

**Purpose**: Main entry point and menu controller
**Parameters**: None
**Returns**: None
**Description**: Displays main menu with 5 options and routes to appropriate function based on user selection.

**Menu Options**:

1. Configure Country → `configure_template()`
2. Import Components → `import_components()`
3. Download Images → `download_images()` (placeholder)
4. Error Checking → `error_checking()` (placeholder)
5. Clean Up → `cleanup()` (placeholder)

---

### `configure_template()`

**Purpose**: Country selection and content copying
**Parameters**: None
**Returns**: None
**Description**: Allows user to select from available countries and copies country-specific footer and offers content to `web-folder/static/`.

**Available Countries**:

- Denmark
- France
- Portugal
- UK-IR

**File Operations**:

- Source: `master/footer/{country}/` → Destination: `web-folder/static/footer/`
- Source: `master/offers/{country}/` → Destination: `web-folder/static/offers/`

---

### `import_components()`

**Purpose**: Template selection and website assembly
**Parameters**: None
**Returns**: None
**Description**: Main component assembly function that extracts templates, selects variants, and generates complete website.

**Process Flow**:

1. Gets list of available component types from `web-components/`
2. Sorts components by logical order
3. Allows user to select which components to import
4. Extracts templates from each component using regex
5. Randomly selects one template variant per component
6. Assembles HTML, CSS, and JavaScript into final website

**Component Processing Order**:

```python
component_order = [
    "header", "hero", "offers", "details_comparison",
    "why_us", "about", "history", "guide", "faqs", "footer"
]
```

**Generated Files**:

- `web-folder/index.html` - Complete HTML document
- `web-folder/css/styles.css` - Combined CSS styles
- `web-folder/scripts/main.js` - Combined JavaScript

---

### `extract_templates(content, file_type)`

**Purpose**: Extract template variants from component files
**Parameters**:

- `content` (string): File content to parse
- `file_type` (string): Type of file ("html", "css", or "js")
  **Returns**: List of template strings
  **Description**: Uses regex patterns to extract numbered templates from component files.

**Regex Patterns**:

- **HTML**: `r'<!-- Template \d+: [^>]+ -->([\s\S]*?)(?=<!-- Template \d+:|$)'`
- **CSS**: `r'/\* Template \d+: [^*]+ \*/([\s\S]*?)(?=/\* Template \d+:|$)'`
- **JS**: `r'// Template \d+: [^\n]+ \n([\s\S]*?)(?=// Template \d+:|$)'`

---

### `extract_template_name(template, file_type)`

**Purpose**: Extract template name from template content
**Parameters**:

- `template` (string): Template content with comment header
- `file_type` (string): Type of file ("html", "css", or "js")
  **Returns**: String template name or None if not found
  **Description**: Extracts the descriptive name from template comment headers.

**Name Extraction Patterns**:

- **HTML**: `r'<!-- Template \d+: ([^>]+) -->'`
- **CSS**: `r'/\* Template \d+: ([^*]+) \*/'`
- **JS**: `r'// Template \d+: ([^\n]+)'`

---

### `insert_html_component(html_doc, template, comp_type)`

**Purpose**: Insert HTML component into appropriate document location
**Parameters**:

- `html_doc` (string): Current HTML document content
- `template` (string): Template HTML to insert
- `comp_type` (string): Component type (header, hero, footer, etc.)
  **Returns**: Updated HTML document string
  **Description**: Intelligently inserts components in logical order within the HTML structure.

**Insertion Rules**:

- **header**: After `<body>` tag
- **hero**: After header section or `<body>` tag if no header
- **footer**: Before `</body>` tag
- **others**: In processing order after hero or header

---

### `parse_html(html_content)`

**Purpose**: Simple HTML content parsing (currently passthrough)
**Parameters**:

- `html_content` (string): HTML content to parse
  **Returns**: Parsed HTML content (currently unchanged)
  **Description**: Placeholder for future HTML parsing functionality.

---

### `download_images()` (Placeholder)

**Purpose**: Download and manage website images
**Parameters**: None
**Returns**: None
**Description**: Planned functionality for downloading images from Unsplash API and generating images with OpenAI API.

**Planned Features** (from `todo.md`):

- Download images from Unsplash API using search tags
- Generate images using OpenAI API
- Image compression and renaming

---

### `error_checking()` (Placeholder)

**Purpose**: Validate generated website for errors
**Parameters**: None  
**Returns**: None
**Description**: Planned functionality for comprehensive website validation.

**Planned Checks** (from `todo.md`):

- Empty links with '#'
- Correct style.css files added to each site
- Proper meta tags
- Logo and favicons on all pages
- Basic syntax errors in HTML, CSS, and JS files

---

### `cleanup()` (Placeholder)

**Purpose**: Final cleanup and optimization
**Parameters**: None
**Returns**: None
**Description**: Planned functionality for final website optimization and cleanup.

## File System Operations

### Directory Structure Operations

```python
# Create directories
os.makedirs(directory_path, exist_ok=True)

# Copy files
shutil.copy2(source_file, destination_file)

# Copy directories
shutil.copytree(source_directory, destination_directory)

# Remove files/directories
os.remove(file_path)
shutil.rmtree(directory_path)
```

### File I/O Operations

```python
# Read file content
with open(file_path, 'r') as f:
    content = f.read()

# Write file content
with open(file_path, 'w') as f:
    f.write(content)
```

## Template System Constants

### Component Types

```python
COMPONENT_TYPES = [
    "header", "footer", "hero", "offers",
    "details_comparison", "why_us", "about",
    "history", "guide", "faqs"
]
```

### Supported Countries

```python
COUNTRIES = [
    "Denmark", "France", "Portugal", "UK-IR"
]
```

### Template Comment Formats

```python
HTML_TEMPLATE_PATTERN = "<!-- Template {number}: {name} -->"
CSS_TEMPLATE_PATTERN = "/* Template {number}: {name} */"
JS_TEMPLATE_PATTERN = "// Template {number}: {name}"
```

### File Paths

```python
# Source paths
WEB_COMPONENTS_DIR = "web-components/"
MASTER_FOOTER_DIR = "master/footer/"
MASTER_OFFERS_DIR = "master/offers/"

# Destination paths
WEB_FOLDER_DIR = "web-folder/"
WEB_FOLDER_CSS = "web-folder/css/"
WEB_FOLDER_JS = "web-folder/scripts/"
WEB_FOLDER_STATIC = "web-folder/static/"
```

## Data Structures

### Template Group Structure

```python
template_groups = {
    "template_name": [
        (template_content, "html"),
        (template_content, "css"),
        (template_content, "js")
    ]
}
```

### Component Data Structure

```python
components_by_type = {
    "component_type": {
        "name": "selected_template_name",
        "templates": [
            (template_content, "html"),
            (template_content, "css"),
            (template_content, "js")
        ]
    }
}
```

## Error Handling Patterns

### File Existence Checks

```python
if os.path.exists(source_path):
    # Proceed with operation
else:
    print(f"Error: {source_path} does not exist.")
    return
```

### User Input Validation

```python
while True:
    try:
        choice = int(input("Your choice: "))
        if 1 <= choice <= max_options:
            break
        else:
            print(f"Please enter a number between 1 and {max_options}.")
    except ValueError:
        print("Please enter a valid number.")
```

### Template Extraction Validation

```python
if not templates:
    print(f"No templates found for {component}, skipping.")
    continue

if not template_groups:
    print(f"No named templates found for {component}, skipping.")
    continue
```

This API reference provides complete documentation of all functions, parameters, return values, and data structures used in the casino website generator system.
