from requests import get


METEO_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/meteo'
DATA_OPTIONS=['json', 'xml', 'csv', 'html']

class Meteo:
    def __init__(self):
        pass

    def get_all_stations(self,
                         data_format:str='json'):
        try:
            assert data_format in DATA_OPTIONS
            result = get(f"{METEO_GENERAL_URL}/format/{data_format}")
            return result._content, result.status_code
        except AssertionError:
            raise Exception("Invalid input")
        except Exception as e:
            raise Exception(f"{e}")
