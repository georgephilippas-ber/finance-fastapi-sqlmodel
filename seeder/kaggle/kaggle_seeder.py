from adapter.kaggle.gics_adapter import GICSAdapter
from client.kaggle.kaggle_client import KaggleGICSClient
from manager.GICS.GICS_manager import GICSSectorManager, GICSIndustryGroupManager, GICSIndustryManager


class KaggleSeeder:
    _kaggle_gics_adapter: GICSAdapter

    _gics_sector_manager: GICSSectorManager
    _gics_industry_group_manager: GICSIndustryGroupManager
    _gics_industry_manager: GICSIndustryManager
    _gics_sub_industry_manager: GICSIndustryManager

    def __init__(self, kaggle_gics_adapter: GICSAdapter, gics_sector_manager: GICSSectorManager,
                 gics_industry_group_manager: GICSIndustryGroupManager,
                 gics_industry_manager: GICSIndustryManager, gics_sub_industry_manager: GICSIndustryManager):
        self._kaggle_gics_adapter = kaggle_gics_adapter

        self._gics_sector_manager = gics_sector_manager
        self._gics_industry_group_manager = gics_industry_group_manager
        self._gics_industry_manager = gics_industry_manager
        self._gics_sub_industry_manager = gics_sub_industry_manager

    def seed_gics(self):
        gics_client_ = KaggleGICSClient('2023')

        for record_ in gics_client_.get_records():
            schema_ = self._kaggle_gics_adapter.adapt(record_)

            if schema_ is not None:
                self._gics_sector_manager.persist()