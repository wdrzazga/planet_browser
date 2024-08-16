from planet import Planet


class PlanetRegistry:

    def __init__(self):
        mercury = Planet('Ma kury', 'Mercury is the smallest planet.', 'resources/images/Mercury.jpg')
        venus = Planet('Wenus', 'Venus is the hottest planet.', 'resources/images/Venus.jpg')
        earth = Planet('Earth', 'You are probably here.', 'resources/images/Earth.jpg', 1)
        mars = Planet('Mars', 'Robots took over Mars', 'resources/images/Mars.jpg', 2)
        jupiter = Planet('Jupiter', 'Jupiter is the biggest planet', 'resources/images/Jupiter.jpg', 92)
        saturn = Planet('Saturn', 'Saturn has the biggest rings', 'resources/images/Saturn.jpg', 83)
        uranus = Planet('Uranus', 'Uranus is rotated by approximately 89°', 'resources/images/Uranus.jpg', 27)
        neptune = Planet('Neptune', 'Neptune is the coldest planet', 'resources/images/Neptune.jpg', 14)
        self.planets = [mercury, venus, earth, mars, jupiter, saturn, uranus, neptune]
