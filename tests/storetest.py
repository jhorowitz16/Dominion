import unittest
import sys
sys.path.append('../')
from store import Store

class TestStoreMethods(unittest.TestCase):

    def test_init_store_two_players(self):
        store = Store()
        self.assertEqual(store.num_players, 2)
        inven = store.base_inventory
        self.assertEqual(inven["COPPER"], 46 + (7 * 2))
        self.assertEqual(inven["SILVER"], 40)
        self.assertEqual(inven["GOLD"], 30)
        self.assertEqual(inven["ESTATE"], 8)
        self.assertEqual(inven["DUCHY"], 8)
        self.assertEqual(inven["PROVINCE"], 8)


    def test_init_store_three_players(self):
        store = Store(3)
        self.assertEqual(store.num_players, 3)
        inven = store.base_inventory
        self.assertEqual(inven["COPPER"], 39 + (7 * 3))
        self.assertEqual(inven["SILVER"], 40)
        self.assertEqual(inven["GOLD"], 30)
        self.assertEqual(inven["ESTATE"], 12)
        self.assertEqual(inven["DUCHY"], 12)
        self.assertEqual(inven["PROVINCE"], 12)

    def test_init_store_four_players(self):
        store = Store(4)
        self.assertEqual(store.num_players, 4)
        inven = store.base_inventory
        self.assertEqual(inven["COPPER"], 32 + (7 * 4))
        self.assertEqual(inven["SILVER"], 40)
        self.assertEqual(inven["GOLD"], 30)
        self.assertEqual(inven["ESTATE"], 12)
        self.assertEqual(inven["DUCHY"], 12)
        self.assertEqual(inven["PROVINCE"], 12)

    def test_init_store_five_players(self):
        store = Store(5)
        self.assertEqual(store.num_players, 5)
        inven = store.base_inventory
        self.assertEqual(inven["COPPER"], 85 + (7 * 5))
        self.assertEqual(inven["SILVER"], 80)
        self.assertEqual(inven["GOLD"], 60)
        self.assertEqual(inven["ESTATE"], 12)
        self.assertEqual(inven["DUCHY"], 12)
        self.assertEqual(inven["PROVINCE"], 15)

    def test_init_store_six_players(self):
        store = Store(6)
        self.assertEqual(store.num_players, 6)
        inven = store.base_inventory
        self.assertEqual(inven["COPPER"], 78 + (7 * 6))
        self.assertEqual(inven["SILVER"], 80)
        self.assertEqual(inven["GOLD"], 60)
        self.assertEqual(inven["ESTATE"], 12)
        self.assertEqual(inven["DUCHY"], 12)
        self.assertEqual(inven["PROVINCE"], 18)

    def test_buy(self):
        store = Store(2)
        count = 8
        while count > 0:
            buy_res = store.buy("PROVINCE")
            count -= 1
            self.assertEqual(store.base_inventory["PROVINCE"], count)
            self.assertEqual(buy_res, "PROVINCE")
        self.assertEqual(store.buy("PROVINCE"), None)
        self.assertEqual(store.buy("PROVINCE"), None)
        self.assertEqual(store.base_inventory["PROVINCE"], 0)


if __name__ == '__main__':
    unittest.main()
