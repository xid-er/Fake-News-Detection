from django.db import transaction
from django.shortcuts import render

from rest_framework import viewsets, mixins
from rest_framework.exceptions import APIException

from apps.endpoints.models import Endpoint, MLAlgorithm, MLAlgorithmStatus, MLRequest
from apps.endpoints.serializers import EndpointSerializer, MLAlgorithmSerializer, MLAlgorithmStatusSerializer, MLRequestSerializer

from apps.main.forms import MLForm

import os
import json
import pickle
from numpy.random import rand
from rest_framework import views, status
from rest_framework.response import Response
from apps.ml.registry import MLRegistry
from fnews.wsgi import registry


class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = EndpointSerializer
    queryset = Endpoint.objects.all()


class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MLAlgorithm.objects.all()


def deactivate_other_statuses(instance):
    old_statuses = MLAlgorithmStatus.objects.filter(parent_mlalgorithm = instance.parent_mlalgorithm,
                                                        created_at__lt=instance.created_at,
                                                        active=True)
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    MLAlgorithmStatus.objects.bulk_update(old_statuses, ["active"])

class MLAlgorithmStatusViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MLAlgorithmStatus.objects.all()
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                # set active=False for other statuses
                deactivate_other_statuses(instance)



        except Exception as e:
            raise APIException(str(e))

class MLRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    serializer_class = MLRequestSerializer
    queryset = MLRequest.objects.all()

class PredictView(views.APIView):
    form_class = MLForm
    initial = {'prediction': 'value'}
    template_name = 'index.html'

    def post(self, request, endpoint_name, format=None):

        form = self.form_class(request.POST)
        if form.is_valid:


            algorithm_version = self.request.query_params.get("version")

            algs = MLAlgorithm.objects.filter(parent_endpoint__name = endpoint_name, status__active=True)

            if algorithm_version is not None:
                algs = algs.filter(version = algorithm_version)

            if len(algs) == 0:
                return Response(
                    {"status": "Error", "message": "ML algorithm is not available"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            alg_index = 0

            #algorithm_object = registry.endpoints[algs[alg_index].id]
            #prediction = algorithm_object.predict(request.data)
            
            module_dir = os.path.dirname(__file__)  # get current directory
            static_path = os.path.join(module_dir, '..', '..', 'static')
            model_path = os.path.join(static_path, 'models', 'simple_model.sav')
            preprocessing_path = os.path.join(static_path, 'preprocessing', 'tfidf_vectorizer.sav')

            model = pickle.load(open(model_path, "rb"))
            #scaler = pickle.load(open("scaler.sav", "rb"))
            preprocessing = pickle.load(open(preprocessing_path, "rb"))

            input_data = request.data['src_text']
            feature = preprocessing.transform([input_data])

            #prediction = model.predict(scaler.transform(request.data))
            prediction = model.predict(feature)


            label = prediction["label"] if "label" in prediction else "error"
            ml_request = MLRequest(
                input_data=json.dumps(request.data),
                full_response=prediction,
                response=label,
                feedback="",
                parent_mlalgorithm=algs[alg_index],
            )
            ml_request.save()

            # TODO: Figure out Django template routing
            #return redirect()
            return render(request, 'main/prediction.html', {'prediction': prediction})
            #return Response(prediction)

        else:
            return render(request, self.template_name, {'form': form})