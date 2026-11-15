from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

player = FirstPersonController()
player.speed = 5
player.cursor.color = color.white
player.camera_pivot.y = 1.5

Music = Audio("alphamusic.mp3", loop=True, AutoPlay=True)

for x in range(20):
    for y in range(1):
        for z in range(20):
            ground = Entity(model="cube", texture="alphagrass", position=(x, y, z), collider="mesh", scale=(1, 1, 1))



def input(key):
    if key == "right mouse down":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="alphagrass", position=pos, collider="box")
            Audio("grasskik.mp3", loop=False, AutoPlay=False)

    if key == "left mouse down":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            destroy(hit.entity)

    if key == "2":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            stone2 = Entity(model="cube", texture="stone2", position=pos, collider="box")
            Audio("stonekik.mp3", loop=False, AutoPlay=False)

    if key == "1":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            stone1 = Entity(model="cube", texture="alphastone", position=pos, collider="box")
            Audio("stonekik.mp3", loop=False, AutoPlay=False)

    if key == "3":
        hit = raycast(camera.world_position, camera.forward, distance=5)
        if hit.entity:
            pos = hit.entity.position + hit.normal
            Entity(model="cube", texture="brick", position=pos, collider="box")
            Audio("stonekik.mp3", loop=False, AutoPlay=False)

    

sky = Sky()
sky.color = color.gray
            
            
        
        
                

app.run()
