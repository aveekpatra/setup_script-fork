#!/usr/bin/env python3

import sys
import os

# Add the scripts folder to the Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
scripts_folder = os.path.join(current_dir, "scripts-folder")
sys.path.append(scripts_folder)

def main():
    """Main entry point for the Casino Website Generator."""
    # Try to import and run the modular system
    try:
        from main_controller import main as main_controller
        main_controller()
        
    except ImportError as e:
        print(f"❌ Error importing modular components: {str(e)}")
        print("\n" + "="*60)
        print("CASINO WEBSITE GENERATOR - FALLBACK MODE")
        print("="*60)
        print("\n⚠️  The modular scripts are not available.")
        print("Please ensure the scripts-folder directory exists with all modules:")
        print("  • main_controller.py")
        print("  • country_config.py") 
        print("  • component_importer.py")
        print("  • image_downloader.py")
        print("  • error_checker.py")
        print("  • cleanup_manager.py")
        print("  • img_processor.py")
        print("\n💡 To fix this issue:")
        print("  1. Check that scripts-folder/ exists in the project directory")
        print("  2. Verify all module files are present")
        print("  3. Try running: python scripts-folder/main_controller.py")
        print("\n🔧 For technical support, check the documentation in scripts-folder/README.md")
        
    except Exception as e:
        print(f"❌ Unexpected error: {str(e)}")
        print("\n💡 Try running the main controller directly:")
        print("   python scripts-folder/main_controller.py")

if __name__ == "__main__":
    main() 