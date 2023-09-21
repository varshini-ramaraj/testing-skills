class DataReader:
    """Not really up for question, straightforward and works"""
    # list of dictionaries
    def read_sources(self):
        pass

    def read_destinations(self):
        pass

    def read_products(self):
        pass

    def read_costs(self):
        pass


class DataCreator:
    def __init__(self, populate_automatically: bool=True):
        if populate_automatically:
            self._create_costs_and_rest()

    def _create_costs_and_rest(self):
        self.create_cost("Source1", "Destination1", "Product1", 100)

    def create_source(self):
        pass

    def create_destination(self):
        pass

    def create_product(self):
        pass

    def create_cost(self, source, destination, product, cost):
        pass