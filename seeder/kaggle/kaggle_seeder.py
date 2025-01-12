from adapter.kaggle.gics_adapter import GICSAdapter
from client.kaggle.kaggle_client import KaggleGICSClient
from manager.GICS.GICS_manager import GICSSectorManager, GICSIndustryGroupManager, GICSIndustryManager, \
    GICSSubIndustryManager


class KaggleSeeder:
    _kaggle_gics_adapter: GICSAdapter

    _gics_sector_manager: GICSSectorManager
    _gics_industry_group_manager: GICSIndustryGroupManager
    _gics_industry_manager: GICSIndustryManager
    _gics_sub_industry_manager: GICSSubIndustryManager

    def __init__(self, kaggle_gics_adapter: GICSAdapter, gics_sector_manager: GICSSectorManager,
                 gics_industry_group_manager: GICSIndustryGroupManager,
                 gics_industry_manager: GICSIndustryManager, gics_sub_industry_manager: GICSSubIndustryManager):
        self._kaggle_gics_adapter = kaggle_gics_adapter

        self._gics_sector_manager = gics_sector_manager
        self._gics_industry_group_manager = gics_industry_group_manager
        self._gics_industry_manager = gics_industry_manager
        self._gics_sub_industry_manager = gics_sub_industry_manager

    def seed_gics(self):
        print('SEEDING - GICS')

        gics_client_ = KaggleGICSClient('2023')

        for record_ in gics_client_.get_records():
            schema_ = self._kaggle_gics_adapter.adapt(record_)

            if schema_ is not None:
                sector_ = self._gics_sector_manager.persist(schema_)
                industry_group_ = self._gics_industry_group_manager.persist(schema_, {'sector_id': sector_.id})
                industry_ = self._gics_industry_manager.persist(schema_, {'industry_group_id': industry_group_.id,
                                                                          'sector_id': sector_.id})
                self._gics_sub_industry_manager.persist(schema_, {'industry_id': industry_.id, 'sector_id': sector_.id,
                                                                  'industry_group_id': industry_group_.id})
