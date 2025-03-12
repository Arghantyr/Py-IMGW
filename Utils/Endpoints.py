from requests import get

SYNOP_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/synop'
METEO_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/meteo'
HYDRO_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/hydro'
HYDRO2_GENERAL_URL='https://danepubliczne.imgw.pl/api/data/hydro2'
DATA_OPTIONS=['json', 'xml', 'csv', 'html']
HYDRO_GROUPS=['hydro', 'hydro2']

class Synop:
    def __init__(self):
        pass

    def get_station_by_id(self,
                          data_format:str='json',
                          station_id:int=None):
        try:
            assert data_format in DATA_OPTIONS
            assert station_id != None
            assert station_id <= 99999
            SYNOP_URL=f'https://danepubliczne.imgw.pl/api/data/synop/id/{station_id}/format/{data_format}'
            result = get(SYNOP_URL)
            return result._content, result.status_code

        except AssertionError:
            raise Exception("Invalid input")
        except Exception as e:
            raise Exception(f"{e}")

    def get_station_by_name(self,
                            station_name:str=None,
                            data_format:str='json'):
        try:
            assert data_format in DATA_OPTIONS
            assert station_name != None
            assert station_name.isalnum() == True
            SYNOP_URL=f'https://danepubliczne.imgw.pl/api/data/synop/station/{station_name}/format/{data_format}'
            result = get(SYNOP_URL)

            return result._content, result.status_code
        except AssertionError:
            raise Exception("Invalid input")
        except Exception as e:
            raise Exception(f"{e}")

    def get_all_stations(self,
                         data_format:str='json'):
        try:
            assert data_format in DATA_OPTIONS
            result = get(f"{SYNOP_GENERAL_URL}/format/{data_format}")
            return result._content, result.status_code
        except AssertionError:
            raise Exception("Invalid input")
        except Exception as e:
            raise Exception(f"{e}")

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

class Hydro:
    def __init__(self):
        pass

    def get_all_stations(self,
                         station_group:str='hydro'):
        try:
            assert station_group in HYDRO_GROUPS
            if station_group == 'hydro':
                result = get(HYDRO_GENERAL_URL)
            elif station_group == 'hydro2':
                result = get(HYDRO2_GENERAL_URL)

            return result._content, result.status_code
        except AssertionError:
            raise Exception("Invalid input")
        except Exception as e:
            raise Exception(f"{e}")
