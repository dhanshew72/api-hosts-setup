from converters.convert_ts import convert_utc_ts
from normalize.normalize_host import NormalizeHost


class NormalizeCrowdstrikeHost(NormalizeHost):
    """
    Normalize data from crowdstrike scanner
    """

    def __init__(self, host_data):
        super().__init__(host_data)

    def normalize(self, host_info):
        """
        Normalize a set of data from crowdstrike
        :return: normalized data from crowdstrike
        """
        return {
            "hostname": host_info["hostname"],
            "first_seen_ts": convert_utc_ts(host_info["first_seen"]),
            "last_seen_ts": convert_utc_ts(host_info["last_seen"]),
            "private_ip": host_info["local_ip"],
            "public_ip": host_info["external_ip"],
            "aws": {
                "aws_service": host_info["service_provider"],
                "aws_ec2_instance_id": host_info["instance_id"],
            }
        }
