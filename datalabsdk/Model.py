from datalabsdk.DataTransform import DataTransform
import numpy as np

class Model(object):
    def __init__(self):
        """
        :rtype : object
        """
        self.int_dimension = None

    def update_param(self, param):
        if not self.int_dimension == None:
            param['n_features'] = self.int_dimension

    def check_status(self):
        raise "Need to be implemented by algorithm"

    def get_required_params(self):
        raise "Need to be assigned"

    def set_parameters(self, **args):
        self.args = args

    def format_check(self, input_path):
        pass
        '''
        :param input_path:
        :return True if this file can be processed:
        '''

    def _fetch_file(self, input_path, **param):
        if self.model == None:
            raise 'Please Train a model before predicting some thing'
        self.update_param(param)
        obj_dt = DataTransform(input_path, param)
        obj_dt.scan_data_type()
        x, y = obj_dt.fetch_data()
        return (x, y)

    def set_label_data(self, label_input_path):
        self.label_input_path = label_input_path

    def set_label_column_index(self, int_label_index):
        self.int_label_index = int_label_index

    def train(self, input_path, **param):
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

    def predict_by_array(self, obj_array):
        raise 'Need to be implemented'

    def validate_by_object(self, obj_test_x, obj_test_y):
        raise 'Need to be implemented'

    def get_category(self):
        return 'General'

    def set_dimension(self, int_dimension):
        self.int_dimension = int_dimension

    def get_model_result(self):
        raise 'Need to be implemented'

    def get_required_params(self):
        raise 'Need to be assign'

    def _verify_params(self,params):
        dict_required_param = self.get_required_params()
        for key in dict_required_param.keys():
            if dict_required_param[key].has_key('required') and not params.has_key('key'):
                return False
        return True
    def get_input_file_format(self):
        raise "Does not assign"

class RecommendationModel(Model):
    def get_category(self):
        return 'Recommendation'

class ClassificationModel(Model):
    def get_category(self):
        return 'Classification'

    def get_performance_metric(self, input_path):
        predict_y = self.predict_by_file(input_path)
        x, valid_y = self._fetch_file(input_path)
        perf_result = (valid_y * 2) + predict_y
        print perf_result
        N = np.size(valid_y)
        PN = np.size(np.where(valid_y == 1))
        NN = np.size(np.where(valid_y == -1))
        TPN = np.size(np.where(perf_result == 3))
        FPN = np.size(np.where(perf_result == -1))
        FNN = np.size(np.where(perf_result == 1))
        TNN = np.size(np.where(perf_result == -3))

        return {
            'TPR': np.divide(float(TPN), PN),
            'SPC': np.divide(float(TNN), NN),
            'PPV': np.divide(float(TPN), (TPN + FPN)),
            'NPV': np.divide(float(TNN), (TNN + FNN)),
            'FPR': np.divide(float(FPN), NN),
            'FNR': np.divide(float(FNN), (TPN + FNN)),
            'FDR': np.divide(float(FPN), (TPN + FPN)),
            'ACC': np.divide((TPN + TNN), float(N)),
            'F1': np.divide((2.0 * TPN), ((2.0 * TPN) + FPN + FNN)),
        }

    def set_predict_file(self, input_path):
        self.predict_file_path = input_path
