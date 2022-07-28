#Josiah Uwanaka Jr
#Final Project
import gamebox, pygame, random
scale = 1.2
camera = gamebox.Camera(int(450*scale),int(300*scale)) #540x360
boundary = camera.y + 100
defender_image = "character-removebg-preview.png"
asteroid_image = "asteroid.png"
background = gamebox.from_image(camera.x,camera.y,"80115706-pixel-art-game-background-with-ground-grass-sky-and-clouds-.jpg")
background.scale_by(scale)
asteroids = []
health_help_image = 'health_help.png'
health_helps = []
health = 50
defender = gamebox.from_image(camera.x, camera.y + 80,defender_image)
defender.scale_by(.25)
fps = 60 #frames per second
tracker = 0
speed = 1
safe = True
def convert(seconds): # got this conversion formula from https://www.geeksforgeeks.org/python-program-to-convert-seconds-into-hours-minutes-and-seconds/
    seconds = seconds % (24 * 3600)
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
      
    return "%02d:%02d" % (minutes, seconds)
def tick(keys):
    """ this is the overall function of the game:
        - last for 100 seconds without running out of health to win
        - move from side to side to touch the asteroids before they hit the ground and lower your health
        - health helpers will drop as hearts to add +5 health at random
        - the droppage speed will increase in increments as well

    Args:
        keys (keys): use the left and right arrow key to move the character from side to side
    """
    global tracker, asteroid_image, asteroids,defender,boundary, health, speed, asteroid_image, safe, health_helps, health_help_image
    if safe:
        camera.clear('white')
        tracker -= 1/fps
        score = tracker + 99
        game_score = int(score)
        camera.draw(background)
        if (score*speed % 1) == 0:
            new = gamebox.from_image(random.randint(50,515), camera.y - 180, asteroid_image)
            new.scale_by(0.15)
            asteroids.append(new)
        if (score*speed % 20) == 0:
            helper = gamebox.from_image(random.randint(50,515), camera.y - 180, health_help_image)
            helper.scale_by(0.05)
            health_helps.append(helper)
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
            camera.draw(asteroid)
        for asteroid in asteroids:
            if asteroid.y >= camera.y + 102:
                health -= 1
                asteroids.remove(asteroid)
            asteroid.y += speed
            camera.draw(asteroid)
        for saver in health_helps:
            if saver.touches(defender):
                health += 5
                health_helps.remove(saver)
                camera.draw(saver)
        for healer in health_helps:
            if healer.y >= camera.y + 102:
                health_helps.remove(healer)
            healer.y += speed
            camera.draw(healer)
        healthbar = gamebox.from_text(camera.left + 50,camera.bottom - 15,"Health: " + str(health), 20,'red')
        #scoreboard = gamebox.from_text(camera.right - 80,camera.bottom - 15,"Time Remaining: " + str(score), 20,'red')
        scoreboard = gamebox.from_text(camera.right - 80,camera.bottom - 15,"Time Remaining: " + str(convert(game_score)), 20,'red')
        camera.draw(healthbar)
        camera.draw(scoreboard)
        if health == 0:
            safe = False
            game_over = gamebox.from_text(camera.x,camera.y,"Oh Noo...Earth Has Been Destroyed!!",35,'red')
            camera.draw(game_over)
            camera.display()
        if game_score == 0:
            safe = False
            win = gamebox.from_text(camera.x,camera.y,"Hooray!! Earth Is Safe",50,'black')
            camera.draw(win)
            camera.display()
    camera.display()
gamebox.timer_loop(fps, tick)