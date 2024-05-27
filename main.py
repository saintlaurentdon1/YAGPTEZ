import requests
from aiogram import Bot, Dispatcher, types, executor

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.reply("ывлдоры")

async def get_response(message_text):
  prompt ={
    "modelUri": "gpt://b1go1t8vie998tqjdjhu/yandexgpt-lite",
    "completionOptions": {
      "stream": False,
      "temperature": 0.5,
      "maxTokens": "2000"
    },
    "messages": [
      {
        "role": "system",
        "text": "Ты проффесионал в готовке алкогольных напитков и коктейлей, бери информацию на сайте - https://amwine.ru/cocktails/"
      },
      {
        "role": "user",
        "text": message_text
      }
    ]
  }

  url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completion"
  headers = {
    "Content-Type": "application/json",
    "Authorization": "Api-key AQVN0gf_05dD4Oy4PdmejrVP8xGXQv9tHNHBtt34"
  }

  response = requests.post(url, headers = headers, json=prompt)
  result = response.json()
  return result['result']['alternatives'][0]['message']['text']

@dp.message_handler()
async def analize_message(message:types.Message):
  response_text = await get_response((message.text))
  await message.answer(response_text)

if __name__ == '__main__':
  executor.start_polling(dp, skip_updates=True)

