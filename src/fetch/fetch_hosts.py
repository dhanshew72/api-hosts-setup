import requests


class FetchHosts:
    """
    A class to retrieve all host data
    """

    def __init__(self, base_url, api_key, limit=2, skip=0):
        self.base_url = base_url
        self.headers = {
            "Accept": "application/json",
            "Token": api_key
        }
        self.params = {"limit": limit, "skip": skip}

    def fetch_all(self, paths):
        """
        Retrieves host data from multiple paths
        :param paths: list of paths for the endpoints
        :return: all host data mapped based on endpoint path
        """
        results = {}
        for path in paths:
            results[path["name"]] = self.fetch(path["full_path"])
        return results

    def fetch(self, path):
        """
        Retrieves host data from a provided path
        :param: full path for endpoint
        :return: json representation of host data
        """
        url = "{}/{}".format(self.base_url, path)
        result = requests.post(url, params=self.params, headers=self.headers).json()
        return result
