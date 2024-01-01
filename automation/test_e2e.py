from automation.conftest import id
from automation.test_create_players import test_create_player
from automation.test_delete import test_delete_player
from automation.test_get_players import test_read_player
from automation.test_update_players import test_update_player


def test_run_e2e_tests(base_url , id:str):

    print("Testing Create Player API...")
    test_create_player(base_url)


    print("\nTesting Update Player API...")
    test_update_player(base_url ,id)

    print("\nTesting Read Player API...")
    test_read_player(base_url)

    print("\nTesting delete Player API...")
    test_delete_player(base_url , id)
