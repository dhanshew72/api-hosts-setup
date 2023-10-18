class NormalizeHost:
    """
    Interface for parsing interface data
    """

    def __init__(self, host_data):
        self.host_data = host_data

    def normalize_all(self):
        """
        Normalizes all the host data and places into al ist
        :return: list of normalized data per data source
        """
        normalize_hosts = []
        for host_info in self.host_data:
            result = self.normalize(host_info)
            normalize_hosts.append(result)
        return normalize_hosts

    def normalize(self, host_info):
        """
        Normalizes host data, must be implemented by each type of host data provided
        """
        raise NotImplementedError("`NormalizeHost` must implement `normalize` function")
