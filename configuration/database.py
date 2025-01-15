from configuration.project import PROJECT_NAME

DATABASE_URL: str = f"mysql://root:development@localhost:3306/{PROJECT_NAME.replace('-', '_')}"
