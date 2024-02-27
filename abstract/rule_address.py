from typing import List, Type
from feature_interface import IFeature
from rule_interface import IRule

class RuleAddress(IRule):
    def __init__(self) -> None:
        self.value = 0
    
    def execute(self, features: List[type[IFeature]]):
        self.value = len(features[0].get_value())
        
    def get_result(self) -> float | int | bool | str:
        return self.value
        