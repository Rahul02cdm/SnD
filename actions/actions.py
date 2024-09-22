from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

from typing import Any, Text, Dict, List
import requests, json
from . import utils
# from . import rasa_cmd as cmd

# class ActionVehicleTechnicalCharacteristics(Action):
#     def name(self) -> Text:
#         return "action_vehicle_technical_characteristics"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = "🤖 Hey! this is action_vehicle_technical_characteristics"
#         cmd.message(dispatcher, text)
#         return []
    
# class ActionRealtimeVehicleOrderingData(Action):
#     def name(self) -> Text:
#         return "action_realtime_vehicle_ordering_data"
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#         text = "🤖 Hey! this is action_realtime_vehicle_ordering_data"
#         cmd.message(dispatcher, text)
#         return []

class ActionMainButton(Action):
    def name(self) -> Text:
        return "action_main_button"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        slot = "main_category"
        main_category = tracker.get_slot(slot)
        if main_category == "vehicle_technical_characteristics":
            text = "🤖 vehicle_technical_characteristics"
            dispatcher.utter_message(text)
        elif main_category == "realtime_vehicle_ordering_data":
            text = "🤖 CHOOSE THE BELOW OPTION"
            vehicle_category = [{"payload":'/vehicle_category_button{"vehicle_category":"IDE"}',"title":"IDE"},
                               {"payload":'/vehicle_category_button{"vehicle_category":"INV"}',"title":"INV"},
                               {"payload":'/vehicle_category_button{"vehicle_category":"CHA"}',"title":"CHA"}]
            dispatcher.utter_message(text = text, buttons = vehicle_category)
        return []

class ActionVehicleCategoryButton(Action):
    def name(self) -> Text:
        return "action_vehicle_category_button"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot = "vehicle_category"
        vehicle_category = tracker.get_slot(slot)
        if vehicle_category == "IDE":
            text = "🤖 ENTER 12 DIGIT IDE VEHICLE NUMBER"
        elif vehicle_category == "INV":
            text = "🤖 ENTER 15 DIGIT INV VEHICLE NUMBER"
        elif vehicle_category == "CHA":
            text = "🤖 ENTER 17 DIGIT CHA VEHICLE NUMBER" 
        dispatcher.utter_message(text)
        return []

class ActionVehicleNumber(Action):
    def name(self) -> Text:
        return "action_Vehicle_number"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # API1 = 'https://zce-re7.intra.renault.fr:9443/internal/bcv/getVehicInfo'
        slot = "vehicle_category"
        vehicle_category = tracker.get_slot(slot)
        vehicle_number = tracker.latest_message['text']
        VNSWTCH = True
        if vehicle_category == "IDE" and len(vehicle_number) == 12:
            text = f"🤖 YOU SELECTS {vehicle_category} and {vehicle_number}"
            dispatcher.utter_message(text)
            data = {"request": {"ACTION": "SEL","TYP_CLE": vehicle_category,"CLE": vehicle_number}}
            print(data)
            # response = requests.post(url=API1,json=data,auth=("awbcv07", "VCBti435"),verify=False)
            # data = json.loads(response.text)['response']    #json.loads(response.text)
            # exist = utils.MSG_APPL(dispatcher, data)
            
        elif vehicle_category == "INV" and len(vehicle_number) == 15:
            text = f"🤖 YOU SELECTS {vehicle_category} and {vehicle_number}"
            dispatcher.utter_message(text)
            data = {"request": {"ACTION": "SEL","TYP_CLE": vehicle_category,"CLE": vehicle_number}}
            print(data)
            # response = requests.post(url=API1,json=data,auth=("awbcv07", "VCBti435"),verify=False)
            # data = json.loads(response.text)['response']    #json.loads(response.text)
            # exist =utils.MSG_APPL(dispatcher, data)
            
        elif vehicle_category == "CHA" and len(vehicle_number) == 17:
            text = f"🤖 YOU SELECTS {vehicle_category} and {vehicle_number}"
            dispatcher.utter_message(text)
            data = {"request": {"ACTION": "SEL","TYP_CLE": vehicle_category,"CLE": vehicle_number}}
            print(data)
            # response = requests.post(url=API1,json=data,auth=("awbcv07", "VCBti435"),verify=False)
            # data = json.loads(response.text)['response']    #json.loads(response.text)
            # exist =utils.MSG_APPL(dispatcher, data)

        else:
            VNSWTCH = False
            text = "🤖 PLEASE ENTER CORRECT VEHICLE NUMBER"
            dispatcher.utter_message(text)
        
        # if VNSWTCH == True:
        #     if exist == True:
        #         # text = "VEHICLE EXISTANCE"
        #         # dispatcher.utter_message(text)
        #         text = "🤖 CHOOSE THE BELOW OPTION"
        #         vehicle_info = [{"payload":'/vehicle_info_button{"vehicle_info":"DESCRIPTION"}',"title":"DESCRIPTION"},
        #                         {"payload":'/vehicle_info_button{"vehicle_info":"DEALER"}',"title":"DEALER"}]
        #         dispatcher.utter_message(text = text, buttons = vehicle_info)

        #     else:
        #         text = "🤖 SORRY!!! VEHICLE NOT EXISTS"
        #         dispatcher.utter_message(text)

        return []

class ActionVehicleInfoButton(Action):
    def name(self) -> Text:
        return "action_vehicle_info_button"
    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        slot = "vehicle_info"
        vehicle_info = tracker.get_slot(slot)
        if vehicle_info == "DESCRIPTION":
            print("DESC")
        elif vehicle_info == "DEALER":
            print("DEAL")
        return []