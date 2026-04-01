from requests import get
from datetime import timedelta
from ratelimit import limits, sleep_and_retry

METEO_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/meteo'
DATA_OPTIONS=['json', 'xml', 'csv', 'html']
DATA_REFRESH_PERIOD=10*60


class Meteo:
    def __init__(self):
        pass
    
    @sleep_and_retry
    @limits(calls=10, period=timedelta(seconds=DATA_REFRESH_PERIOD).total_seconds())
    def get_all_stations(self,
                         data_format:str='json'):
        try:
            if data_format not in DATA_OPTIONS:
                raise Exception("Invalid data format")

            result = get(f"{METEO_GENERAL_URL}/format/{data_format}")
            return result._content, result.status_code

        except Exception as e:
            raise Exception(f"{e}")
