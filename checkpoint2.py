#Josiah Uwanaka Jr
#Checkpoint 2
import gamebox, pygame, random
scale = 1.2
camera = gamebox.Camera(int(450*scale),int(300*scale)) #540x360
boundary = camera.y + 100
background = gamebox.from_image(camera.x,camera.y,"80115706-pixel-art-game-background-with-ground-grass-sky-and-clouds-.jpg")
background.scale_by(scale)
asteroids = []
health = 50
defender = gamebox.from_color(camera.x, camera.y + 105,'red',30,30)
fps = 60 #frames per second
tracker = 0
speed = 1
def tick(keys):
    global tracker, asteroids,defender,boundary, health, speed
    camera.clear('white')
    tracker += 1
    score = tracker/fps
    game_score = int(score)
    camera.draw(background)
    if (score*speed % 1) == 0:
        new = gamebox.from_circle(random.randint(50,515), camera.y - 180, 'grey', 20)
        asteroids.append(new)
    if score % 20 == 0:
        speed += 1
    if pygame.K_RIGHT in keys:
            defender.x += 5
    if pygame.K_LEFT in keys:
        defender.x -= 5
    if defender.x > camera.right:
        defender.x = camera.right
    if defender.x < camera.left:
        defender.x = camera.left
    camera.draw(defender)
    for asteroid in asteroids:
        if asteroid.touches(defender):
            asteroids.remove(asteroid)
        if asteroid.y >= camera.y + 100:
            health -= 1
            asteroids.remove(asteroid)
        asteroid.y += speed
        camera.draw(asteroid)
    
    healthbar = gamebox.from_text(60,15,"Health: " + str(health), 30,'black')
    scoreboard = gamebox.from_text(60,35,"Time: " + str(game_score), 30,'black')
    camera.draw(healthbar)
    camera.draw(scoreboard)
    camera.display()
gamebox.timer_loop(fps, tick)
"""
so my general code works and I have changed up a few things. Instead of clicking on the atseroids, I am just going to make the defender
go across the screen and touch the asteroids. I am in the process for loooking for images for my defender and asteroids so I just made them
shapes for the time being. I am not sure why but after some time running, my code crashes mentioning something about their not being an 
asteroid to remove from the asteroid list even though they are still being made so I have to fix that. Other than that I just need to add the
restart button and collectible items for the game. But I want to make the game go faster in increments but keep the rate of asteroids droping 
the same.
"""