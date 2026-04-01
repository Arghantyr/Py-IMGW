from requests import get
from datetime import timedelta
from ratelimit import limits, sleep_and_retry

SYNOP_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/synop'
DATA_OPTIONS=['json', 'xml', 'csv', 'html']
DATA_REFRESH_PERIOD=10*60

class Synop:
    def __init__(self):
        pass
    
    @sleep_and_retry
    @limits(calls=100, period=timedelta(seconds=DATA_REFRESH_PERIOD).total_seconds())
    def get_station_by_id(self,
                          data_format:str='json',
                          station_id:int=None):
        try:
            if data_format not in DATA_OPTIONS:
                raise Exception("Invalid data format.")

            SYNOP_URL=f'https://danepubliczne.imgw.pl/api/data/synop/id/{station_id}/format/{data_format}'
            result = get(SYNOP_URL)
            return result._content, result.status_code

        except Exception as e:
            raise Exception(f"{e}")

    @sleep_and_retry
    @limits(calls=100, period=timedelta(seconds=DATA_REFRESH_PERIOD).total_seconds())
    def get_station_by_name(self,
                            station_name:str=None,
                            data_format:str='json'):
        try:
            if data_format not in DATA_OPTIONS:
                raise Exception("Invalid data format.")
            if not station_name.isalnum():
                raise Exception("Invalid station name.")

            SYNOP_URL=f'https://danepubliczne.imgw.pl/api/data/synop/station/{station_name}/format/{data_format}'
            result = get(SYNOP_URL)

            return result._content, result.status_code

        except Exception as e:
            raise Exception(f"{e}")
    
    @sleep_and_retry
    @limits(calls=100, period=timedelta(seconds=DATA_REFRESH_PERIOD).total_seconds())
    def get_all_stations(self,
                         data_format:str='json'):
        try:
            if data_format not in DATA_OPTIONS:
                raise Exception("Invalid data format.")

            result = get(f"{SYNOP_GENERAL_URL}/format/{data_format}")

            return result._content, result.status_code

        except Exception as e:
            raise Exception(f"{e}")
