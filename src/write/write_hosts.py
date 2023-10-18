import pymongo


class WriteHosts:
    """
    Class for writing hosts data to db
    """

    def __init__(self, db_host, db_name, db_collection):
        self.db_client = pymongo.MongoClient(db_host)[db_name]
        self.db_collection = db_collection
        self._create_host_index()

    def write(self, db_data):
        """
        Writes all data to db
        :param db_data: list of data to write
        :return: result of the insert
        """
        for row in db_data:
            filter_row = {"hostname": row["hostname"]}
            # The idea behind upserting is to grab the latest information from scans
            self.db_client[self.db_collection].replace_one(filter_row, row, upsert=True)

    def _create_host_index(self):
        """
        Creates an index for hostname field in db
        """
        list_of_collections = self.db_client.list_collection_names()
        if self.db_collection not in list_of_collections:
            self.db_client[self.db_collection].create_index("hostname", unique=True)
