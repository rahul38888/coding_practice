# from langflow.field_typing import Data
from langflow.custom import Component
from langflow.io import DataInput, Output
from langflow.schema import Data

import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")


class StopwordComponent(Component):
    display_name = "Stopword remover"
    description = "Remove stop words from a list of text"
    documentation: str = "http://docs.langflow.org/components/custom"
    icon = "code"
    name = "CustomComponent"
    stop_words = set(stopwords.words("english"))

    inputs = [
        DataInput(
            name="input_values",
            display_name="Input Values",
            info="The input values to remove stop word from",
            value="I have a dream that one day this nation will rise up and "
                  "live out the true meaning of its creed ",
            tool_mode=True,
        ),
    ]

    outputs = [
        Output(display_name="Output", name="output", method="build_output"),
    ]

    def build_output(self) -> Data:
        data_list = self.input_values if self.input_values else []

        for data in data_list:
            tokens = nltk.word_tokenize(data.data["text"])
            lemma_tokens = [t for t in tokens if t not in self.stop_words]

            data.data["text"] = " ".join(lemma_tokens)

        self.status = data_list
        return data_list
