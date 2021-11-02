import requests

if __name__ == '__main__':
    URL = "https://www.billboard.com/charts/hot-100"
    page = requests.get(URL)

    print(page.text)














