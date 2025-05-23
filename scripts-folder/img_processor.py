#!/usr/bin/env python3
"""
Image Processor Module

Handles image processing and optimization for casino website images
in the Casino Website Generator.
"""

import os
import shutil
from typing import List, Dict, Tuple, Optional


def process_images():
    """
    Main function for image processing and optimization.
    
    Provides options for:
    - Resize images for web optimization
    - Compress and optimize file sizes
    - Convert between formats
    - Generate responsive image sets
    - Fix image issues
    """
    print("=== Image Processing System ===")
    print("1. Resize Images")
    print("2. Optimize File Sizes")
    print("3. Convert Formats")
    print("4. Generate Responsive Sets")
    print("5. Fix Image Issues")
    print("6. Batch Process All")
    
    while True:
        try:
            choice = int(input("\nYour choice (1-6): "))
            if 1 <= choice <= 6:
                break
            else:
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print("Please enter a valid number.")
    
    if choice == 1:
        resize_images()
    elif choice == 2:
        optimize_file_sizes()
    elif choice == 3:
        convert_formats()
    elif choice == 4:
        generate_responsive_sets()
    elif choice == 5:
        fix_image_issues()
    elif choice == 6:
        batch_process_all()


def resize_images():
    """
    Resize images to appropriate dimensions for web use.
    
    Standard casino website image sizes:
    - Hero banners: 1920x800
    - Header logos: 200x60
    - Game thumbnails: 300x200
    - Promotional banners: 800x400
    - Footer decorations: 100x50
    """
    print("Resizing images for web optimization...")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    images_dir = os.path.join(current_dir, "web-folder", "static", "images")
    
    if not os.path.exists(images_dir):
        print("Error: Images directory not found!")
        return
    
    # Standard sizes for different image types
    standard_sizes = get_standard_image_sizes()
    
    print("Standard image sizes:")
    for category, size in standard_sizes.items():
        print(f"  {category}: {size[0]}x{size[1]}")
    
    print("\nImage resizing feature is not yet implemented.")
    print("Planned functionality:")
    print("- Automatic size detection")
    print("- Batch resizing")
    print("- Aspect ratio preservation")
    print("- Quality optimization")


def optimize_file_sizes():
    """
    Optimize image file sizes without significant quality loss.
    
    Optimizations:
    - JPEG compression (85% quality)
    - PNG optimization
    - Remove metadata
    - Progressive JPEG encoding
    """
    print("Optimizing image file sizes...")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    images_dir = os.path.join(current_dir, "web-folder", "static", "images")
    
    optimization_stats = {
        'processed': 0,
        'size_saved': 0,
        'errors': 0
    }
    
    image_files = _get_image_files(images_dir)
    
    for image_file in image_files:
        try:
            original_size = os.path.getsize(image_file)
            
            # Placeholder for optimization
            optimized_size = _optimize_image_file(image_file)
            
            if optimized_size:
                size_saved = original_size - optimized_size
                optimization_stats['processed'] += 1
                optimization_stats['size_saved'] += size_saved
                print(f"Optimized: {os.path.basename(image_file)} (saved {size_saved} bytes)")
            else:
                optimization_stats['errors'] += 1
        except Exception as e:
            optimization_stats['errors'] += 1
            print(f"Error processing {os.path.basename(image_file)}: {str(e)}")
    
    _display_optimization_summary(optimization_stats)


def convert_formats():
    """
    Convert images between different formats.
    
    Conversions:
    - PNG to WebP (for modern browsers)
    - JPEG to WebP (for modern browsers)
    - Large PNG to JPEG (for photos)
    - SVG optimization
    """
    print("Converting image formats...")
    
    print("Available conversions:")
    print("1. PNG to WebP")
    print("2. JPEG to WebP")
    print("3. PNG to JPEG (photos)")
    print("4. Optimize SVG")
    
    while True:
        try:
            choice = int(input("\nConversion type (1-4): "))
            if 1 <= choice <= 4:
                break
            else:
                print("Please enter a number between 1 and 4.")
        except ValueError:
            print("Please enter a valid number.")
    
    conversion_types = {
        1: "PNG to WebP",
        2: "JPEG to WebP", 
        3: "PNG to JPEG",
        4: "SVG optimization"
    }
    
    print(f"Selected: {conversion_types[choice]}")
    print("Format conversion feature is not yet implemented.")
    print("Planned functionality:")
    print("- Batch conversion")
    print("- Quality preservation")
    print("- Fallback generation")
    print("- Browser compatibility")


def generate_responsive_sets():
    """
    Generate responsive image sets for different screen sizes.
    
    Generates:
    - Mobile versions (480px width)
    - Tablet versions (768px width)
    - Desktop versions (1200px width)
    - Retina versions (2x resolution)
    """
    print("Generating responsive image sets...")
    
    screen_sizes = {
        'mobile': 480,
        'tablet': 768,
        'desktop': 1200,
        'retina': 2400
    }
    
    print("Target screen sizes:")
    for size_name, width in screen_sizes.items():
        print(f"  {size_name}: {width}px width")
    
    print("\nResponsive image generation is not yet implemented.")
    print("Planned functionality:")
    print("- Multiple size generation")
    print("- Srcset HTML generation")
    print("- Picture element support")
    print("- Automatic optimization")


def fix_image_issues():
    """
    Fix common image issues in casino websites.
    
    Fixes:
    - Broken image links
    - Missing alt text
    - Incorrect dimensions
    - Poor quality images
    - Missing responsive attributes
    """
    print("Fixing image issues...")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_folder = os.path.join(current_dir, "web-folder")
    
    issues_found = {
        'broken_links': 0,
        'missing_alt': 0,
        'poor_quality': 0,
        'missing_responsive': 0
    }
    
    # Check HTML files for image issues
    html_files = _get_html_files(web_folder)
    
    for html_file in html_files:
        file_issues = _check_image_issues_in_html(html_file)
        for issue_type, count in file_issues.items():
            issues_found[issue_type] += count
    
    _display_image_issues_summary(issues_found)


def batch_process_all():
    """
    Perform all image processing operations in sequence.
    
    Operations:
    1. Fix image issues
    2. Resize to standard sizes
    3. Optimize file sizes
    4. Generate responsive sets
    5. Convert to modern formats
    """
    print("Starting batch processing of all images...")
    
    print("Step 1: Fixing image issues...")
    fix_image_issues()
    
    print("\nStep 2: Resizing images...")
    resize_images()
    
    print("\nStep 3: Optimizing file sizes...")
    optimize_file_sizes()
    
    print("\nStep 4: Generating responsive sets...")
    generate_responsive_sets()
    
    print("\nStep 5: Converting formats...")
    convert_formats()
    
    print("\n✅ Batch processing completed!")


def get_standard_image_sizes() -> Dict[str, Tuple[int, int]]:
    """
    Get standard image sizes for different casino website elements.
    
    Returns:
        dict: Category names mapped to (width, height) tuples
    """
    return {
        'hero_banner': (1920, 800),
        'header_logo': (200, 60),
        'game_thumbnail': (300, 200),
        'promo_banner': (800, 400),
        'footer_decoration': (100, 50),
        'favicon': (32, 32),
        'apple_touch_icon': (180, 180),
        'casino_card': (400, 300),
        'slot_machine': (300, 400),
        'roulette_table': (400, 300)
    }


def validate_image_quality(image_path: str) -> Dict[str, any]:
    """
    Validate image quality and return recommendations.
    
    Args:
        image_path (str): Path to image file
        
    Returns:
        dict: Quality assessment and recommendations
    """
    if not os.path.exists(image_path):
        return {'error': 'File not found'}
    
    file_size = os.path.getsize(image_path)
    file_ext = os.path.splitext(image_path)[1].lower()
    
    recommendations = []
    
    # Check file size
    if file_size > 1024 * 1024:  # 1MB
        recommendations.append("File size is large, consider compression")
    
    # Check format
    if file_ext in ['.bmp', '.tiff']:
        recommendations.append("Consider converting to JPEG or PNG")
    
    return {
        'file_size': file_size,
        'format': file_ext,
        'recommendations': recommendations
    }


def generate_srcset_html(base_image_path: str, sizes: List[int]) -> str:
    """
    Generate HTML srcset attribute for responsive images.
    
    Args:
        base_image_path (str): Base image path
        sizes (list): List of widths for responsive versions
        
    Returns:
        str: HTML srcset attribute value
    """
    base_name = os.path.splitext(base_image_path)[0]
    extension = os.path.splitext(base_image_path)[1]
    
    srcset_parts = []
    for size in sizes:
        responsive_path = f"{base_name}_{size}w{extension}"
        srcset_parts.append(f"{responsive_path} {size}w")
    
    return ", ".join(srcset_parts)


# Private helper functions

def _get_image_files(directory: str) -> List[str]:
    """Get all image files in directory and subdirectories."""
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg', '.bmp']
    image_files = []
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if any(file.lower().endswith(ext) for ext in image_extensions):
                image_files.append(os.path.join(root, file))
    
    return image_files


def _get_html_files(directory: str) -> List[str]:
    """Get all HTML files in directory and subdirectories."""
    html_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
    return html_files


def _optimize_image_file(image_path: str) -> Optional[int]:
    """
    Optimize a single image file (placeholder).
    
    Args:
        image_path (str): Path to image file
        
    Returns:
        int or None: New file size or None if failed
    """
    # Placeholder for image optimization
    # Would use PIL/Pillow or similar library
    print(f"Image optimization not yet implemented for: {os.path.basename(image_path)}")
    return None


def _check_image_issues_in_html(html_file: str) -> Dict[str, int]:
    """
    Check for image issues in an HTML file.
    
    Args:
        html_file (str): Path to HTML file
        
    Returns:
        dict: Count of different issue types found
    """
    issues = {
        'broken_links': 0,
        'missing_alt': 0,
        'poor_quality': 0,
        'missing_responsive': 0
    }
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        import re
        
        # Find all img tags
        img_pattern = r'<img[^>]*>'
        img_tags = re.findall(img_pattern, content, re.IGNORECASE)
        
        for img_tag in img_tags:
            # Check for missing alt attribute
            if 'alt=' not in img_tag.lower():
                issues['missing_alt'] += 1
            
            # Check for missing responsive attributes
            if 'srcset=' not in img_tag.lower() and 'sizes=' not in img_tag.lower():
                issues['missing_responsive'] += 1
            
            # Extract src attribute
            src_match = re.search(r'src\s*=\s*["\']([^"\']*)["\']', img_tag, re.IGNORECASE)
            if src_match:
                src = src_match.group(1)
                
                # Check if image file exists (relative to HTML file)
                if not src.startswith('http'):  # Local file
                    html_dir = os.path.dirname(html_file)
                    img_path = os.path.join(html_dir, src)
                    if not os.path.exists(img_path):
                        issues['broken_links'] += 1
    
    except Exception as e:
        print(f"Error checking {html_file}: {str(e)}")
    
    return issues


def _display_optimization_summary(stats: Dict[str, int]) -> None:
    """Display image optimization summary."""
    print(f"\n{'='*50}")
    print("IMAGE OPTIMIZATION SUMMARY")
    print(f"{'='*50}")
    print(f"✅ Images Processed: {stats['processed']}")
    print(f"💾 Total Size Saved: {stats['size_saved']} bytes")
    print(f"❌ Errors: {stats['errors']}")
    
    if stats['processed'] > 0:
        avg_savings = stats['size_saved'] / stats['processed']
        print(f"📊 Average Savings: {avg_savings:.2f} bytes per image")


def _display_image_issues_summary(issues: Dict[str, int]) -> None:
    """Display image issues summary."""
    print(f"\n{'='*50}")
    print("IMAGE ISSUES SUMMARY")
    print(f"{'='*50}")
    
    total_issues = sum(issues.values())
    
    for issue_type, count in issues.items():
        issue_name = issue_type.replace('_', ' ').title()
        status = "❌" if count > 0 else "✅"
        print(f"{status} {issue_name}: {count}")
    
    print(f"\n📊 Total Issues Found: {total_issues}")
    
    if total_issues == 0:
        print("🎉 No image issues found!")
    else:
        print("⚠️  Please review and fix the issues above.")


def create_casino_image_manifest() -> Dict[str, any]:
    """
    Create a manifest of required casino website images.
    
    Returns:
        dict: Manifest of required images by category
    """
    return {
        "header": {
            "logo": {
                "required": True,
                "formats": ["png", "svg"],
                "size": "200x60",
                "description": "Main casino logo"
            },
            "background": {
                "required": False,
                "formats": ["jpg", "webp"],
                "size": "1920x400",
                "description": "Header background pattern"
            }
        },
        "hero": {
            "main_banner": {
                "required": True,
                "formats": ["jpg", "webp"],
                "size": "1920x800",
                "description": "Main hero banner"
            },
            "jackpot_banner": {
                "required": False,
                "formats": ["jpg", "webp"],
                "size": "800x400",
                "description": "Jackpot promotion banner"
            }
        },
        "games": {
            "poker_thumbnail": {
                "required": True,
                "formats": ["jpg", "webp"],
                "size": "300x200",
                "description": "Poker game thumbnail"
            },
            "roulette_thumbnail": {
                "required": True,
                "formats": ["jpg", "webp"],
                "size": "300x200",
                "description": "Roulette game thumbnail"
            },
            "slots_thumbnail": {
                "required": True,
                "formats": ["jpg", "webp"],
                "size": "300x200",
                "description": "Slot machine thumbnail"
            }
        },
        "icons": {
            "favicon": {
                "required": True,
                "formats": ["ico"],
                "size": "32x32",
                "description": "Browser favicon"
            },
            "apple_touch_icon": {
                "required": True,
                "formats": ["png"],
                "size": "180x180",
                "description": "Apple touch icon"
            }
        }
    } 