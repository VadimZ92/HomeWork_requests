# Задание 1
import requests
import json
from pprint import pprint
import os

def superhero_request():
    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url).json()
    for dict_response in response:
        for key_dict, value_dict in dict_response.items():
            if value_dict == 'Captain America':
                Captain_America_intelligence = dict_response['powerstats']['intelligence']
            if value_dict == 'Hulk':
                Hulk_intelligence = dict_response['powerstats']['intelligence']
            if value_dict == 'Thanos':
                Thanos_intelligence = dict_response['powerstats']['intelligence']
    if Thanos_intelligence > Hulk_intelligence and Thanos_intelligence > Captain_America_intelligence:
        character = 'Thanos'
    elif Captain_America_intelligence > Hulk_intelligence and Captain_America_intelligence > Thanos_intelligence:
        character = 'Captain America'
    else:
        character = 'Hulk'
    return f"Самым умным из (Captain_America, Hulk, Thanos), " \
           f"является {character}, с результатом" \
           f" {max(Captain_America_intelligence, Hulk_intelligence, Thanos_intelligence)}"


# Задание 2


class YandexDisk:


    def __init__(self, token):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }


    def _get_upload_link(self, disk_file_path):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {"path": disk_file_path, "overwrite": "true"}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path, file_name1):
        href = self._get_upload_link(disk_file_path=disk_file_path).get("href", "")
        response = requests.put(href, data=open(file_name1, 'rb'))
        response.raise_for_status()
        if response.status_code == 201:
            print("Success, загрузка на ЯндексДиск завершена")


#Задание 3

def questions_stackoverflow():
    params = {
        'sort': 'votes',
        'fromdate': 1656057920,
        'todate': 1656230720,
        'tagged': 'python',
        'site': 'stackoverflow'
    }
    req = requests.get('https://api.stackexchange.com/2.3/questions', params).json()
    return req


if __name__ == '__main__':
    print()
    print(superhero_request())
    print()
    with open('Token.txt', 'r') as file_object:
        token = file_object.read().strip()
    file_name1 = "HoumWork8.txt"
    token = token
    ya = YandexDisk(token=token)
    ya.upload_file_to_disk(disk_file_path="HoumWork8.txt", file_name1="HoumWork8.txt")
    print()
    pprint(questions_stackoverflow())