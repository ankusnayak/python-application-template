from enum import Enum
import os


class Environment(str, Enum):
    LOCAL = "local"
    STAGING = "staging"
    PROD = "prod"


def get_env() -> Environment:
    return Environment(os.getenv("ENV", Environment.LOCAL))
