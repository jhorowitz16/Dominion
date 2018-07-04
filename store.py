
class Store:
    def __init__(self, num_players=2):
        """
        this is at the start of the game, pre-dealing hands

        """

        # money
        copper_count = 120 if (num_players) > 4 else 60
        silver_count = 80 if (num_players > 4) else 40
        gold_count = 60 if (num_players > 4) else 30

        # VPs
        base_vp_count = 12 if (num_players > 2) else 8
        province_count = base_vp_count + (
            (num_players - 4) * 3 if (num_players > 4) else 0)

        curse_count = 10 * (num_players - 1)

        self.base_inventory = {
            "COPPER": copper_count,
            "SILVER": silver_count,
            "GOLD": gold_count,
            "ESTATE": base_vp_count,
            "DUCHY": base_vp_count,
            "PROVINCE": province_count,
            "CURSE": curse_count
        }
        self.num_players = num_players


    def buy(self, card_name):
        """
        returns boolean the card name when bought, or None when illegal buy
        on legal buy, decrement the relevant count
        """
        inven = self.base_inventory
        if card_name in inven and inven[card_name] > 0:
            # decrement the card
            inven[card_name] -= 1
            return card_name
        else:
            print("ERROR: cannot buy " + card_name)
            return None

    def __str__(self):
        s = "======\n"
        s += "players: " + str(self.num_players) + "\n"
        for k in self.base_inventory:
            s += k + ": " + str(self.base_inventory[k])
        s = "======\n"
        return s
