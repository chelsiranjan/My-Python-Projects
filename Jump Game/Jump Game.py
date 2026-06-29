import pygame
import random

pygame.init()

width, height = 1000 , 550
screen = pygame.display.set_mode((width, height))

background = pygame.image.load(r'C:\Users\Chelsi\Downloads\Super Mario Bros_ Level editor.jfif')
background = pygame.transform.scale(background, (width, height))

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

obstacle2_width = 25
obstacle2_height = 45
obstacle2_x = width + 400
obstacle2_y = ground_y - obstacle2_height
obstacle2_speed = 15


score_font = pygame.font.Font(None, 40)
game_over_font = pygame.font.Font(None, 110)
font = pygame.font.Font(None, 40)

score = 0

shake = False
shake_duration = 30
shake_timer = 0
shake_intensity = 5 

game_over = False

running = True
game_over = False
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if game_over and event.key == pygame.K_SPACE:
                running = False

        
    if not game_over:
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
        obstacle2_x -= obstacle2_speed  

        if obstacle_x < -obstacle_width:
            obstacle_x = width + random.randint(200,500)
            score +=1

        if obstacle2_x < -obstacle2_width:
            obstacle2_x = obstacle_x + random.randint(250,400)
            score +=1

        player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
        obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
        obstacle2_rect = pygame.Rect(obstacle2_x, obstacle2_y, obstacle2_width, obstacle2_height)
       

        if player_rect.colliderect(obstacle_rect):
            game_over = True
            shake = True
            shake_timer = shake_duration

        if player_rect.colliderect(obstacle2_rect):
            game_over = True
            shake = True
            shake_timer = shake_duration

    else:
        if shake_timer > 0:
            shake_timer -= 1
        else:
            shake = False
            game_over = True


    offset_x = 0
    offset_y = 0

    if shake:
        offset_x = random.randint(-shake_intensity, shake_intensity)
        offset_y = random.randint(-shake_intensity, shake_intensity)



    screen.fill((0, 0, 0))

    screen.blit(background, (offset_x, offset_y))


    pygame.draw.rect(screen,(0, 0, 255),(player_x, player_y,player_width, player_height))
    pygame.draw.rect(screen,(255, 0, 0),(obstacle_x, obstacle_y,obstacle_width, obstacle_height))
    pygame.draw.rect(screen,(200,0,0),(obstacle2_x, obstacle2_y, obstacle2_width, obstacle2_height))

    score_text = font.render(f'Score: {score}',True,(0, 0, 0))
    screen.blit(score_text, (20, 20))


    if game_over:
        game_over_text = game_over_font.render('GAME OVER',True,(0, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(width // 2, height // 2 - 40))
        screen.blit(game_over_text, game_over_rect)

        exit_text = font.render('PRESS SPACE TO EXIT', True, (0, 0, 0))
        exit_rect = exit_text.get_rect(center=(width // 2, height // 2 + 40))
        screen.blit(exit_text, exit_rect)



    pygame.display.update()
    clock.tick(60)

pygame.quit()