from abc import ABC, abstractmethod
from typing import Union

class IFeature(ABC):
    # {
    #     "attributeName": "consumerPaymentInstrument.entityInfo.global.billingAddressDigest",
    #     "value": str | int | float | bool
    # }    
    @abstractmethod
    def get_attribute_name(self)->str:
        return self.attribute_name
    
    
    @abstractmethod
    def get_value(self)->Union[str,int,float,bool]:
        return self.value