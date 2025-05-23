# Development Workflow Guide

## Understanding the Project Flow

### High-Level Workflow

1. **User executes `starter.py`** → Main menu appears
2. **Country Configuration** → Copies country-specific content
3. **Component Import** → Selects and combines templates
4. **Website Generation** → Creates complete casino website in `web-folder/`

### Developer Workflow

1. **Analyze Requirements** → Understand what needs to be built/modified
2. **Identify Target Area** → Generator script vs. templates vs. output
3. **Make Changes** → Follow established patterns and conventions
4. **Test Generation** → Run `starter.py` to verify changes work
5. **Validate Output** → Check generated website in `web-folder/`

## Working with Different Project Areas

### 1. Modifying the Generator Script (`starter.py`)

**When to modify:**

- Adding new menu options
- Changing template selection logic
- Implementing placeholder functions
- Modifying file processing workflows

**Key areas:**

```python
def main():                    # Main menu system
def configure_template():      # Country selection logic
def import_components():       # Template assembly system
def extract_templates():       # Template parsing logic
def insert_html_component():   # HTML assembly rules
```

**Development process:**

1. Understand current function logic
2. Make incremental changes
3. Test with small modifications first
4. Verify file paths and regex patterns
5. Test end-to-end website generation

### 2. Creating/Modifying Templates (`web-components/`)

**When to modify:**

- Adding new design variants
- Updating casino content
- Improving responsive design
- Adding new interactive features

**Template structure per component:**

```
component-name/
├── component.html  # All HTML templates (1-10)
├── component.css   # All CSS templates (1-10)
└── component.js    # All JS templates (1-10)
```

**Development process:**

1. Choose target component directory
2. Edit the appropriate file (.html, .css, or .js)
3. Follow exact template comment syntax
4. Maintain numbering convention (1-10)
5. Test template extraction with generator
6. Verify output in generated website

### 3. Managing Country Content (`master/`)

**When to modify:**

- Adding new country support
- Updating legal requirements
- Changing country-specific offers
- Modifying footer content

**Structure:**

```
master/
├── footer/         # Country-specific footer content
│   └── {country}/  # Denmark, France, Portugal, UK-IR, etc.
└── offers/         # Country-specific offers content
    └── {country}/  # Denmark, France, Portugal, UK-IR
```

**Development process:**

1. Create new country directory
2. Add required content files
3. Update `countries` list in `starter.py`
4. Test country selection and file copying
5. Verify content appears in generated website

### 4. Implementing Placeholder Features

**Current placeholders in `starter.py`:**

- `download_images()` - Image downloading system
- `error_checking()` - Website validation
- `cleanup()` - Final optimization

**Empty script files:**

- `scripts-folder/checker.py` - Error checking logic
- `scripts-folder/downlaod_image.py` - Image download logic
- `scripts-folder/img_fix.py` - Image processing logic

**Implementation approach:**

1. Study the TODO list in `todo.md`
2. Design the feature scope
3. Implement in appropriate location
4. Integrate with main menu system
5. Test thoroughly with existing workflow

## Testing and Validation

### Local Testing Process

1. **Run the generator:**

   ```bash
   python3 starter.py
   ```

2. **Test each menu option:**

   - Option 1: Configure Country → Verify files copied
   - Option 2: Import Components → Check template selection
   - Option 3-5: Test placeholder functions

3. **Validate output:**
   - Check `web-folder/index.html` structure
   - Verify `web-folder/css/styles.css` compilation
   - Test `web-folder/scripts/main.js` functionality
   - Validate responsive design

### Website Testing

1. **Open generated website:**

   ```bash
   cd web-folder
   # Use local server or open index.html directly
   ```

2. **Test functionality:**

   - Navigation menus
   - Responsive design
   - Interactive elements
   - Form submissions (if any)
   - Mobile compatibility

3. **Validate casino requirements:**
   - Age verification notices present
   - Responsible gambling messages
   - Legal compliance elements
   - Bonus/promotion displays

## Common Development Scenarios

### Adding a New Component Type

1. **Create component directory:**

   ```bash
   mkdir web-components/new-component
   ```

2. **Create component files:**

   - `new-component.html` (with 10 templates)
   - `new-component.css` (with 10 templates)
   - `new-component.js` (with 10 templates)

3. **Update component order in `starter.py`:**

   ```python
   component_order = [
       "header", "hero", "offers", "new-component",
       "details_comparison", "why_us", "about",
       "history", "guide", "faqs", "footer"
   ]
   ```

4. **Test component integration**

### Modifying Template Extraction Logic

1. **Understand current regex patterns:**

   ```python
   # HTML: <!-- Template \d+: [^>]+ -->
   # CSS:  /\* Template \d+: [^*]+ \*/
   # JS:   // Template \d+: [^\n]+
   ```

2. **Test regex changes carefully:**

   - Use regex testing tools
   - Verify with existing templates
   - Test edge cases

3. **Update extraction functions accordingly**

### Adding Country Support

1. **Create country directories:**

   ```bash
   mkdir master/footer/NewCountry
   mkdir master/offers/NewCountry
   ```

2. **Add country content files**

3. **Update starter.py countries list:**
   ```python
   countries = [
       "Denmark", "France", "Portugal",
       "UK-IR", "NewCountry"
   ]
   ```

## Debugging Common Issues

### Template Extraction Problems

**Issue**: Templates not being extracted
**Solution**:

- Check comment syntax exactly matches regex
- Verify template numbering (1-10)
- Ensure no special characters in template names

### File Path Issues

**Issue**: Files not found during copying
**Solution**:

- Verify directory structure matches expectations
- Check for typos in path construction
- Ensure source files exist before copying

### HTML Assembly Problems

**Issue**: Components not inserting correctly
**Solution**:

- Review `insert_html_component()` logic
- Check component processing order
- Verify HTML structure assumptions

### CSS/JS Compilation Issues

**Issue**: Styles or scripts not working
**Solution**:

- Check template extraction worked
- Verify CSS variables and selectors
- Test JavaScript syntax and dependencies

## Performance Considerations

### Template Processing

- Template extraction uses regex on potentially large files
- Random selection processes all templates before choosing
- File I/O operations copy country content

### Generated Website

- CSS compilation combines all component styles
- JavaScript compilation combines all component scripts
- Image optimization should be implemented in placeholder functions

### Development Efficiency

- Test changes incrementally
- Use small template sets for rapid iteration
- Cache extracted templates during development

## Best Practices

### Code Organization

- Keep template syntax consistent
- Use descriptive template names
- Maintain logical component organization
- Document complex regex patterns

### Content Management

- Update country content regularly
- Maintain legal compliance across all countries
- Keep casino terminology current
- Test responsive design across devices

### Quality Assurance

- Validate HTML semantics
- Test accessibility compliance
- Check cross-browser compatibility
- Verify legal requirement coverage

This workflow guide ensures consistent, efficient development while maintaining the integrity of the casino website generation system.
