from typing import Optional, Dict

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

    def persist(self, schema: GICSSchema, foreign_keys: Optional[Dict] = None) -> Optional[GICSSector]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.name = schema.sector

            self._session.flush()
            return existing_

        sector_ = GICSSector(name=schema.sector)

        try:
            self._session.add(sector_)
            self._session.flush()
            return sector_
        except Exception as e:
            print(e)

            self._session.rollback()
            return None

    def by_id(self, id_: int) -> Optional[GICSSector]:
        query_ = select(GICSSector).where(GICSSector.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSSector]:
        query_ = select(GICSSector).where(GICSSector.name == name)

        return self._session.exec(query_).first()


class GICSIndustryGroupManager(Manager):
    _sector_manager: GICSSectorManager

    def __init__(self, session: Session, sector_manager: GICSSectorManager):
        super().__init__(session)

        self._sector_manager = sector_manager

    def retrieve_unique(self, schema: GICSSchema) -> Optional[GICSIndustryGroup]:
        query_ = select(GICSIndustryGroup).where(GICSIndustryGroup.name == schema.industry_group)

        return self._session.exec(query_).first()

    def persist(self, schema: GICSSchema, foreign_keys: Optional[dict] = None) -> Optional[GICSIndustryGroup]:
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.name = schema.industry_group

            self._session.flush()
            return existing_

        industry_group_ = GICSIndustryGroup(name=schema.industry_group, sector_id=foreign_keys['sector_id'])

        try:
            self._session.add(industry_group_)
            self._session.flush()

            return industry_group_
        except Exception as e:
            print(e)

            self._session.rollback()
            return None

    def by_id(self, id_: int) -> Optional[GICSIndustryGroup]:
        query_ = select(GICSIndustryGroup).where(GICSIndustryGroup.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSIndustryGroup]:
        query_ = select(GICSIndustryGroup).where(GICSIndustryGroup.name == name)

        return self._session.exec(query_).first()


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
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.name = schema.industry

            self._session.flush()
            return existing_

        industry_ = GICSIndustry(name=schema.industry, sector_id=foreign_keys['sector_id'],
                                 industry_group_id=foreign_keys['industry_group_id'])

        try:
            self._session.add(industry_)
            self._session.flush()

            return industry_
        except Exception as e:
            print(e)

            self._session.rollback()
            return None

    def by_id(self, id_: int) -> Optional[GICSIndustry]:
        query_ = select(GICSIndustry).where(GICSIndustry.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSIndustry]:
        query_ = select(GICSIndustry).where(GICSIndustry.name == name)

        return self._session.exec(query_).first()


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
        existing_ = self.retrieve_unique(schema)

        if existing_ is not None:
            existing_.name = schema.sub_industry

            self._session.flush()
            return existing_

        sub_industry_ = GICSSubIndustry(name=schema.sub_industry, sector_id=foreign_keys['sector_id'],
                                        industry_group_id=foreign_keys['industry_group_id'],
                                        industry_id=foreign_keys['industry_id'])

        try:
            self._session.add(sub_industry_)
            self._session.flush()

            return sub_industry_
        except Exception as e:
            print(e)

            self._session.rollback()
            return None

    def by_id(self, id_: int) -> Optional[GICSSubIndustry]:
        query_ = select(GICSSubIndustry).where(GICSSubIndustry.id == id_)

        return self._session.exec(query_).first()

    def by_name(self, name: str) -> Optional[GICSSubIndustry]:
        query_ = select(GICSSubIndustry).where(GICSSubIndustry.name == name)

        return self._session.exec(query_).first()


if __name__ == "__main__":
    pass
