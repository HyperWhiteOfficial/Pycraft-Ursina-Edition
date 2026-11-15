from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from ursina.shaders import lit_with_shadows_shader
import sys
import time

app = Ursina()

hand = Entity(parent=camera.ui, model="cube", color=color.orange,
              position=(0.75, -0.6, 0), scale=(0.16, 0.16, 1.7), rotation=(25, 5, -50))
player = FirstPersonController(y=2)
player.cursor.color = color.white
menumusic = Audio("assets/musics/moogcity2.mp3", AutoPlay=True, loop=True)

def Start_Game():
    player.enabled = True,
    hand.enabled = True,
    destroy(StartButton),
    destroy(ExutButton),
    destroy(menubackground)
    music = Audio("assets/musics/ariamath.mp3", autoplay=True, loop=True, volume=0.3)
    destroy(menumusic)

def Exit_Game():
    application.quit()

def Close_INV():
        destroy(inven)
        player.enabled = True
        exb.enabled = False

def IN_MM():
    application.quit()

def In_Game():
    player.enabled = True
    GameB.enabled = False
    InMainMenu.enabled = False
        



player.enabled = False
hand.enabled = False
menubackground = Entity(parent=camera.ui, model="quad", texture="assets/images/grassmenu3.png", scale=(2, 2))
Text = Entity(parent=camera.ui, text="Minecraft", y=0.2, origin=(0, 0), scale=(0.13, 0.13), color=color.white)
StartButton = Button(parent=camera.ui, text="Играть", y=0, scale=(0.13, 0.13), on_click=Start_Game, enabled=True)
ExutButton = Button(parent=camera.ui, text="Выйти", y=-0.2, scale=(0.13, 0.13), on_click=Exit_Game, enabled=True)


ground = Entity(model="plane", texture="grass", collider="box", scale=(1000, 5, 1000))

inven = Entity(parent=camera.ui, model="quad", scale=(1, 0.50), color=color.black, enabled=False)
exb = Button(parent=camera.ui, text="X", scale=(0.07, 0.07), color=color.red, position=(0.46, 0.30, 0.30), on_click=Close_INV, enabled = False)



Entity.default_shader = lit_with_shadows_shader

player.camera_pivot.y = 1.5
player.speed = 5
player.gravity = 1
SIZE = 15


world_parent = Entity()
for x in range(SIZE):
    for z in range(SIZE):
        for y in range(5):
            Entity(model="cube", texture="assets/images/grass2.png", collider="box", position=(x, y, z))

world_parent.combine()

world_collider = Entity(model=None, collider='box',
                        position=(SIZE/2 - 0.5, 0.5, SIZE/2 - 0.5),
                        scale=(SIZE, 2, SIZE))


#Кнопки выхода:
InMainMenu = Button(parent=camera.ui, text="В Главное меню", scale=(0.13, 0.13), position=(0.20, 0.15, 0.50), enabled=False, on_click=IN_MM)
GameB = Button(parent=camera.ui, text="Продолжить", scale=(0.13, 0.13), position=(0.20, 0.30, 0.50), enabled=False, on_click=In_Game)



slot3 = Entity(parent=camera.ui, model="quad", texture="assets/images/bedrock.png", position=(0.01, -0.4, 0.1), scale=(0.07, 0.07, 0.07))
slot4 = Entity(parent=camera.ui, model="quad", texture="assets/images/stone2.png", position=(0.09, -0.4, 0.1), scale=(0.07, 0.07, 0.07))
slot5 = Entity(parent=camera.ui, model="quad", texture="assets/images/d.png", position=(0.17, -0.4, 0.1), scale=(0.07, 0.07, 0.07))
slot2 = Entity(parent=camera.ui, model="quad", texture="assets/images/brick.png", position=(-0.07, -0.4, 0.1), scale=(0.07, 0.07, 0.07))
slot1 = Entity(parent=camera.ui, model="quad", texture="assets/images/stone.png", position=(-0.15, -0.4, 0.1), scale=(0.07, 0.07, 0.07))
slot0 = Entity(parent=camera.ui, model="quad", texture="assets/images/grass2.png", position=(-0.23, -0.4, 0.1), scale=(0.07, 0.07, 0.07))
slot6 = Entity(parent=camera.ui, model="quad", texture="assets/images/d2.png", position=(0.25, -0.4, 0.1), scale=(0.07, 0.07, 0.07))


def input(key):
    if key == "shift":
        player.speed = 30

    if key == "alt":
        player.speed = 5

    if key == "1":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="assets/images/grass2.png" ,collider="box", position=pos)
            Audio("assets/musics/grasskik.mp3", AutoPlay=False, loop=False)
            
    if key == "5":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="assets/images/stone2.png", collider="box", position=pos)
            Audio("assets/musics/Stonekik.mp3", AutoPlay=False, loop=False)

    if key == "6":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="assets/images/d.png", collider="box", position=pos)
            Audio("assets/musics/woodkik.mp3", AutoPlay=False, loop=False)

    if key == "left mouse down":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity and hit.entity != ground and hit.entity != menubackground:
            destroy(hit.entity)

    if key == "7":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="assets/images/d2.png", collider="box", position=pos)
            Audio("assets/musics/woodkik.mp3", AutoPlay=False, loop=False)

    if key == "2":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="stone", collider="box", position=pos)
            Audio("assets/musics/Stonekik.mp3", AutoPlay=False, loop=False)

    if key == "3":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="assets/images/brick.png", collider="box", position=pos)
            Audio("assets/musics/Stonekik.mp3", AutoPlay=False, loop=False)

    if key == "4":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            bedrock = Entity(model="cube", texture="assets/images/bedrock.png", collider="box", position=pos)
            Audio("assets/musics/Stonekik.mp3", AutoPlay=False, loop=False)

    if key == "f":
        if player.gravity == 0:
            player.gravity = 1
        else:
            player.gravity = 0

    if key == "e":
        if not inven.enabled:
            inven.enabled = True
            mouse.locked = False
            player.enabled = False
        else:
            inven.enabled = False
            mouse.locked = True
            player.enabled = True

    if key == "escape":
        if not InMainMenu.enabled:
            InMainMenu.enabled = True
            GameB.enabled = True
            player.enabled = False
        else:
            InMainMenu.enabled = False
            GameB.enabled = False
            player.enabled = True

            
            
           
sky = Sky()

app.run()



 
