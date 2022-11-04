from task2 import CityInfo

def test_can_parse_city_name(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: "Zagreb")
    ci = CityInfo()

    city_name = ci.get_city_name()

    assert city_name == "Zagreb"

def test_can_get_city_info():
    city_name = "Zagreb"
    ci = CityInfo()




def test_can_get_city_temperature():
    city_name = "Zagreb"
    ci = CityInfo()

    

def test_can_write_to_file():
    pass
