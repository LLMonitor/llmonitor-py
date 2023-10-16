from llmonitor import monitor, users, agent, tool
import openai
import os
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.environ.get('OPENAI_API_KEY')

monitor(openai)

with users.identify('user1', user_props={"email": "123@gle.com"}):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=[{"role": "user", "content": "Hello world"}]
    )
    print(completion.choices[0].message.content)


@agent("My great agent", user_id="123", tags=["test", "test2"])
def my_agent(a, b, c, test, test2):
    tool1("hello")
    output = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello world"}],
        user_id="123",
    )
    print(output)
    tool2()
    return "Agent output"


@tool(name="tool 1", user_id="123")
def tool1(a):
    return "Output 1"


@tool()
def tool2():
    return "Output 2"


my_agent(1, 2, 3, test="sdkj", test2="sdkj")
