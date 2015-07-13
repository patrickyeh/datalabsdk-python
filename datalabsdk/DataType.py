__all__ = ['NumDenseCSV','LibSVM']
import numpy as np
from sklearn.datasets import load_svmlight_file

class DataType(object):
    def __init__(self,input_path,param):
        self.input_path = input_path
        self.param = param

    def _getIterReader(self):
        obj_file = open('r',self.input_path)
        return obj_file

    def check_data_compatibility(self):
        str_record = ''
        with open(self.input_path,'r') as f:
            str_record = f.readline()
        try:
            self._transform(str_record)
            return True
        except:
            return False

    def _transform(self,str_record):
        '''
        Transform string to np array or other
        :param str_record:
        :return:
        '''
        raise 'Need to be implemented'

    def fetch_data_lazy(self):
        obj_file = self._getIterReader()
        for inst in obj_file:
            yield self._transform(inst)
        obj_file.close()

    def fetch_data(self,label_idx=1):
        res = None
        for inst in self._getIterReader():
            if res == None:
                res = np.array(self._transform(inst))
            else:
                res = np.vstack(res,np.array(self._transform(inst)))
        if label_idx == None:
            return res
        else:
            if label_idx > len(res) -1:
                raise 'Over dimension'
            else:
                y = res[:,label_idx]
                x = np.delete(res,(label_idx),axis=1)
                return x,y


class NumDenseCSV(DataType):
    def _transform(self,str_record):
        lst_record = str_record.split(',')
        for idx in xrange(len(lst_record)):
            lst_record[idx] = float(lst_record[idx])
        return lst_record


class LibSVM(DataType):
    def fetch_data(self,label_idx=None):

        return load_svmlight_file(self.input_path,**self.param)

    def check_data_compatibility(self):
        try:
            load_svmlight_file(self.input_path)
            return True
        except Exception as ex:
            print ex.message
            return False
