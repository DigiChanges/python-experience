    
class UserDisabledException(Exception):
    def __init__(self):
        self.name = "Your user is disable."

