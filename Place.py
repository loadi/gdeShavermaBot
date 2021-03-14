import json
import requests
from typing import Union
from random import choice
from string import ascii_uppercase


class Place:
    place: Union[int, float]

    def __init__(self, placeId: Union[int, str]) -> None:
        self.place = placeId

    def __register(self) -> dict:
        url = "https://gdesha.ru/api/v1/Devices/saveGcmToken"
        payload = f"regId=3F516D9A-FF7E-4F14-962B-{''.join(choice(ascii_uppercase) for _ in range(12))}"
        return self.__post(url, payload)["result"]["registrationId"]

    def __addMark(self, mark: int) -> None:
        url = "https://gdesha.ru/api/v1/Rates/add"
        id = self.__register()
        payload = f"placeId={self.place}&regId={id}&value={mark}"
        self.__post(url, payload)

    def flood(self, mark: int, num: int) -> None:
        try:
            for i in range(num):
                self.__addMark(mark)
                print(f"Сделано {i + 1} из {num}")
        except KeyboardInterrupt:
            print("Отправка оценок принудительно остановлена")

    def getInfo(self) -> dict:
        url = f"https://gdesha.ru/api/v1/Places/getInfo?placeId={self.place}&regId=3F516D9A-FF7E-4F14-962B-39A6977ECF7F"
        return self.__get(url)["result"]

    def __post(self, url: str, payload: str) -> dict:
        resp = requests.post(url, payload, headers={'Content-Type': 'application/x-www-form-urlencoded'})
        if resp.status_code != 200:
            raise Exception(f"Wrong response status: {resp.text}")
        else:
            return json.loads(resp.text)

    def __get(self, url: str) -> dict:
        resp = requests.get(url)
        if resp.status_code != 200:
            raise Exception(f"Wrong response status: {resp.text}")
        else:
            return json.loads(resp.text)
