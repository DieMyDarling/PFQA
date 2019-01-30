import pytest
from fixture.application import Application

fixture = None


@pytest.fixture
def app(request):
    global fixture
    if fixture is None:
        fixture = Application()
    else:
        if not fixture.is_valid():
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def app(request):
    global fixture
    browser = request.config.getoption("--browser")
    baseurl = request.config.getoption("--baseurl")
    if fixture is None:
        fixture = Application(browser=browser, baseurl=baseurl)
    else:
        if not fixture.is_valid():
            fixture = Application(browser=browser, baseurl=baseurl)
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="Firefox")
    parser.addoption("--baseurl", action="store", default="http://localhost/addressbook/")
