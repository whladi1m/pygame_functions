import pygame
import sys

# Initialize PyGame
pygame.init()
print("PyGame initialized!")

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("PyGame Universal Button Example")
clock = pygame.time.Clock()

def draw_button(
    surface,
    rect,
    bg_color=None,
    border_radius=0,
    text=None,
    font_name=None,
    text_color=BLACK,
    image=None,
    hover_color=None,
    hover_text=None,
    mouse_pos=None,
):
    """
    Draws a button with optional styles (color, rounded, text, image, hover effect, and font adjustment).

    Parameters:
        surface (pygame.Surface): The surface to draw the button on.
        rect (pygame.Rect): The rectangle representing the button's position and size.
        bg_color (tuple): Background color of the button.
        border_radius (int): Corner radius for rounded buttons (0 = square corners).
        text (str): Text to display on the button.
        font_name (str): Font name for rendering the text (None for default font).
        text_color (tuple): Color of the text.
        image (pygame.Surface): Image to display on the button.
        hover_color (tuple): Color of the button when hovered.
        mouse_pos (tuple): The current mouse position for hover detection.
        hover_text (str): Text of the button when hovered.
    """
    is_hovered = mouse_pos and rect.collidepoint(mouse_pos)
    button_color = hover_color if is_hovered and hover_color else bg_color
    text_to_display = hover_text if is_hovered and hover_text else text

    # Draw button background (with optional rounded corners)
    if button_color:
        pygame.draw.rect(surface, button_color, rect, border_radius=border_radius)

    # Draw image if provided
    if image:
        image = pygame.transform.scale(image, (rect.width, rect.height))
        surface.blit(image, rect.topleft)

    # Draw text if provided
    if text_to_display:
        # Adjust font size to fit within the button rectangle
        adjusted_font = adjust_font_size_to_fit(text_to_display, font_name, rect)
        text_surface = adjusted_font.render(text_to_display, True, text_color)
        text_rect = text_surface.get_rect(center=rect.center)
        surface.blit(text_surface, text_rect)


def adjust_font_size_to_fit(
    text,
    font_name,
    rect,
    max_font_size=50,
    min_font_size=10
):
    """
    Adjusts the font size so the text fits within the given button rect.

    Parameters:
        text (str): The text to display on the button.
        font_name (str): The name of the font (e.g., "Arial" or None for the default PyGame font).
        rect (pygame.Rect): The rectangle representing the button dimensions.
        max_font_size (int): The maximum font size to start testing from.
        min_font_size (int): The minimum font size allowed.

    Returns:
        pygame.font.Font: A font object with the appropriate size.
    """
    for font_size in range(max_font_size, min_font_size - 1, -1):
        font = pygame.font.Font(font_name, font_size)
        text_width, text_height = font.size(text)

        # Check if the text fits within the button rect
        if text_width <= rect.width - 3 and text_height <= rect.height:
            return font

    # If no size fits, return the smallest font
    return pygame.font.Font(font_name, min_font_size)


# Main game loop
def main():
    # Load resources
    print("Loading resources...")

    # Try to load the image, handle missing image gracefully
    try:
        button_image = pygame.image.load("example_image.png")  # Replace with your image path
        print("Image loaded successfully!")
    except pygame.error as e:
        print(f"Error loading image: {e}")
        button_image = None  # Use None if the image is missing

    # Button styles
    button1_style = {
        "rect": pygame.Rect(50, 50, 200, 50),
        "bg_color": BLUE,
        "border_radius": 10,
        "text": "Long Text Here! sadadsaddsad",  # Text to test dynamic resizing
        "font_name": None,  # Default font
        "text_color": WHITE,
        "hover_color": GRAY,
        "hover_text": "Hover Text Buddy!",
    }
    button2_style = {
        "rect": pygame.Rect(50, 150, 200, 50),
        "bg_color": RED,
        "text": "Short Text",
        "font_name": None,
        "text_color": WHITE,
        "hover_color": GREEN,
    }
    button3_style = {
        "rect": pygame.Rect(50, 250, 200, 100),
        "image": button_image,
        "bg_color": GRAY if not button_image else None,  # Use background color if no image
        "hover_color": GRAY,
    }

    print("Starting the main game loop...")
    while True:
        screen.fill(WHITE)
        mouse_pos = pygame.mouse.get_pos()

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print("Exiting game...")
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # Left mouse button
                    if button1_style["rect"].collidepoint(mouse_pos):
                        print("Rounded button clicked!")
                    elif button2_style["rect"].collidepoint(mouse_pos):
                        print("Text button clicked!")
                    elif button3_style["rect"].collidepoint(mouse_pos):
                        print("Image button clicked!")

        # Draw buttons
        draw_button(screen, **button1_style, mouse_pos=mouse_pos)
        draw_button(screen, **button2_style, mouse_pos=mouse_pos)
        draw_button(screen, **button3_style, mouse_pos=mouse_pos)

        # Update the display
        pygame.display.flip()
        clock.tick(60)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        pygame.quit()
        sys.exit()
