cards = {
    "advance": {
        "priority": 1,
        "actions": ["moveUpOne"]
    },
    "retreat": {
        "priority": 1,
        "actions": ["moveDownOne"]
    },
    "strafe right": {
        "priority": 1,
        "actions": ["moveRightOne"]
    },
    "strafe left": {
        "priority": 1,
        "actions": ["moveLeftOne"]
    },
    "sharpen": {
        "priority": 3,
        "actions": ["addAttackStack", "addAttackStack"]
    },
    "defend": {
        "priority": 3,
        "actions": ["addDefenceStack", "addDefenceStack"]
    },
    "charge": {
        "priority": 4,
        "actions": ["addAttackStack", "moveUpOne"]
    },
    "fortify": {
        "priority": 4,
        "actions": ["addDefenceStack", "addPriorityStack"]
    },
    "weaken": {
        "priority": 3,
        "actions": ["addNegativeDefenceStack", "addNegativePriorityStack"]
    },
    "cripple": {
        "priority": 4,
        "actions": ["addAttackStack", "addNegativeDefenceStack"]
    },
    "flank": {
        "priority": 3,
        "actions": ["moveRightOne", "addAttackStack"]
    },
    "entrench": {
        "priority": 4,
        "actions": ["addDefenceStack", "addDefenceStack"]
    },
    "strike": {
        "priority": 3,
        "actions": ["addAttackStack", "moveUpOne"]
    },
    "overwhelm": {
        "priority": 5,
        "actions": ["addAttackStack", "addAttackStack", "addAttackStack"]
    },
    "reinforce": {
        "priority": 4,
        "actions": ["addDefenceStack", "addPriorityStack"]
    },
    "deliberate advance": {
        "priority": 3,
        "actions": ["moveUpOne", "addDefenceStack"]
    },
    "reposition": {
        "priority": 2,
        "actions": ["moveUpOne", "moveLeftOne"]
    },
    "sabotage": {
        "priority": 4,
        "actions": ["addNegativeAttackStack", "addNegativePriorityStack"]
    },
    "counter": {
        "priority": 4,
        "actions": ["addAttackStack", "addDefenceStack"]
    },
    "speed burst": {
        "priority": 3,
        "actions": ["addPriorityStack", "moveUpOne"]
    },
    "sidestep": {
        "priority": 2,
        "actions": ["moveLeftOne", "moveRightOne"]
    },
    "outflank": {
        "priority": 5,
        "actions": ["moveRightOne", "addAttackStack", "moveLeftOne"]
    },
    "strategic push": {
        "priority": 5,
        "actions": ["addPriorityStack", "moveRightOne", "addDefenceStack"]
    },
    "delay": {
        "priority": 2,
        "actions": ["addNegativePriorityStack"]
    },
    "tactical retreat": {
        "priority": 3,
        "actions": ["moveDownOne", "addDefenceStack"]
    },
    "focus": {
        "priority": 4,
        "actions": ["addPriorityStack", "addAttackStack"]
    },
    "crippling blow": {
        "priority": 5,
        "actions": ["addAttackStack", "addNegativeDefenceStack"]
    },
    "barrier": {
        "priority": 4,
        "actions": ["addDefenceStack", "addDefenceStack", "addDefenceStack"]
    },
    "test": {
        "priority": 1,
        "actions": ["addNegativeAttackStackToOpp"]
    }
}



class Card:
    def __init__(self, name) -> None:
        self.priority, self.actions = cards[name]['priority'], cards[name]["actions"]
        self.name = name

    def useCard(self, target, gameState):
        for action in cards[self.name]["actions"]:
            target.takeAction(action, gameState)