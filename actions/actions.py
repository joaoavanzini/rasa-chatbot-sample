# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from rasa_sdk.forms import FormValidationAction
from rasa_sdk.types import DomainDict
from rasa_sdk.events import SlotSet 
#
#
class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "validate_nome"

    def run(self, 
            dispatcher: CollectingDispatcher,
            slot_value: Any,
            tracker: Tracker,
            domain: DomainDict,
            )-> Dict[Text, Any]:
        
        nome = slot_value

        # Imprimir hello world para o usuário
        dispatcher.utter_message(text=nome)

        return []
