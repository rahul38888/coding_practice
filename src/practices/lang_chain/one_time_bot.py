import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

os.environ["LANGCHAIN_PROJECT"] = "testing-site"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

model = ChatOpenAI(model="gpt-4o-mini")


if __name__ == '__main__':
    response = model.invoke(
        [HumanMessage(content="Who is the first president of India?")])
    print(response)

    response = model.invoke(
        [HumanMessage(content="And the second one?")])
    print(response)
