from PIL import Image, ImageDraw, ImageFont

# Create a white background image
image_width, image_height = 220, 60
background_color = (255, 255, 255)  # White color
image = Image.new("RGB", (image_width, image_height), background_color)

# Create a drawing context
draw = ImageDraw.Draw(image)

# Add text to the image
text = """Made by:
Ashvath Suresh Babu Piriya (2162014)
Arun S Kurian (2162010)
Joel Mathew Pulluvelil (2160354)"""

text_color = (0, 0, 0)  # Black color
font = ImageFont.load_default()  # You can use a different font if desired
text_position = (1, 1)  # Adjust the position as needed
draw.text(text_position, text, fill=text_color, font=font)

# Save the image to a file
image.save('resources/texture_image.png')
