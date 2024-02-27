from rule_interface import IRule
from feature_interface import IFeature
from feature_billing_address import FeatureBillingAddress
from rule_address import RuleAddress
from controller_interface import IController
from typing import List, Type

class TelcelController(IController):
    def __init__(self) -> None:
        self.features=[]
        self.rules:List[Type[IRule]] = []
        
    def get_features(self) -> List[type[IFeature]]:
        feature_A = FeatureBillingAddress("portland")
        feature_B = FeatureBillingAddress("atlanta")
        self.features.append(feature_A)
        self.features.append(feature_B)
        return self.features
    
    def get_rules(self) -> List[type[IRule]]:
        rule1= RuleAddress()
        rule2= RuleAddress() 
        self.rules.append(rule1)
        self.rules.append(rule2)
        return self.rules
    
    def execute(self) -> int:
        total = 0
        for rule in self.rules:
            total += rule.get_result()          
        return total