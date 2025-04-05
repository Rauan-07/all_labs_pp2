import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Moving Rectangle")

rect_x, rect_y = 400, 300
rect_width, rect_height = 50, 30
speed = 20

running = True
while running:
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP] and rect_y - speed >= 0:
        rect_y -= speed
    if keys[pygame.K_DOWN] and rect_y + rect_height + speed <= 600:
        rect_y += speed
    if keys[pygame.K_LEFT] and rect_x - speed >= 0:
        rect_x -= speed
    if keys[pygame.K_RIGHT] and rect_x + rect_width + speed <= 800:
        rect_x += speed
    
    screen.fill('White')
    pygame.draw.rect(screen, 'Blue', (rect_x, rect_y, rect_width, rect_height))
    pygame.display.update()

pygame.quit()
