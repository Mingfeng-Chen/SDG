# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 18:59:18 2023

@author: 34677
"""

import os
import openai

openai.api_key = ""
messages=[
  {"role": "system", "content": "You are a poetic assistant who excels in describing visually appealing scenes with a creative talent."},
  {"role": "user", "content": "According to the semantic meaning of the text, this paragraph can be divided into several scenarios. Please describe these scenarios in English phrases in detail and have a visual sense:"}
]
Chinese = "孔子于乡党，恂恂如也，似不能言者；其在宗庙朝庭，便便言，唯谨尔。"
messages[1]["content"] = messages[1]["content"] + Chinese
print(messages)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=messages
)
answer = completion.choices[0].message["content"]
print(answer)

num_scene = answer.count("Scen")
all_scene = []
for i in range(num_scene):
    all_scene.append(answer.split('\n')[3 * i + 1])
print(all_scene)


