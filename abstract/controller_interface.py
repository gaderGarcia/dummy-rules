from abc import ABC, abstractmethod
from typing import List, Type, final
from feature_interface import IFeature
from rule_interface import IRule

class IController(ABC):
    
    @abstractmethod
    def get_features(self)->List[Type[IFeature]]:
        pass
    
    @abstractmethod
    def get_rules(self)->List[Type[IRule]]:
        pass
    
    @abstractmethod
    def execute_logic(self)->int:
        """ This method execute the logic of the order of the rules
        The rules should already complete the work to populate the values
        Returns:
            int: fraud probability score
        """
        pass
    
    @final
    def execute(self):
        if self.preExecute() == False:
            raise Exception("Features or Rules are empty")
        self.execute_logic()
    
    def preExecute(self)->bool:
        return len(self.get_features()) >0 and len(self.get_rules())>0 
    
    def postExecute(self)->bool:
        return True
    