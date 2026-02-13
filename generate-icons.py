#!/usr/bin/env python3
"""Generate all app icons for Light Up ring light app"""

from PIL import Image, ImageDraw
import os

def create_ring_icon(size, filename):
    """Create a ring light icon at specified size"""
    # Create image with transparency
    img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Calculate dimensions
    margin = size * 0.1
    outer_radius = (size - margin * 2) / 2
    ring_thickness = size * 0.12
    inner_radius = outer_radius - ring_thickness
    center = size / 2
    
    # Draw outer circle (ring)
    draw.ellipse(
        [margin, margin, size - margin, size - margin],
        fill='white',
        outline=None
    )
    
    # Draw inner circle (cut out middle to make ring)
    inner_margin = center - inner_radius
    draw.ellipse(
        [inner_margin, inner_margin, size - inner_margin, size - inner_margin],
        fill=(0, 0, 0, 0),
        outline=None
    )
    
    # Draw center dot
    dot_size = size * 0.15
    dot_margin = center - (dot_size / 2)
    draw.ellipse(
        [dot_margin, dot_margin, dot_margin + dot_size, dot_margin + dot_size],
        fill='white',
        outline=None
    )
    
    img.save(filename, 'PNG')
    print(f"Created {filename} ({size}x{size})")

def create_social_image(width, height, filename):
    """Create social media preview image"""
    img = Image.new('RGB', (width, height), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    
    # Draw large ring in center
    center_x = width / 2
    center_y = height / 2
    ring_size = min(width, height) * 0.5
    margin = (width - ring_size) / 2 if width < height else (height - ring_size) / 2
    
    outer_radius = ring_size / 2
    ring_thickness = ring_size * 0.15
    inner_radius = outer_radius - ring_thickness
    
    # Draw ring
    draw.ellipse(
        [center_x - outer_radius, center_y - outer_radius, 
         center_x + outer_radius, center_y + outer_radius],
        fill='white',
        outline=None
    )
    
    # Cut out center
    draw.ellipse(
        [center_x - inner_radius, center_y - inner_radius,
         center_x + inner_radius, center_y + inner_radius],
        fill=(0, 0, 0),
        outline=None
    )
    
    # Center dot
    dot_size = ring_size * 0.12
    draw.ellipse(
        [center_x - dot_size/2, center_y - dot_size/2,
         center_x + dot_size/2, center_y + dot_size/2],
        fill='white',
        outline=None
    )
    
    img.save(filename, 'PNG')
    print(f"Created {filename} ({width}x{height})")

def create_favicon():
    """Create multi-size favicon.ico"""
    sizes = [16, 32, 48]
    images = []
    
    for size in sizes:
        img = Image.new('RGBA', (size, size), (0, 0, 0, 0))
        draw = ImageDraw.Draw(img)
        
        margin = max(2, size * 0.1)
        outer_radius = (size - margin * 2) / 2
        ring_thickness = max(2, size * 0.12)
        inner_radius = outer_radius - ring_thickness
        center = size / 2
        
        # Draw ring
        draw.ellipse(
            [margin, margin, size - margin, size - margin],
            fill='white',
            outline=None
        )
        
        # Cut center
        inner_margin = center - inner_radius
        draw.ellipse(
            [inner_margin, inner_margin, size - inner_margin, size - inner_margin],
            fill=(0, 0, 0, 0),
            outline=None
        )
        
        # Center dot
        dot_size = max(2, size * 0.15)
        dot_margin = center - (dot_size / 2)
        draw.ellipse(
            [dot_margin, dot_margin, dot_margin + dot_size, dot_margin + dot_size],
            fill='white',
            outline=None
        )
        
        images.append(img)
    
    images[0].save('favicon.ico', format='ICO', sizes=[(s, s) for s in sizes])
    print(f"Created favicon.ico (multi-size: {sizes})")

if __name__ == '__main__':
    # Create app icons
    create_ring_icon(16, 'icon-16.png')
    create_ring_icon(32, 'icon-32.png')
    create_ring_icon(192, 'icon-192.png')
    create_ring_icon(512, 'icon-512.png')
    
    # Create social media images
    create_social_image(1200, 630, 'og-image.png')
    create_social_image(1200, 630, 'twitter-image.png')
    
    # Create favicon
    create_favicon()
    
    print("\n✓ All icons generated successfully!")
