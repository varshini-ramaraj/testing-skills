import pytest

from fake_model_data.model_creator import FakeModelCreator, FakeModel


class TestFakeModelDataCount:
    def test_model_data_count_is_as_expected(self):
        # Arrange
        # Act
        model_creator = FakeModelCreator()

        # Assert
        assert type(model_creator.model) == FakeModel
        assert len(model_creator.model.sources) == 3
        assert len(model_creator.model.destinations) == 3
        assert len(model_creator.model.products) == 3
        assert len(model_creator.model.costs) == 0


if __name__ == "__main__":
    pytest.main()
