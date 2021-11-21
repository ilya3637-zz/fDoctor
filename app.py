import datetime
import pytest
import requests


@pytest.fixture(name="current_weather")
def fixture_get_current():
    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q=moscow,ru&appid=4b0791ca8007dc606da2eb4b73137e59")
    return response


@pytest.fixture(name="historical_5_days")
def fixture_get_historical():
    five_days_ago = datetime.date.today() - datetime.timedelta(hours=119)
    unix_time = five_days_ago.strftime("%s")
    response = requests.get("http://api.openweathermap.org/data/2.5/onecall/timemachine?lat=55.7558&lon=37.6173&dt=" + unix_time + "&appid=4b0791ca8007dc606da2eb4b73137e59")
    return response


def test_1(current_weather):
    assert current_weather.status_code == 200, "Вернулся некорректный код для current weather"
    assert current_weather.json(), "Вернулся некорректный json для current weather"


def test_2(historical_5_days):
    assert historical_5_days.status_code == 200, "Вернулся некорректный код для historical 5 days"
    assert historical_5_days.json(), "Вернулся некорректный json для historical 5 days"