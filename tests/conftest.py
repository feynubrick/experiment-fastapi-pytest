from fastapi.testclient import TestClient
import pytest

from main import app
from utils.logger import logger


@pytest.fixture(scope="session")
def client():
    logger.debug("[fixture] client: ARRANGE")
    return TestClient(app)
