from datalabsdk.DataTransform import DataTransform


class Model(object):
    def __init__(self):
        """
        :rtype : object
        """
        pass

    def check_status(self):
        raise "Need to be implemented by algorithm"

    def set_parameters(self, **args):
        self.args = args

    def format_check(self, input_path):
        pass
        '''
        :param input_path:
        :return True if this file can be processed:
        '''
    def _fetch_file(self,input_path,**param):
        if self.model == None:
            raise 'Please Train a model before predicting some thing'

        obj_dt = DataTransform(input_path,param)
        obj_dt.scan_data_type()
        x,y = obj_dt.fetch_data()
        return (x,y)

    def set_label_data(self,label_input_path):
        self.label_input_path = label_input_path

    def set_label_column_index(self,int_label_index):
        self.int_label_index = int_label_index

    def train(self, input_path,**param):
        '''
        :param input_path:
        :return a model object:
        '''
        raise 'Need to be implemented'

    def predict_by_file(self, input_data):
        '''
        :param input_data:
        :return predict label:
        '''
        raise 'Need to be implemented'

    def transfermation(self, input_data):
        pass

    def predict_by_array(self,obj_array):
        raise 'Need to be implemented'

    def validate_by_object(self,obj_test_x,obj_test_y):
        raise 'Need to be implemented'

class ClassificationModel(Model):
    def get_category(self):
        return 'Classification'
