import pygame
import random

pygame.init()

width, height = 800, 550
screen = pygame.display.set_mode((width, height))

background = pygame.image.load(r'C:\Users\Chelsi\Downloads\Super Mario Bros_ Level editor.jfif')
background = pygame.transform.scale(background, (width, height))

#player = pygame.image.load(r'')
#obstacle = pygame.image.load(r'')

ground_y = 460

player_x = 100
player_width = 50
player_height = 50
player_y = ground_y - player_height

velocity_y = 0
gravity = 0.8
jump_power = -15
on_ground = True

obstacle_width = 30
obstacle_height = 50
obstacle_x = width
obstacle_y = ground_y - obstacle_height
obstacle_speed = 15

font = pygame.font.Font(None, 40)

score = 0

running = True
game_over = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and on_ground:
        velocity_y = jump_power
        on_ground = False

    velocity_y += gravity

    player_y += velocity_y

    if player_y + player_height >= ground_y:
        player_y = ground_y - player_height
        velcity_y = 0
        on_ground = True


    obstacle_x -= obstacle_speed

    if obstacle_x < -obstacle_width:
        obstacle_x = width + random.randint(200,500)
        score +=1

    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)

    if player_rect.colliderect(obstacle_rect):
        game_over = True


    screen.blit(background, (0, 0))


    pygame.draw.rect(screen,(0, 0, 255),(player_x, player_y,player_width, player_height))
    pygame.draw.rect(screen,(255, 0, 0),(obstacle_x, obstacle_y,obstacle_width, obstacle_height))

    score_text = font.render(f'Score: {score}',True,(0, 0, 0))
    screen.blit(score_text, (20, 20))




    pygame.display.update()
    clock.tick(60)

pygame.quit()