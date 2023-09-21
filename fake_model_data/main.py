import logging

from fake_model_data.data_reader import DataReader

logger = logging.getLogger(__name__)


class FakeModelData:
    # Add something here
    def __init__(self,
                 sites,
                 data_two,
                 data_three,
                 data_four):
        # PPT Note: Does not allow for mocking of anyone of them, will fail immediately
        self.init_data(sites, data_two, data_three, data_four)
        # PPT Note: Initialize this here does not allow for mocking
        self.model = Model()
        # PPT Note: Initialize this here does not allow for mocking
        self.data_reader = DataReader()

    def init_data(self, sites, data_two, data_three, data_four):
        if sites is None:
            raise Exception("No Sites")
        if data_two is None:
            raise Exception("No Data two")
        if data_three is None:
            raise Exception("No Data three")
        if data_four is None:
            raise Exception("No Data four")

        # more setup for all four of them

        # something about case conversion and matching
        # SOmething about checking for specific values
        # Varshini please write everything in one function
        # Reading a file? Reading two files
        # ... how far do I take this example
    def load_site_data(self) -> None:
        logger.info("Loading Sites data")
        sites_null_lat_long_count = 0
        sites_total_count = 0

        # PPT Note: Can make this an actual read in here - and then changing that is the point
        sites_data = self.data_reader.read_sites()
        for site_data in sites_data:
            sites_total_count += 1
            site = Site()
            # PPT Note: Need to standardize string
            # PPT Note: Need to remove strings
            # PPT note: lets assume this parentheses part isn't the issue
            site.name = site_data["SiteName"]
            site.orig_name = site.name
            site.is_customer = False
            latitude = site_data["Latitude"]
            longitude = site_data["Longitude"]

            # PPT note: Can function this
            sites_null_lat_long_count += latitude is None or longitude is None
            # PPT note: can function this
            # PPT note: will fail if latitude/longitude is None, error happens inside constructor and so is confusing, could be functionized
            site.geo_coordinate = Coordinate(float(latitude), float(longitude))

            self.model.add_site(site)


class Site:
    def __init__(self):
        self.name = None

    pass


class Coordinate:
    def __init__(self, lat: float, lon: float):
        self.latitude = lat
        self.longitude = lon


class Model:
    def __init__(self):
        # PPT note: lack of type hinting leads to its own issues
        self._d_sites = dict()
        self.sites = list()

    def add_site(self, site: Site) -> Site:
        # PPT note: Case agnostic check needs to happen
        lookup_name = site.name
        if lookup_name not in self._d_sites:
            self._d_sites[lookup_name] = site
            self.sites.append(site)
            return site
        return self._d_sites[lookup_name]
