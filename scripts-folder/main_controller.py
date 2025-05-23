#!/usr/bin/env python3
"""
Main Controller Module

Orchestrates all functionality of the Casino Website Generator
by importing and calling functions from individual modules.
"""

import sys
import os

# Add the scripts folder to the Python path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Import all module functions
from country_config import configure_template
from component_importer import import_components
from image_downloader import download_images
from error_checker import error_checking
from cleanup_manager import cleanup


def main():
    """
    Main function to display menu and handle user choices.
    
    This replaces the main() function from starter.py and imports
    all functionality from the modular scripts.
    """
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
    
    # Route to appropriate module function
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


def run_full_workflow():
    """
    Run the complete casino website generation workflow.
    
    Executes all steps in sequence:
    1. Configure country-specific content
    2. Import and assemble components
    3. Download/process images
    4. Check for errors
    5. Cleanup and optimize
    """
    print("===== FULL WORKFLOW EXECUTION =====")
    print("This will run all steps in sequence.\n")
    
    confirm = input("Do you want to proceed with full workflow? (y/n): ").strip().lower()
    if confirm != 'y':
        print("Workflow cancelled.")
        return
    
    try:
        print("\n🔸 Step 1: Configuring country-specific content...")
        configure_template()
        
        print("\n🔸 Step 2: Importing and assembling components...")
        import_components()
        
        print("\n🔸 Step 3: Processing images...")
        download_images()
        
        print("\n🔸 Step 4: Checking for errors...")
        error_checking()
        
        print("\n🔸 Step 5: Final cleanup and optimization...")
        cleanup()
        
        print("\n🎉 Full workflow completed successfully!")
        print("Your casino website is ready in the web-folder/ directory.")
        
    except Exception as e:
        print(f"\n❌ Error during workflow execution: {str(e)}")
        print("Please check the individual steps and try again.")


def quick_build():
    """
    Quick build option for experienced users.
    
    Runs country configuration and component import only,
    skipping optional steps like image processing and cleanup.
    """
    print("===== QUICK BUILD =====")
    print("This will configure country and import components only.\n")
    
    try:
        print("🔸 Configuring country...")
        configure_template()
        
        print("\n🔸 Importing components...")
        import_components()
        
        print("\n✅ Quick build completed!")
        print("Your basic casino website is ready.")
        print("You can run individual tools for images, error checking, and cleanup.")
        
    except Exception as e:
        print(f"\n❌ Error during quick build: {str(e)}")


def show_project_status():
    """
    Display current project status and available options.
    
    Shows:
    - Current configuration
    - Generated files status
    - Available next steps
    """
    print("===== PROJECT STATUS =====")
    
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    web_folder = os.path.join(current_dir, "web-folder")
    
    # Check for generated files
    has_index = os.path.exists(os.path.join(web_folder, "index.html"))
    has_css = os.path.exists(os.path.join(web_folder, "css", "styles.css"))
    has_js = os.path.exists(os.path.join(web_folder, "scripts", "main.js"))
    has_static = os.path.exists(os.path.join(web_folder, "static"))
    
    print(f"📁 Project Directory: {current_dir}")
    print(f"🌐 Web Folder: {web_folder}")
    print("\n📋 Generated Files Status:")
    print(f"   {'✅' if has_index else '❌'} index.html")
    print(f"   {'✅' if has_css else '❌'} CSS files")
    print(f"   {'✅' if has_js else '❌'} JavaScript files")
    print(f"   {'✅' if has_static else '❌'} Static content")
    
    # Recommend next steps
    print("\n🎯 Recommended Next Steps:")
    if not (has_index and has_css and has_js):
        print("   1. Run 'Configure Country' and 'Import Components'")
    else:
        print("   1. Run 'Error Checking' to validate the website")
        print("   2. Process images if needed")
        print("   3. Run 'Clean Up' for optimization")


def show_module_info():
    """
    Display information about all available modules.
    """
    print("===== MODULE INFORMATION =====")
    
    modules = {
        "country_config.py": {
            "description": "Handles country selection and content copying",
            "main_function": "configure_template()",
            "features": ["Country selection", "Footer content copying", "Offers content copying"]
        },
        "component_importer.py": {
            "description": "Enhanced component system with JSON configuration and modular files",
            "main_function": "import_components()",
            "features": ["JSON-based component configuration", "Modular file structure", "Advanced theming system", "Real component files (not templates)"]
        },
        "image_downloader.py": {
            "description": "Downloads and manages website images",
            "main_function": "download_images()",
            "features": ["Unsplash API integration", "AI image generation", "Image organization"]
        },
        "error_checker.py": {
            "description": "Validates generated websites for errors",
            "main_function": "error_checking()",
            "features": ["Link validation", "HTML/CSS/JS syntax checking", "Casino compliance"]
        },
        "cleanup_manager.py": {
            "description": "Optimizes and cleans up generated websites",
            "main_function": "cleanup()",
            "features": ["File compression", "Code minification", "Production builds"]
        },
        "img_processor.py": {
            "description": "Processes and optimizes images",
            "main_function": "process_images()",
            "features": ["Image resizing", "Format conversion", "Quality optimization"]
        }
    }
    
    for module_name, info in modules.items():
        print(f"\n📦 {module_name}")
        print(f"   Description: {info['description']}")
        print(f"   Main Function: {info['main_function']}")
        print(f"   Features: {', '.join(info['features'])}")


def interactive_menu():
    """
    Extended interactive menu with additional options.
    """
    while True:
        print("\n" + "="*60)
        print("         CASINO WEBSITE GENERATOR - MAIN MENU")
        print("="*60)
        print("Basic Operations:")
        print("  1. Configure Country")
        print("  2. Import Components") 
        print("  3. Download Images")
        print("  4. Error Checking")
        print("  5. Clean Up")
        print("\nAdvanced Options:")
        print("  6. Full Workflow (Run All Steps)")
        print("  7. Quick Build (Country + Components)")
        print("  8. Show Project Status")
        print("  9. Module Information")
        print("  0. Exit")
        
        try:
            choice = int(input("\nSelect option (0-9): "))
            
            if choice == 0:
                print("Thank you for using Casino Website Generator!")
                break
            elif choice == 1:
                configure_template()
            elif choice == 2:
                import_components()
            elif choice == 3:
                download_images()
            elif choice == 4:
                error_checking()
            elif choice == 5:
                cleanup()
            elif choice == 6:
                run_full_workflow()
            elif choice == 7:
                quick_build()
            elif choice == 8:
                show_project_status()
            elif choice == 9:
                show_module_info()
            else:
                print("Invalid choice. Please select 0-9.")
                
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\n\nExiting Casino Website Generator...")
            break
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            print("Please try again or report this issue.")


if __name__ == "__main__":
    # Check if running with command line arguments
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        
        if arg == "country":
            configure_template()
        elif arg == "components":
            import_components()
        elif arg == "images":
            download_images()
        elif arg == "check":
            error_checking()
        elif arg == "cleanup":
            cleanup()
        elif arg == "workflow":
            run_full_workflow()
        elif arg == "quick":
            quick_build()
        elif arg == "status":
            show_project_status()
        else:
            print(f"Unknown command: {arg}")
            print("Available commands: country, components, images, check, cleanup, workflow, quick, status")
    else:
        # Run interactive menu if no arguments
        interactive_menu() 