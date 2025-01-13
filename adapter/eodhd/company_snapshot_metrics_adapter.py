from typing import List, Dict, Optional

from abstract.adapter.adapter import Adapter
from schema.company.company import CompanySnapshotMetricsSchema


class CompanySnapshotMetricsAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[CompanySnapshotMetricsSchema]:
        pass

    def adapt_many(self, json_list_: List[Dict]) -> List[CompanySnapshotMetricsSchema]:
        pass
