from logging import error
from typing import Optional, Tuple

from celery import Celery
from celery.signals import worker_process_init

from configuration.environment import ENVIRONMENT
from configuration.project import PROJECT_NAME
from core.ai.ai import LargeLanguageModel
from core.environment.environment import EnvironmentType

celery = Celery(PROJECT_NAME, broker="memory://")

if ENVIRONMENT == EnvironmentType.DEVELOPMENT:
    celery.conf.task_always_eager = True
    celery.conf.task_eager_propagates = True
    celery.conf.task_store_eager_result = True

large_language_moder_worker_instance: Optional[LargeLanguageModel] = LargeLanguageModel()


@worker_process_init.connect
def init_worker(**kwargs):
    error("Initializing worker...")
    error(kwargs)

    global large_language_moder_worker_instance
    large_language_moder_worker_instance = LargeLanguageModel()


@celery.task
def infer(query: str) -> Tuple[str, float]:
    global large_language_moder_worker_instance

    return large_language_moder_worker_instance.query(query)
