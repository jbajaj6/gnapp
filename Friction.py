class Friction:
    def __init__(self):
        self.coeff = -0.015

    def get(self, vel):
        return vel*self.coeff