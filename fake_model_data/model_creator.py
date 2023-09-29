import logging

from fake_model_data.data_reader import DataReader

logger = logging.getLogger(__name__)


class FakeModelCreator:
    def __init__(self):
        # Note: Does not allow for mocking of anyone of them, will fail immediately
        # Note: Initialize this here does not allow for mocking
        self.model = FakeModel()
        self.data_reader = DataReader(populate_automatically=True)
        self.read_all_data()

    def read_all_data(self):
        sources_data = self.data_reader.read_sources()
        destination_data = self.data_reader.read_destinations()
        products_data = self.data_reader.read_products()
        costs_data = self.data_reader.read_costs()
        self.init_data(sources_data, destination_data, products_data, costs_data)

    def init_data(self, sources, destinations, products, costs):
        if sources is None:
            raise Exception("No Sources")
        if destinations is None:
            raise Exception("No destinations")
        if products is None:
            raise Exception("No Products")
        if costs is None:
            raise Exception("No costs")

        self.load_source_data(sources)
        self.load_destination_data(destinations)
        self.load_product_data(products)
        self.load_costs(costs)

    def load_source_data(self, sources_data) -> None:
        logger.info("Loading Sources data")

        for source_data in sources_data:
            source = Source()
            # Note: lets assume this parentheses part isn't the issue
            source.name = source_data["SourceName"]
            source.orig_name = source.name
            source.is_destination = False
            latitude = source_data["Latitude"]
            longitude = source_data["Longitude"]

            source.geo_coordinate = Coordinate(float(latitude), float(longitude))

            self.model.add_source(source)

    def load_destination_data(self, destinations_data) -> None:
        logger.info("Loading destinations data")

        for destination_data in destinations_data:
            destination = Destination()
            destination.name = destination_data["DestinationName"]
            destination.orig_name = destination.name
            destination.is_destination = False
            latitude = destination_data["Latitude"]
            longitude = destination_data["Longitude"]

            destination.geo_coordinate = Coordinate(float(latitude), float(longitude))

            self.model.add_destination(destination)

    def load_product_data(self, products_data):
        logger.info("Loading Product data")

        for product_data in products_data:
            product_name = product_data["ProductName"]
            weight = float(
                product_data["UnitWeight"]
            )
            cubic = float(
                product_data["UnitVolume"]
            )
            self.model.add_product(Product(product_name, weight, cubic))

    def load_costs(self, costs_data):
        logger.info("Loading Unit Costs")

        for cost_data in costs_data:
            source_name = cost_data["SourceName"]
            destination_name = cost_data["DestinationName"]
            product_name = cost_data["ProductName"]
            cost = float(cost_data["UnitCost"])
            self.model.add_cost(Cost(source_name, destination_name, product_name, cost))


class Source:
    def __init__(self):
        self.name = None


class Destination:
    def __init__(self):
        self.name = None


class Product:
    def __init__(self, name, weight, volume):
        self.name = name
        self.weight = weight
        self.volume = volume


class Cost:
    def __init__(self, source: Source, destination: Destination, product: Product, unit_cost):
        self.source = source
        self.destination = destination
        self.product = product
        self.unit_cost = unit_cost


class Coordinate:
    def __init__(self, lat: float, lon: float):
        self.latitude = lat
        self.longitude = lon


class FakeModel:
    def __init__(self):
        self._d_sources = dict()
        self._d_destinations = dict()
        self._d_products = dict()
        self.sources = list()
        self.destinations = list()
        self.products = list()
        self.costs = list()

    def add_source(self, source: Source) -> Source:
        lookup_name = source.name
        if lookup_name not in self._d_sources:
            self._d_sources[lookup_name] = source
            self.sources.append(source)
            return source
        return self._d_sources[lookup_name]

    def add_destination(self, destination: Destination):
        lookup_name = destination.name
        if lookup_name not in self._d_destinations:
            self._d_destinations[lookup_name] = destination
            self.destinations.append(destination)
            return destination
        return self._d_destinations[lookup_name]

    def add_product(self, product):
        lookup_name = product.name
        if lookup_name not in self._d_products:
            self._d_products[lookup_name] = product
            self.products.append(product)
        return self._d_products[lookup_name]

    def add_cost(self, cost: Cost):
        # Search for source, destination, and product from other lists, then add cost here
        return
