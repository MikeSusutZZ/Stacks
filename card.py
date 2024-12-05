cards = {
    "sharpen": {
        "priority": 3,
        "actions": ["addAttackStack", "addAttackStack"]
    },
    "approach": {
        "priority": 2,
        "actions": ["moveUpOne"]
    },
    "strafe right": {
        "priority": 4,
        "actions": ["moveRightOne"]
    }
}


class Card:
    def __init__(self, name) -> None:
        self.priority, self.actions = cards[name]['priority'], cards[name]["actions"]
        self.name = name

    def useCard(self, target, gameState):
        for action in cards[self.name]["actions"]:
            target.takeAction(action, gameState)