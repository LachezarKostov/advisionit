import os
from SubProcessInputHandler import list_of_files_in_folder
from SubProcessInputHandler import csv_to_list


class ConnectorParams(object):
    root_dir = os.path.dirname(os.path.abspath(__file__))
    api_key = "c9d542e8830df68f8a0d8a14d5edfadd7222ed5593dc0284fe919489352c09bc"
    url = 'https://www.virustotal.com/vtapi/v2/url/report'
    source_folder_path = os.path.join(root_dir, 'files')  # string - file path for entity list files
    iteration_entities_count = 4  # int - how many entities to process each interval (ignore the rest)
    files_paths = list_of_files_in_folder(source_folder_path)
    list_of_url_list = csv_to_list(files_paths)


class ConnectorResult(object):
    alerts = None  # Dictionary {string, any} - connector output with data per entity. Key = Entity, value = entity data
    run_interval_seconds = None  # int - iterations interval in seconds for current connector
    script_file_path = None  # string - the file path to the connector script
    connector_name = None  # string - connector name
    params = None  # ConnectorParams object - see below
    output_folder_path = None  # string - file path for connector output
