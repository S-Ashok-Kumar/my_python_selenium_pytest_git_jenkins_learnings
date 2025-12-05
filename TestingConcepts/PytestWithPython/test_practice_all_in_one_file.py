import pytest


@pytest.fixture(scope="session")
def setup():
    print("[I will launch browser]")
    browser = 'Firefox'
    version = 20
    yield browser, version
    print("[I will close the browser]")


@pytest.mark.order(3)
@pytest.mark.sanity
@pytest.mark.regression
def test_kakathiya(setup):
    browser, version = setup
    print("I am from Kakathiya")
    print("Browser & Version used is: ", browser, version)


# @pytest.mark.skip
@pytest.mark.order(5)
@pytest.mark.regression
def test_tulasi(setup):
    print("I am from Tulasi")


@pytest.mark.order(1)
@pytest.mark.sanity
def test_victory(setup):
    print("I am from Victory")


# @pytest.mark.skip
@pytest.mark.order(4)
@pytest.mark.sanity
def test_aadersha(setup):
    print("I am from Aadersha")


@pytest.mark.order(2)
@pytest.mark.regression
def test_chaitanya(setup):
    print("I am from Chaitanya")
