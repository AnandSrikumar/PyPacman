import pygame
import sys

def display_text_in_fonts(screen, fonts):
    # Define the text and its position
    text = "Anand making game"
    y_pos = 50
    
    # Draw the text using different fonts
    for font_name in fonts:
        font = pygame.font.SysFont(font_name, 36)
        text_surface = font.render(text, True, (0, 0, 0))  # Black color
        screen.blit(text_surface, (50, y_pos))
        y_pos += 50  # Move down for the next font

def main():
    # Initialize Pygame
    pygame.init()
    
    # Set up the display
    screen_width, screen_height = 800, 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Pygame Fonts Display')
    
    # List of 10 font names to display
    fonts = [
        'arial', 'couriernew', 'timesnewroman', 'verdana', 'calibri', 'comic sans ms',
        'georgia', 'impact', 'helvetica', 'trebuchet ms'
    ]
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        # Clear the screen
        screen.fill((255, 255, 255))  # White background
        
        # Display text in different fonts
        display_text_in_fonts(screen, fonts)
        
        # Update the display
        pygame.display.flip()

if __name__ == "__main__":
    main()
