import requests
import configparser


def read_config(path, section, parameter):
    config = configparser.ConfigParser()
    config.read(path)
    value = config.get(section, parameter)
    return value


class YandexDisk:

    def __init__(self, token: str):
        self.token = token
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def make_dir(self, dir_name):
        # headers = {
        #     'Content-Type': 'application/json',
        #     'Authorization': f'OAuth {self.token}'
        # }
        # проверяю наличие каталога с заданным именем, если его нет, создаю
        url = 'https://cloud-api.yandex.net/v1/disk/resources/'
        params = {'path': f'disk:/{dir_name}'}
        result = requests.put(url, headers=self.headers, params=params)
        return result.status_code


if __name__ == '__main__':
    yandex_token = read_config('tokens.ini', 'Tokens', 'YandexToken')
    my_yandex = YandexDisk(yandex_token)
    print(my_yandex.make_dir('Test directory'))