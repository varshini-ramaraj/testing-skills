class ModelParser:
    def parse_model(self):
        return False


fake_model_data = ModelParser().parse_model()
if not fake_model_data:
    raise Exception("Parsing went wrong")