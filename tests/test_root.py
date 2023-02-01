from fastapi.testclient import TestClient
from utils.logger import logger


def test_root(client: TestClient):
    res = client.get("/")
    logger.debug(f"res.status_code: {res.status_code}")
    logger.debug(f"res.headers: {res.headers}")
    logger.debug(f"res.json(): {res.json()}")
    assert res.status_code == 200
