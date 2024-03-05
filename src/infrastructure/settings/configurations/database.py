from pydantic import PostgresDsn, BaseModel


class DatabaseConfiguration(BaseModel):
    """Настрйки конфигурации базы данной"""
    user: str
    password: str
    host: str
    port: int
    name: str
    engine: str

    @property
    def dsn(cls):
        login = f"{cls.user}:{cls.password}"
        ip_port = f"{cls.host}:{cls.port}"

        if cls.engine.startswith("postgresql"):
            return PostgresDsn(f"{cls.engine}://{login}@{ip_port}/{cls.name}")
        elif cls.engine.startswith("sqlite"):
            return f"{cls.engine}:///{cls.name}.db"
        else:
            return f"{cls.engine}://{login}@{ip_port}/{cls.name}"
        
    @property
    def sync_dsn(cls):
        return f"postgresql://" \
               f"{cls.user}:" \
               f"{cls.password}@" \
               f"{cls.host}:" \
               f"{cls.port}/" \
               f"{cls.name}"
