"""
WSGI config for fnews project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fnews.settings')

application = get_wsgi_application()

# ML registry
import inspect
from apps.ml.registry import MLRegistry
from sklearn.linear_model import LogisticRegression

try:
    registry = MLRegistry() # create ML registry
    lr = LogisticRegression()
    # add to ML registry
    registry.add_algorithm(endpoint_name="logistic_regression",
                            algorithm_object=lr,
                            algorithm_name="logistic regressuin",
                            algorithm_status="production",
                            algorithm_version="0.0.1",
                            owner="xider",
                            algorithm_description="Logistic Regression algorithm",
                            algorithm_code=inspect.getsource(LogisticRegression))

except Exception as e:
    print("Exception while loading the algorithms to the registry,", str(e))