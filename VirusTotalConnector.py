import requests
import pprint
import time
import json
import os
from Task.SubProcessOutputHandler import SubProcessInputOutputHandler
from Task.DataModels import ConnectorParams


def main():
    connector_params = ConnectorParams()
    api_key = ConnectorParams.api_key
    url_api = ConnectorParams.url
    list_of_ulr_list = ConnectorParams.list_of_url_list
    # connector_result = None

    for list_of_url in list_of_ulr_list:
        result = {}
        for site in list_of_url:
            result[site] = ""
            params = {'apikey': api_key, 'resource': site}
            response = requests.get(url_api, params=params)
            response_json = json.loads(response.content)
            response_positives = response_json['positives']

            if response_positives <= 0:
                result[site] = "NOT MALICIOUS"

            elif response_positives == 1:
                result[site] = "MAYBE MALICIOUS"

            elif response_positives >= 1:
                result[site] = "MALICIOUS"

            time.sleep(21)
            print(result)

        for key, val in result.items():
            print(key, " : ", val)


    #
    # # TODO Implement Connector Logic
    # raise Exception("IMPLEMENT")


if __name__ == "_main_":
    main()
main()
