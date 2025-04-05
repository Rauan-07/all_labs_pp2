import pygame

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("button with words")

pygame.mixer.music.load("c:/Users/kadae/Desktop/python/all_labs_pp2/lab7/music/NewJeans - ASAP.mp3")  
pygame.mixer.music.play(-1)  


WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

font = pygame.font.Font(None, 40)

text1 = "button1"
text2 = "button2"

button1 = pygame.Rect(150, 150, 150, 50)
button2 = pygame.Rect(300, 150, 150, 50)

running = True
while running:
    screen.fill(WHITE)

    pygame.draw.rect(screen, BLUE, button1)
    pygame.draw.rect(screen, RED, button2)

    text1_render = font.render(text1, True, WHITE)
    text2_render = font.render(text2, True, WHITE)
    
    screen.blit(text1_render, (button1.x + 20, button1.y + 10))
    screen.blit(text2_render, (button2.x + 20, button2.y + 10))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if button1.collidepoint(event.pos):
                text2 = "ararara"
            elif button2.collidepoint(event.pos):
                text1 = "gagagaagag"

pygame.quit()
