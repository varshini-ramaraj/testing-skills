from fake_model_data.main import FakeModelCreator


class ModelParser:
    def parse_model(self):
        fake_model_creator = FakeModelCreator()
        return True

fake_model_data = ModelParser().parse_model()
if not fake_model_data:
    raise Exception("Parsing went wrong")