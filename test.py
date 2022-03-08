from pytest import fixture, mark

from main import Card, Barrel, Player, unique_player_name, can_cross_out_number, not_number_in_card


@fixture
def card_instance():
    return Card(
        [72, 56, 70, 15, 43, 55, 80, 89, 37, 44, 6, 18, 26, 64, 84, 85, 46, 79, 23, 22, 12, 75, 20, 57, 19, 50, 69])


@fixture
def barrel_instance():
    return Barrel(
        [40, 74, 82, 79, 71, 44, 28, 38, 10, 19, 54, 27, 20, 50, 81, 70, 52, 9, 29, 69, 37, 14, 77, 42, 31, 55, 66])


@fixture
def player_instance():
    return Player('Player1', card_instance, False)


class TestCard:
    # Card.__str__
    def test_card(self, card_instance):
        assert '72 56 70 15 43 55 80 89 37 \n44 06 18 26 64 84 85 46 79 \n23 22 12 75 20 57 19 50 69 \n' == str(
            card_instance)

    # can_cross_out_number
    def test_can_cross_out_number(self, card_instance):
        assert can_cross_out_number('y', 80, card_instance) is True

    # can_cross_out_number
    @mark.parametrize(('player_response', 'number'), [
        ('n', 80),
        ('y', 1)
    ])
    def test_not_can_cross_out_number(self, player_response, number, card_instance):
        assert can_cross_out_number(player_response, number, card_instance) is False

    # not_number_in_card
    def test_not_number_in_card(self, card_instance):
        assert not_number_in_card('n', 1, card_instance) is True


class TestBarrel:
    # Barrel.__init__
    @mark.parametrize('numbers', [
        None,
        [40, 74, 82, 79, 71, 44, 28, 38, 10, 19, 54, 27, 20, 50, 81, 70, 52, 9, 29, 69, 37, 14, 77, 42, 31, 55, 66]
    ])
    def test_barrel(self, numbers):
        barrel = Barrel(numbers)
        assert barrel.numbers is not None


class TestPlayer:
    # test_not_unique_player_name
    def test_not_unique_player_name(self, player_instance):
        assert unique_player_name([player_instance], 'Player1') is False

    # test_unique_player_name
    def test_unique_player_name(self, player_instance):
        assert unique_player_name([player_instance], 'Player2') is True
