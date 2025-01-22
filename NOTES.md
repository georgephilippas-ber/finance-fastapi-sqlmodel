### TODO

* **Concurrency**
    * Currently relying on a synchronous _SQLAlchemy_ engine shared among requests. Optimally, this needs to be an
      `AsyncEngine`
      shared
      across all application services managed exclusively by `asyncio`.
    * Subsequently, all SQLAlchemy-based database calls are blocking. Scalability concerns without advanced `asyncio`
      functionality must be addressed using horizontal scaling means i.e. connections, processes, machines.
    * Celery is in _eager mode_ when it comes to running AI models in independent workers. Further configuration
      required to bypass the _GIL_.
* **Search**
    * Currently, all search criteria are **AND** logically connected. 
