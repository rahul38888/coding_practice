import uvicorn
from fastapi import FastAPI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langserve import add_routes

prompt_template = ChatPromptTemplate.from_messages(
    [("system", "You are my {relation}"), ("user", "{my_text}")])

model = ChatOpenAI(model="gpt-4o-mini")

parser = StrOutputParser()

chain = prompt_template | model | parser

app = FastAPI(title="Meet and greet",
              version="1.0beta",
              description="An API demo where you meet and greet with someone")

add_routes(
    app,
    chain,
    path="/greet"
)

if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8080)
