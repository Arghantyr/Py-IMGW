from requests import get


HYDRO_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/hydro'
HYDRO2_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/hydro2'
DATA_OPTIONS=['json', 'xml', 'csv', 'html']
HYDRO_GROUPS=['hydro', 'hydro2']

class Hydro:
    def __init__(self):
        pass

    def get_all_stations(self,
                         data_format:str='json',
                         station_group:str='hydro'):
        try:
            assert data_format in DATA_OPTIONS
            assert station_group in HYDRO_GROUPS
            if station_group == 'hydro':
                base_url = HYDRO_GENERAL_URL
            elif station_group == 'hydro2':
                base_url = HYDRO2_GENERAL_URL

            result = get(f"{base_url}/format/{data_format}")

            return result._content, result.status_code
        except AssertionError:
            raise Exception("Invalid input")
        except Exception as e:
            raise Exception(f"{e}")
