#!/usr/bin/env python3

import random
import os
import shutil
import re

def main():
    """Main function to display menu and handle user choices."""
    print("\n===== Casino Website Starter Tool =====\n")
    print("Select an option:")
    print("1. Configure Country")
    print("2. Import Components")
    print("3. Download Images")
    print("4. Error Checking")
    print("5. Clean Up")

    while True:
        try:
            choice = int(input("\nYour choice (1-5): "))
            if 1 <= choice <= 5:
                break
            else:
                print("Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")
    
    if choice == 1:
        configure_template()
    elif choice == 2:
        import_components()
    elif choice == 3:
        download_images()
    elif choice == 4:
        error_checking()
    elif choice == 5:
        cleanup()

def configure_template():
    """Configure starter template by selecting a country and copying related files."""
    # List of countries from which we'll randomly select 7
    countries = [
        "Denmark", "France", "Portugal", "UK-IR"
    ]

    # Display countries with their indices
    print("Please select a country by entering its number:")
    for i, country in enumerate(countries, 1):
        print(f"{i}. {country}")

    # Get user input
    while True:
        try:
            choice = int(input(f"\nYour choice (1-{len(countries)}): "))
            if 1 <= choice <= len(countries):
                break
            else:
                print(f"Please enter a number between 1 and {len(countries)}.")
        except ValueError:
            print("Please enter a valid number.")

    # Get the selected country
    selected_country = countries[choice - 1]
    print(f"\nYou selected: {selected_country}")

    # Define source and destination paths for footer
    current_dir = os.path.dirname(os.path.abspath(__file__))
    footer_source_dir = os.path.join(current_dir, "master", "footer", selected_country)
    footer_dest_dir = os.path.join(current_dir, "web-folder", "static", "footer")

    # Ensure the footer destination directory exists
    os.makedirs(footer_dest_dir, exist_ok=True)

    # Copy all files from footer source to footer destination
    if os.path.exists(footer_source_dir):
        print(f"\nCopying footer files from {footer_source_dir} to {footer_dest_dir}...")
        # First, remove existing files in the destination directory
        for item in os.listdir(footer_dest_dir):
            item_path = os.path.join(footer_dest_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        
        # Copy new files from the selected country
        for item in os.listdir(footer_source_dir):
            source_item = os.path.join(footer_source_dir, item)
            dest_item = os.path.join(footer_dest_dir, item)
            if os.path.isfile(source_item):
                shutil.copy2(source_item, dest_item)
                print(f"Copied footer file: {item}")
            elif os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item)
                print(f"Copied footer directory: {item}")
        
        print("\nFooter files copied successfully!")
    else:
        print(f"\nError: Footer source directory {footer_source_dir} does not exist.")

    # Define source and destination paths for offers
    offers_source_dir = os.path.join(current_dir, "master", "offers", selected_country)
    offers_dest_dir = os.path.join(current_dir, "web-folder", "static", "offers")

    # Ensure the offers destination directory exists
    os.makedirs(offers_dest_dir, exist_ok=True)

    # Copy all files from offers source to offers destination
    if os.path.exists(offers_source_dir):
        print(f"\nCopying offers files from {offers_source_dir} to {offers_dest_dir}...")
        # First, remove existing files in the destination directory
        for item in os.listdir(offers_dest_dir):
            item_path = os.path.join(offers_dest_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        
        # Copy new files from the selected country
        for item in os.listdir(offers_source_dir):
            source_item = os.path.join(offers_source_dir, item)
            dest_item = os.path.join(offers_dest_dir, item)
            if os.path.isfile(source_item):
                shutil.copy2(source_item, dest_item)
                print(f"Copied offers file: {item}")
            elif os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item)
                print(f"Copied offers directory: {item}")
        
        print("\nOffers files copied successfully!")
    else:
        print(f"\nError: Offers source directory {offers_source_dir} does not exist.")

def import_components():
    """Import components from web-components folder to web-folder."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    components_dir = os.path.join(current_dir, "web-components")
    web_folder_dir = os.path.join(current_dir, "web-folder")
    
    # Check if web-components directory exists
    if not os.path.exists(components_dir):
        print(f"Error: web-components directory not found at {components_dir}")
        return
    
    # Ask if the user wants to clean up destination files before importing
    while True:
        cleanup_response = input("\nDo you want to clean up destination files before importing? (y/n): ").strip().lower()
        if cleanup_response in ['y', 'n']:
            break
        print("Please enter 'y' or 'n'.")
    
    cleanup_files = cleanup_response == 'y'
    
    # Get all component types (subdirectories in web-components)
    component_types = [d for d in os.listdir(components_dir) 
                      if os.path.isdir(os.path.join(components_dir, d)) and not d.startswith('.')]
    
    if not component_types:
        print("No component types found in web-components directory.")
        return
    
    # Define logical order for components
    component_order = [
        "header", "hero", "offers", "details_comparison", 
        "why_us", "about", "history", "guide", "faqs", "footer"
    ]
    
    # Sort component types based on the defined order
    sorted_component_types = sorted(
        component_types,
        key=lambda x: component_order.index(x) if x in component_order else len(component_order)
    )
    
    print("\nAvailable component types:")
    for i, comp_type in enumerate(sorted_component_types, 1):
        print(f"{i}. {comp_type}")
    
    # Ask user which components to import
    print("\nSelect components to import (comma-separated numbers, or 'all' for all):")
    selection = input("Your selection: ").strip().lower()
    
    selected_components = []
    if selection == 'all':
        selected_components = sorted_component_types
    else:
        try:
            indices = [int(idx.strip()) for idx in selection.split(',')]
            for idx in indices:
                if 1 <= idx <= len(sorted_component_types):
                    selected_components.append(sorted_component_types[idx-1])
                else:
                    print(f"Ignoring invalid selection: {idx}")
        except ValueError:
            print("Invalid input. Please enter comma-separated numbers.")
            return
    
    if not selected_components:
        print("No valid components selected.")
        return
    
    print(f"\nSelected components: {', '.join(selected_components)}")
    
    # Create directories in web-folder if they don't exist
    css_dir = os.path.join(web_folder_dir, "css")
    js_dir = os.path.join(web_folder_dir, "scripts")
    os.makedirs(css_dir, exist_ok=True)
    os.makedirs(js_dir, exist_ok=True)
    
    # Path to the files
    index_file = os.path.join(web_folder_dir, "index.html")
    css_file = os.path.join(css_dir, "styles.css")
    js_file = os.path.join(js_dir, "main.js")
    
    # Clean up destination files if requested
    if cleanup_files:
        print("\nCleaning up destination files...")
        
        # Create/reset HTML file
        with open(index_file, 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casino Website</title>
    <link rel="stylesheet" href="css/styles.css">
    <meta name="description" content="The best online casino games and bonuses">
    <meta name="author" content="Casino Website">
</head>

<body>
    <!-- Content will be added by the import_components function -->

    <script src="scripts/main.js"></script>
</body>

</html>""")
        
        # Create/reset CSS file
        with open(css_file, 'w') as f:
            f.write("""/* Main Styles */
:root {
    --primary-color: #2c3e50;
    --secondary-color: #e74c3c;
    --accent-color: #f1c40f;
    --text-color: #333;
    --light-color: #ecf0f1;
    --dark-color: #2c3e50;
    --success-color: #2ecc71;
    --warning-color: #f39c12;
    --danger-color: #e74c3c;
    --border-radius: 4px;
    --box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: var(--text-color);
    background-color: var(--light-color);
}

a {
    text-decoration: none;
    color: var(--primary-color);
}

a:hover {
    color: var(--secondary-color);
}

li {
    list-style: none;
}

.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 15px;
}

.btn {
    display: inline-block;
    padding: 8px 16px;
    border: none;
    border-radius: var(--border-radius);
    background-color: var(--primary-color);
    color: white;
    cursor: pointer;
    transition: background-color 0.3s;
}

.btn:hover {
    background-color: var(--secondary-color);
}

.btn-primary {
    background-color: var(--primary-color);
}

.btn-secondary {
    background-color: var(--secondary-color);
}

.btn-accent {
    background-color: var(--accent-color);
    color: var(--dark-color);
}

/* Responsive utilities */
@media (max-width: 768px) {
    .container {
        padding: 0 10px;
    }
}

/* Casino-specific styles */
.casino-card {
    border-radius: var(--border-radius);
    background-color: white;
    padding: 15px;
    margin-bottom: 20px;
    box-shadow: var(--box-shadow);
}

.bonus-tag {
    display: inline-block;
    background-color: var(--accent-color);
    color: var(--dark-color);
    padding: 4px 8px;
    border-radius: var(--border-radius);
    font-weight: bold;
    font-size: 0.9em;
}

.age-verification {
    background-color: var(--dark-color);
    color: white;
    text-align: center;
    padding: 10px;
    font-size: 0.9em;
}

/* Common Header Elements */
.header-content {
  display: flex;
  align-items: center;
  justify-content: space-between;
  height: 70px;
}

.logo-link {
  display: flex;
  align-items: center;
  gap: 10px;
  font-weight: 700;
  font-size: 1.5rem;
}

.logo-icon {
  font-size: 1.8rem;
}

.nav-list {
  display: flex;
  gap: 2rem;
}

.nav-link {
  font-weight: 500;
  position: relative;
  padding: 0.5rem 0;
  transition: all 0.3s ease;
}

.nav-link.active,
.nav-link:hover {
  color: #3b82f6;
}

.cta-button {
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  transition: all 0.3s ease;
  border: none;
  cursor: pointer;
  display: inline-block;
}

.mobile-menu-toggle {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
  padding: 8px;
}

.mobile-menu-toggle span {
  width: 24px;
  height: 2px;
  background-color: currentColor;
  border-radius: 1px;
  transition: all 0.3s ease;
}

/* Component styles will be added by the import_components function */""")
        
        # Create/reset JS file
        with open(js_file, 'w') as f:
            f.write("""// Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Casino website loaded');
    
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Add responsible gambling collapsible info
    const responsibleGamblingElements = document.querySelectorAll('.responsible-gambling-toggle');
    if (responsibleGamblingElements.length > 0) {
        responsibleGamblingElements.forEach(element => {
            element.addEventListener('click', function() {
                const content = this.nextElementSibling;
                if (content.style.maxHeight) {
                    content.style.maxHeight = null;
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            });
        });
    }
});

// Component scripts will be added by the import_components function""")
        
        print("Files reset to default state.")
    else:
        # Ensure files exist if not cleaning up
        if not os.path.exists(css_file):
            with open(css_file, 'w') as f:
                f.write("/* Main Styles */\n\n")
        
        if not os.path.exists(js_file):
            with open(js_file, 'w') as f:
                f.write("// Main JavaScript\n\n")
                
        if not os.path.exists(index_file):
            with open(index_file, 'w') as f:
                f.write("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Casino Website</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <script src="scripts/main.js"></script>
</body>
</html>""")
    
    # Read the current files
    with open(index_file, 'r') as f:
        html_content = f.read()
    
    with open(css_file, 'r') as f:
        css_content = f.read()
    
    with open(js_file, 'r') as f:
        js_content = f.read()
    
    # Parse the HTML to insert components in the right places
    html_doc = parse_html(html_content)
    
    # Dictionary to hold all component data grouped by type
    components_by_type = {}
    
    # Process each selected component
    for comp_type in selected_components:
        comp_dir = os.path.join(components_dir, comp_type)
        templates = []
        
        # Find HTML templates in this component directory
        html_files = [f for f in os.listdir(comp_dir) if f.endswith('.html')]
        if html_files:
            # For simplicity, we'll just use the first HTML file found
            html_file = os.path.join(comp_dir, html_files[0])
            with open(html_file, 'r') as f:
                html_templates = extract_templates(f.read(), "html")
                templates.extend([(template, "html") for template in html_templates])
        
        # Find CSS templates
        css_files = [f for f in os.listdir(comp_dir) if f.endswith('.css')]
        if css_files:
            css_file_path = os.path.join(comp_dir, css_files[0])
            with open(css_file_path, 'r') as f:
                css_templates = extract_templates(f.read(), "css")
                templates.extend([(template, "css") for template in css_templates])
        
        # Find JS templates
        js_files = [f for f in os.listdir(comp_dir) if f.endswith('.js')]
        if js_files:
            js_file_path = os.path.join(comp_dir, js_files[0])
            with open(js_file_path, 'r') as f:
                js_templates = extract_templates(f.read(), "js")
                templates.extend([(template, "js") for template in js_templates])
        
        if not templates:
            print(f"No templates found for {comp_type}, skipping.")
            continue
        
        # Group templates by their name
        template_groups = {}
        for template, file_type in templates:
            template_name = extract_template_name(template, file_type)
            if template_name:
                if template_name not in template_groups:
                    template_groups[template_name] = []
                template_groups[template_name].append((template, file_type))
        
        if not template_groups:
            print(f"No named templates found for {comp_type}, skipping.")
            continue
        
        # Randomly select a template group
        selected_template_name = random.choice(list(template_groups.keys()))
        selected_templates = template_groups[selected_template_name]
        
        print(f"Selected '{selected_template_name}' for {comp_type}")
        
        # Store the component data for later processing in the correct order
        components_by_type[comp_type] = {
            'name': selected_template_name,
            'templates': selected_templates
        }
    
    # Process HTML components in the logical order
    for comp_type in component_order:
        if comp_type not in components_by_type:
            continue
        
        component_data = components_by_type[comp_type]
        for template, file_type in component_data['templates']:
            if file_type == "html":
                html_doc = insert_html_component(html_doc, template, comp_type)
    
    # Process CSS and JS components
    for comp_type in component_order:
        if comp_type not in components_by_type:
            continue
        
        component_data = components_by_type[comp_type]
        for template, file_type in component_data['templates']:
            if file_type == "css":
                css_content = f"{css_content}\n\n/* {comp_type.capitalize()} Styles */\n{template}"
            elif file_type == "js":
                js_content = f"{js_content}\n\n// {comp_type.capitalize()} JavaScript\n{template}"
    
    # Write back the modified files
    with open(index_file, 'w') as f:
        f.write(html_doc)
    
    with open(css_file, 'w') as f:
        f.write(css_content)
    
    with open(js_file, 'w') as f:
        f.write(js_content)
    
    print("\nComponents imported successfully!")

def parse_html(html_content):
    """Simple parsing of HTML content."""
    return html_content

def extract_templates(content, file_type):
    """Extract templates from content based on file type."""
    templates = []
    
    if file_type == "html":
        # Extract HTML templates (between comments)
        pattern = r'<!-- Template \d+: [^>]+ -->([\s\S]*?)(?=<!-- Template \d+:|$)'
        matches = re.finditer(pattern, content)
        for match in matches:
            templates.append(match.group(0))
    
    elif file_type == "css":
        # Extract CSS templates (between comments)
        pattern = r'/\* Template \d+: [^*]+ \*/([\s\S]*?)(?=/\* Template \d+:|$)'
        matches = re.finditer(pattern, content)
        for match in matches:
            templates.append(match.group(0))
    
    elif file_type == "js":
        # Extract JS templates (between comments)
        pattern = r'// Template \d+: [^\n]+ \n([\s\S]*?)(?=// Template \d+:|$)'
        matches = re.finditer(pattern, content)
        for match in matches:
            templates.append(match.group(0))
    
    return templates

def extract_template_name(template, file_type):
    """Extract template name from the template content."""
    if file_type == "html":
        match = re.search(r'<!-- Template \d+: ([^>]+) -->', template)
    elif file_type == "css":
        match = re.search(r'/\* Template \d+: ([^*]+) \*/', template)
    elif file_type == "js":
        match = re.search(r'// Template \d+: ([^\n]+)', template)
    else:
        return None
    
    return match.group(1).strip() if match else None

def insert_html_component(html_doc, template, comp_type):
    """Insert HTML component into the appropriate place in the document."""
    # Simple implementation - we'll insert components based on their type
    
    # Remove the template comment
    template_content = re.sub(r'<!-- Template \d+: [^>]+ -->', '', template, 1).strip()
    
    # First check if we have body content already
    body_content_exists = re.search(r'<body>(.*?)</body>', html_doc, re.DOTALL)
    
    if comp_type == "header":
        # Headers should always be inserted right after the opening <body> tag
        if "<body>" in html_doc:
            return html_doc.replace("<body>", f"<body>\n\n    <!-- Header Section -->\n    {template_content}\n")
        else:
            # If no body tag found, something is wrong with the HTML
            return html_doc
    
    elif comp_type == "hero":
        # Hero should be inserted after header if it exists, or after body tag if no header
        if "<!-- Header Section -->" in html_doc:
            # Find the end of the header section content
            header_match = re.search(r'<!-- Header Section -->(.*?)(?=<!--|\n\s*\n|</body>)', html_doc, re.DOTALL)
            if header_match:
                header_content = header_match.group(0)
                return html_doc.replace(header_content, f"{header_content}\n\n    <!-- Hero Section -->\n    {template_content}")
            else:
                # Fallback if regex match fails
                return html_doc.replace("<!-- Header Section -->", f"<!-- Header Section -->\n\n    <!-- Hero Section -->\n    {template_content}")
        else:
            # If no header, insert after body tag
            return html_doc.replace("<body>", f"<body>\n\n    <!-- Hero Section -->\n    {template_content}\n")
    
    elif comp_type == "footer":
        # Footer should always be at the end, right before closing </body> tag
        return html_doc.replace("</body>", f"\n    <!-- Footer Section -->\n    {template_content}\n\n</body>")
    
    else:
        # For other components, determine their position in the document
        # Check for existing components to position relative to
        if "<!-- Hero Section -->" in html_doc:
            # Insert after hero section
            hero_match = re.search(r'<!-- Hero Section -->(.*?)(?=<!--|\n\s*\n|</body>)', html_doc, re.DOTALL)
            if hero_match:
                hero_content = hero_match.group(0)
                return html_doc.replace(hero_content, f"{hero_content}\n\n    <!-- {comp_type.capitalize()} Section -->\n    {template_content}")
            else:
                # Fallback
                return html_doc.replace("<!-- Hero Section -->", f"<!-- Hero Section -->\n\n    <!-- {comp_type.capitalize()} Section -->\n    {template_content}")
        
        elif "<!-- Header Section -->" in html_doc and "<!-- Hero Section -->" not in html_doc:
            # If we have a header but no hero, insert after header
            header_match = re.search(r'<!-- Header Section -->(.*?)(?=<!--|\n\s*\n|</body>)', html_doc, re.DOTALL)
            if header_match:
                header_content = header_match.group(0)
                return html_doc.replace(header_content, f"{header_content}\n\n    <!-- {comp_type.capitalize()} Section -->\n    {template_content}")
            else:
                # Fallback
                return html_doc.replace("<!-- Header Section -->", f"<!-- Header Section -->\n\n    <!-- {comp_type.capitalize()} Section -->\n    {template_content}")
        
        else:
            # Default: insert before the script tag or </body> if no script
            if "<script" in html_doc:
                # Find the first script tag
                script_match = re.search(r'(\s*<script.*?)', html_doc, re.DOTALL)
                if script_match:
                    script_tag = script_match.group(1)
                    return html_doc.replace(script_tag, f"\n    <!-- {comp_type.capitalize()} Section -->\n    {template_content}\n{script_tag}")
                else:
                    # Fallback
                    return html_doc.replace("<script", f"\n    <!-- {comp_type.capitalize()} Section -->\n    {template_content}\n\n    <script", 1)
            else:
                # Insert before </body>
                return html_doc.replace("</body>", f"\n    <!-- {comp_type.capitalize()} Section -->\n    {template_content}\n\n</body>")

def download_images():
    print("Download images option selected. This feature is not yet implemented.")

def error_checking():
    """Placeholder function for error checking."""
    print("Error checking option selected. This feature is not yet implemented.")

def cleanup():
    """Placeholder function for cleanup."""
    print("Cleanup option selected. This feature is not yet implemented.")

if __name__ == "__main__":
    main() 