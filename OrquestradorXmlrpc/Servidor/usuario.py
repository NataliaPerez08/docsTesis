class Usuario:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.private_networks = list()

    def __str__(self):
        return "Name: " + self.name

    def add_private_network(self, private_network):
        self.private_networks.append(private_network)

    def remove_private_network(self, private_network):
        self.private_networks.remove(private_network)

    def get_private_networks(self):
        return self.private_networks

    def get_private_network(self, private_network_id):
        for private_network in self.private_networks:
            if private_network.id == private_network_id:
                return private_network
        return None

    def add_private_network(self, private_network):
        self.private_networks.append(private_network)

    def get_num_private_networks(self):
        return len(self.private_networks)