### TODO

* **Concurrency**
    * Currently relying on a synchronous _SQLAlchemy_ engine shared among requests. This needs to be an AsyncEngine
      shared
      across all application services managed exclusively by `asyncio`.
    * Celery is working in _eager mode_ when it comes to running AI models in independent workers.
* **Search**
    * Currently, all search criteria are **AND**. 
