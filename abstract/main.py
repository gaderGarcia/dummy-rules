from telcel_execution import TelcelController

telcelController = TelcelController()
features=telcelController.get_features()
rules = telcelController.get_rules()

for rule in rules:
    rule.execute(features)
    
print(telcelController.execute())