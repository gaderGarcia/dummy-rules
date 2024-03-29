from pydantic import BaseModel
from abc import ABC,abstractmethod

class IStageIterator(ABC):
    @abstractmethod
    def __iter__(self):
        return self

    @abstractmethod
    def __next__(self):
        raise StopIteration

    @abstractmethod
    def get_remaining_stages(self):
        return []

class IController(ABC):

    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def getStageIterator(self, startingStage, transaction) -> IStageIterator:
        pass

    @abstractmethod
    def execute(self, transaction, transaction_meta_data):
        pass

class TransactionEvaluation(BaseModel):
    preAuth: dict | None = None
    postAuth: dict | None = None
    oneStepPostAuth: dict | None = None

class Controller(IController):
    def __init__(self, transaction) -> None:
        pass

    def execute(self, transaction:BaseModel, meta_data: dict):
        print(f"Something to print:{transaction.transactionId}, metadata:{meta_data}")
        if transaction.transactionEvaluation is None:
            transaction.transactionEvaluation = TransactionEvaluation()
        if transaction.transactionEvaluation.oneStepPostAuth is None:
            transaction.transactionEvaluation.oneStepPostAuth = dict()
        
        transaction.transactionEvaluation.oneStepPostAuth["score"] = 88

    def getStageIterator(self, startingStage, transaction) -> IStageIterator:
        pass

# class Controller:
#     def execute(self, transaction:BaseModel, meta_data: dict):
#         print(f"Something to print:{transaction.transactionId}, metadata:{meta_data}")
#         transaction.transactionEvaluation.oneStepPostAuth["score"] = 88