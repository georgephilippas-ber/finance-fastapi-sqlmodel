from abstract.adapter.adapter import Adapter
from typing import List, Dict
from datetime import date

class EndOfDayChangeOverview(Adapter):
    def __init__(self, ):
        super().__init__()

    def adapt(self, json_: List[Dict]) -> Dict:
        first_ = json_[0]
        latest_ = json_[-1]
        dates_ = map(lambda json_:  date.fromisoformat(json_['date']), json_)

