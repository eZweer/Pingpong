import sys
import pygame
import random

# Window size
x = 1000
y = 650

# Recket size
racket_width = 100
racket_height = 15

racket_x = x / 2
racket_y = y - 60

#ball siiz
ball_x = int(x / 2)
ball_y = int(y / 2)
ball_radius = 15

#ball speed
ball_speed_x = 1
ball_speed_y = -2

# other global variable
live = 0
speed = 0
go_faster = 0
counter = 0

def main ():
    global counter, ball_x, ball_y , racket_x, racket_y
    pygame.init()
    
    # create Window
    font = pygame.font.Font('freesansbold.ttf', 32)
    pygame.display.set_caption('Ping Pong')
    screen = pygame.display.set_mode([x, y])
    screen.fill((0, 0, 0))
    
    #Create ball and racked
    pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius, 0)
    pygame.draw.rect(screen, (255, 40, 0), (racket_x, racket_y, racket_width, racket_height), 0)
    
    pygame.display.flip()
    
    
    def racket_block():
        # Stop Racked on screen edge
        global speed
        if racket_x <= 0 or racket_x >= x - racket_width:
            speed = 0


    def ball_movement():
        # movement of the ball
        global ball_x, ball_y
        ball_x += ball_speed_x
        ball_y += ball_speed_y
        
    def racket_movement():
        # movment of the recket
        global racket_x
        racket_x += speed    


    def reset():
        global live, ball_speed_x, ball_speed_y, ball_x, ball_y, speed, racket_y, racket_x , go_faster
        # reset x and y of Racked 
        racket_x = x / 2
        racket_y = y - 50

        # reset x and y of ball
        ball_x = int(x / 2)
        ball_y = int(y / 2)

        #reset speed
        speed = 0

        # ball get random start speed
        ball_speed_x = random.randint(-2 , 2)
        if ball_speed_x == 0:
            ball_speed_x = 1
        if ball_x < 0:
            ball_speed_x - go_faster
        else:
            ball_speed_x + go_faster

        ball_speed_y = random.randint(-2, 2)
        if ball_speed_y == 0:
            ball_speed_y = 1
        if ball_x < 0:
            ball_speed_y - go_faster
        else:
            ball_speed_y + go_faster
            
        screen.fill((0, 0, 0))
        
        # recreate ball and racket
        pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius, 0)
        pygame.draw.rect(screen, (255, 40, 0), (racket_x, racket_y, racket_width, racket_height), 0)
        pygame.display.flip()
        pygame.time.wait(1000)


    def ballblock():
        global ball_speed_x, ball_speed_y, live, counter
        # Stop Racked on screen edge
        if ball_x - ball_radius <= 0:
            ball_speed_x *= -1
        if ball_y - ball_radius <= 0:
            ball_speed_y *= -1
        if ball_x + ball_radius >= x:
            ball_speed_x *= -1
        #Change ball direction if Rachet is touched
        if ball_y >= y-55 and ball_y <= y - 50:
            if ball_x >= racket_x - 5 and ball_x <= racket_x + racket_width:
                ball_speed_y *= -1
                counter += 1    
            else:
                live -= 1
                reset()


    

    def start():
            global speed, live , ball_speed_x , ball_speed_y, go_faster, go_faster
            live = 3
            #start game loop as long as there are still lives left
            while live > 0:
                #set keys
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_LEFT:
                            speed = -2 - go_faster
                        if event.key == pygame.K_RIGHT:
                            speed = 2 + go_faster
                # increase speed every 10 points        
                if counter % 10 == 0 and counter != 0:
                    go_faster += 1
                    if ball_speed_x > 0:
                        ball_speed_x +=1
                    else:
                        ball_speed_x += -1
                    if ball_speed_y > 0:
                        ball_speed_y += 1
                    else:
                        ball_speed_y += -1

                screen.fill((0, 0, 0))
                
                
                racket_movement()
                racket_block()
                
                ball_movement()
                ballblock()
                
               
                
                # show live on upper left side
                show_live = font.render("Live: "+str(live), True, (0, 255, 0))
                show_liveRect = show_live.get_rect()
                show_liveRect.center = (x - (x-60), y - (y-20))
                screen.blit(show_live, show_liveRect)
                
                # show Points on bottom left side
                show_points = font.render("Points: "+str(counter), True, (0, 255, 0))
                show_pointsRect = show_points.get_rect()
                show_pointsRect.center = (x - 100, y - 20)
                screen.blit(show_points, show_pointsRect)
                
                pygame.draw.rect(screen, (255, 40, 0), (racket_x, racket_y, racket_width, racket_height), 0)
                pygame.draw.circle(screen, (255, 255, 0), (ball_x, ball_y), ball_radius, 0)
                pygame.display.flip()
                pygame.time.wait(5)
            else:
                pygame.quit()
    #start game            
    start()
    
if __name__ == "__main__":
    main()