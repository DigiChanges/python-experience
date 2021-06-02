    
class ForbiddenException(Exception):
    def __init__(self):
        self.name = "You do not have the access permissions."
