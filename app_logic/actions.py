from . import data
import random


class ActionCard:
    def __init__(self, action1:str, action2:str, action3:str) -> None:
        self.action1 = action1
        self.action2 = action2
        self.action3 = action3


class CardDeck:
    def __init__(self, round_phase: str) -> None:
        self.round_phase = round_phase
        self.rank_1_actions = list()
        self.rank_2_actions = list()
        self.rank_3_actions = list()
        self._build_deck()
    
    def _build_deck(self) -> None:
        data_manager = data.DataRequest()
        actions = data_manager.get_actions_data()
        phase_actions = actions.loc[actions['battle_round_phase'].str.lower() == f'{self.round_phase} phase']
        self.rank_1_actions = list(phase_actions['action_one'])
        self.rank_2_actions = list(phase_actions['action_two'])
        self.rank_3_actions = list(phase_actions['action_three'])

    def pull_card(self) -> ActionCard:
        return ActionCard(
            random.choice(self.rank_1_actions),
            random.choice(self.rank_2_actions),
            random.choice(self.rank_3_actions)
        )
        


