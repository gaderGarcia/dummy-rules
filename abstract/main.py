from telcel_execution import TelcelController

telcelController = TelcelController()

#Here we can use the FeatureMetadata to extract
# and mapping the values from the objects
features=telcelController.get_features()
#Call the FeatureMetadata to extract data from source
#we can run this in parallel too?

#Here the parallel process to get the process
rules = telcelController.get_rules()
for rule in rules:
    rule.execute(features)
    
print(f"TelcelController requires another step: {telcelController.execute()}")
print(f"The result of TelcelController is: {telcelController.get_fraud_score()}")