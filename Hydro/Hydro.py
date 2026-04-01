from datetime import timedelta
from ratelimit import limits, sleep_and_retry
from requests import get


HYDRO_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/hydro'
HYDRO2_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/hydro2'
DATA_OPTIONS=['json', 'xml', 'csv', 'html']
HYDRO_GROUPS=['hydro', 'hydro2']
DATA_REFRESH_PERIOD=10*60

class Hydro:
    def __init__(self):
        pass
    
    @sleep_and_retry
    @limits(calls=10, period=timedelta(seconds=DATA_REFRESH_PERIOD).total_seconds())
    def get_all_stations(self,
                         data_format:str='json',
                         station_group:str='hydro'):
        try:
            if data_format not in DATA_OPTIONS:
                raise Exception("Invalid data type.")
            
            if station_group not in HYDRO_GROUPS:
                raise Exception("Invalid station group")


            if station_group == 'hydro':
                base_url = HYDRO_GENERAL_URL
            elif station_group == 'hydro2':
                base_url = HYDRO2_GENERAL_URL

            result = get(f"{base_url}/format/{data_format}")

            return result._content, result.status_code

        except Exception as e:
            raise Exception(f"{e}")
