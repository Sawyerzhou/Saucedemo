import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from utils.read_data import get_config


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="prod", help="Environment: dev, staging, prod")


@pytest.fixture(scope="session")
def config(request):
    env = request.config.getoption("--env")
    cfg = get_config()
    # 根据 env 覆盖 base_url
    if env in cfg.get("environments", {}):
        cfg["base_url"] = cfg["environments"][env]["base_url"]
    return cfg


@pytest.fixture(scope="function")
def driver(config):
    browser = config.get("browser", "chrome")
    if browser == "chrome":
        driver = webdriver.Chrome(service=Service(r"E:\tools\chromedriver.exe"))
    elif browser == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(r"E:\tools\geckodriver.exe"))
    elif browser == "edge":
        driver = webdriver.Edge(service=EdgeService(r"E:\tools\msedgedriver.exe"))
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    driver.maximize_window()
    driver.get(config["base_url"])
    yield driver
    driver.quit()


def pytest_runtest_makereport(item, call):
    # 仅在测试失败且是执行阶段时处理
    if call.when == "call" and call.excinfo is not None:
        # 获取测试函数中的 driver fixture 实例
        driver = item.funcargs.get("driver", None)
        if driver:
            screenshot = driver.get_screenshot_as_png()
            allure.attach(
                screenshot,
                name="screenshot_on_failure",
                attachment_type=allure.attachment_type.PNG
            )