# from langflow.field_typing import Data
from langflow.custom import Component
from langflow.io import MessageTextInput, Output, DictInput
from langflow.schema.message import Message
from urllib.parse import urlencode


class UrlBuilderComponent(Component):
    display_name = "Url Builder"
    description = "Url builder with path and query parameters"
    # documentation: str = "http://docs.langflow.org/components/custom"
    icon = "Globe"
    name = "UrlBuilderComponent"

    inputs = [
        MessageTextInput(
            name="url_string",
            display_name="URL String",
            info="Url string",
        ),
        MessageTextInput(
            name="path_params",
            display_name="Path Parameters",
            list=True,
            info="Enter one or more path parameters, in order.",
            advanced=True,
        ),
        DictInput(
            name="query_params",
            display_name="Query Parameters",
            list=True,
            info="Enter one or more query parameters key-pairs, in order.",
            advanced=True,
        ),
    ]

    outputs = [
        Output(display_name="URL Message", name="output",
               method="build_url_message"),
    ]

    def build_url_message(self) -> Message:
        url_string = self.url_string
        if url_string[-1] == '/':
            url_string = url_string[:-1]
        url_parts = [url_string]
        url_parts.extend(self.path_params)

        url = "/".join(url_parts)

        query_params = dict()
        for k, v in self.query_params.items():
            if k:
                query_params[k] = v

        if query_params:
            url = url + "?" + urlencode(query_params)

        result = Message(text=url)
        self.status = result
        return result
