from typing import Dict, Set

from vis_escape.game.core.rules import AlwaysAllowRule, TriggerActiveRule
from vis_escape.objects.item import Item
from vis_escape.objects.receptacle import Receptacle


class MovingBookshelfFixed(Receptacle):
    def __init__(self, id: str, interactable_states: Dict[str, Set[str]]):
        super().__init__(
            id=id,
            possible_states={"fixed", "original", "moved"},
            initial_state="fixed",
            interactable_states=interactable_states,
        )

        self.add_transition(
            "original", "push_bookshelf_to_right", "moved", AlwaysAllowRule()
        )
        self.add_transition(
            "moved", "push_bookshelf_to_left", "original", AlwaysAllowRule()
        )
