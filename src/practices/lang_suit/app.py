import os

from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

os.environ["LANGCHAIN_TRACING_V2"] = "true"

model = ChatOpenAI(model="gpt-4o-mini")
parser = StrOutputParser()


messages = [
    SystemMessage(content="You are a friend of mine"),
    HumanMessage(content="Hey Ram! How are you?")
]

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "You are my {relation}"), ("user", "{my_text}")])


if __name__ == '__main__':

    # response = model.invoke(messages)
    # print(response.content)

    # chain = model | parser
    # response = chain.invoke(messages)
    # print(response)

    # messages = prompt_template.invoke({"relation": "wife", "my_text": "How was last night love?"})
    # print(messages.to_messages())

    chain = prompt_template | model | parser
    response = chain.invoke({"relation": "wife", "my_text": "How was last night love?"})
    print(response)

