from Vec import Vec
from random import random
from WindowSingleton import hole_pos


def collide(pos, vel, dt):
    hit = False
    Nn = Vec(0, 0, 0)
    if pos.x <= -1.5:  # left wall
        Nn = Vec(1, 0, 0)
        hit = True
    if pos.x >= 1.5:  # right wall
        Nn = Vec(-1, 0, 0)
        hit = True
    if pos.y <= 0:  # bottom wall
        Nn = Vec(0, 1, 0)
        hit = True
    if pos.y >= 6:  # top wall
        Nn = Vec(0, -1, 0)
        hit = True

    if hit:
        pos -= vel * dt
        Nn.rotate((0.5-random())*0.004)
        speed_kept = 1-(0.2*abs(vel.normalize().dot(Nn))+0.004*random())
        vel += 2*(Nn*abs(vel.dot(Nn)))*speed_kept

    return (pos, vel)


def checkInHole(pos, vel):
    effective_radius = - (1/32) * vel.magnitude() + 0.05
    if (hole_pos - pos).magnitude() < effective_radius:
        return True
    return False


def tick(forces, mass, velocity, position, dt):
    if checkInHole(position, velocity):
        return (hole_pos, Vec(0, 0, 0))

    position, velocity = collide(position, velocity, dt)

    acceleration = forces / mass
    velocity += acceleration * dt
    position += velocity * dt

    return (position, velocity)
