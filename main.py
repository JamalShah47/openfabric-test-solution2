import os
import warnings
from ontology_dc8f06af066e4a7880a5938933236037.simple_text import SimpleText
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from openfabric_pysdk.context import OpenfabricExecutionRay
from openfabric_pysdk.loader import ConfigClass
from time import time
import json
sciencebot = ChatBot("Science Bot", read_only = False)
trainBot = ChatterBotCorpusTrainer(sciencebot)
trainBot.train ("chatterbot.corpus.english.science","data-corpus.yml")


############################################################
# Callback function called on update config
############################################################
def config(configuration: ConfigClass):
    with open("config/execution.json", "w") as jsonfile:
        configuration_obj = json.load(jsonfile)
        configuration_obj ["config_class"]  = configuration
        json.dump(configuration_obj, jsonfile)
    pass


############################################################
# Callback function called on each execution pass
############################################################
def execute(request: SimpleText, ray: OpenfabricExecutionRay) -> SimpleText:
    output = []
    for text in request.text:
        response = sciencebot.get_response(text)
        output.append(response)

    return SimpleText(dict(text=output))
