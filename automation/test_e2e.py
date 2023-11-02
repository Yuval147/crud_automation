from automation.test_create_players import test_create_player
from automation.test_get_players import test_read_player
from automation.test_update_players import test_update_player


def test_run_e2e_tests(base_url):
    print("Running end-to-end tests...\n")

    print("Testing Create Player API...")
    test_create_player(base_url)

    print("\nTesting Read Player API...")
    test_read_player(base_url)

    print("\nTesting Update Player API...")
    player_id = "1"
    test_update_player(base_url, player_id)


