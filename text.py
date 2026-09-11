# from tools.tavily_tool import tavily_search
# from tools.flight_tool import search_flights
# from backend import run_travel_agent
# # respone = travily_search("Best hotel in nepal")
# # print (respone)
# user_input = input ('Enter Travel plan')
# res = run_travel_agent(
#     user_input=user_input,
#     thread_id='test_user'
# )
# print(res['answer'])


import asyncio
from mcp_client import get_all_tools

if __name__ == "__main__":
    asyncio.run(get_all_tools())