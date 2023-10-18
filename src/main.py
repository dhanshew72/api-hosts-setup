from config import Config
from fetch.fetch_hosts import FetchHosts
from normalize.combine_hosts import CombineHosts
from write.write_hosts import WriteHosts

CONFIG = Config("config.yaml").read()


def run():
    """
    Runs every part to grab, normalize and write hosts data
    """
    host_data = CONFIG["host_data"]

    results = FetchHosts(
        base_url=host_data["base_url"],
        api_key=host_data["api_key"],
        limit=host_data["limit"],
        skip=host_data["skip"]
    ).fetch_all(host_data["paths"])

    combined_data = CombineHosts(results).combine_hosts()

    mongodb = CONFIG["mongodb"]
    WriteHosts(
        db_host=mongodb["host"],
        db_name=mongodb["db"],
        db_collection=mongodb["collection"]
    ).write(combined_data)


if __name__ == "__main__":
    run()
