from planet import Planet


class PlanetRegistry:

    def __init__(self):
        mercury = Planet('Ma kury', 'Merkury jest najmniejszą planetą.', 'images/Mercury.jpg')
        venus = Planet('Wenus', 'Wenus jest najgorętszą planetą.', 'images/Venus.jpg')
        self.planets = [mercury, venus]
