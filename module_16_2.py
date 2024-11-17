from fastapi import FastAPI, Path
from typing import Annotated
app = FastAPI()

@app.get("/")  #  При получении в запросе "/" отрабатывает функция welcome()
async def welcome() -> str:
    return "Главная страница"    # Возвращаем сообщение

@app.get("/user")  #  При получении в запросе "/user?username='Iliya'&age=24" отрабатывает функция user_3()
async def user_3(username=str, age=int) -> str:
        return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

@app.get("/user/admin")  #  При получении в запросе "/user/admin" отрабатывает функция user_1()
async def user_1() -> str:
        return "Вы вошли как администратор"

@app.get("/user/{user_id}")  #  При получении в запросе "/user/123" отрабатывает функция user_2()
async def user_2(user_id: Annotated[int, Path(ge=1,                         # user_id только больше или равен нулю
                                              le=100,                       # user_id не более ста
                                              description="Enter User ID",  # описание для ввода user_id
                                              example=1)]) -> str:          # пример

        return f"Вы вошли как пользователь № {user_id}"  # Возвращаем сообщение

@app.get("/user/{username}/{age}")
async def user_4(username: Annotated[str, Path(min_length=5,                       # минимальная длина
                                               max_length=20,                      # максимальная длина
                                               description="Enter your username",  # Описание для ввода username
                                               example="montes")],                 # Пример
                age: Annotated[int, Path(ge=18,                              # age только больше или равен 18
                                    le=120,                                  # age не более 120
                                    description="Enter username",            # описание для ввода age
                                    example=24)]) -> dict:                   # пример age
        return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

"""
  Запускаем в терминале PyCharm
python -m uvicorn module_16_2:app  
      где module_16_2 - имя файла, 
      app - объект FastAPI() в коде module_16_2.py

Для входа в FastAPI Swagger UI вводим http://127.0.0.1:8000/docs
"""