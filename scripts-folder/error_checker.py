#!/usr/bin/env python3
"""
Error Checker Module

Handles comprehensive error checking and validation for generated casino websites
in the Casino Website Generator.
"""

import os
import re
import html.parser
from typing import List, Dict, Tuple, Optional


def error_checking():
    """
    Main function for comprehensive website error checking.
    
    Performs validation checks on the generated casino website:
    - Empty links with '#'
    - Missing or incorrect CSS files
    - Proper meta tags
    - Logo and favicon presence
    - Basic syntax errors in HTML, CSS, and JS
    """
    print("=== Website Error Checking ===")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_folder = os.path.join(current_dir, "web-folder")
    
    if not os.path.exists(web_folder):
        print("Error: web-folder directory not found!")
        return
    
    print("Starting comprehensive website validation...")
    
    # Run all validation checks
    results = {
        "empty_links": check_empty_links(web_folder),
        "css_files": check_css_files(web_folder),
        "meta_tags": check_meta_tags(web_folder),
        "logos_favicons": check_logos_and_favicons(web_folder),
        "html_syntax": check_html_syntax(web_folder),
        "css_syntax": check_css_syntax(web_folder),
        "js_syntax": check_js_syntax(web_folder),
        "casino_compliance": check_casino_compliance(web_folder),
        "responsive_design": check_responsive_design(web_folder)
    }
    
    # Display results summary
    display_results_summary(results)


def check_empty_links(web_folder: str) -> Dict[str, List[str]]:
    """
    Check for empty links with '#' in HTML files.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results with found empty links
    """
    print("Checking for empty links...")
    
    empty_links = []
    html_files = _get_html_files(web_folder)
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Find all href attributes
        href_pattern = r'href\s*=\s*["\']([^"\']*)["\']'
        matches = re.findall(href_pattern, content, re.IGNORECASE)
        
        for match in matches:
            if match == '#' or match == '':
                empty_links.append({
                    'file': os.path.relpath(html_file, web_folder),
                    'link': match,
                    'line': _get_line_number(content, f'href="{match}"')
                })
    
    return {
        'status': 'PASS' if not empty_links else 'FAIL',
        'issues': empty_links,
        'count': len(empty_links)
    }


def check_css_files(web_folder: str) -> Dict[str, any]:
    """
    Check that correct CSS files are linked and exist.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of CSS file validation
    """
    print("Checking CSS file references...")
    
    issues = []
    html_files = _get_html_files(web_folder)
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find CSS link references
        css_pattern = r'<link[^>]*href\s*=\s*["\']([^"\']*\.css)["\'][^>]*>'
        css_links = re.findall(css_pattern, content, re.IGNORECASE)
        
        for css_link in css_links:
            # Resolve relative path
            css_path = os.path.join(web_folder, css_link)
            if not os.path.exists(css_path):
                issues.append({
                    'file': os.path.relpath(html_file, web_folder),
                    'missing_css': css_link,
                    'line': _get_line_number(content, css_link)
                })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def check_meta_tags(web_folder: str) -> Dict[str, any]:
    """
    Check for proper meta tags in HTML files.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of meta tag validation
    """
    print("Checking meta tags...")
    
    required_meta_tags = [
        'charset',
        'viewport',
        'description',
        'author'
    ]
    
    issues = []
    html_files = _get_html_files(web_folder)
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing_tags = []
        
        for tag in required_meta_tags:
            if tag == 'charset':
                if not re.search(r'<meta[^>]*charset[^>]*>', content, re.IGNORECASE):
                    missing_tags.append('charset')
            elif tag == 'viewport':
                if not re.search(r'<meta[^>]*name\s*=\s*["\']viewport["\'][^>]*>', content, re.IGNORECASE):
                    missing_tags.append('viewport')
            elif tag == 'description':
                if not re.search(r'<meta[^>]*name\s*=\s*["\']description["\'][^>]*>', content, re.IGNORECASE):
                    missing_tags.append('description')
            elif tag == 'author':
                if not re.search(r'<meta[^>]*name\s*=\s*["\']author["\'][^>]*>', content, re.IGNORECASE):
                    missing_tags.append('author')
        
        if missing_tags:
            issues.append({
                'file': os.path.relpath(html_file, web_folder),
                'missing_meta_tags': missing_tags
            })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def check_logos_and_favicons(web_folder: str) -> Dict[str, any]:
    """
    Check for logo and favicon presence.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of logo and favicon validation
    """
    print("Checking logos and favicons...")
    
    issues = []
    
    # Check for favicon
    favicon_paths = [
        os.path.join(web_folder, 'favicon.ico'),
        os.path.join(web_folder, 'static', 'images', 'favicon.ico'),
        os.path.join(web_folder, 'static', 'images', 'icons', 'favicon.ico')
    ]
    
    favicon_found = any(os.path.exists(path) for path in favicon_paths)
    if not favicon_found:
        issues.append({
            'type': 'favicon',
            'message': 'No favicon.ico found',
            'searched_paths': favicon_paths
        })
    
    # Check for logo references in HTML
    html_files = _get_html_files(web_folder)
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for logo-related elements
        logo_patterns = [
            r'class\s*=\s*["\'][^"\']*logo[^"\']*["\']',
            r'<img[^>]*alt\s*=\s*["\'][^"\']*logo[^"\']*["\'][^>]*>',
            r'<img[^>]*src\s*=\s*["\'][^"\']*logo[^"\']*["\'][^>]*>'
        ]
        
        logo_found = any(re.search(pattern, content, re.IGNORECASE) for pattern in logo_patterns)
        
        if not logo_found:
            issues.append({
                'type': 'logo',
                'file': os.path.relpath(html_file, web_folder),
                'message': 'No logo elements found'
            })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def check_html_syntax(web_folder: str) -> Dict[str, any]:
    """
    Check for basic HTML syntax errors.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of HTML syntax validation
    """
    print("Checking HTML syntax...")
    
    issues = []
    html_files = _get_html_files(web_folder)
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic HTML validation
            parser = HTMLValidator()
            parser.feed(content)
            
            if parser.errors:
                issues.append({
                    'file': os.path.relpath(html_file, web_folder),
                    'errors': parser.errors
                })
        except Exception as e:
            issues.append({
                'file': os.path.relpath(html_file, web_folder),
                'errors': [f"Parse error: {str(e)}"]
            })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def check_css_syntax(web_folder: str) -> Dict[str, any]:
    """
    Check for basic CSS syntax errors.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of CSS syntax validation
    """
    print("Checking CSS syntax...")
    
    issues = []
    css_files = _get_css_files(web_folder)
    
    for css_file in css_files:
        try:
            with open(css_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic CSS validation
            css_errors = _validate_css_basic(content)
            
            if css_errors:
                issues.append({
                    'file': os.path.relpath(css_file, web_folder),
                    'errors': css_errors
                })
        except Exception as e:
            issues.append({
                'file': os.path.relpath(css_file, web_folder),
                'errors': [f"Parse error: {str(e)}"]
            })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def check_js_syntax(web_folder: str) -> Dict[str, any]:
    """
    Check for basic JavaScript syntax errors.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of JavaScript syntax validation
    """
    print("Checking JavaScript syntax...")
    
    issues = []
    js_files = _get_js_files(web_folder)
    
    for js_file in js_files:
        try:
            with open(js_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Basic JS validation
            js_errors = _validate_js_basic(content)
            
            if js_errors:
                issues.append({
                    'file': os.path.relpath(js_file, web_folder),
                    'errors': js_errors
                })
        except Exception as e:
            issues.append({
                'file': os.path.relpath(js_file, web_folder),
                'errors': [f"Parse error: {str(e)}"]
            })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def check_casino_compliance(web_folder: str) -> Dict[str, any]:
    """
    Check for casino-specific compliance requirements.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of casino compliance validation
    """
    print("Checking casino compliance...")
    
    issues = []
    html_files = _get_html_files(web_folder)
    
    required_elements = [
        {
            'name': 'Age Verification',
            'patterns': [r'18\+', r'21\+', r'age.verification', r'must.be.*years']
        },
        {
            'name': 'Responsible Gambling',
            'patterns': [r'responsible.gambling', r'gamble.responsibly', r'gambling.problem']
        },
        {
            'name': 'Terms and Conditions',
            'patterns': [r'terms.*conditions', r'terms.*service', r'T&C']
        }
    ]
    
    for html_file in html_files:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        missing_elements = []
        
        for element in required_elements:
            found = any(re.search(pattern, content, re.IGNORECASE) for pattern in element['patterns'])
            if not found:
                missing_elements.append(element['name'])
        
        if missing_elements:
            issues.append({
                'file': os.path.relpath(html_file, web_folder),
                'missing_compliance': missing_elements
            })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def check_responsive_design(web_folder: str) -> Dict[str, any]:
    """
    Check for responsive design implementation.
    
    Args:
        web_folder (str): Path to web-folder directory
        
    Returns:
        dict: Results of responsive design validation
    """
    print("Checking responsive design...")
    
    issues = []
    css_files = _get_css_files(web_folder)
    
    responsive_indicators = [
        r'@media',
        r'max-width',
        r'min-width',
        r'viewport',
        r'mobile',
        r'tablet',
        r'desktop'
    ]
    
    for css_file in css_files:
        with open(css_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        responsive_found = any(re.search(indicator, content, re.IGNORECASE) for indicator in responsive_indicators)
        
        if not responsive_found:
            issues.append({
                'file': os.path.relpath(css_file, web_folder),
                'message': 'No responsive design indicators found'
            })
    
    return {
        'status': 'PASS' if not issues else 'FAIL',
        'issues': issues,
        'count': len(issues)
    }


def display_results_summary(results: Dict[str, Dict]) -> None:
    """
    Display a summary of all validation results.
    
    Args:
        results (dict): All validation results
    """
    print("\n" + "="*50)
    print("WEBSITE VALIDATION SUMMARY")
    print("="*50)
    
    total_issues = 0
    
    for check_name, result in results.items():
        status = result['status']
        count = result['count']
        total_issues += count
        
        status_symbol = "✅" if status == 'PASS' else "❌"
        print(f"{status_symbol} {check_name.replace('_', ' ').title()}: {status}")
        
        if count > 0:
            print(f"   └─ {count} issue(s) found")
    
    print("\n" + "-"*50)
    print(f"Total Issues Found: {total_issues}")
    
    if total_issues == 0:
        print("🎉 All checks passed! Website is ready for deployment.")
    else:
        print("⚠️  Please review and fix the issues above before deployment.")


# Helper functions

def _get_html_files(directory: str) -> List[str]:
    """Get all HTML files in directory and subdirectories."""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files


def _get_css_files(directory: str) -> List[str]:
    """Get all CSS files in directory and subdirectories."""
    css_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.css'):
                css_files.append(os.path.join(root, file))
    return css_files


def _get_js_files(directory: str) -> List[str]:
    """Get all JavaScript files in directory and subdirectories."""
    js_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                js_files.append(os.path.join(root, file))
    return js_files


def _get_line_number(content: str, search_text: str) -> int:
    """Get line number where text appears in content."""
    lines = content.split('\n')
    for i, line in enumerate(lines):
        if search_text in line:
            return i + 1
    return 0


def _validate_css_basic(content: str) -> List[str]:
    """Basic CSS validation."""
    errors = []
    
    # Check for unmatched braces
    open_braces = content.count('{')
    close_braces = content.count('}')
    
    if open_braces != close_braces:
        errors.append(f"Unmatched braces: {open_braces} open, {close_braces} close")
    
    # Check for common syntax errors
    if re.search(r';\s*}', content):
        errors.append("Semicolon before closing brace found")
    
    return errors


def _validate_js_basic(content: str) -> List[str]:
    """Basic JavaScript validation."""
    errors = []
    
    # Check for unmatched parentheses
    open_parens = content.count('(')
    close_parens = content.count(')')
    
    if open_parens != close_parens:
        errors.append(f"Unmatched parentheses: {open_parens} open, {close_parens} close")
    
    # Check for unmatched braces
    open_braces = content.count('{')
    close_braces = content.count('}')
    
    if open_braces != close_braces:
        errors.append(f"Unmatched braces: {open_braces} open, {close_braces} close")
    
    return errors


class HTMLValidator(html.parser.HTMLParser):
    """Simple HTML validator."""
    
    def __init__(self):
        super().__init__()
        self.errors = []
        self.stack = []
    
    def handle_starttag(self, tag, attrs):
        if tag not in ['area', 'base', 'br', 'col', 'embed', 'hr', 'img', 'input', 'link', 'meta', 'param', 'source', 'track', 'wbr']:
            self.stack.append(tag)
    
    def handle_endtag(self, tag):
        if self.stack and self.stack[-1] == tag:
            self.stack.pop()
        elif tag in self.stack:
            self.errors.append(f"Mismatched closing tag: {tag}")
    
    def error(self, message):
        self.errors.append(message) 