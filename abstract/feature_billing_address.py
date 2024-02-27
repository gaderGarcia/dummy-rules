from feature_interface import IFeature

class FeatureBillingAddress(IFeature):
    def __init__(self,value):
        self.attribute_name="consumerPaymentInstrument.entityInfo.global.billingAddressDigest"
        self.value=value
    
    def get_value(self) -> str | int | float | bool:
        return self.value
    
    def get_attribute_name(self) -> str:
        return self.attribute_name