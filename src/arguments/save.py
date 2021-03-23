import os as os
import json as json
import uuid as uuid


class SaveSearchResults(object):
    def __init__(self, result_json):
        self.result_json = self.__get_as_dict(result_json[0])
        self.save_results_filename = self.generate_file_name(os.getcwd())

        self.save_data_to_file(self.result_json, self.save_results_filename)

    def save_data_to_file(self, data, filename):
        with open(os.path.join(os.getcwd(), f"{filename}.json"),
                  "w") as result_writer:
            json.dump(data, result_writer, indent=6)

    def __get_as_dict(self, json_array):
        result_dict = {}
        for index, element in enumerate(json_array):
            result_dict[index] = json_array[index]
        return dict(result_dict)

    def generate_file_name(self, directory):
        file_list = os.listdir(directory)
        filename = str(uuid.uuid4()).replace("-", "_")[:4]
        while filename in file_list:
            filename = str(uuid.uuid4()).replace("-", "_")[:4]

        return filename 

    def __repr__(self):
        return str(self.save_results_filename)