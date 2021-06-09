    
class RoleDisabledException(Exception):
    def __init__(self):
        self.name = "Your role is disable."

