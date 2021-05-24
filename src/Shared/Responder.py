from dataclasses import dataclass
from injector import inject


@inject
@dataclass
class Responder():
    def send(self):
        print ("Responder")
        return 'Responder'