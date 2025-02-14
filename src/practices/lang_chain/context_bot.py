import os

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import START, MessagesState, StateGraph

os.environ["LANGCHAIN_PROJECT"] = "testing-site"
os.environ["LANGCHAIN_TRACING_V2"] = "true"

model = ChatOpenAI(model="gpt-4o-mini")

workflow = StateGraph(state_schema=MessagesState)


def call_model(state: MessagesState):
    result = model.invoke(state["messages"])
    return {"messages": result}


workflow.add_edge(START, "model_call")
workflow.add_node("model_call", call_model)

memory = MemorySaver()

app = workflow.compile(checkpointer=memory)

my_config = {"configurable": {"thread_id": "rahul"}}


def invoke_lang_graph(query: str, config: dict):
    one_message = [HumanMessage(content=query)]
    output = app.invoke({"messages": one_message}, config)
    print(output["messages"][-1].pretty_print())


if __name__ == '__main__':
    invoke_lang_graph("Who is the first president of India?", my_config)

    invoke_lang_graph("And the second one?", my_config)
