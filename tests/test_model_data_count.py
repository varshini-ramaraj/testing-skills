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

    def test_ensure_that_source_destination_and_product_exist(self):
        pass
        # Arrange

        # Act


        # Assert

    def test_if_source_and_destination_are_same_return_zero(self):
        pass
        # Arrange

        # Act


        # Assert

    def test_when_cost_submitted_in_is_not_a_good_number_throw_exception(self):
        pass
        # Arrange
        # negative value would apply here
        # also, maybe None value should apply here

        # Act


        # Assert

    def test_if_source_does_not_exist(self):
        pass
        # Arrange

        # Act


        # Assert

    def test_if_duplicate_source_destination_product_choose_last(self):
        pass
        # Arrange

        # Act


        # Assert

    def test_if_duplicate_source_destination_product_log_to_user(self):
        pass
        # Arrange

        # Act


        # Assert

    def test_that_cost_is_added_to_the_model(self):
        # Arrange
        # Act
        model_creator = FakeModelCreator()

        # Assert
        assert type(model_creator.model) == FakeModel
        assert len(model_creator.model.sources) == 3
        assert len(model_creator.model.destinations) == 3
        assert len(model_creator.model.products) == 3
        assert len(model_creator.model.costs) == 1

if __name__ == "__main__":
    pytest.main()
