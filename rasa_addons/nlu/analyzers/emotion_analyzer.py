from rasa.nlu.components import Component
from rasa.nlu import utils
from rasa.nlu.model import Metadata

import nltk
import os

class EmotionAnalyzer(Component):
    """A pre-trained emotion component"""

    name = "emotion_analyzer"
    provides = ["entities"]
    requires = []
    defaults = {}
    language_list = ["en"]


    def __init__(self, component_config=None):
        super(EmotionAnalyzer, self).__init__(component_config)


    
    def train(self, training_data, cfg, **kwargs):
        """Not needed, because the the model is pretrained"""
        pass



    def convert_to_rasa(self, value, confidence):
        """Convert model output into the Rasa NLU compatible output format."""
        
        entity = {"value": value,
                  "confidence": confidence,
                  "entity": "emotion",
                  "extractor": "emotion_extractor"}

        return entity


    def process(self, message, **kwargs):
        """Retrieve the text message, pass it to the classifier
            and append the prediction results to the message class."""
        pass

    def persist(self, model_dir):
        """Pass because a pre-trained model is already persisted"""

        pass
