from typing import Dict, Set

from vis_escape.game.core.rules import AlwaysAllowRule
from vis_escape.objects.item import Item
from vis_escape.objects.receptacle import Receptacle


class TV(Receptacle):
    def __init__(self, id: str, interactable_states: Dict[str, Set[str]]):
        super().__init__(
            id=id,
            possible_states={"off", "on"},
            initial_state="off",
            interactable_states=interactable_states,
        )
