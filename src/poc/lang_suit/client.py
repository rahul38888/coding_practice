from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8080/greet/")

if __name__ == '__main__':
    response = remote_chain.invoke({"relation": "crush", "my_text": "Hey Anika. Would you go on a date with me?"})
    print(response)
