class FeynModel:
    def __init__(self, name=None):
        self.name = name
        self.particles = []
        self.vertices = []
        self.parameters = []
        self.lorentz = []
        self.couplings = []
        self.orders = []
        self.functions = []
        self.decays = []

    def add_particle(self, particle):
        if particle not in self.particles:
            self.particles.append(particle)
        else:
            raise Exception("Particle %s already exists" % particle)

    def add_decay(self, decay):
        if decay not in self.decays:
            self.decays.append(decay)
        else:
            raise Exception("Decay %s already exists" % decay)

    def add_function(self, function):
        if function not in self.functions:
            self.functions.append(function)
        else:
            raise Exception("Function %s already exists" % function)

    def add_order(self, order):
        if order not in self.orders:
            self.orders.append(order)
        else:
            raise Exception("Order %s already exists" % order)

    def add_parameter(self, parameter):
        if parameter not in self.parameters:
            self.parameters.append(parameter)
        else:
            raise Exception("Parameter %s already exists" % parameter)

    def add_coupling(self, coupling):
        if coupling not in self.couplings:
            self.couplings.append(coupling)
        else:
            raise Exception("Coupling %s already exists" % coupling)

    def add_lorentz(self, lorentz):
        if lorentz not in self.lorentz:
            self.lorentz.append(lorentz)
        else:
            raise Exception("Lorentz %s already exists" % lorentz)

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

    def get_lorentz(self, name=None):
        """Return lorentz with given name"""
        for lorentz in self.lorentz:
            if lorentz.name == name:
                return lorentz
        return None

    def get_coupling(self, name=None):
        """Return coupling with given name"""
        for coupling in self.couplings:
            if coupling.name == name:
                return coupling
        return None
