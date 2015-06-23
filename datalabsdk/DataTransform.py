__all__ = ['DataTransform']
from datalabsdk import DataType


class DataTransform(object):
    def __init__(self,input_path,param):
        self.input_path = input_path
        self.dt = None
        self.dt_type = None
        self.param = param

    def get_type(self):
        return self.dt_type

    def scan_data_type(self):
        lst_type = DataType.__all__
        for str_type in lst_type:

            dt = eval('DataType.%s'%(str_type))(self.input_path,self.param)
            if dt.check_data_compatibility():
                self.dt = dt
                self.dt_type = str_type
                break


    def _check_status(self):
        if self.dt == None:
            raise "Not Campatible data type!!"

    def fetch_data(self):
        self._check_status()
        return self.dt.fetch_data()
