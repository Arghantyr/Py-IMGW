from requests import get


METEO_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/meteo'
DATA_OPTIONS=['json', 'xml', 'csv', 'html']


class Meteo:
    def __init__(self):
        pass

    def get_all_stations(self,
                         data_format:str='json'):
        try:
            if data_format not in DATA_OPTIONS:
                raise Exception("Invalid data format")

            result = get(f"{METEO_GENERAL_URL}/format/{data_format}")
            return result._content, result.status_code

        except Exception as e:
            raise Exception(f"{e}")
