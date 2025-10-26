"""
Slideshow component with automatic carousel (no built-in navigation)
"""

import tkinter as tk
from PIL import Image, ImageTk
import os
import glob
from constants.app_config import AppConfig

class Slideshow:
    def __init__(self, parent):
        self.parent = parent
        self.current_index = 0
        self.images = []
        self.photo_images = []
        self.auto_timer = None
        
        # Load images
        self.load_images()
        
        # Create slideshow frame
        self.create_slideshow()
        
        # Start auto slideshow
        self.start_auto_slideshow()
    
    def load_images(self):
        """Load images from assets/images folder"""
        image_folder = "assets/images"
        if os.path.exists(image_folder):
            # Get all image files
            image_extensions = ['*.png', '*.jpg', '*.jpeg', '*.gif', '*.bmp']
            image_files = []
            for ext in image_extensions:
                image_files.extend(glob.glob(os.path.join(image_folder, ext)))
            
            # Sort files for consistent order
            image_files.sort()
            
            # Load and resize images
            for img_path in image_files:
                try:
                    # Open and resize image
                    img = Image.open(img_path)
                    img = img.resize((AppConfig.SLIDESHOW_WIDTH, AppConfig.SLIDESHOW_HEIGHT), Image.Resampling.LANCZOS)
                    
                    # Convert to PhotoImage for tkinter
                    photo = ImageTk.PhotoImage(img)
                    self.photo_images.append(photo)
                    self.images.append(img_path)
                except Exception as e:
                    print(f"Error loading image {img_path}: {e}")
        
        # If no images found, create a placeholder
        if not self.images:
            self.create_placeholder_image()
    
    def create_placeholder_image(self):
        """Create a placeholder image if no images are found"""
        img = Image.new('RGB', (AppConfig.SLIDESHOW_WIDTH, AppConfig.SLIDESHOW_HEIGHT), '#e0e0e0')
        photo = ImageTk.PhotoImage(img)
        self.photo_images.append(photo)
        self.images.append("placeholder")
    
    def create_slideshow(self):
        """Create the slideshow UI components"""
        # Main slideshow container
        self.slideshow_frame = tk.Frame(
            self.parent,
            bg=AppConfig.PRIMARY_COLOR
        )
        
        # Image display area without borders or margins
        self.image_container = tk.Frame(
            self.slideshow_frame,
            bg=AppConfig.PRIMARY_COLOR,
            relief=tk.FLAT,
            bd=0
        )
        self.image_container.pack(fill=tk.BOTH, expand=True)
        
        # Image label without padding/borders
        self.image_label = tk.Label(
            self.image_container,
            bg=AppConfig.PRIMARY_COLOR,
            relief=tk.FLAT,
            bd=0
        )
        self.image_label.pack(fill=tk.BOTH, expand=True)
        
        # Display first image
        if self.photo_images:
            self.display_current_image()
    
    def display_current_image(self):
        """Display the current image"""
        if self.photo_images:
            self.image_label.configure(image=self.photo_images[self.current_index])
    
    def next_image(self):
        """Show next image"""
        if self.photo_images:
            self.current_index = (self.current_index + 1) % len(self.photo_images)
            self.display_current_image()
            self.restart_auto_slideshow()
    
    def previous_image(self):
        """Show previous image"""
        if self.photo_images:
            self.current_index = (self.current_index - 1) % len(self.photo_images)
            self.display_current_image()
            self.restart_auto_slideshow()
    
    def get_current_info(self):
        """Get current slide info"""
        if self.photo_images:
            return f"{self.current_index + 1} / {len(self.photo_images)}"
        return "0 / 0"
    
    def start_auto_slideshow(self):
        """Start automatic slideshow"""
        if len(self.photo_images) > 1:
            self.auto_timer = self.parent.after(AppConfig.SLIDESHOW_INTERVAL, self.auto_next)
    
    def auto_next(self):
        """Automatically go to next image"""
        self.next_image()
    
    def restart_auto_slideshow(self):
        """Restart the auto slideshow timer"""
        if self.auto_timer:
            self.parent.after_cancel(self.auto_timer)
        self.start_auto_slideshow()
    
    def stop_auto_slideshow(self):
        """Stop the automatic slideshow"""
        if self.auto_timer:
            self.parent.after_cancel(self.auto_timer)
            self.auto_timer = None
    
    def get_frame(self):
        """Return the slideshow frame"""
        return self.slideshow_frame