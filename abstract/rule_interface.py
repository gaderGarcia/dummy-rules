from abc import ABC, abstractmethod
from typing import List, Type, Union

from feature_interface import IFeature

class IRule(ABC):
    
    @abstractmethod
    def execute(self, features:List[Type[IFeature]]):
        """maybe this should be an object containing
        key-Feature as value
        {
            "identifierName":Feature Object,
        }
        Because it will be easy for the developer
        to pull the feature based on a key that 
        he already set and know in this code.
        """
        pass
    
    @abstractmethod
    def get_result(self)->Union[float, int, bool]:
        pass