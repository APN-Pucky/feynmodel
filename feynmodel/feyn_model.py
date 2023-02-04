class FeynModel:
    def __init__(self, name=None):
        self.name = name
        self.particles = []
        self.vertices = []
        self.parameters = []

    def add_particle(self, particle):
        if particle not in self.particles:
            self.particles.append(particle)
        else:
            raise Exception("Particle %s already exists" % particle)

    def add_parameter(self, parameter):
        if parameter not in self.parameters:
            self.parameters.append(parameter)
        else:
            raise Exception("Parameter %s already exists" % parameter)

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices.append(vertex)
        else:
            raise Exception("Vertex %s already exists" % vertex)

    def get_particle(self, name=None, pdg_code=None):
        """Return particle with given name or pdg_code"""
        for particle in self.particles:
            matched = True
            if name is not None and particle.name != name:
                matched = False
            if pdg_code is not None and particle.pdg_code != pdg_code:
                matched = False
            if matched:
                return particle
        return None

    def get_parameter(self, name=None):
        """Return parameter with given name"""
        for parameter in self.parameters:
            if parameter.name == name:
                return parameter
        return None
