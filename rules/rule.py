import random
#rule.py
def calculate_score(customer:str)->int:
    """ calculate_score function
    Parameters:
    - customer: order.entityInfo.global.customer.name
    Returns:
    - score:int """
        
    lenght = len(customer)
    random_score=random.randrange(11)
    score = random_score - lenght
    if score < 0:
        return 0
    return score

def calculate_pi(param1: int, param2: str) -> float:
    """ This is a function
    Parameters:
    - param1: order.entityInfo.global.nuData.score
    - param2: order.entityInfo.global.eKata.IdentityRiskScoreIsNull

    Returns:
    - float: This function returns a float.  """    
    return 3.14

def report_success(job:object, connection:object, result:object,*args:object, **kwargs:object)->None:
    print(f"SUCCESS JOB, The value is: {result}")
    
def report_failure(job:object, connection:object, type:object, value:object, traceback:object)->None:
    print(f"Job Failed due to: {traceback}")