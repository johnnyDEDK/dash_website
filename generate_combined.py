#!/usr/bin/env python3
"""
Combined Save the Date design generator.
Configurable spacing and photo positioning.

Based on analysis of refined2 and expanded_v3.
"""

import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance


# =============================================================================
# CONFIGURATION - Edit these values to adjust the design
# =============================================================================

# -----------------------------------------------------------------------------
# AVAILABLE FONTS (macOS paths - adjust for other systems)
# -----------------------------------------------------------------------------
# Elegant Serif fonts (recommended for wedding designs):
#   'Didot'           - Classic French serif, very elegant, thin strokes
#   'Bodoni 72'       - Italian serif, high contrast, dramatic
#   'Baskerville'     - Traditional English serif, readable
#   'Palatino'        - Humanist serif, warm and elegant
#   'Cochin'          - French serif, slightly ornate
#   'Georgia'         - Modern serif, very readable
#   'Times New Roman' - Classic, widely available
#
# Script/Calligraphy fonts (for romantic feel):
#   'Snell Roundhand' - Formal script, very elegant
#   'Brush Script MT' - Casual script
#   'Zapfino'         - Elaborate calligraphic
#
# Sans-Serif fonts (for modern/minimal look):
#   'Helvetica Neue'  - Clean Swiss design
#   'Avenir'          - Geometric, modern
#   'Futura'          - Geometric, bold
#   'Gill Sans'       - Humanist sans-serif
# -----------------------------------------------------------------------------

FONT_PATHS = {
    # Serif fonts
    'Didot': '/System/Library/Fonts/Supplemental/Didot.ttc',
    'Bodoni 72': '/System/Library/Fonts/Supplemental/Bodoni 72.ttc',
    'Baskerville': '/System/Library/Fonts/Supplemental/Baskerville.ttc',
    'Palatino': '/System/Library/Fonts/Supplemental/Palatino.ttc',
    'Cochin': '/System/Library/Fonts/Supplemental/Cochin.ttc',
    'Georgia': '/System/Library/Fonts/Supplemental/Georgia.ttf',
    'Times New Roman': '/System/Library/Fonts/Supplemental/Times New Roman.ttf',
    'Garamond': '/System/Library/Fonts/Supplemental/AppleGaramond.ttf',

    # Script fonts
    'Snell Roundhand': '/System/Library/Fonts/Supplemental/Snell Roundhand.ttc',
    'Brush Script MT': '/System/Library/Fonts/Supplemental/Brush Script.ttf',
    'Zapfino': '/System/Library/Fonts/Zapfino.ttf',

    # Sans-serif fonts
    'Helvetica Neue': '/System/Library/Fonts/HelveticaNeue.ttc',
    'Avenir': '/System/Library/Fonts/Avenir.ttc',
    'Futura': '/System/Library/Fonts/Supplemental/Futura.ttc',

    # Fallback
    'Times': '/System/Library/Fonts/Times.ttc',
}

# =============================================================================
# SHARED CONFIG (applies to both formats unless overridden)
# =============================================================================
CONFIG_SHARED = {
    # --- Colors (Terracotta palette) ---
    'color_background': (252, 249, 245),
    'color_dark': (55, 45, 40),
    'color_warm_gray': (125, 110, 100),
    'color_terracotta': (164, 120, 100),

    # --- Photo Background ---
    'photo_path': '/Users/Florian.Thams/Projekte/claude-skills/project-management-context/hochzeit/PHOTO-2026-02-15-11-10-32.jpg',
    'photo_opacity': 0.13,
    'photo_blur': 4,
    'photo_brightness': 1.45,
    'photo_offset_x': -30,
    'photo_offset_y': 0,
    'photo_scale': 1.0,  # 1.0 = fit to cover, <1.0 = zoom out (show more), >1.0 = zoom in

    # --- Fonts ---
    'font_header': 'Didot',
    'font_names': 'Didot',
    'font_ampersand': 'Bodoni 72',
    'font_date': 'Didot',
    'font_location': 'Didot',

    # --- Text Content ---
    'text_header': 'SAVE OUR DATE',
    'text_name1': 'Beatrice',
    'text_name2': 'Florian',
    'text_ampersand': '&',
    'text_date': ['15', '08', '26'],
    'text_location': 'UNTERNBERG HOF | RUHPOLDING',

    # --- Output ---
    'output_dir': '/Users/Florian.Thams/Projekte/claude-skills/project-management-context/hochzeit/designs/2c_final',
    'output_name': 'combined_v6.png',

    # --- Debug ---
    'debug_show_bounds': False,
}

# =============================================================================
# DIGITAL FORMAT CONFIG (1080x1920 - Mobile/WhatsApp)
# =============================================================================
CONFIG_DIGITAL = {
    'output_format': 'digital',
    'canvas_width': 1080,
    'canvas_height': 1920,

    # Font sizes (optimized for digital)
    'font_size_header': 44,
    'font_size_names': 90,
    'font_size_ampersand': 560,
    'font_size_date': 74,
    'font_size_location': 44,

    # Spacing (optimized for digital)
    'top_margin': 180,
    'header_to_line': 70,
    'line_length_top': 80,
    'line_to_beatrice': 214,
    'beatrice_to_amp': 40,
    'amp_to_florian': 32,
    'florian_to_line': 100,
    'line_length_bottom': 80,
    'line_to_date': 80,
    'date_spacing': 45,
    'date_to_location': 80,
}

# =============================================================================
# PRINT A6 FORMAT CONFIG (1240x1748 @ 300 DPI - 105mm x 148mm)
# =============================================================================
# Adjusted to fit shorter A6 canvas (1748px vs digital's 1920px = 172px less)
CONFIG_PRINT_A6 = {
    'output_format': 'print_a6',
    'print_dpi': 300,
    'canvas_width': 1240,
    'canvas_height': 1748,

    # Photo adjustments (A6 has wider aspect ratio, so needs different settings)
    'photo_scale': 1.15,      # Zoom out to show similar content as digital version
    'photo_offset_x': -30,    # Adjust horizontal position (positive = show more left)
    'photo_offset_y': -30,      # Adjust vertical position (positive = show more top)

    # Font sizes (same as digital)
    'font_size_header': 32,
    'font_size_names': 90,
    'font_size_ampersand': 560,
    'font_size_date': 74,
    'font_size_location': 32,

    # Spacing (reduced to fit A6 height)
    'top_margin': 140,           # Reduced from 180
    'header_to_line': 70,        # Reduced from 90
    'line_length_top': 90,
    'line_to_beatrice': 150,     # Reduced from 184
    'beatrice_to_amp': 40,
    'amp_to_florian': 32,
    'florian_to_line': 70,       # Reduced from 100
    'line_length_bottom': 70,    # Reduced from 80
    'line_to_date': 80,          # Reduced from 80
    'date_spacing': 45,          # Reduced from 45
    'date_to_location': 80,      # Reduced from 80
}

# =============================================================================
# ACTIVE CONFIG - Choose which format to generate
# =============================================================================
# Set to 'digital' or 'print_a6'
ACTIVE_FORMAT = 'digital'


def get_config(format_name=None):
    """Get merged config for specified format."""
    fmt = format_name or ACTIVE_FORMAT
    config = CONFIG_SHARED.copy()

    if fmt == 'print_a6':
        config.update(CONFIG_PRINT_A6)
    else:
        config.update(CONFIG_DIGITAL)

    return config


# For backwards compatibility
CONFIG = get_config(ACTIVE_FORMAT)


# =============================================================================
# FONT HANDLING
# =============================================================================

def get_font_path(font_name):
    """Get font path from font name, with fallback."""
    if font_name in FONT_PATHS:
        path = FONT_PATHS[font_name]
        if os.path.exists(path):
            return path
        print(f"Warning: Font '{font_name}' not found at {path}")

    # Try fallback
    fallback = FONT_PATHS.get('Times') or FONT_PATHS.get('Didot')
    if fallback and os.path.exists(fallback):
        print(f"Using fallback font: Times")
        return fallback

    # Last resort: find any available font
    for name, path in FONT_PATHS.items():
        if os.path.exists(path):
            print(f"Using available font: {name}")
            return path

    raise FileNotFoundError("No fonts found!")


def get_canvas_size(cfg):
    """Calculate canvas size based on output format."""
    if cfg['canvas_width'] and cfg['canvas_height']:
        return cfg['canvas_width'], cfg['canvas_height']

    if cfg['output_format'] == 'print_a6':
        # A6 = 105mm x 148mm at specified DPI
        dpi = cfg['print_dpi']
        width = int(105 * dpi / 25.4)   # 1240px at 300dpi
        height = int(148 * dpi / 25.4)  # 1748px at 300dpi
        return width, height
    else:
        # Digital: mobile/WhatsApp format
        return 1080, 1920


def get_scale_factor(cfg):
    """Get scale factor for print vs digital.

    For print, we scale by height (not width) since A6 has different aspect ratio.
    This ensures vertical content fits, though it will appear smaller horizontally.
    """
    if cfg['output_format'] == 'print_a6':
        # Scale by height to ensure vertical content fits
        digital_height = 1920
        _, print_height = get_canvas_size(cfg)
        return print_height / digital_height
    return 1.0


# =============================================================================
# BACKGROUND
# =============================================================================

def create_background(cfg):
    """Create canvas with photo background."""
    width = cfg['canvas_width']
    height = cfg['canvas_height']
    bg_color = cfg['color_background']

    canvas = Image.new('RGB', (width, height), bg_color)

    photo_path = cfg['photo_path']
    if not os.path.exists(photo_path):
        print(f"Warning: Photo not found at {photo_path}")
        return canvas

    # Load photo
    photo = Image.open(photo_path)

    # Scale to cover canvas with extra margin for offset movement
    # Add padding to allow moving the photo around
    max_offset = max(abs(cfg['photo_offset_x']), abs(cfg['photo_offset_y']), 200)
    padded_width = width + max_offset * 2
    padded_height = height + max_offset * 2

    photo_ratio = photo.width / photo.height
    padded_ratio = padded_width / padded_height

    if photo_ratio > padded_ratio:
        new_height = padded_height
        new_width = int(padded_height * photo_ratio)
    else:
        new_width = padded_width
        new_height = int(padded_width / photo_ratio)

    # Apply photo_scale: <1.0 zooms out (shows more), >1.0 zooms in
    # We scale DOWN the computed dimensions to show MORE of the image
    photo_scale = cfg.get('photo_scale', 1.0)
    if photo_scale != 1.0:
        # Inverse: smaller scale value = larger photo relative to canvas = more visible
        scale_factor = 1.0 / photo_scale
        new_width = int(new_width * scale_factor)
        new_height = int(new_height * scale_factor)

    photo = photo.resize((new_width, new_height), Image.LANCZOS)

    # Calculate crop position
    # Start from center, then apply user offset
    base_x = (new_width - width) // 2
    base_y = (new_height - height) // 2

    # Apply user offset (positive = shift image content in that direction)
    # offset_x > 0: show more of the LEFT side of photo (move crop window left)
    # offset_y > 0: show more of the TOP of photo (move crop window up)
    x_offset = base_x - cfg['photo_offset_x']
    y_offset = base_y - cfg['photo_offset_y']

    # Clamp to valid range
    x_offset = max(0, min(x_offset, new_width - width))
    y_offset = max(0, min(y_offset, new_height - height))

    photo = photo.crop((x_offset, y_offset, x_offset + width, y_offset + height))

    # Apply effects
    photo = photo.filter(ImageFilter.GaussianBlur(radius=cfg['photo_blur']))

    enhancer = ImageEnhance.Brightness(photo)
    photo = enhancer.enhance(cfg['photo_brightness'])

    # Blend with background
    canvas = Image.blend(canvas, photo, cfg['photo_opacity'])

    return canvas


# =============================================================================
# DRAWING HELPERS
# =============================================================================

def draw_centered_text(draw, y, text, font, color, canvas_width):
    """Draw text centered horizontally at given y position."""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    x = (canvas_width - text_width) // 2
    draw.text((x, y), text, font=font, fill=color)
    return text_height


def draw_vertical_line(draw, y_start, length, color, canvas_width, line_width=2):
    """Draw centered vertical line."""
    x = canvas_width // 2
    draw.line([(x, y_start), (x, y_start + length)], fill=color, width=line_width)
    return length


def get_actual_text_bounds(text, font, color):
    """
    Render text to find actual pixel bounds (not just font metrics).
    Returns (width, height, top_offset, bottom_offset) where offsets
    indicate how much the actual pixels extend beyond the bbox.
    """
    # Get font metrics bbox
    bbox = font.getbbox(text)
    bbox_width = bbox[2] - bbox[0]
    bbox_height = bbox[3] - bbox[1]

    # Create temporary image with padding
    padding = 100
    temp_width = bbox_width + padding * 2
    temp_height = bbox_height + padding * 2

    temp_img = Image.new('RGB', (temp_width, temp_height), (255, 255, 255))
    temp_draw = ImageDraw.Draw(temp_img)

    # Draw text centered in temp image
    x = padding
    y = padding
    temp_draw.text((x, y), text, font=font, fill=color)

    # Scan to find actual top and bottom with content
    pixels = temp_img.load()
    actual_top = temp_height
    actual_bottom = 0

    for py in range(temp_height):
        for px in range(temp_width):
            r, g, b = pixels[px, py]
            if r < 250 or g < 250 or b < 250:  # Non-white pixel
                actual_top = min(actual_top, py)
                actual_bottom = max(actual_bottom, py)

    # Calculate how much the actual rendering extends beyond bbox
    rendered_top = actual_top - padding
    rendered_bottom = actual_bottom - padding

    actual_height = actual_bottom - actual_top + 1

    return bbox_width, actual_height, rendered_top, rendered_bottom


def measure_text_actual_bounds(text, font):
    """
    Measure actual rendered bounds of text by drawing on white background.

    Returns dict with:
      - bbox_height: font metric height
      - top_offset: offset from draw point to actual visual top (negative = above draw point)
      - bottom_offset: offset from draw point to actual visual bottom
      - actual_height: total visual height in pixels
    """
    bbox = font.getbbox(text)
    bbox_width = bbox[2] - bbox[0]
    bbox_height = bbox[3] - bbox[1]

    # Create temp image with extra space
    padding = 300
    temp_img = Image.new('RGB', (bbox_width + padding * 2, bbox_height + padding * 2), (255, 255, 255))
    temp_draw = ImageDraw.Draw(temp_img)

    # Draw at padding offset - this is where PIL places the bbox top
    draw_origin_y = padding
    temp_draw.text((padding, draw_origin_y), text, font=font, fill=(0, 0, 0))

    # Find actual top and bottom by scanning
    pixels = temp_img.load()
    actual_top_px = None
    actual_bottom_px = None

    # Scan top to bottom to find first row with content
    for py in range(temp_img.height):
        for px in range(temp_img.width):
            r, _, _ = pixels[px, py]
            if r < 240:  # Dark pixel (with some tolerance for anti-aliasing)
                if actual_top_px is None:
                    actual_top_px = py
                actual_bottom_px = py
                break  # Found content in this row, move to next row

    if actual_top_px is None:
        actual_top_px = draw_origin_y
        actual_bottom_px = draw_origin_y + bbox_height

    # Calculate offsets relative to draw origin
    # top_offset: negative means visual top is ABOVE the draw point
    top_offset = actual_top_px - draw_origin_y
    # bottom_offset: how far below draw point the visual bottom is
    bottom_offset = actual_bottom_px - draw_origin_y

    return {
        'bbox_height': bbox_height,
        'bbox_width': bbox_width,
        'top_offset': top_offset,      # Usually 0 or small positive
        'bottom_offset': bottom_offset, # Usually bbox_height + descender
        'actual_height': actual_bottom_px - actual_top_px + 1,
    }


def draw_text_with_actual_bounds(draw, y_for_visual_top, text, font, color, canvas_width):
    """
    Draw text positioned so its actual visual top is at y_for_visual_top.
    Returns the actual visual top and bottom positions.

    The gap between elements should be measured from visual_bottom of one
    to visual_top of the next.
    """
    # Measure actual bounds
    bounds = measure_text_actual_bounds(text, font)

    # top_offset: how far below draw point the visual top actually appears
    # If top_offset = 5, visual top is 5px below where we draw
    # To place visual top at y_for_visual_top, we draw at y_for_visual_top - top_offset
    draw_y = y_for_visual_top - bounds['top_offset']

    # Center horizontally
    x = (canvas_width - bounds['bbox_width']) // 2

    # Draw the text
    draw.text((x, draw_y), text, font=font, fill=color)

    # Calculate actual visual positions
    actual_visual_top = draw_y + bounds['top_offset']
    actual_visual_bottom = draw_y + bounds['bottom_offset']

    print(f"    Bounds: top_offset={bounds['top_offset']}px, bottom_offset={bounds['bottom_offset']}px, actual_height={bounds['actual_height']}px")

    return {
        'visual_top': actual_visual_top,
        'visual_bottom': actual_visual_bottom,
        'draw_y': draw_y,
        'bounds': bounds,
    }


# =============================================================================
# MAIN DESIGN GENERATOR
# =============================================================================

def generate_design(cfg):
    """Generate the combined design."""
    # Get canvas dimensions from config (no auto-scaling, use explicit values)
    width = cfg['canvas_width']
    height = cfg['canvas_height']

    print(f"Generating design ({cfg['output_format']})...")
    print(f"  Canvas: {width}x{height}")

    # Create background
    canvas = create_background(cfg)
    draw = ImageDraw.Draw(canvas)

    # Load fonts with per-element selection (no scaling - use config values directly)
    font_header = ImageFont.truetype(
        get_font_path(cfg['font_header']),
        cfg['font_size_header']
    )
    font_names = ImageFont.truetype(
        get_font_path(cfg['font_names']),
        cfg['font_size_names']
    )
    font_ampersand = ImageFont.truetype(
        get_font_path(cfg['font_ampersand']),
        cfg['font_size_ampersand']
    )
    font_date = ImageFont.truetype(
        get_font_path(cfg['font_date']),
        cfg['font_size_date']
    )
    font_location = ImageFont.truetype(
        get_font_path(cfg['font_location']),
        cfg['font_size_location']
    )

    # Use spacing values directly from config (no scaling)
    top_margin = cfg['top_margin']
    header_to_line = cfg['header_to_line']
    line_length_top = cfg['line_length_top']
    line_to_beatrice = cfg['line_to_beatrice']
    beatrice_to_amp = cfg['beatrice_to_amp']
    amp_to_florian = cfg['amp_to_florian']
    florian_to_line = cfg['florian_to_line']
    line_length_bottom = cfg['line_length_bottom']
    line_to_date = cfg['line_to_date']
    date_spacing = cfg['date_spacing']
    date_to_location = cfg['date_to_location']

    current_y = top_margin

    # --- 1. Header ---
    h = draw_centered_text(draw, current_y, cfg['text_header'],
                           font_header, cfg['color_warm_gray'], width)
    print(f"  Header: y={current_y}, height={h}px")
    current_y += h + header_to_line

    # --- 2. Top Line ---
    h = draw_vertical_line(draw, current_y, line_length_top,
                           cfg['color_terracotta'], width)
    print(f"  Top line: y={current_y}, length={h}px")
    current_y += h + line_to_beatrice

    # --- 3. Beatrice (with actual bounds) ---
    beatrice_result = draw_text_with_actual_bounds(
        draw, current_y, cfg['text_name1'],
        font_names, cfg['color_dark'], width
    )
    print(f"  Beatrice: visual_top={beatrice_result['visual_top']}, visual_bottom={beatrice_result['visual_bottom']}px")

    # Debug: draw bounds
    if cfg.get('debug_show_bounds'):
        draw.line([(0, beatrice_result['visual_top']), (50, beatrice_result['visual_top'])], fill=(255, 0, 0), width=2)
        draw.line([(0, beatrice_result['visual_bottom']), (50, beatrice_result['visual_bottom'])], fill=(0, 255, 0), width=2)

    # Gap is from Beatrice's actual visual bottom to ampersand's actual visual top
    amp_visual_top = beatrice_result['visual_bottom'] + beatrice_to_amp

    # --- 4. Ampersand (with actual bounds) ---
    amp_result = draw_text_with_actual_bounds(
        draw, amp_visual_top, cfg['text_ampersand'],
        font_ampersand, cfg['color_dark'], width
    )
    print(f"  Ampersand: visual_top={amp_result['visual_top']}, visual_bottom={amp_result['visual_bottom']}px")
    actual_gap_above = amp_result['visual_top'] - beatrice_result['visual_bottom']
    print(f"    ACTUAL gap Beatrice→Amp: {actual_gap_above}px")

    # Debug: draw bounds
    if cfg.get('debug_show_bounds'):
        draw.line([(0, amp_result['visual_top']), (50, amp_result['visual_top'])], fill=(255, 0, 0), width=2)
        draw.line([(0, amp_result['visual_bottom']), (50, amp_result['visual_bottom'])], fill=(0, 255, 0), width=2)

    # Gap from ampersand's actual visual bottom to Florian's actual visual top
    florian_visual_top = amp_result['visual_bottom'] + amp_to_florian

    # --- 5. Florian (with actual bounds) ---
    florian_result = draw_text_with_actual_bounds(
        draw, florian_visual_top, cfg['text_name2'],
        font_names, cfg['color_dark'], width
    )
    print(f"  Florian: visual_top={florian_result['visual_top']}, visual_bottom={florian_result['visual_bottom']}px")
    actual_gap_below = florian_result['visual_top'] - amp_result['visual_bottom']
    print(f"    ACTUAL gap Amp→Florian: {actual_gap_below}px")

    # Debug: draw bounds
    if cfg.get('debug_show_bounds'):
        draw.line([(0, florian_result['visual_top']), (50, florian_result['visual_top'])], fill=(255, 0, 0), width=2)
        draw.line([(0, florian_result['visual_bottom']), (50, florian_result['visual_bottom'])], fill=(0, 255, 0), width=2)

    current_y = florian_result['visual_bottom'] + florian_to_line

    # --- 6. Bottom Line ---
    h = draw_vertical_line(draw, current_y, line_length_bottom,
                           cfg['color_terracotta'], width)
    print(f"  Bottom line: y={current_y}, length={h}px")
    current_y += h + line_to_date

    # --- 7. Date Numbers ---
    for i, date_part in enumerate(cfg['text_date']):
        h = draw_centered_text(draw, current_y, date_part,
                               font_date, cfg['color_dark'], width)
        print(f"  Date {date_part}: y={current_y}, height={h}px")
        if i < len(cfg['text_date']) - 1:
            current_y += h + date_spacing
        else:
            current_y += h + date_to_location

    # --- 8. Location ---
    h = draw_centered_text(draw, current_y, cfg['text_location'],
                           font_location, cfg['color_warm_gray'], width)
    print(f"  Location: y={current_y}, height={h}px")
    current_y += h

    # Calculate bottom margin
    bottom_margin = height - current_y
    print(f"  Bottom margin: {bottom_margin}px")

    # Save with format-specific filename
    os.makedirs(cfg['output_dir'], exist_ok=True)

    # Add format suffix to filename
    base_name = cfg['output_name'].rsplit('.', 1)[0]
    ext = cfg['output_name'].rsplit('.', 1)[1] if '.' in cfg['output_name'] else 'png'
    format_suffix = f"_{cfg['output_format']}"
    output_name = f"{base_name}{format_suffix}.{ext}"

    output_path = os.path.join(cfg['output_dir'], output_name)

    # For print, save at higher quality and include DPI metadata
    if cfg['output_format'] == 'print_a6':
        # Save with DPI metadata for print
        canvas.save(output_path, 'PNG', dpi=(cfg['print_dpi'], cfg['print_dpi']))
        print(f"\nSaved (print A6 @ {cfg['print_dpi']} DPI): {output_path}")
    else:
        canvas.save(output_path, 'PNG')
        print(f"\nSaved (digital): {output_path}")

    return canvas, output_path


# =============================================================================
# ENTRY POINT
# =============================================================================

def generate_both():
    """Generate both digital and print versions."""
    print("=" * 60)
    print("Generating DIGITAL version")
    print("=" * 60)
    generate_design(get_config('digital'))

    print("\n" + "=" * 60)
    print("Generating PRINT A6 version")
    print("=" * 60)
    generate_design(get_config('print_a6'))


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        fmt = sys.argv[1].lower()
        if fmt == 'both':
            generate_both()
        elif fmt in ('digital', 'print_a6'):
            generate_design(get_config(fmt))
        else:
            print(f"Unknown format: {fmt}")
            print("Usage: python generate_combined.py [digital|print_a6|both]")
    else:
        # Generate based on ACTIVE_FORMAT setting
        generate_design(get_config(ACTIVE_FORMAT))
