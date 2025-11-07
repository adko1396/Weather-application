import socket
import ntplib
from time import ctime
import countries
import requests
import sys


def Weather(CityName):
    city = CityName

    url = f"https://wttr.in/{city}"

    try:
        ResP = requests.get(url)
        print(ResP.text)
        MyGithub(True)
        # print("🌐 Github: adko1396  \n")
    except Exception:
        print("🌐 Please connect to the internet to use this application!")


def check_internet(host="8.8.8.8", port=53, timeout=3):
    try:
        socket.setdefaulttimeout(timeout)
        socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
        return True
    except socket.error:
        return False


def get_internet_time():
    try:
        client = ntplib.NTPClient()
        response = client.request("pool.ntp.org")
        print("                      🕓 Date : ", ctime(response.tx_time))
    except Exception as e:
        print("")


def MyGithub(a=False):
    if a == False:
        get_internet_time()

        print(
            """

                   |----------[⛅ Weather App ⛅]----------|


+@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @+
@@                                                     @@
@@      ^^^^^                                          @@
@@     /__-__\   Programming isn't about what you know @@
@@    (| o.o |)   It's about what you can figure out   @@
@@      \   /                                          @@
@@     _/   \_                                         @@
@@    (       )     .----------------------------.     @@
@@   / /     \ \    |   Github:    adko1396      |     @@
@@   \ |     | /    '----------------------------'     @@
@@    \|     |/                                        @@
@@     |_   _|                                         @@
@@     | | | |                                         @@
@@     ( ) ( )   Testing leads to failure              @@
@@     |_| |_|   and failure leads to understanding    @@
@@ _.-' _j L_ '-._                                     @@
@@(___.'     '.___)                                    @@
+@ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @ @+
"""
        )
    else:
        print(
            """
        +======================+
        |    !G I T H U B!     |
        |                      |
        |        /\_/\         |
        |       (>o.o<)        |
        |                      |
        |     ID: ADKO1396     |
        |                      |
        +======================+
"""
        )


def help():
    print("🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨⛅🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨🟨 \n")
    print(
        "⭕ To see the weather in your city, simply type its name and you'll be able to view the forecast. \n"
    )
    print("💻 Type : Your city name \n")
    print("📃 |=> To view the list of countries, type the 'countries' command. \n")
    print("💻 |=> Type : countries \n")
    print("🚪 |=> To exit the program, type 'exit'\n")


def Start():
    print("🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦⛅🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦🟦 \n")
    print(
        "🖤 Hello, welcome to the weather app! If you like this app, please follow my GitHub. Thank you! For guidance. \n"
    )
    print("🛑 you can use the help command \n")
    print("💻 Type : help \n")


def City_Help():
    print("🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫⛅🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫🟫 \n")
    print("🌄 To view the cities of your country, type : \city_help. \n")
    print("💻 Type : \city_help \n")


def get_country_function():
    Countries_Value = countries
    print(" \n")
    print(
        "❌ To enter your country, you must write the first letter of your country in uppercase. For example: Iran Or Turkey Or Germany   \n  \n"
    )
    value = input("🌌 Enter the name of your country : ")
    function_name = f"Countries_Value.{value}"
    try:
        country_function = getattr(Countries_Value, value)
        Countries_Value.CountryName_All_V4(value)
        return country_function()

    except AttributeError:
        print(f"❌ Function for country '{value}' not found!")
        return None


def Value_User():
    value = input("💬 Type Command : ")

    if value == "exit":
        sys.exit(0)

    if value == "help":
        help()
        Value_User()
    if value == "countries":
        Countries_Value = countries
        Countries_Value.all()
        City_Help()

        Value_User()
    if value == "\city_help":
        get_country_function()

        Value_User()

    else:
        Weather(value)
        Value_User()


def main():
    if check_internet():
        MyGithub()

        Start()

        Value_User()

    else:
        print("🌐 Please connect to the internet to use this application! ")


if __name__ == "__main__":
    main()
