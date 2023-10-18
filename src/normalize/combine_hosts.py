from normalize.normalize_crowdstrike_host import NormalizeCrowdstrikeHost
from normalize.normalize_qualys_host import NormalizeQualysHost


class CombineHosts:
    """
    Class to help combine all data from hosts sources
    """

    def __init__(self, hosts_data):
        self.hosts_data = hosts_data

    def combine_hosts(self):
        """
        Combines all the hosts data together based on the available types.
        :return: combined hosts data merged
        """
        hosts_runner = [
            NormalizeCrowdstrikeHost(self.hosts_data["crowdstrike"]),
            NormalizeQualysHost(self.hosts_data["qualys"])
        ]
        combined = {}
        # This is pretty ugly, but hosts runner just runs all the types of host we have
        # Then combines them via a key in a dictionary with combined then returns of values after updating
        for host_runner in hosts_runner:
            res = host_runner.normalize_all()
            for item in res:
                hostname = item["hostname"]
                if combined.get(hostname):
                    combined[hostname].update(item)
                else:
                    combined[hostname] = item
        return list(combined.values())
