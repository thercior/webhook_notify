from django.conf import settings
import requests


class CallMeBot:

    def __init__(self):
        self.__base_url = settings.CALLMEBOT_API_URL
        self.__phone_number = settings.CALLMEBOT_PHONE_NUMER
        self.__api_key = settings.CALLMEBOT_API_KEY

    def send_message(self, message):
        response = requests.get(
            url=f'{self.__base_url}?phone={self.__phone_number}&text={message}&apikey={self.__api_key}'
        )

        return response.text
