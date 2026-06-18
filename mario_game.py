import tkinter as tk
import random
WIDTH, HEIGHT = 900, 650
root = tk.Tk()
root.title("Rectangle Adventure Deluxe")
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="darkgreen")
canvas.pack()

player = canvas.create_rectangle(40, 40, 70, 70, fill="blue")

health = 100
score = 0
has_gun = False
has_key = False

# Walls
walls = [
    canvas.create_rectangle(300, 100, 500, 130, fill="gray"),
    canvas.create_rectangle(150, 300, 180, 500, fill="gray"),
    canvas.create_rectangle(550, 250, 750, 280, fill="gray")
]

# Items
gun_item = canvas.create_rectangle(120, 120, 145, 145, fill="yellow")
medkit_item = canvas.create_rectangle(600, 100, 625, 125, fill="pink")
treasure_item = canvas.create_rectangle(700, 500, 725, 525, fill="gold")
key_item = canvas.create_rectangle(500, 500, 525, 525, fill="orange")

# Exit door
exit_door = canvas.create_rectangle(820, 560, 870, 620, fill="brown")

# Enemies
enemies = []
for i in range(9):
    x = random.randint(100, 750)
    y = random.randint(100, 550)
    enemy = canvas.create_rectangle(x, y, x + 30, y + 30, fill="red")
    enemies.append(enemy)

# Boss
boss = canvas.create_rectangle(700, 200, 760, 260, fill="purple")

bullets = []

info = tk.Label(root, text="Health:100   Score:0")
info.pack()


def touching(a, b):
    ax1, ay1, ax2, ay2 = canvas.coords(a)
    bx1, by1, bx2, by2 = canvas.coords(b)

    return ax2 > bx1 and ax1 < bx2 and ay2 > by1 and ay1 < by2


def move(event):
    global has_gun, has_key, health, score

    dx = 0
    dy = 0

    if event.keysym == "Left":
        dx = -10
    elif event.keysym == "Right":
        dx = 10
    elif event.keysym == "Up":
        dy = -10
    elif event.keysym == "Down":
        dy = 10

    canvas.move(player, dx, dy)

    # Stop player from walking through walls
    for wall in walls:
        if touching(player, wall):
            canvas.move(player, -dx, -dy)

    # Pick up gun
    if canvas.type(gun_item) and touching(player, gun_item):
        has_gun = True
        canvas.delete(gun_item)

    # Pick up medkit
    if canvas.type(medkit_item) and touching(player, medkit_item):
        health = min(100, health + 30)
        canvas.delete(medkit_item)

    # Treasure
    if canvas.type(treasure_item) and touching(player, treasure_item):
        score += 100
        canvas.delete(treasure_item)

    # Key
    if canvas.type(key_item) and touching(player, key_item):
        has_key = True
        canvas.delete(key_item)

    # Win
    if has_key and touching(player, exit_door):
        root.title("YOU WIN!")


def shoot(event):
    if not has_gun:
        return

    x1, y1, x2, y2 = canvas.coords(player)

    bullet = canvas.create_rectangle(
        x2,
        (y1 + y2) / 2 - 2,
        x2 + 12,
        (y1 + y2) / 2 + 2,
        fill="white"
    )

    bullets.append(bullet)


def update():
    global health, score

    # Enemy movement
    for enemy in enemies:
        ex1, ey1, ex2, ey2 = canvas.coords(enemy)
        px1, py1, px2, py2 = canvas.coords(player)

        if ex1 < px1:
            canvas.move(enemy, 2, 0)
        else:
            canvas.move(enemy, -2, 0)

        if ey1 < py1:
            canvas.move(enemy, 0, 2)
        else:
            canvas.move(enemy, 0, -2)

        if touching(player, enemy):
            health -= 1

    # Boss damage
    if canvas.type(boss) and touching(player, boss):
        health -= 2

    # Bullets
    for bullet in bullets[:]:
        canvas.move(bullet, 15, 0)

        # Enemy hit
        for enemy in enemies[:]:
            if touching(bullet, enemy):
                canvas.delete(enemy)
                enemies.remove(enemy)
                canvas.delete(bullet)
                bullets.remove(bullet)
                score += 10
                break

        # Boss hit
        if canvas.type(boss) and touching(bullet, boss):
            canvas.delete(boss)
            score += 200

    info.config(text=f"Health:{health}   Score:{score}")

    if health <= 0:
        root.title("GAME OVER")

    root.after(30, update)


root.bind("<Key>", move)
root.bind("<space>", shoot)

update()
root.mainloop()






