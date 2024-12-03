cards = {
    "sharpen": ["addAttackStack", "addAttackStack"]
}

class Card:
    def __init__(self, name) -> None:
        self.actions = cards[name]
        self.name = name

    def useCard(self, target):
        for action in cards[self.name]:
            target.takeAction(action)