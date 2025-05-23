#!/usr/bin/env python3
"""
Country Configuration Module

Handles country selection and copying of country-specific content
for the Casino Website Generator.
"""

import os
import shutil


def configure_template():
    """
    Configure starter template by selecting a country and copying related files.
    
    Allows user to select from available countries and copies country-specific
    footer and offers content to web-folder/static/ directory.
    
    Available Countries:
    - Denmark
    - France  
    - Portugal
    - UK-IR
    
    File Operations:
    - Source: master/footer/{country}/ → Destination: web-folder/static/footer/
    - Source: master/offers/{country}/ → Destination: web-folder/static/offers/
    """
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
    current_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    footer_source_dir = os.path.join(current_dir, "master", "footer", selected_country)
    footer_dest_dir = os.path.join(current_dir, "web-folder", "static", "footer")

    # Copy footer content
    _copy_country_content(footer_source_dir, footer_dest_dir, "footer")

    # Define source and destination paths for offers
    offers_source_dir = os.path.join(current_dir, "master", "offers", selected_country)
    offers_dest_dir = os.path.join(current_dir, "web-folder", "static", "offers")

    # Copy offers content
    _copy_country_content(offers_source_dir, offers_dest_dir, "offers")


def _copy_country_content(source_dir, dest_dir, content_type):
    """
    Copy country-specific content from source to destination directory.
    
    Args:
        source_dir (str): Source directory path
        dest_dir (str): Destination directory path  
        content_type (str): Type of content being copied ("footer" or "offers")
    """
    # Ensure the destination directory exists
    os.makedirs(dest_dir, exist_ok=True)

    # Copy all files from source to destination
    if os.path.exists(source_dir):
        print(f"\nCopying {content_type} files from {source_dir} to {dest_dir}...")
        
        # First, remove existing files in the destination directory
        for item in os.listdir(dest_dir):
            item_path = os.path.join(dest_dir, item)
            if os.path.isfile(item_path):
                os.remove(item_path)
            elif os.path.isdir(item_path):
                shutil.rmtree(item_path)
        
        # Copy new files from the selected country
        for item in os.listdir(source_dir):
            source_item = os.path.join(source_dir, item)
            dest_item = os.path.join(dest_dir, item)
            if os.path.isfile(source_item):
                shutil.copy2(source_item, dest_item)
                print(f"Copied {content_type} file: {item}")
            elif os.path.isdir(source_item):
                shutil.copytree(source_item, dest_item)
                print(f"Copied {content_type} directory: {item}")
        
        print(f"\n{content_type.capitalize()} files copied successfully!")
    else:
        print(f"\nError: {content_type.capitalize()} source directory {source_dir} does not exist.")


def get_available_countries():
    """
    Get list of available countries for configuration.
    
    Returns:
        list: List of supported country names
    """
    return ["Denmark", "France", "Portugal", "UK-IR"]


def validate_country_support(country):
    """
    Validate if a country is supported by the system.
    
    Args:
        country (str): Country name to validate
        
    Returns:
        bool: True if country is supported, False otherwise
    """
    available_countries = get_available_countries()
    return country in available_countries 