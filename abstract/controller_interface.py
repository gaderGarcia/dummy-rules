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
    def get_fraud_score(self)->int:
        pass

    @final
    def execute(self)->str:
        if self.preExecute() == False:
            raise Exception("Features or Rules are empty")
        
        #Method that AO will implement to add the logic they require
        self.execute_logic()

        #Validation post AO logic to review if we need more steps to execute
        return self.postExecute()       
    
    @abstractmethod
    def execute_logic(self)->int:
        """ This method execute the logic of the order of the rules
        The rules should already complete the work to populate the values
        Returns:
            int: fraud probability score
        """
        pass      
    
    def preExecute(self)->bool:
        return len(self.get_features()) >0 and len(self.get_rules())>0 
    
    @abstractmethod
    def postExecute(self)->str:
        #No other Controller or Execution Plan is required
        #If we want anothe execution plan then we pass the class
        #TelcelControllerB
        return ""
    