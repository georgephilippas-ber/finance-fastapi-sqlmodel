from typing import Optional

from sqlmodel import Session, select

from abstract.manager.manager import Manager
from model.GICS.GICS import GICSSector, GICSIndustryGroup, GICSIndustry, GICSSubIndustry
from schema.company.company import GICSSchema


class GICSSectorManager(Manager):
    def __init__(self, session: Session):
        super().__init__(session)

    def retrieve_unique(self, schema: GICSSchema) -> Optional[GICSSector]:
        query_ = select(GICSSector).where(GICSSector.name == schema.sector)

        return self._session.exec(query_).first()

    def persist(self, schema: GICSSchema, foreign_keys: Optional[dict] = None) -> Optional[GICSSector]:
        pass

    def by_id(self, id_: str) -> Optional[GICSSector]:
        query_ = select(GICSSector).where(GICSSector.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSSector]:
        query_ = select(GICSSector).where(GICSSector.name == name)

        return self._session.exec(query_).first()

    def delete_all(self):
        query_ = select(GICSSector)
        query_results_ = self._session.exec(query_)

        for query_result_ in query_results_:
            self._session.delete(query_result_)

        self._session.commit()


class GICSIndustryGroupManager(Manager):
    _sector_manager: GICSSectorManager

    def __init__(self, session: Session, sector_manager: GICSSectorManager):
        super().__init__(session)

        self._sector_manager = sector_manager

    def retrieve_unique(self, schema: GICSSchema) -> Optional[GICSIndustryGroup]:
        query_ = select(GICSIndustryGroup).where(GICSIndustryGroup.name == schema.industry_group)

        return self._session.exec(query_).first()

    def persist(self, schema: GICSSchema, foreign_keys: Optional[dict] = None) -> Optional[GICSIndustryGroup]:
        pass

    def by_id(self, id_: str) -> Optional[GICSIndustryGroup]:
        query_ = select(GICSIndustryGroup).where(GICSIndustryGroup.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSIndustryGroup]:
        query_ = select(GICSIndustryGroup).where(GICSIndustryGroup.name == name)

        return self._session.exec(query_).first()

    def delete_all(self):
        query_ = select(GICSIndustryGroup)
        query_results_ = self._session.exec(query_)

        for query_result_ in query_results_:
            self._session.delete(query_result_)

        self._session.commit()


class GICSIndustryManager(Manager):
    _sector_manager: GICSSectorManager
    _industry_group_manager: GICSIndustryGroupManager

    def __init__(self, session: Session, sector_manager: GICSSectorManager,
                 industry_group_manager: GICSIndustryGroupManager):
        super().__init__(session)

        self._sector_manager = sector_manager
        self._industry_group_manager = industry_group_manager

    def retrieve_unique(self, schema: GICSSchema) -> Optional[GICSIndustry]:
        query_ = select(GICSIndustry).where(GICSIndustry.name == schema.industry)

        return self._session.exec(query_).first()

    def persist(self, schema: GICSSchema, foreign_keys: Optional[dict] = None) -> Optional[GICSIndustry]:
        pass

    def by_id(self, id_: str) -> Optional[GICSIndustry]:
        query_ = select(GICSIndustry).where(GICSIndustry.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSIndustry]:
        query_ = select(GICSIndustry).where(GICSIndustry.name == name)

        return self._session.exec(query_).first()

    def delete_all(self):
        query_ = select(GICSIndustry)
        query_results_ = self._session.exec(query_)

        for query_result_ in query_results_:
            self._session.delete(query_result_)

        self._session.commit()


class GICSSubIndustryManager(Manager):
    _sector_manager: GICSSectorManager
    _industry_group_manager: GICSIndustryGroupManager
    _industry_manager: GICSIndustryManager

    def __init__(self, session: Session, sector_manager: GICSSectorManager,
                 industry_group_manager: GICSIndustryGroupManager, industry_manager: GICSIndustryManager):
        super().__init__(session)

        self._session = session

        self._sector_manager = sector_manager
        self._industry_group_manager = industry_group_manager
        self._industry_manager = industry_manager

    def retrieve_unique(self, schema: GICSSchema) -> Optional[GICSSubIndustry]:
        query_ = select(GICSSubIndustry).where(GICSSubIndustry.name == schema.sub_industry)

        return self._session.exec(query_).first()

    def persist(self, schema: GICSSchema, foreign_keys: Optional[dict] = None) -> Optional[GICSSubIndustry]:
        pass

    def by_id(self, id_: str) -> Optional[GICSSubIndustry]:
        query_ = select(GICSSubIndustry).where(GICSSubIndustry.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSSubIndustry]:
        query_ = select(GICSSubIndustry).where(GICSSubIndustry.name == name)

        return self._session.exec(query_).first()

    def delete_all(self):
        query_ = select(GICSSubIndustry)
        query_results_ = self._session.exec(query_)

        for query_result_ in query_results_:
            self._session.delete(query_result_)

        self._session.commit()


if __name__ == "__main__":
    pass
