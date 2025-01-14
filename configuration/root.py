from core.environment.environment import EnvironmentType
from configuration.project import PROJECT_NAME

ENVIRONMENT: EnvironmentType = EnvironmentType.DEVELOPMENT
DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"
