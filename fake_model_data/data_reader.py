class DataReader:
    """Not really up for question, straightforward and works"""
    def __init__(self, populate_automatically: bool):
        self._data_creator = DataCreator(populate_automatically)

    def read_sources(self):
        return self._data_creator.source_data

    def read_destinations(self):
        return self._data_creator.destination_data

    def read_products(self):
        return self._data_creator.product_data

    def read_costs(self):
        return self._data_creator.cost_data


class DataCreator:
    """Make sure we can do the same either with this or with tests"""
    def __init__(self, populate_automatically: bool=True):
        if populate_automatically:
            self._create_sources()
            self._create_destinations()
            self._create_products()
            self._create_costs()

    def _create_sources(self):
        source_1 = ("Source1", None, None)
        source_2 = ("Source2", 0, 1e-4)
        source_3 = ("Source3", 100, 100)
        sources = [source_1, source_2, source_3]
        self.source_data = list()
        for source in sources:
            source_dict = self.create_source(source)
            self.source_data.append(source_dict)

    def _create_destinations(self):
        destination_1 = ("Destination1", None, None)
        destination_2 = ("Destination2", 0, 1e-4)
        destination_3 = ("Destination3", 100, 100)
        destinations = [destination_1, destination_2, destination_3]
        self.destination_data = list()
        for destination in destinations:
            destination_dict = self.create_destination(destination)
            self.destination_data.append(destination_dict)

    def _create_products(self):
        product_1 = ("Product1", None, None)
        product_2 = ("Product2", 1.0, 2.0)
        product_3 = ("Product3", 10.0, -11.5)
        products = [product_1, product_2, product_3]
        self.product_data = list()
        for product in products:
            product_dict = self.create_product(product)
            self.product_data.append(product_dict)

    def _create_costs(self):
        cost_1 = ("Source1", "Destination1", "Product1", 100)
        cost_2 = ("Source2", "Destination2", "Product2", 100)
        cost_3 = ("Source3", "Destination3", "Product3", 100)
        cost_4 = ("Source4", "Destination4", "Product4", 100)
        costs = [cost_1, cost_2, cost_3, cost_4]
        self.cost_data = list()
        for cost in costs:
            cost_dict = self.create_cost(cost)
            self.cost_data.append(cost_dict)

    def create_source(self, source):
        source_dict = dict()
        source_name, lat, long = source
        source_dict["SourceName"] = source_name
        source_dict["Latitude"] = lat
        source_dict["Longitude"] = long
        return source_dict

    def create_destination(self, destination):
        destination_dict = dict()
        destination_name, lat, long = destination
        # PPT note: upper case vs lower case maybe - should we put it here tho? decide
        destination_dict["DestinationName"] = destination_name
        destination_dict["Latitude"] = lat
        destination_dict["Longitude"] = long
        return destination_dict

    def create_product(self, product):
        product_dict = dict()
        product_name, lat, long = product
        # PPT note: upper case vs lower case maybe - should we put it here tho? decide
        product_dict["ProductName"] = product_name
        product_dict["UnitWeight"] = lat
        product_dict["UnitVolume"] = long
        return product_dict

    def create_cost(self, cost_data):
        cost_dict = dict()
        source, destination, product, cost = cost_data
        # PPT note: upper case vs lower case maybe - should we put it here tho? decide
        cost_dict["SourceName"] = source
        cost_dict["DestinationName"] = destination
        cost_dict["ProductName"] = product
        cost_dict["UnitCost"] = cost
        return cost_dict