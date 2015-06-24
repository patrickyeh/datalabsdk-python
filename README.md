# datalabsdk-python

###Installation

Using pip install to install the sdk:
pip install datalabsdk

###Usage
You should import the specificed class and implement the function for matching your algorithm interface. Following is an example of classfication algorithm power by sklearn, that's try to wrap the algorithm into our sdk!

```
from datalab.Model import ClassificationModel
import numpy as np
from sklearn.neighbors import RadiusNeighborsClassifier
from sklearn import tree
from datalab.DataTransform import DataTransform

class DecisionTreeModel(ClassificationModel):
    def __init__(self):
        self.model = None

    def train(self,input_path,**param):
        obj_dt = DataTransform(input_path,param)
        obj_dt.scan_data_type()
        x,y = obj_dt.fetch_data()
        clf = tree.DecisionTreeClassifier()
        model = clf.fit(x,y)
        self.model = model

        return model

    def predict_by_file(self,input_path,**param):
        x,y = self._fetch_file(input_path,**param)
        return self.predict_by_object(x)

    def validate_by_file(self,input_path,**param):
        x,y = self._fetch_file(input_path,**param)
        return self.validate_by_object(x,y)

    def predict_by_object(self,obj_array):
        return self.model.predict(obj_array)

    def validate_by_object(self,obj_test_x,obj_test_y):
        return self.model.score(obj_test_x,obj_test_y)
```
###SDK
