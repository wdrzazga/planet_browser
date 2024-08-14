from planet import Planet


class PlanetRegistry:

    def __init__(self):
        mercury = Planet('Ma kury', 'Mercury is the smallest planet.', 'resources/images/Mercury.jpg')
        venus = Planet('Wenus', 'Venus is the hottest planet.', 'resources/images/Venus.jpg')
        earth = Planet('Earth', 'You are probably here.', 'resources/images/Earth.jpg')
        mars = Planet('Mars', 'Robots took over Mars', 'resources/images/Mars.jpg')
        self.planets = [mercury, venus, earth, mars]
