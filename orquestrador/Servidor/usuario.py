class Usuario:
    def __init__(self, nombre,contra):
        self.nombre = nombre
        self.contra = contra
        self.endpoints = []
        self.subred = None # 

    def __str__(self):
        return f"Usuario {self.nombre} con {len(self.endpoints)} endpoints"
    
    def agregar_endpoint(self, endpoint):
        self.endpoints.append(endpoint)

    def eliminar_endpoint(self, endpoint):
        self.endpoints.remove(endpoint)

    def recuperar_endpoints(self):
        return self.endpoints

    