from abc import ABC, abstractmethod

class IPagination(ABC):

     @abstractmethod
     def getLimit(self) -> int:
          pass

     @abstractmethod
     def getOffset(self) -> int:
          pass

     @abstractmethod
     def getCurrentUrl(self) -> str:
          pass

     @abstractmethod
     def getNextUrl(self) -> str:
          pass

     @abstractmethod
     def getExist(self) -> bool:
          pass
