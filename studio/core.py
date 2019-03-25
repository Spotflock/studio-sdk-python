from __future__ import print_function

import json

import requests


class StudioClient:
    """
        This is Spotflock Studio Python SDK Client for v1.2.0.
        For more information, visit https://studio.spotflock.com/documentation/

        Attributes:
            api_key (str): API Key Generated for an app in Spotflock Studio.
    """

    def __init__(self, api_key):
        """
            The constructor for Spotflock Studio Client.

            Parameters:
                api_key (str): API Key Generated for an app in Spotflock Studio.

            Returns:
                StudioClient: Client object for Spotflock Studio.
        """
        self.api_key = api_key
        self.base_url = 'https://studio.spotflock.com/api/v1'

    def sentiment_analysis(self, text):
        """
            The function to call sentiment analysis service in Phoenix Language.
            For more information, visit https://studio.spotflock.com

            Parameters:
                text (str): The text on which sentiment analysis is to be applied.

            Returns:
                obj: A json obj containing sentiment analysis response.
        """

        body = {'text': text}
        body = json.dumps(body)
        url = self.base_url + '/language-service/phoenix-language/nlp/sentiment'
        headers = {"ApiKey": self.api_key, "Content-type": "application/json"}
        response = requests.post(url=url, data=body, headers=headers).json()
        return response

    def pos_tagger(self, text):
        """
            The function to call pos tagger service in Phoenix Language.
            For more information, visit https://studio.spotflock.com

            Parameters:
                text (str): The text on which sentiment analysis is to be applied.

            Returns:
                obj: A json obj containing pos tagger response.
        """

        body = {'text': text}
        body = json.dumps(body)
        url = self.base_url + '/language-service/phoenix-language/nlp/pos'
        headers = {"ApiKey": self.api_key, "Content-type": "application/json"}
        response = requests.post(url=url, data=body, headers=headers).json()
        return response

    def face_detection_image(self, image_path):
        """
            The function to call face detection service in Phoenix Vision.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-vision/

            Parameters:
                image_path (str): The path of the image file.

            Returns:
                text : A base64 encoded image with face detected.
        """
        body = {'file': (image_path, open(image_path, 'rb'), "multipart/form-data")}
        url = self.base_url + '/vision-service/phoenix-vision/face-detection/image'
        headers = {"ApiKey": self.api_key}
        response = requests.post(url=url, files=body, headers=headers).text
        return response

    def face_detection_json(self, image_path):
        """
            The function to call face detection service in Phoenix Vision.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-vision/

            Parameters:
                image_path (str): The path of the image file.

            Returns:
                obj : A list of co-ordinates for all faces detected in the image.
        """
        body = {'file': (image_path, open(image_path, 'rb'), "multipart/form-data")}
        url = self.base_url + '/vision-service/phoenix-vision/face-detection/json'
        headers = {"ApiKey": self.api_key}
        response = requests.post(url=url, files=body, headers=headers).json()
        return response

    def license_plate_detection_image(self, image_path):
        """
            The function to call license-plate detection service in Phoenix Vision.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-vision/

            Parameters:
                image_path (str): The path of the image file.

            Returns:
                text : A base64 encoded image with license-plate detected.
        """
        body = {'file': (image_path, open(image_path, 'rb'), "multipart/form-data")}
        url = self.base_url + '/vision-service/phoenix-vision/license-plate/image'
        headers = {"ApiKey": self.api_key}
        response = requests.post(url=url, files=body, headers=headers).text
        return response

    def license_plate_detection_json(self, image_path):
        """
            The function to call license-plate detection service in Phoenix Vision.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-vision/

            Parameters:
                image_path (str): The path of the image file.

            Returns:
                obj : A list of co-ordinates all license_plates detected in the image.
        """
        body = {'file': (image_path, open(image_path, 'rb'), "multipart/form-data")}
        url = self.base_url + '/vision-service/phoenix-vision/license-plate/json'
        headers = {"ApiKey": self.api_key}
        response = requests.post(url=url, files=body, headers=headers).json()
        return response

    def train(self, lib, service, model_name, algorithm, dataset_url, label, train_percentage, features,
              save_model=True,
              params=None):
        """
            The function call to train service in Phoenix ML.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-ml/

        :param lib: Library for training the model. Currently we are supporting spotflock and weka libraries.
        :param service: Valid parameter values are classification, regression.
        :param model_name: Model name and with this name model will be saved.
        :param algorithm: algorithm by which model will be trained.
        :param dataset_url: dataset file location in spotflock storage.
        :param label: label of the column in dataset file.
        :param train_percentage: % of data will be used for training and model will be tested against remaining % of data.
        :param features: column name list which is used to train classification model.
        :param save_model: If true model will saved
        :param params:
        :return:
            obj: A json obj containing model info..
        """
        url = self.base_url + '/ml-service/phoenix-ml/' + service + '/train'
        headers = {"ApiKey": self.api_key, "Content-type": "application/json"}
        if params is None:
            params = {}
        body = {
            "library": lib,
            "task": "train",
            "config": {
                "name": model_name,
                "algorithm": algorithm,
                "datasetUrl": dataset_url,
                "label": label,
                "trainPercentage": train_percentage,
                "features": features,
                "saveModel": save_model,
                "params": params
            }
        }
        response = requests.post(url=url, json=body, headers=headers)
        response = response.json()
        return response

    def predict(self, lib, service, dataset_url, model_url, params=None):
        """
             The function call to predict service in Phoenix ML.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-ml/

        :param lib: Library for training the model. Currently we are supporting spotflock and weka libraries.
        :param service: Valid parameter values are classification, regression.
        :param dataset_url: dataset file location in spotflock storage.
        :param model_url: trained model location in spotflock storage.
        :param params:
        :return:
            obj: A json obj containing the file info which has the predictions.
        """
        url = self.base_url + '/ml-service/phoenix-ml/' + service + '/predict'
        headers = {"ApiKey": self.api_key, "Content-type": "application/json"}
        if params is None:
            params = {}
        body = {
            "library": lib,
            # "service": service,
            "config": {
                "datasetUrl": dataset_url,
                "modelUrl": model_url,
                "params": params
            }
        }
        response = requests.post(url=url, json=body, headers=headers).json()
        return response

    def cluster(self, text):
        """
         The function call to cluster service in Phoenix ML.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-ml/

        :param text: text
        :return:
            obj: A json obj.
        """
        body = {'text': text}
        body = json.dumps(body)
        url = self.base_url + '/ml-service/phoenix-ml/cluster'
        headers = {"ApiKey": self.api_key, "Content-type": "application/json"}
        response = requests.post(url=url, data=body, headers=headers)
        response = response.json()
        return response

    def job_status(self, job_id):
        """
            The function call to get the job status in Phoenix ML.
            For more information, visit https://studio.spotflock.com/docs/ai/phoenix-ml/

        :param job_id: job id from the train api response.
        :return:
            obj: A json obj containing the status details.
        """
        url = self.base_url + "/ml-service/phoenix-ml/job/status?id={0}".format(job_id)
        # url = "http://10.1.2.110:8199/phoenix-ml/job/status?id=12"
        headers = {"ApiKey": self.api_key}
        response = requests.get(url=url, headers=headers)
        return response.text

    def job_output(self, job_id):
        """
                The function call to get the job output in Phoenix ML.
                For more information, visit https://studio.spotflock.com/docs/ai/phoenix-ml/

        :param job_id: job id from the train api response.
        :return:
            obj: A json obj containing the job output details.
        """

        url = self.base_url + "/ml-service/phoenix-ml/output/findBy?jobId={0}".format(job_id)
        headers = {"ApiKey": self.api_key}
        response = requests.get(url=url, headers=headers)
        return response.json()

    def store(self, file_path):
        """
             The function call to store in Phoenix ML.
             For more information, visit https://studio.spotflock.com/docs/ai/phoenix-ml/

        :param file_path: The path of the dataset file.
        :return:
            obj: A json obj containing the file path in storage.
        """
        url = self.base_url + "/solution-service/cloud-solution/storage"
        headers = {"ApiKey": self.api_key}
        files = {'file': open(str(file_path), 'rb')}
        response = requests.post(url=url, headers=headers, files=files, verify=False)
        response = response.json()
        return response

    def download(self, file_url):
        """
                The function call to download the prediction file in Phoenix ML.
                For more information, visit https://studio.spotflock.com/docs/ai/phoenix-ml/


        :param file_url:
        :return:
            txt:  file text containing the file.
        """
        url = self.base_url + "/storage-service/cloud-storage/s3/file/download?url={0}".format(file_url)

        headers = {"ApiKey": self.api_key}
        response = requests.get(url=url, headers=headers)
        return response
