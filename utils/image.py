from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_image(quote: str, author: str, book: str, output_path: str):
    width, height = 1080, 1080
    background_color = "#1a1a1a"
    text_color = "#ffffff"

    image = Image.new("RGB", (width, height), color=background_color)
    draw = ImageDraw.Draw(image)

    try:
        font = ImageFont.truetype("LibreBaskerville.ttf", 48)
        author_font = ImageFont.truetype("LibreBaskerville.ttf", 36)
    except:
        font = ImageFont.load_default()
        author_font = ImageFont.load_default()

    # Word-wrap the quote
    wrapped_quote = textwrap.fill(quote, width=35)
    author_text = f"– {author}, {book}"

    # Calculate Y-position
    quote_bbox = draw.textbbox((0, 0), wrapped_quote, font=font)
    author_bbox = draw.textbbox((0, 0), author_text, font=author_font)

    total_height = (quote_bbox[3] - quote_bbox[1]) + (author_bbox[3] - author_bbox[1]) + 40
    y_start = (height - total_height) // 2

    # Draw text
    draw.text((80, y_start), wrapped_quote, font=font, fill=text_color)
    
    # Add extra line gap (~40px) below the quote
    author_y = y_start + (quote_bbox[3] - quote_bbox[1]) + 40
    draw.text((80, author_y), author_text, font=author_font, fill=text_color)


    image.save(output_path, format="PNG", optimize=True)
