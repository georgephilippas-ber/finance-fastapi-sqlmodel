from typing import Dict, Optional, List

from abstract.adapter.adapter import Adapter
from schema.company.company import GICSSchema


class GICSAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[GICSSchema]:
        return GICSSchema(sector=json_['General']['GicSector'], industry=json_['General']['GicIndustry'],
                          industry_group=json_['General']['GicGroup'], sub_industry=json_['General']['GicSubIndustry'])

    def adapt_many(self, json_list_: List[Dict]) -> List[GICSSchema]:
        return [self.adapt(json_) for json_ in json_list_]
