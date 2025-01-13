from typing import Dict, Optional, List

from abstract.adapter.adapter import Adapter
from schema.GICS.gics import GICSSchema


class GICSAdapter(Adapter):
    def __init__(self):
        super().__init__()

    def adapt(self, json_: Dict) -> Optional[GICSSchema]:
        return GICSSchema(sector=json_['Sector'].strip(), sector_id=json_['SectorId'],
                          industry=json_['Industry'].strip(),
                          industry_id=json_['IndustryId'],
                          industry_group=json_['IndustryGroup'].strip(), industry_group_id=json_['IndustryGroupId'],
                          sub_industry=json_['SubIndustry'].strip(), sub_industry_id=json_['SubIndustryId'])

    def adapt_many(self, json_list_: List[Dict]) -> List[GICSSchema]:
        return [self.adapt(json_) for json_ in json_list_]
