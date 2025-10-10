from PIL import Image, ImageDraw, ImageFont

def text_to_handwriting(text, output_file="handwriting.png"):
    # Create a blank white canvas
    img = Image.new("RGB", (800, 1000), "white")
    draw = ImageDraw.Draw(img)

    # Load a handwriting-style font (you can download your favorite handwriting TTF font)
    try:
        font = ImageFont.truetype("Segoe Script.ttf", 24)  # Windows example
    except:
        font = ImageFont.load_default()

    # Draw the text
    draw.multiline_text((50, 50), text, fill=(0, 0, 0), font=font, spacing=10)

    # Save image
    img.save(output_file)
    print(f"[✓] Handwriting saved as {output_file}")

if __name__ == "__main__":
    text = """
    1.1 INTRODUCTION
    The programming language 'C' was developed in the early 1970s by Dennis Ritchie at Bell Laboratories.
    Although C was initially developed for writing system software, today it has become such a popular 
    language that a variety of software programs are written using this language.
    """
    text_to_handwriting(text)
