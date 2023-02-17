from Populate import Populate
from Vec import Vec
from GNA import GNA
from WindowSingleton import WindowSingleton
from graphics import update as refresh
from time import time

position = Vec(0, 0, 0)
velocity = Vec(0, 0, 0)
tT = 0

epoch = 0  
gna = GNA(.005, 35, 350, Populate, 0.5, False)

def update():
    """ Will be called as many times as possible. """
    gna()

    return

def fixedUpdate():
    """ Will be called at most _FPS number of times per second. Put costly graphics operations in here. """
    refresh()

    return


if __name__ == '__main__':
    # DrawBG()
    WindowSingleton()

    timeSinceUpdate = time()
    _FPS = 30
    _SPF = 1/_FPS # seconds per frame refresh


    while True:
        update()

        if time() - timeSinceUpdate > _SPF:
            timeSinceUpdate = time()
            fixedUpdate()