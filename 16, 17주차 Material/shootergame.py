from simgame import *
import time
window = GameWindow("Shoot!", 800, 800, "white")
character = GameImage("char.png", 400, 400)

hp = 5
hp_text = GameText(hp, 700, 50, "red", 40)

a = 0
enemies = []
def gameloop():
    global a, enemies, hp
    hp_text.set_text(hp)
    if time.time() - a > 2:
        a = time.time()
        pos = window.get_random_edge()
        enemy = GameImage("enemy.png", pos[0], pos[1])
        enemies.append(enemy)
    for e in enemies:
        d = window.get_direction(e, character)
        e.move(d[0] * 7, d[1] * 7)
        dist = window.get_distance(e, character)
        if dist < 50:
            e.delete()
            enemies.remove(e)
            hp -= 1
    for b in bullets:
        if b.dir == "left":
            move = [-30, 0]
        elif b.dir == "right":
            move = [30, 0]
        elif b.dir == "up":
            move = [0, -30]
        elif b.dir == "down":
            move = [0, 30]
        b.move(move[0], move[1])
        if b.is_outside():
            b.delete()
            bullets.remove(b)

shoot_dir = "left"
def move_left():
    global shoot_dir
    shoot_dir = "left"
    character.move(-50, 0)
def move_right():
    global shoot_dir
    shoot_dir = "right"
    character.move(50, 0)
def move_up():
    global shoot_dir
    shoot_dir = "up"
    character.move(0, -50)
def move_down():
    global shoot_dir
    shoot_dir = "down"
    character.move(0, 50)

bullets = []
def shoot():
    global character, shoot_dir, bullets
    pos = character.get_position()
    bullet = GameImage("bullet.png", pos[0], pos[1])
    bullet.dir = shoot_dir
    bullets.append(bullet)
    
window.link("<Left>", move_left)
window.link("<Right>", move_right)
window.link("<Up>", move_up)
window.link("<Down>", move_down)
window.link("z", shoot)

window.start_loop(gameloop, 0.1)

