from django.test import TestCase
from apps.ml.registry import MLRegistry

import inspect
from sklearn.linear_model import LogisticRegression

class MLTests(TestCase):
    def test_registry(self):
        registry = MLRegistry()
        self.assertEqual(len(registry.endpoints), 0)
        endpoint_name = "logistic_regression"
        algorithm_object = LogisticRegression()
        algorithm_name = "logistic regression"
        algorithm_status = "production"
        algorithm_version = "0.0.1"
        algorithm_owner = "xider"
        algorithm_description = "Logistic Regression algorithm"
        algorithm_code = inspect.getsource(LogisticRegression)
        # add to registry
        registry.add_algorithm(endpoint_name, algorithm_object, algorithm_name,
                    algorithm_status, algorithm_version, algorithm_owner,
                    algorithm_description, algorithm_code)
        # there should be one endpoint available
        self.assertEqual(len(registry.endpoints), 1)