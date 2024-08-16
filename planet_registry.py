from planet import Planet


class PlanetRegistry:

    def __init__(self):
        mercury = Planet('Ma kury', 'Mercury is the smallest planet.', 'resources/images/Mercury.jpg')
        venus = Planet('Wenus', 'Venus is the hottest planet.', 'resources/images/Venus.jpg')
        earth = Planet('Earth', 'You are probably here.', 'resources/images/Earth.jpg')
        mars = Planet('Mars', 'Robots took over Mars', 'resources/images/Mars.jpg')
        jupiter = Planet('Jupiter', 'Jupiter is the biggest planet', 'resources/images/Jupiter.jpg')
        saturn = Planet('Saturn', 'Saturn has the biggest rings', 'resources/images/Saturn.jpg')
        uranus = Planet('Uranus', 'Uranus is rotated by approximately 89°', 'resources/images/Uranus.jpg')
        neptune = Planet('Neptune', 'Neptune is the coldest planet', 'resources/images/Neptune.jpg')
        self.planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
