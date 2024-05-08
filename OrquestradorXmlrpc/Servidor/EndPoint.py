class Endpoint:
    def __init__(self, identificador, ):
        self.identificador = identificador
        self.ip_wireguard = ""
        self.ip_publico = ""

    def get_identificador(self):
        return self.identificador
    
    def get_ip_wireguard(self):
        return self.ip_wireguard
    
    def get_ip_publico(self):
        return self.ip_publico
    
    def set_ip_wireguard(self, ip_wireguard):
        self.ip_wireguard = ip_wireguard

    def set_ip_publico(self, ip_publico):
        self.ip_publico = ip_publico