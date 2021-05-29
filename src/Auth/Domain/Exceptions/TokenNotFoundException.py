    
class TokenNotFoundException(Exception):
    def __init__(self):
        self.name = "Token not found."

