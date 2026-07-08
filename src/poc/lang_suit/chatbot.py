import uuid
from operator import itemgetter

from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory
from langchain_core.messages import HumanMessage, trim_messages, AIMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_openai import ChatOpenAI

store = dict()

model = ChatOpenAI(model="gpt-4o-mini")


def get_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


# with_message_history = RunnableWithMessageHistory(model, get_history)
#
# config = {"configurable": {"session_id": str(uuid.uuid4())}}
#
# response = with_message_history.invoke(
#     [HumanMessage(content="Suggest one name for my tech Youtube channel")],
#     config=config
# )
#
# print(response.content)
#
#
# response = with_message_history.invoke(
#     [HumanMessage(content="Tell me one more")],
#     config=config
# )
#
# print(response.content)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a professional coach here to help users with their career."),
    MessagesPlaceholder(variable_name="message")
])

trimmer = trim_messages(
    max_tokens=10,
    token_counter=model,
    strategy="last",
    include_system=True,
    allow_partial=False,
    start_on="human"
)

chain = RunnablePassthrough.assign(messages=itemgetter("message") | trimmer) | prompt | model

with_message_history = RunnableWithMessageHistory(chain, get_history, input_messages_key="message")

config = {"configurable": {"session_id": str(uuid.uuid4())}}


if __name__ == '__main__':
    while True:
        text = input("Me: ")
        response = with_message_history.invoke(
            {"message": HumanMessage(text)},
            config=config
        )
        print("Anika: " + response.content)

