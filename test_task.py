from task import CityInfo

def test_can_parse_city_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Zagreb")
    ci = CityInfo()

    city_name = ci.get_city_name()

    assert city_name == "Zagreb"


def test_can_get_city_info():
    city_name = "Zagreb"
    ci = CityInfo()

    city_info = ci.get_city_info(city_name)

    assert city_info["code"] == 200


def test_cant_get_city_info_bc_city_name():
    city_name = "dsdsds"
    ci = CityInfo()

    city_info = ci.get_city_info(city_name)

    assert city_info["code"] == 400


def test_can_get_city_temperature():
    city_name = "Zagreb"
    ci = CityInfo()

    city_temp = ci.get_city_temperature(city_name)

    assert city_temp["code"] == 200


def test_cant_get_city_temperature_bc_city_name():
    city_name = "dfdfdfd"
    ci = CityInfo()

    city_temp = ci.get_city_temperature(city_name)

    assert city_temp["code"] == '404'


def test_cant_get_city_temperature_bc_api_key(monkeypatch):
    city_name = "Zagreb"
    monkeypatch.setenv('API_KEY', "123")
    ci = CityInfo()

    city_temp = ci.get_city_temperature(city_name)

    assert city_temp["code"] == 401

