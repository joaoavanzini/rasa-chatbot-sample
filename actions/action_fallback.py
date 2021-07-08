#==================================================================
# Action Fallback - implementa mensagens personalizadas para o
# default fallback
#==================================================================
from .__init__ import *

from random import choice
from rasa_sdk.events import UserUtteranceReverted
from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet 


class ActionDefaultFallback(Action):
    """Executes the fallback action and goes back to the previous state
    of the dialogue"""

    def name(self) -> Text:
        return "action_default_fallback"

    async def run(
            self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any],
            ) -> List[Dict[Text, Any]]:
        
        text = tracker.get_intent_of_latest_message()
        print (text)

        # Revert user message which led to fallback.
        return []