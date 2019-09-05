import os
import pytest
import threading
import logging

RLOCK = threading.RLock()

def pytest_addoption(parser):
    parser.addoption("--env", action = "store", default = 'test', help = "The environment where the test should run: test/staging/production")


@pytest.fixture(autouse = True)
def collect_information(request):
        with RLOCK:
                run_info = {"environment": "test"}
                os.environ["DEBUSSY"] = request.config.getoption('--env')