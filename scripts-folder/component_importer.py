#!/usr/bin/env python3
"""
Enhanced Component Importer Module

A robust, error-proof component system for the Casino Website Generator.
Features:
- JSON-based component configuration
- Modular file structure
- Advanced theming system
- Better error handling
- Responsive design utilities
- **NEW: Mix-and-Match Random Combinations**
"""

import os
import json
import random
import shutil
import colorsys
import re
from typing import Dict, List, Optional, Tuple, Any
from pathlib import Path


class ColorUtils:
    """Utility class for color manipulation and theme generation."""
    
    @staticmethod
    def hex_to_rgb(hex_color: str) -> Tuple[int, int, int]:
        """Convert hex color to RGB tuple."""
        hex_color = hex_color.lstrip('#')
        if len(hex_color) == 3:
            hex_color = ''.join([c*2 for c in hex_color])
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    @staticmethod
    def rgb_to_hex(r: int, g: int, b: int) -> str:
        """Convert RGB to hex color."""
        return f"#{r:02x}{g:02x}{b:02x}"
    
    @staticmethod
    def rgb_to_hsl(r: int, g: int, b: int) -> Tuple[float, float, float]:
        """Convert RGB to HSL."""
        r, g, b = r/255.0, g/255.0, b/255.0
        return colorsys.rgb_to_hls(r, g, b)
    
    @staticmethod
    def hsl_to_rgb(h: float, s: float, l: float) -> Tuple[int, int, int]:
        """Convert HSL to RGB."""
        r, g, b = colorsys.hls_to_rgb(h, l, s)
        return int(r*255), int(g*255), int(b*255)
    
    @staticmethod
    def adjust_lightness(hex_color: str, factor: float) -> str:
        """Adjust the lightness of a color. Factor > 1 lightens, < 1 darkens."""
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = ColorUtils.rgb_to_hsl(r, g, b)
        l = max(0, min(1, l * factor))
        r, g, b = ColorUtils.hsl_to_rgb(h, s, l)
        return ColorUtils.rgb_to_hex(r, g, b)
    
    @staticmethod
    def adjust_saturation(hex_color: str, factor: float) -> str:
        """Adjust the saturation of a color."""
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = ColorUtils.rgb_to_hsl(r, g, b)
        s = max(0, min(1, s * factor))
        r, g, b = ColorUtils.hsl_to_rgb(h, s, l)
        return ColorUtils.rgb_to_hex(r, g, b)
    
    @staticmethod
    def get_complementary(hex_color: str) -> str:
        """Get complementary color."""
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = ColorUtils.rgb_to_hsl(r, g, b)
        h = (h + 0.5) % 1.0
        r, g, b = ColorUtils.hsl_to_rgb(h, s, l)
        return ColorUtils.rgb_to_hex(r, g, b)
    
    @staticmethod
    def get_triadic(hex_color: str) -> List[str]:
        """Get triadic colors."""
        r, g, b = ColorUtils.hex_to_rgb(hex_color)
        h, l, s = ColorUtils.rgb_to_hsl(r, g, b)
        
        colors = []
        for offset in [1/3, 2/3]:
            new_h = (h + offset) % 1.0
            r2, g2, b2 = ColorUtils.hsl_to_rgb(new_h, s, l)
            colors.append(ColorUtils.rgb_to_hex(r2, g2, b2))
        return colors
    
    @staticmethod
    def ensure_contrast(text_color: str, bg_color: str, min_ratio: float = 4.5) -> str:
        """Ensure text color has sufficient contrast against background."""
        def get_luminance(hex_color: str) -> float:
            r, g, b = ColorUtils.hex_to_rgb(hex_color)
            r, g, b = [c/255.0 for c in (r, g, b)]
            r = r/12.92 if r <= 0.03928 else ((r + 0.055)/1.055) ** 2.4
            g = g/12.92 if g <= 0.03928 else ((g + 0.055)/1.055) ** 2.4
            b = b/12.92 if b <= 0.03928 else ((b + 0.055)/1.055) ** 2.4
            return 0.2126 * r + 0.7152 * g + 0.0722 * b
        
        def contrast_ratio(color1: str, color2: str) -> float:
            lum1 = get_luminance(color1)
            lum2 = get_luminance(color2)
            lighter = max(lum1, lum2)
            darker = min(lum1, lum2)
            return (lighter + 0.05) / (darker + 0.05)
        
        current_ratio = contrast_ratio(text_color, bg_color)
        if current_ratio >= min_ratio:
            return text_color
        
        # If contrast is insufficient, use white or black
        white_ratio = contrast_ratio("#ffffff", bg_color)
        black_ratio = contrast_ratio("#000000", bg_color)
        
        return "#ffffff" if white_ratio > black_ratio else "#000000"


class ComponentImporter:
    """Enhanced component importer with JSON-based configuration and mix-and-match features."""
    
    def __init__(self):
        self.current_dir = Path(__file__).parent.parent
        self.components_dir = self.current_dir / "web-components-v2"
        self.web_folder = self.current_dir / "web-folder"
        self.themes_dir = self.current_dir / "themes"
        self.custom_theme = None  # Will store generated theme
        
        # Component processing order
        self.component_order = [
            "header", "hero", "offers", "details_comparison", 
            "why_us", "about", "history", "guide", "faqs", "footer"
        ]
        
        # Theme compatibility matrix for smart mixing
        self.theme_compatibility = {
            "modern": ["modern", "minimal", "luxury"],
            "luxury": ["luxury", "vintage", "modern"], 
            "neon": ["neon", "modern", "minimal"],
            "minimal": ["minimal", "modern", "neon"],
            "vintage": ["vintage", "luxury", "minimal"]
        }
        
        # Default theme configuration
        self.default_theme = {
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

    def get_theme_preferences(self) -> Tuple[str, str]:
        """Get user's theme preferences for primary color and light/dark mode."""
        print("\n🎨 Custom Theme Generation")
        print("=" * 40)
        
        # Get primary color
        while True:
            primary_color = input("Enter primary color (hex, e.g., #ff6b35 or #d4af37): ").strip()
            
            # Validate hex color format
            if re.match(r'^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$', primary_color):
                break
            else:
                print("❌ Invalid hex color format. Please use #RRGGBB or #RGB format.")
        
        # Get theme mode
        print("\n🌙 Theme Mode:")
        print("  1. Light Theme - Bright backgrounds, dark text")
        print("  2. Dark Theme - Dark backgrounds, light text")
        
        while True:
            mode_choice = input("Select theme mode (1-2, default=2): ").strip()
            if mode_choice in ['1', '2', '']:
                break
            else:
                print("❌ Please enter 1 or 2")
        
        theme_mode = "light" if mode_choice == "1" else "dark"
        
        print(f"\n✅ Theme Configuration:")
        print(f"   Primary Color: {primary_color}")
        print(f"   Theme Mode: {theme_mode.title()}")
        
        return primary_color, theme_mode

    def generate_custom_theme(self, primary_color: str, theme_mode: str) -> Dict[str, Any]:
        """Generate a complete theme from primary color and mode preference."""
        
        # Generate color palette
        triadic = ColorUtils.get_triadic(primary_color)
        complementary = ColorUtils.get_complementary(primary_color)
        
        # Select secondary and accent colors
        secondary_color = triadic[0] if triadic else ColorUtils.adjust_saturation(primary_color, 0.7)
        accent_color = triadic[1] if len(triadic) > 1 else complementary
        
        # Generate theme colors based on mode
        if theme_mode == "light":
            background = "#ffffff"
            surface = "#f8f9fa"
            surface_elevated = "#ffffff"
            text_primary = "#1a1a1a"
            text_secondary = "#6c757d"
            border_color = "#dee2e6"
            
            # Adjust primary colors for light theme
            primary_adjusted = ColorUtils.adjust_lightness(primary_color, 0.8)
            secondary_adjusted = ColorUtils.adjust_lightness(secondary_color, 0.9)
            accent_adjusted = ColorUtils.adjust_lightness(accent_color, 0.8)
            
        else:  # dark theme
            background = "#0a0a0a"
            surface = "#1a1a1a"
            surface_elevated = "#2d2d2d"
            text_primary = "#ffffff"
            text_secondary = "#a0a0a0"
            border_color = "#333333"
            
            # Adjust primary colors for dark theme
            primary_adjusted = ColorUtils.adjust_lightness(primary_color, 1.2)
            secondary_adjusted = ColorUtils.adjust_lightness(secondary_color, 1.1)
            accent_adjusted = ColorUtils.adjust_lightness(accent_color, 1.1)
        
        # Ensure text contrast
        text_primary = ColorUtils.ensure_contrast(text_primary, background)
        text_secondary = ColorUtils.ensure_contrast(text_secondary, background)
        
        # Generate status colors
        success_color = "#28a745" if theme_mode == "light" else "#4caf50"
        warning_color = "#ffc107" if theme_mode == "light" else "#ff9800"
        error_color = "#dc3545" if theme_mode == "light" else "#f44336"
        
        theme = {
            "name": f"custom-{theme_mode}",
            "description": f"Custom {theme_mode} theme with {primary_color} primary color",
            "mode": theme_mode,
            "colors": {
                "primary": primary_adjusted,
                "primary-rgb": f"{ColorUtils.hex_to_rgb(primary_adjusted)[0]}, {ColorUtils.hex_to_rgb(primary_adjusted)[1]}, {ColorUtils.hex_to_rgb(primary_adjusted)[2]}",
                "secondary": secondary_adjusted,
                "accent": accent_adjusted,
                "background": background,
                "surface": surface,
                "surface-elevated": surface_elevated,
                "text": text_primary,
                "text-secondary": text_secondary,
                "border": border_color,
                "success": success_color,
                "warning": warning_color,
                "error": error_color,
                
                # Casino-specific colors
                "gold": ColorUtils.adjust_lightness("#ffd700", 1.1 if theme_mode == "dark" else 0.9),
                "silver": ColorUtils.adjust_lightness("#c0c0c0", 1.1 if theme_mode == "dark" else 0.8),
                "bronze": ColorUtils.adjust_lightness("#cd7f32", 1.1 if theme_mode == "dark" else 0.8),
                
                # Interactive states
                "hover": ColorUtils.adjust_lightness(primary_adjusted, 1.1),
                "active": ColorUtils.adjust_lightness(primary_adjusted, 0.9),
                "focus": ColorUtils.adjust_saturation(primary_adjusted, 1.2),
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
            },
            "shadows": {
                "small": "0 1px 3px rgba(0, 0, 0, 0.12), 0 1px 2px rgba(0, 0, 0, 0.24)" if theme_mode == "light" else "0 1px 3px rgba(0, 0, 0, 0.5), 0 1px 2px rgba(0, 0, 0, 0.3)",
                "medium": "0 3px 6px rgba(0, 0, 0, 0.16), 0 3px 6px rgba(0, 0, 0, 0.23)" if theme_mode == "light" else "0 3px 6px rgba(0, 0, 0, 0.6), 0 3px 6px rgba(0, 0, 0, 0.4)",
                "large": "0 10px 20px rgba(0, 0, 0, 0.19), 0 6px 6px rgba(0, 0, 0, 0.23)" if theme_mode == "light" else "0 10px 20px rgba(0, 0, 0, 0.7), 0 6px 6px rgba(0, 0, 0, 0.5)"
            }
        }
        
        return theme

    def validate_component_structure(self) -> bool:
        """Validate that component structure is ready for import."""
        if not self.components_dir.exists():
            print("❌ Component directory not found")
            return False
        
        available_components = self.get_available_components()
        if not available_components:
            print("❌ No components found")
            return False
        
        valid_components = 0
        for comp_name in available_components:
            config = self.load_component_config(comp_name)
            variants = config.get('variants', [])
            
            valid_variants = 0
            for variant in variants:
                variant_name = variant['name']
                comp_dir = self.components_dir / comp_name
                html_file = comp_dir / f"{variant_name}.html"
                
                if html_file.exists():
                    valid_variants += 1
            
            if valid_variants > 0:
                valid_components += 1
                print(f"✅ {comp_name}: {valid_variants} valid variant(s)")
            else:
                print(f"⚠️  {comp_name}: No valid variants found")
        
        if valid_components == 0:
            print("❌ No valid components found")
            return False
        
        print(f"\n✅ Validation complete: {valid_components}/{len(available_components)} components ready")
        return True

    def setup_directories(self) -> bool:
        """Setup and validate required directories."""
        try:
            self.web_folder.mkdir(exist_ok=True)
            (self.web_folder / "css").mkdir(exist_ok=True)
            (self.web_folder / "js").mkdir(exist_ok=True)
            (self.web_folder / "assets").mkdir(exist_ok=True)
            return True
        except Exception as e:
            print(f"❌ Error setting up directories: {e}")
            return False

    def get_available_components(self) -> List[str]:
        """Get list of available components with JSON configs."""
        if not self.components_dir.exists():
            return []
        
        components = []
        for component_dir in self.components_dir.iterdir():
            if component_dir.is_dir() and not component_dir.name.startswith('.'):
                config_file = component_dir / "component.json"
                if config_file.exists():
                    components.append(component_dir.name)
        
        return components

    def load_component_config(self, component_name: str) -> Dict[str, Any]:
        """Load component configuration from JSON."""
        config_file = self.components_dir / component_name / "component.json"
        if config_file.exists():
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"⚠️  Error loading config for {component_name}: {e}")
        return {"description": "Component information unavailable", "variants": []}

    def get_user_selection(self, available_components: List[str]) -> Tuple[List[str], str]:
        """Get user's component selection and mixing mode."""
        print(f"\n📦 Available Components ({len(available_components)}):")
        
        # Sort by processing order
        sorted_components = []
        for comp in self.component_order:
            if comp in available_components:
                sorted_components.append(comp)
        
        # Add any components not in the order
        for comp in available_components:
            if comp not in sorted_components:
                sorted_components.append(comp)
        
        for i, comp in enumerate(sorted_components, 1):
            config = self.load_component_config(comp)
            print(f"  {i:2}. {comp:<20} - {config.get('description', 'No description')}")
        
        print("\n💡 Selection Options:")
        print("  • Enter numbers separated by commas (e.g., 1,2,5)")
        print("  • Type 'all' for all components")
        print("  • Type 'essential' for header, hero, footer")
        
        selection = input("\nYour selection: ").strip().lower()
        
        if selection == 'all':
            selected_components = sorted_components
        elif selection == 'essential':
            selected_components = [c for c in ['header', 'hero', 'footer'] if c in sorted_components]
        else:
            try:
                indices = [int(x.strip()) for x in selection.split(',')]
                selected_components = [sorted_components[i-1] for i in indices if 1 <= i <= len(sorted_components)]
            except (ValueError, IndexError):
                print("❌ Invalid selection format")
                return [], "single"
        
        # Get mixing mode
        print("\n🎲 Mix-and-Match Options:")
        print("  1. Single Random - One random variant per component (default)")
        print("  2. Smart Mix - Thematically compatible random variants") 
        print("  3. Wild Mix - Completely random mixing")
        
        mode_choice = input("\nSelect mixing mode (1-3, default=1): ").strip()
        mode_map = {
            "1": "single",
            "2": "smart", 
            "3": "wild",
            "": "single"
        }
        
        mixing_mode = mode_map.get(mode_choice, "single")
        return selected_components, mixing_mode

    def generate_random_combinations(self, components: List[str], count: int = 5) -> List[Dict[str, str]]:
        """Generate multiple random component combinations with validation."""
        combinations = []
        
        for i in range(count):
            combination = {}
            for comp_name in components:
                config = self.load_component_config(comp_name)
                variants = config.get('variants', [])
                if variants:
                    # Validate that variant files actually exist
                    valid_variants = []
                    for variant in variants:
                        variant_name = variant['name']
                        comp_dir = self.components_dir / comp_name
                        html_file = comp_dir / f"{variant_name}.html"
                        if html_file.exists():
                            valid_variants.append(variant)
                    
                    if valid_variants:
                        selected_variant = random.choice(valid_variants)
                        combination[comp_name] = selected_variant['name']
                    else:
                        print(f"⚠️  No valid variants found for {comp_name}")
            
            if combination:  # Only add if we have components
                combinations.append(combination)
        
        return combinations

    def generate_smart_combinations(self, components: List[str]) -> Dict[str, str]:
        """Generate thematically compatible random combinations with validation."""
        # Start with a random base theme
        base_themes = list(self.theme_compatibility.keys())
        base_theme = random.choice(base_themes)
        compatible_themes = self.theme_compatibility[base_theme]
        
        combination = {}
        for comp_name in components:
            config = self.load_component_config(comp_name)
            variants = config.get('variants', [])
            
            # Filter variants by theme compatibility and file existence
            compatible_variants = []
            for variant in variants:
                variant_theme = variant.get('theme', 'modern')
                variant_name = variant['name']
                comp_dir = self.components_dir / comp_name
                html_file = comp_dir / f"{variant_name}.html"
                
                if variant_theme in compatible_themes and html_file.exists():
                    compatible_variants.append(variant)
            
            # Fallback to any valid variant if no compatible ones found
            if not compatible_variants:
                for variant in variants:
                    variant_name = variant['name']
                    comp_dir = self.components_dir / comp_name
                    html_file = comp_dir / f"{variant_name}.html"
                    if html_file.exists():
                        compatible_variants.append(variant)
            
            if compatible_variants:
                selected_variant = random.choice(compatible_variants)
                combination[comp_name] = selected_variant['name']
            else:
                print(f"⚠️  No valid variants found for {comp_name}")
        
        return combination

    def create_enhanced_structure(self):
        """Create the enhanced component structure."""
        print("\n=== Creating Enhanced Component Structure ===")
        
        # Create directories
        self.components_dir.mkdir(exist_ok=True)
        self.themes_dir.mkdir(exist_ok=True)
        
        # Create themes
        self._create_themes()
        
        # Create sample components
        self._create_sample_components()
        
        print("\n✅ Enhanced structure created successfully!")
        print(f"📁 Components: {self.components_dir}")
        print(f"🎨 Themes: {self.themes_dir}")

    def _create_themes(self):
        """Create theme files."""
        themes = [
            self.default_theme,
            {
                "name": "casino-luxury",
                "description": "Luxury gold and black theme",
                "colors": {
                    "primary": "#ffd700",
                    "secondary": "#000000",
                    "accent": "#ff0000",
                    "background": "#1a1a1a",
                    "surface": "#2a2a2a",
                    "text": "#ffffff",
                    "text-secondary": "#cccccc"
                },
                "typography": {
                    "font-primary": "Playfair Display, serif",
                    "font-display": "Cinzel, serif"
                }
            },
            {
                "name": "casino-neon", 
                "description": "Vibrant neon gaming theme",
                "colors": {
                    "primary": "#00ffff",
                    "secondary": "#ff00ff",
                    "accent": "#ffff00",
                    "background": "#0a0a0a",
                    "surface": "#1a1a2e",
                    "text": "#ffffff",
                    "text-secondary": "#a0a0a0"
                },
                "typography": {
                    "font-primary": "Orbitron, monospace",
                    "font-display": "Exo 2, sans-serif"
                }
            }
        ]
        
        for theme in themes:
            theme_file = self.themes_dir / f"{theme['name']}.json"
            with open(theme_file, 'w', encoding='utf-8') as f:
                json.dump(theme, f, indent=2)
        
        print(f"🎨 Created {len(themes)} themes")

    def _create_sample_components(self):
        """Create sample component directory structure and configurations."""
        components = [
            {
                "name": "header",
                "description": "Professional casino header with navigation",
                "category": "navigation",
                "version": "1.0.0",
                "variants": [
                    {"name": "modern", "description": "Modern gradient header with smooth animations", "html": "modern.html", "css": "modern.css", "js": "modern.js"},
                    {"name": "luxury", "description": "Luxury gold header with premium styling", "html": "luxury.html", "css": "luxury.css", "js": "luxury.js"},
                    {"name": "neon", "description": "Vibrant neon gaming header with glow effects", "html": "neon.html", "css": "neon.css", "js": "neon.js"},
                    {"name": "minimal", "description": "Clean minimalist header with subtle elegance", "html": "minimal.html", "css": "minimal.css", "js": "minimal.js"},
                    {"name": "vintage", "description": "Classic vintage casino header with retro charm", "html": "vintage.html", "css": "vintage.css", "js": "vintage.js"}
                ],
                "dependencies": [],
                "casino_compliance": {
                    "age_verification": True,
                    "responsible_gambling": True,
                    "legal_notices": True
                }
            },
            {
                "name": "hero",
                "description": "Engaging hero section",
                "category": "content",
                "version": "1.0.0",
                "variants": [
                    {"name": "jackpot", "description": "High-energy jackpot showcase with animated counters", "html": "jackpot.html", "css": "jackpot.css", "js": "jackpot.js"},
                    {"name": "welcome", "description": "Welcoming hero with bonus offers and registration CTA", "html": "welcome.html", "css": "welcome.css", "js": "welcome.js"},
                    {"name": "vip", "description": "Exclusive VIP membership hero with luxury styling", "html": "vip.html", "css": "vip.css", "js": "vip.js"},
                    {"name": "tournament", "description": "Dynamic tournament hero with live leaderboards", "html": "tournament.html", "css": "tournament.css", "js": "tournament.js"},
                    {"name": "live", "description": "Live casino hero with real-time dealer streams", "html": "live.html", "css": "live.css", "js": "live.js"}
                ],
                "dependencies": [],
                "casino_compliance": {
                    "age_verification": True,
                    "responsible_gambling": True,
                    "legal_notices": True
                }
            },
            {
                "name": "footer",
                "description": "Professional footer with legal compliance",
                "category": "navigation",
                "version": "1.0.0",
                "variants": [
                    {"name": "comprehensive", "description": "Full footer with all sections and social links", "html": "comprehensive.html", "css": "comprehensive.css", "js": "comprehensive.js"},
                    {"name": "minimal", "description": "Clean minimal footer with essential links only", "html": "minimal.html", "css": "minimal.css", "js": "minimal.js"},
                    {"name": "premium", "description": "Premium footer with VIP support and awards", "html": "premium.html", "css": "premium.css", "js": "premium.js"},
                    {"name": "gaming", "description": "Gaming-focused footer with game categories", "html": "gaming.html", "css": "gaming.css", "js": "gaming.js"},
                    {"name": "corporate", "description": "Corporate footer with company information", "html": "corporate.html", "css": "corporate.css", "js": "corporate.js"}
                ],
                "dependencies": [],
                "casino_compliance": {
                    "age_verification": True,
                    "responsible_gambling": True,
                    "legal_notices": True
                }
            }
        ]
        
        for comp_config in components:
            self._create_component_structure(comp_config)
        
        print(f"📦 Created {len(components)} component directories with {sum(len(c['variants']) for c in components)} total variant slots")
        print("💡 Note: You'll need to create the actual HTML/CSS/JS files for each variant")

    def _create_component_structure(self, config: Dict[str, Any]):
        """Create component directory and configuration file."""
        comp_dir = self.components_dir / config["name"]
        comp_dir.mkdir(exist_ok=True)
        
        # Create component.json
        with open(comp_dir / "component.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2)


def import_components():
    """
    Enhanced component import system with mix-and-match functionality.
    """
    print("=== Enhanced Component Import System with Mix-and-Match ===")
    
    importer = ComponentImporter()
    
    # Check if enhanced structure exists
    if not importer.components_dir.exists():
        print("❌ Enhanced component structure not found.")
        setup_choice = input("Would you like to set up the enhanced structure? (y/n): ").strip().lower()
        if setup_choice == 'y':
            importer.create_enhanced_structure()
        else:
            print("Setup cancelled.")
            return
    
    # Setup directories
    if not importer.setup_directories():
        return
    
    # Validate component structure
    print("\n🔍 Validating component structure...")
    if not importer.validate_component_structure():
        print("❌ Component validation failed. Please check your component files.")
        return
    
    # Get available components
    available_components = importer.get_available_components()
    if not available_components:
        print("❌ No components found in enhanced structure.")
        return

    # Get user selection and mixing mode
    selected_components, mixing_mode = importer.get_user_selection(available_components)
    if not selected_components:
        print("❌ No components selected.")
        return
    
    # Generate custom theme
    print(f"\n🎨 Theme Generation for {len(selected_components)} components...")
    primary_color, theme_mode = importer.get_theme_preferences()
    custom_theme = importer.generate_custom_theme(primary_color, theme_mode)
    importer.custom_theme = custom_theme
    
    print(f"✅ Generated {theme_mode} theme with {primary_color} primary color")

    print(f"\n🔧 Processing {len(selected_components)} components with {mixing_mode} mixing mode...")
    
    # Generate combinations based on mode
    selected_combination = {}
    
    if mixing_mode == "single":
        # Traditional single random selection
        for comp_name in selected_components:
            config = importer.load_component_config(comp_name)
            variants = config.get('variants', [])
            if variants:
                selected_variant = random.choice(variants)
                selected_combination[comp_name] = selected_variant['name']
    
    elif mixing_mode == "smart":
        selected_combination = importer.generate_smart_combinations(selected_components)
    
    elif mixing_mode == "wild":
        combinations = importer.generate_random_combinations(selected_components, 1)
        selected_combination = combinations[0] if combinations else {}
    
    if not selected_combination:
        print("❌ No valid combination generated.")
        return
    
    # Validate all selected components have valid variants
    validated_combination = {}
    for comp_name, variant_name in selected_combination.items():
        comp_dir = importer.components_dir / comp_name
        html_file = comp_dir / f"{variant_name}.html"
        
        if html_file.exists():
            validated_combination[comp_name] = variant_name
        else:
            print(f"⚠️  Skipping {comp_name} ({variant_name}) - files not found")
            # Try to find any valid variant for this component
            config = importer.load_component_config(comp_name)
            variants = config.get('variants', [])
            for variant in variants:
                test_html = comp_dir / f"{variant['name']}.html"
                if test_html.exists():
                    validated_combination[comp_name] = variant['name']
                    print(f"✅ Using fallback: {comp_name} ({variant['name']})")
                    break
    
    if not validated_combination:
        print("❌ No valid components found after validation.")
        return

    # Display selected combination
    print(f"\n🎨 Final Validated Combination:")
    print("=" * 50)
    for comp, variant in validated_combination.items():
        config = importer.load_component_config(comp)
        variant_info = next((v for v in config.get('variants', []) if v['name'] == variant), {})
        description = variant_info.get('description', 'No description')
        print(f"  {comp:<15} → {variant:<12} ({description})")
    print("=" * 50)
    
    # Generate base website
    _generate_base_website(importer)
    
    # Import components in proper order (header first, footer last)
    success_count = 0
    failed_components = []
    
    # Process in specific order for proper HTML structure
    ordered_components = []
    
    # Header first
    if 'header' in validated_combination:
        ordered_components.append(('header', validated_combination['header']))
    
    # Then all other components except footer
    for comp_name, variant_name in validated_combination.items():
        if comp_name not in ['header', 'footer']:
            ordered_components.append((comp_name, variant_name))
    
    # Footer last
    if 'footer' in validated_combination:
        ordered_components.append(('footer', validated_combination['footer']))
    
    print(f"\n🔧 Processing {len(ordered_components)} components in order...")
    
    for comp_name, variant_name in ordered_components:
        success = _import_selected_component(importer, comp_name, variant_name)
        if success:
            print(f"  ✅ {comp_name} ({variant_name})")
            success_count += 1
        else:
            print(f"  ❌ {comp_name} ({variant_name}) - failed")
            failed_components.append(f"{comp_name} ({variant_name})")

    # Summary
    print(f"\n🎉 Enhanced mix-and-match component import completed!")
    print(f"✅ Successfully imported: {success_count}/{len(ordered_components)} components")
    if failed_components:
        print(f"❌ Failed components: {', '.join(failed_components)}")
    print(f"📁 Website generated in: {importer.web_folder}")


def _import_selected_component(importer: ComponentImporter, comp_name: str, variant_name: str) -> bool:
    """Import a specific component variant with comprehensive validation."""
    try:
        config = importer.load_component_config(comp_name)
        variant_info = next((v for v in config.get('variants', []) if v['name'] == variant_name), None)
        
        if not variant_info:
            print(f"⚠️  Variant {variant_name} not found for {comp_name}")
            return False
        
        comp_dir = importer.components_dir / comp_name
        imported_files = 0
        
        # Process HTML (required)
        html_file = comp_dir / f"{variant_name}.html"
        if html_file.exists():
            try:
                with open(html_file, 'r', encoding='utf-8') as f:
                    html_content = f.read()
                _insert_component_html(importer, html_content, comp_name)
                imported_files += 1
            except Exception as e:
                print(f"⚠️  Error processing HTML for {comp_name}: {e}")
                return False
        else:
            print(f"❌ Required HTML file not found: {html_file}")
            return False
        
        # Process CSS (optional but recommended)
        css_file = comp_dir / f"{variant_name}.css"
        if css_file.exists():
            try:
                with open(css_file, 'r', encoding='utf-8') as f:
                    css_content = f.read()
                _append_component_css(importer, css_content)
                imported_files += 1
            except Exception as e:
                print(f"⚠️  Error processing CSS for {comp_name}: {e}")
        
        # Process JS (optional)
        js_file = comp_dir / f"{variant_name}.js"
        if js_file.exists():
            try:
                with open(js_file, 'r', encoding='utf-8') as f:
                    js_content = f.read()
                _append_component_js(importer, js_content)
                imported_files += 1
            except Exception as e:
                print(f"⚠️  Error processing JS for {comp_name}: {e}")
        
        if imported_files == 0:
            print(f"❌ No files imported for {comp_name} ({variant_name})")
            return False
            
        return True
        
    except Exception as e:
        print(f"❌ Error importing {comp_name} ({variant_name}): {e}")
        return False


def _generate_base_website(importer: ComponentImporter):
    """Generate base website structure with custom theme."""
    # Create base HTML
    html_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Professional Casino Website</title>
    <meta name="description" content="Experience the best online casino games">
    <link rel="stylesheet" href="css/styles.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@400;500;600;700;800&display=swap" rel="stylesheet">
</head>
<body>
    <!-- Components will be inserted here -->
    
    <!-- Legal Notice -->
    <div class="legal-notice">
        18+ Only. Please gamble responsibly. BeGambleAware.org
    </div>
    
    <script src="js/main.js"></script>
</body>
</html>'''
    
    with open(importer.web_folder / "index.html", 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    # Generate CSS with custom theme or fallback to default
    if importer.custom_theme:
        theme = importer.custom_theme
        css_content = f'''/* Enhanced Casino Website - Custom {theme["mode"].title()} Theme */

:root {{
    /* Primary Colors */
    --color-primary: {theme["colors"]["primary"]};
    --color-primary-rgb: {theme["colors"]["primary-rgb"]};
    --color-secondary: {theme["colors"]["secondary"]};
    --color-accent: {theme["colors"]["accent"]};
    
    /* Background Colors */
    --color-background: {theme["colors"]["background"]};
    --color-surface: {theme["colors"]["surface"]};
    --color-surface-elevated: {theme["colors"]["surface-elevated"]};
    
    /* Text Colors */
    --color-text: {theme["colors"]["text"]};
    --color-text-secondary: {theme["colors"]["text-secondary"]};
    
    /* Border & Interactive */
    --color-border: {theme["colors"]["border"]};
    --color-hover: {theme["colors"]["hover"]};
    --color-active: {theme["colors"]["active"]};
    --color-focus: {theme["colors"]["focus"]};
    
    /* Status Colors */
    --color-success: {theme["colors"]["success"]};
    --color-warning: {theme["colors"]["warning"]};
    --color-error: {theme["colors"]["error"]};
    
    /* Casino Colors */
    --color-gold: {theme["colors"]["gold"]};
    --color-silver: {theme["colors"]["silver"]};
    --color-bronze: {theme["colors"]["bronze"]};
    
    /* Typography */
    --font-primary: {theme["typography"]["font-primary"]};
    --font-display: {theme["typography"]["font-display"]};
    
    /* Spacing & Layout */
    --spacing-base: {theme["spacing"]["base"]};
    --border-radius: {theme["borders"]["radius"]};
    --border-width: {theme["borders"]["width"]};
    
    /* Shadows */
    --shadow-small: {theme["shadows"]["small"]};
    --shadow-medium: {theme["shadows"]["medium"]};
    --shadow-large: {theme["shadows"]["large"]};
    
    /* Transitions */
    --transition: all 0.3s ease;
    --transition-fast: all 0.15s ease;
    --transition-slow: all 0.5s ease;
}}'''
    else:
        # Fallback to default theme
        css_content = '''/* Enhanced Casino Website - Base Styles */

:root {
    --color-primary: #d4af37;
    --color-secondary: #1a1a1a;
    --color-accent: #ff6b35;
    --color-background: #0f0f0f;
    --color-surface: #1e1e1e;
    --color-text: #ffffff;
    --color-text-secondary: #b0b0b0;
    
    --font-primary: Inter, system-ui, sans-serif;
    --font-display: Poppins, sans-serif;
    
    --spacing-base: 1rem;
    --border-radius: 8px;
    --transition: all 0.3s ease;
}'''
    
    # Add common base styles
    css_content += '''

/* Reset and Base */
*, *::before, *::after {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

html {
    font-size: 16px;
    scroll-behavior: smooth;
}

body {
    font-family: var(--font-primary);
    background-color: var(--color-background);
    color: var(--color-text);
    line-height: 1.6;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

/* Utilities */
.container {
    width: 100%;
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 var(--spacing-base);
}

/* Buttons */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: var(--border-radius);
    font-family: var(--font-primary);
    font-weight: 500;
    text-decoration: none;
    cursor: pointer;
    transition: var(--transition);
    position: relative;
    overflow: hidden;
}

.btn-primary {
    background: linear-gradient(135deg, var(--color-primary), var(--color-accent));
    color: var(--color-background);
    box-shadow: var(--shadow-small);
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: var(--shadow-medium);
    background: linear-gradient(135deg, var(--color-hover), var(--color-accent));
}

.btn-primary:active {
    transform: translateY(0);
    background: linear-gradient(135deg, var(--color-active), var(--color-accent));
}

.btn-secondary {
    background: var(--color-surface);
    color: var(--color-text);
    border: var(--border-width) solid var(--color-border);
}

.btn-secondary:hover {
    background: var(--color-surface-elevated);
    border-color: var(--color-primary);
}

/* Cards */
.card {
    background: var(--color-surface);
    border-radius: var(--border-radius);
    padding: 1.5rem;
    box-shadow: var(--shadow-small);
    border: var(--border-width) solid var(--color-border);
    transition: var(--transition);
}

.card:hover {
    box-shadow: var(--shadow-medium);
    transform: translateY(-2px);
}

/* Text Styles */
.text-primary { color: var(--color-primary); }
.text-secondary { color: var(--color-text-secondary); }
.text-success { color: var(--color-success); }
.text-warning { color: var(--color-warning); }
.text-error { color: var(--color-error); }

/* Backgrounds */
.bg-primary { background-color: var(--color-primary); }
.bg-secondary { background-color: var(--color-secondary); }
.bg-surface { background-color: var(--color-surface); }
.bg-surface-elevated { background-color: var(--color-surface-elevated); }

/* Legal Notice */
.legal-notice {
    position: fixed;
    bottom: 0;
    left: 0;
    right: 0;
    background: var(--color-surface);
    color: var(--color-text);
    text-align: center;
    padding: 0.5rem;
    font-size: 0.875rem;
    z-index: 1000;
    border-top: var(--border-width) solid var(--color-border);
    backdrop-filter: blur(10px);
}

/* Responsive */
@media (max-width: 768px) {
    .container {
        padding: 0 1rem;
    }
    
    html {
        font-size: 14px;
    }
    
    .btn {
        padding: 0.5rem 1rem;
    }
}

@media (max-width: 480px) {
    html {
        font-size: 13px;
    }
    
    .card {
        padding: 1rem;
    }
}

/* Component styles will be appended below */
'''
    
    with open(importer.web_folder / "css" / "styles.css", 'w', encoding='utf-8') as f:
        f.write(css_content)
    
    # Create base JavaScript
    js_content = '''// Enhanced Casino Website - Base JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('🎰 Enhanced casino website loaded');
    
    // Initialize all components
    initializeAllComponents();
    
    // Setup global handlers
    setupGlobalHandlers();
    
    // Setup theme system
    setupThemeSystem();
});

function initializeAllComponents() {
    console.log('🔧 Initializing enhanced components...');
    // Component initialization functions will be called here
}

function setupGlobalHandlers() {
    // Global keyboard navigation
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            // Close any open menus
            document.querySelectorAll('.mobile-nav.active').forEach(nav => {
                nav.classList.remove('active');
            });
        }
    });
    
    // Smooth scrolling for internal links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function(e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
}

function setupThemeSystem() {
    // Add dynamic theme switching capabilities
    const root = document.documentElement;
    
    // Theme animation support
    function animateThemeChange() {
        root.style.setProperty('--transition', 'all 0.3s ease');
        setTimeout(() => {
            root.style.removeProperty('--transition');
        }, 300);
    }
    
    // Expose theme utilities globally
    window.casinoTheme = {
        animate: animateThemeChange
    };
}

// Component scripts will be appended below
'''
    
    with open(importer.web_folder / "js" / "main.js", 'w', encoding='utf-8') as f:
        f.write(js_content)


def _insert_component_html(importer: ComponentImporter, html_content: str, comp_type: str):
    """Insert component HTML into the main HTML file with proper positioning."""
    html_file = importer.web_folder / "index.html"
    
    with open(html_file, 'r', encoding='utf-8') as f:
        current_html = f.read()
    
    # Insert based on component type with proper ordering
    if comp_type == "header":
        insertion_point = "<body>"
        new_html = current_html.replace(insertion_point, f"{insertion_point}\n    {html_content}\n")
    elif comp_type == "footer":
        insertion_point = "    <!-- Legal Notice -->"
        new_html = current_html.replace(insertion_point, f"    {html_content}\n\n{insertion_point}")
    elif comp_type == "hero":
        # Hero goes right after header, or after <body> if no header
        if "<!-- Header End -->" in current_html:
            insertion_point = "<!-- Header End -->"
            new_html = current_html.replace(insertion_point, f"{insertion_point}\n    {html_content}\n")
        else:
            # Find the last header tag or use body
            if "</header>" in current_html:
                insertion_point = "</header>"
                new_html = current_html.replace(insertion_point, f"{insertion_point}\n    {html_content}\n")
            else:
                insertion_point = "<body>"
                if insertion_point in current_html:
                    lines = current_html.split('\n')
                    for i, line in enumerate(lines):
                        if insertion_point in line:
                            lines.insert(i + 1, f"    {html_content}")
                            break
                    new_html = '\n'.join(lines)
                else:
                    new_html = current_html
    else:
        # Other components go in the main content area, before footer/legal notice
        insertion_point = "    <!-- Legal Notice -->"
        if insertion_point in current_html:
            new_html = current_html.replace(insertion_point, f"    {html_content}\n\n{insertion_point}")
        else:
            # Fallback: add before closing body tag
            insertion_point = "</body>"
            new_html = current_html.replace(insertion_point, f"    {html_content}\n{insertion_point}")
    
    # Add component marker comments for debugging
    html_content_with_markers = f"<!-- {comp_type.title()} Component Start -->\n    {html_content}\n    <!-- {comp_type.title()} Component End -->"
    new_html = new_html.replace(html_content, html_content_with_markers.strip())
    
    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)


def _append_component_css(importer: ComponentImporter, css_content: str):
    """Append component CSS to main stylesheet."""
    css_file = importer.web_folder / "css" / "styles.css"
    
    with open(css_file, 'a', encoding='utf-8') as f:
        f.write(f"\n\n/* Component Styles */\n{css_content}")


def _append_component_js(importer: ComponentImporter, js_content: str):
    """Append component JavaScript to main script."""
    js_file = importer.web_folder / "js" / "main.js"
    
    with open(js_file, 'a', encoding='utf-8') as f:
        f.write(f"\n\n// Component Script\n{js_content}")


if __name__ == "__main__":
    import_components() 