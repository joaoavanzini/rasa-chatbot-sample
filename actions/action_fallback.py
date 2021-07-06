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
        
        text = tracker.latest_message['text']
        

        variacao = choice(
            [
                "Ops...",
                "Poxa...",
                "Poxa vida...",
                "Foi mal...",
                "Caramba..."
            ]
        )

        events = [e['name'] for e in tracker.events if e['event'] == 'action' and e['name'] not in ['action_listen']]
        if events[-1] != self.name():
            dispatcher.utter_message(
                choice(
                    [
                        f"{variacao} me desculpe, mas não consegui entender.",
                        "Desculpe, mas não consegui entender o que você disse.",
                        "Não entendi muito bem o que você disse, ainda estou aprendendo.",
                        f"{variacao}, não entendi o que você quis dizer, tente repetir de outra forma.",
                        f"{variacao}, não achei o que você está procurando."
                    ]
                )
            )
            dispatcher.utter_message("Tente me escrever o que precisa com outras palavras...")
        else:
            if events[-2] != self.name():
                dispatcher.utter_message(
                    choice(
                        [
                            f"{variacao} ainda não consegui entender.",
                            "Ainda não consegui entender.",
                            "Ainda não ficou muito claro.",
                            "Ainda não achei o que você está procurando.",
                            f"{variacao} ainda não entendi."
                        ]
                    )
                )
                dispatcher.utter_message("Tente me escrever o que precisa com outras palavras...")
            else:
                dispatcher.utter_message("Realmente não consegui entender. 😕")
                dispatcher.utter_message("Tentaremos a conversa novamente mais tarde.")

        # Revert user message which led to fallback.
        return [UserUtteranceReverted()]