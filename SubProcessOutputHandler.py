from Task.DataModels import ConnectorParams


class SubProcessInputOutputHandler(object):
    @property
    def connector_params(self):
        result = ConnectorParams()
        print(result)
        raise Exception("NOT IMPLEMENTED")

        # TODO: parse stdin input into ConnectorParams object and return it with populated values
        result.source_file_path = "NOT IMPLMENTED"
        result.iteration_count = "NOT IMPLMENTED"

        return result

    def end(self, connector_result):
        """ connector_result is of type ConnectorResult"""
        raise Exception("NOT IMPLEMENTED")
        # TODO - pass connector result as stdout
        # TODO - end current process