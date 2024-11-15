from pydantic import BaseModel

class Controller:
    def __init__(self, BaseModel) -> None:
        pass

    def execute(self, transaction:BaseModel, meta_data: dict):
        print(f"Something to print:{transaction.transactionId}, metadata:{meta_data}")
        transaction.transactionEvaluation.oneStepPostAuth["score"] = 88