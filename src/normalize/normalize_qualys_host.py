from converters.convert_ts import convert_utc_ts
from normalize.normalize_host import NormalizeHost


class NormalizeQualysHost(NormalizeHost):
    """
    Normalize data from qualys scanner
    """

    def __init__(self, host_data):
        super().__init__(host_data)

    def normalize(self, host_info):
        """
        Normalize a set of data from qualys
        :return: normalized data from qualys
        """
        return {
            "hostname": host_info["dnsHostName"],
            "status": self._normalize_status(host_info["agentInfo"]["status"]),
            "vulnerabilities": self._normalize_vulnerabilities(host_info["vuln"]["list"]),
            "vulnerabilities_count": len(self._normalize_vulnerabilities(host_info["vuln"]["list"]))
        }

    @staticmethod
    def _normalize_status(status):
        """
        Helper function to set status eg ACTIVE or INACTIVE
        This could be an enum
        :param status: improperly formatted status eg STATUS_INACTIVE or STATUS_ACTIVE
        :return: properly formatted status
        """
        return status.split('_')[1]

    @staticmethod
    def _normalize_vulnerabilities(vulns):
        """
        Nomralize the vulnerabilities list to id and timestamps
        :param vulns: list of vulnerability data
        :return: normalized vulnerability data
        """
        normalize_vulns = []
        for vuln in vulns:
            normalize_vulns.append(
                {
                    "vulnerability_id": vuln["HostAssetVuln"]["hostInstanceVulnId"]["$numberLong"],
                    "vulnerability_first_seen_ts": convert_utc_ts(vuln["HostAssetVuln"]["firstFound"]),
                    "vulnerability_last_seen_ts": convert_utc_ts(vuln["HostAssetVuln"]["lastFound"])
                }
            )
        return normalize_vulns
