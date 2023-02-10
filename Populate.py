from Vec import Vec
import math
from random import gauss, random, uniform
from Engine import tick
from WindowSingleton import WindowSingleton, ppm, hole_pos
from Friction import Friction
from graphics import Circle, Point
from math import pi

class Populate:
    def __init__(self, velocity, friction, position=Vec(0, 0, 0), dt=.01, mass=.045):
        self.veli = velocity
        self.position = position
        self.dead = False
        self.velocity = velocity
        self.sphere = Circle(Point((3.5 + self.position.x) * ppm, (7 - self.position.y) * ppm), 0.045 * ppm)
        self.sphere.setFill("white")
        self.sphere.draw(WindowSingleton().instance())
        self.deltaV = 0
        self.deltaP = 0
        self.dt = dt
        self.friction = friction
        self.mass = mass
    
    @staticmethod
    def createNew(dt=.005):
        mass = 0.021335 # kg
        
        friction = Friction()
        return Populate(Vec(uniform(-5, 5), uniform(-5, 5), 0), friction, Vec(0, 0.2, 0), dt, mass=mass)

    @staticmethod
    def createFrom(populate, stdDev):
        x = gauss(populate.veli.x, stdDev)
        y = gauss(populate.veli.y, stdDev)

        return Populate(Vec(x, y, 0), populate.friction, Vec(0, 0.2, 0), populate.dt, populate.mass)

        
    def update(self):
        if self.dead:
            return

        forces = self.friction.get(self.velocity)
        p, v = tick(forces, self.mass, self.velocity, self.position, self.dt)
        self.velocity = v
        self.position = p
                
        if self.velocity.magnitude() <= 0.01:
            self.dead = True
            return True
        else: 
            return False
        
    def display(self):
        self.sphere.move(self.velocity.x * self.dt * ppm, self.velocity.y * self.dt * ppm * -1)
        
    def __call__(self):
        if self.dead:
            return
        
        died = self.update()
        self.display()
        return died
        
    def getScore(self):
        return (hole_pos - self.position).magnitude()

    def __del__(self):
        self.sphere.undraw()
