#!/usr/bin/env python3
"""
Cleanup Manager Module

Handles final cleanup and optimization for generated casino websites
in the Casino Website Generator.
"""

import os
import shutil
import gzip
from typing import List, Dict, Optional


def cleanup():
    """
    Main function for final website cleanup and optimization.
    
    Performs:
    - Remove temporary files
    - Optimize file sizes
    - Clean up empty directories
    - Organize final file structure
    - Generate production-ready files
    """
    print("=== Website Cleanup System ===")
    print("1. Basic Cleanup")
    print("2. Full Optimization")
    print("3. Production Build")
    print("4. Clean Everything")
    
    while True:
        try:
            choice = int(input("\nYour choice (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    if choice == 1:
        basic_cleanup()
    elif choice == 2:
        full_optimization()
    elif choice == 3:
        production_build()
    elif choice == 4:
        clean_everything()


def basic_cleanup():
    """
    Perform basic cleanup operations.
    
    - Remove temporary files
    - Clean up empty directories
    - Remove duplicate files
    - Clear browser cache files
    """
    print("Starting basic cleanup...")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_folder = os.path.join(current_dir, "web-folder")
    
    if not os.path.exists(web_folder):
        print("Error: web-folder directory not found!")
        return
    
    cleanup_stats = {
        'temp_files': 0,
        'empty_dirs': 0,
        'cache_files': 0,
        'duplicate_files': 0
    }
    
    # Remove temporary files
    cleanup_stats['temp_files'] = _remove_temp_files(web_folder)
    
    # Remove empty directories
    cleanup_stats['empty_dirs'] = _remove_empty_directories(web_folder)
    
    # Remove cache files
    cleanup_stats['cache_files'] = _remove_cache_files(web_folder)
    
    # Remove duplicate files
    cleanup_stats['duplicate_files'] = _remove_duplicate_files(web_folder)
    
    _display_cleanup_summary("Basic Cleanup", cleanup_stats)


def full_optimization():
    """
    Perform full optimization of the website.
    
    - Minify CSS and JavaScript
    - Optimize images
    - Compress files
    - Remove unused code
    """
    print("Starting full optimization...")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_folder = os.path.join(current_dir, "web-folder")
    
    optimization_stats = {
        'css_minified': 0,
        'js_minified': 0,
        'images_optimized': 0,
        'files_compressed': 0
    }
    
    # Minify CSS files
    optimization_stats['css_minified'] = _minify_css_files(web_folder)
    
    # Minify JavaScript files
    optimization_stats['js_minified'] = _minify_js_files(web_folder)
    
    # Optimize images
    optimization_stats['images_optimized'] = _optimize_images(web_folder)
    
    # Compress files
    optimization_stats['files_compressed'] = _compress_files(web_folder)
    
    _display_cleanup_summary("Full Optimization", optimization_stats)


def production_build():
    """
    Create production-ready build of the website.
    
    - Combine and minify all assets
    - Generate optimized file structure
    - Create deployment package
    - Generate sitemap and robots.txt
    """
    print("Creating production build...")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_folder = os.path.join(current_dir, "web-folder")
    dist_folder = os.path.join(current_dir, "dist")
    
    # Create dist directory
    if os.path.exists(dist_folder):
        shutil.rmtree(dist_folder)
    os.makedirs(dist_folder)
    
    production_stats = {
        'files_copied': 0,
        'assets_bundled': 0,
        'metadata_created': 0
    }
    
    # Copy optimized files to dist
    production_stats['files_copied'] = _copy_for_production(web_folder, dist_folder)
    
    # Bundle assets
    production_stats['assets_bundled'] = _bundle_assets(dist_folder)
    
    # Generate metadata files
    production_stats['metadata_created'] = _generate_metadata(dist_folder)
    
    _display_cleanup_summary("Production Build", production_stats)


def clean_everything():
    """
    Clean everything and reset to initial state.
    
    - Remove all generated files
    - Reset web-folder to default state
    - Clear all caches
    - Remove temporary directories
    """
    print("WARNING: This will remove all generated content!")
    confirm = input("Are you sure you want to proceed? (yes/no): ").strip().lower()
    
    if confirm != 'yes':
        print("Cleanup cancelled.")
        return
    
    print("Cleaning everything...")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_folder = os.path.join(current_dir, "web-folder")
    dist_folder = os.path.join(current_dir, "dist")
    
    # Remove dist folder
    if os.path.exists(dist_folder):
        shutil.rmtree(dist_folder)
        print("Removed dist/ directory")
    
    # Clean web-folder
    if os.path.exists(web_folder):
        # Keep directory structure but remove content
        for item in os.listdir(web_folder):
            item_path = os.path.join(web_folder, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        print("Cleaned web-folder/ directory")
    
    print("✅ Everything cleaned successfully!")


def get_file_sizes(directory: str) -> Dict[str, int]:
    """
    Get file sizes for all files in directory.
    
    Args:
        directory (str): Directory to analyze
        
    Returns:
        dict: File paths mapped to sizes in bytes
    """
    file_sizes = {}
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_sizes[file_path] = os.path.getsize(file_path)
            except OSError:
                file_sizes[file_path] = 0
    
    return file_sizes


def calculate_space_saved(before_sizes: Dict[str, int], after_sizes: Dict[str, int]) -> int:
    """
    Calculate space saved between before and after file sizes.
    
    Args:
        before_sizes (dict): File sizes before cleanup
        after_sizes (dict): File sizes after cleanup
        
    Returns:
        int: Bytes saved
    """
    before_total = sum(before_sizes.values())
    after_total = sum(after_sizes.values())
    return before_total - after_total


# Private helper functions

def _remove_temp_files(directory: str) -> int:
    """Remove temporary files."""
    temp_patterns = [
        '*.tmp',
        '*.temp',
        '*.bak',
        '*.log',
        '.DS_Store',
        'Thumbs.db',
        '*.swp',
        '*.swo'
    ]
    
    removed_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            for pattern in temp_patterns:
                if file.endswith(pattern.replace('*', '')) or file == pattern.replace('*', ''):
                    file_path = os.path.join(root, file)
                    try:
                        os.remove(file_path)
                        removed_count += 1
                        print(f"Removed temp file: {file}")
                    except OSError:
                        pass
    
    return removed_count


def _remove_empty_directories(directory: str) -> int:
    """Remove empty directories."""
    removed_count = 0
    
    for root, dirs, files in os.walk(directory, topdown=False):
        for dir_name in dirs:
            dir_path = os.path.join(root, dir_name)
            try:
                if not os.listdir(dir_path):  # Empty directory
                    os.rmdir(dir_path)
                    removed_count += 1
                    print(f"Removed empty directory: {dir_name}")
            except OSError:
                pass
    
    return removed_count


def _remove_cache_files(directory: str) -> int:
    """Remove browser cache and system cache files."""
    cache_patterns = [
        '.cache',
        '__pycache__',
        '*.pyc',
        '*.pyo',
        'node_modules'
    ]
    
    removed_count = 0
    
    for root, dirs, files in os.walk(directory):
        # Remove cache directories
        for dir_name in dirs[:]:  # Use slice to modify list during iteration
            if any(dir_name.endswith(pattern.replace('*', '')) for pattern in cache_patterns):
                dir_path = os.path.join(root, dir_name)
                try:
                    shutil.rmtree(dir_path)
                    dirs.remove(dir_name)  # Don't walk into removed directory
                    removed_count += 1
                    print(f"Removed cache directory: {dir_name}")
                except OSError:
                    pass
        
        # Remove cache files
        for file in files:
            if any(file.endswith(pattern.replace('*', '')) for pattern in cache_patterns):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    removed_count += 1
                    print(f"Removed cache file: {file}")
                except OSError:
                    pass
    
    return removed_count


def _remove_duplicate_files(directory: str) -> int:
    """Remove duplicate files based on content."""
    file_hashes = {}
    duplicates = []
    
    # Calculate file hashes
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'rb') as f:
                    content = f.read()
                    file_hash = hash(content)
                    
                    if file_hash in file_hashes:
                        duplicates.append(file_path)
                    else:
                        file_hashes[file_hash] = file_path
            except OSError:
                pass
    
    # Remove duplicates
    removed_count = 0
    for duplicate in duplicates:
        try:
            os.remove(duplicate)
            removed_count += 1
            print(f"Removed duplicate: {os.path.basename(duplicate)}")
        except OSError:
            pass
    
    return removed_count


def _minify_css_files(directory: str) -> int:
    """Minify CSS files (basic implementation)."""
    minified_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.css'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Basic minification
                    minified = _basic_css_minify(content)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(minified)
                    
                    minified_count += 1
                    print(f"Minified CSS: {file}")
                except OSError:
                    pass
    
    return minified_count


def _minify_js_files(directory: str) -> int:
    """Minify JavaScript files (basic implementation)."""
    minified_count = 0
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.js'):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Basic minification
                    minified = _basic_js_minify(content)
                    
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(minified)
                    
                    minified_count += 1
                    print(f"Minified JS: {file}")
                except OSError:
                    pass
    
    return minified_count


def _optimize_images(directory: str) -> int:
    """Optimize images (placeholder)."""
    print("Image optimization feature is not yet implemented.")
    print("Planned optimizations:")
    print("- JPEG compression")
    print("- PNG optimization")
    print("- WebP conversion")
    print("- SVG minification")
    return 0


def _compress_files(directory: str) -> int:
    """Compress files with gzip."""
    compressed_count = 0
    
    compressible_extensions = ['.html', '.css', '.js', '.txt', '.xml', '.json']
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if any(file.endswith(ext) for ext in compressible_extensions):
                try:
                    # Create compressed version
                    with open(file_path, 'rb') as f_in:
                        with gzip.open(f"{file_path}.gz", 'wb') as f_out:
                            shutil.copyfileobj(f_in, f_out)
                    
                    compressed_count += 1
                    print(f"Compressed: {file}")
                except OSError:
                    pass
    
    return compressed_count


def _copy_for_production(source: str, dest: str) -> int:
    """Copy files for production build."""
    copied_count = 0
    
    for root, dirs, files in os.walk(source):
        for file in files:
            if not file.endswith('.gz'):  # Skip compressed files
                source_file = os.path.join(root, file)
                rel_path = os.path.relpath(source_file, source)
                dest_file = os.path.join(dest, rel_path)
                
                # Create destination directory
                os.makedirs(os.path.dirname(dest_file), exist_ok=True)
                
                try:
                    shutil.copy2(source_file, dest_file)
                    copied_count += 1
                except OSError:
                    pass
    
    return copied_count


def _bundle_assets(directory: str) -> int:
    """Bundle CSS and JS assets."""
    print("Asset bundling feature is not yet implemented.")
    print("Planned bundling:")
    print("- Combine multiple CSS files")
    print("- Combine multiple JS files")
    print("- Generate asset manifest")
    return 0


def _generate_metadata(directory: str) -> int:
    """Generate metadata files for production."""
    metadata_files = ['sitemap.xml', 'robots.txt', '.htaccess']
    created_count = 0
    
    # Generate robots.txt
    robots_content = """User-agent: *
Disallow: /static/
Allow: /

Sitemap: https://example.com/sitemap.xml
"""
    
    try:
        with open(os.path.join(directory, 'robots.txt'), 'w') as f:
            f.write(robots_content)
        created_count += 1
        print("Generated robots.txt")
    except OSError:
        pass
    
    # Generate basic sitemap.xml
    sitemap_content = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://example.com/</loc>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
</urlset>
"""
    
    try:
        with open(os.path.join(directory, 'sitemap.xml'), 'w') as f:
            f.write(sitemap_content)
        created_count += 1
        print("Generated sitemap.xml")
    except OSError:
        pass
    
    return created_count


def _basic_css_minify(content: str) -> str:
    """Basic CSS minification."""
    import re
    
    # Remove comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Remove extra whitespace
    content = re.sub(r'\s+', ' ', content)
    
    # Remove spaces around specific characters
    content = re.sub(r'\s*([{}:;,>+~])\s*', r'\1', content)
    
    return content.strip()


def _basic_js_minify(content: str) -> str:
    """Basic JavaScript minification."""
    import re
    
    # Remove single-line comments
    content = re.sub(r'//.*$', '', content, flags=re.MULTILINE)
    
    # Remove multi-line comments
    content = re.sub(r'/\*.*?\*/', '', content, flags=re.DOTALL)
    
    # Remove extra whitespace
    content = re.sub(r'\s+', ' ', content)
    
    # Remove spaces around specific characters
    content = re.sub(r'\s*([{}();,=+\-*/<>!&|])\s*', r'\1', content)
    
    return content.strip()


def _display_cleanup_summary(operation: str, stats: Dict[str, int]) -> None:
    """Display cleanup operation summary."""
    print(f"\n{'='*50}")
    print(f"{operation.upper()} SUMMARY")
    print(f"{'='*50}")
    
    total_actions = sum(stats.values())
    
    for action, count in stats.items():
        action_name = action.replace('_', ' ').title()
        print(f"✅ {action_name}: {count}")
    
    print(f"\n📊 Total Actions: {total_actions}")
    
    if total_actions > 0:
        print(f"🎉 {operation} completed successfully!")
    else:
        print(f"ℹ️  No cleanup actions were needed.") 