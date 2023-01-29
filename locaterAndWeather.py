# %%
"""



"""
# imported libraries
import os

import socket
import requests
import re
import http.client

#global variables
# main welcome intro text
mainIntroText = """Welcome to Locator and weather app
    Here you can check weather and your ip
    """
########################################################################





# check the router and seach for the ip address
# return router ip4
def get_network_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# check computer ip and name
# return host name and ip


def get_host():
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    return hostname, IPAddr

# make request for public ip from free api 'https://api.ipify.org'
# return public ip


def get_public_ip():
    try:
        ip = requests.get('https://api.ipify.org').text
    except:
        ip = "Error: Not able to get public IP, check your internet connection."
    return ip

# make request for ip address from free api "http://ip-api.com/xml/"
# need ip address
# return address, isp


class Get_IP_Address():

    def __init__(self, ip) -> None:
        self.ip = ip

    def makeRequest(self):
        try:
            self.ipAddress = requests.get(
                "http://ip-api.com/xml/{}".format(self.ip)).text
        except:
            self.ipAddress = None

    def searchXml(self, find):
        pattern = "(?<={}\>)(.*?)(?=\<)"
        return re.search(pattern.format(find), self.ipAddress).group()

    def get_city_country(self):
        try:
            return self.searchXml("city"), self.searchXml("countryCode")
        except:
            return None, None

    def get_address(self):
        try:
            address = f"""Address: {self.searchXml("city")}, {self.searchXml("region")}, {self.searchXml("country")}, {self.searchXml("zip")}
Cordinates: Latitude {self.searchXml("lat")}, Longitude {self.searchXml("lon")}
ISP: {self.searchXml("isp")}
Timezone: {self.searchXml("timezone")}"""
        except:
            address = "Error: Not able to get your address, check your internet connection."
        return address


# get weather frow free api https://rapidapi.com/community/api/open-weather-map/endpoints
# require city and countryCode


def get_weather(city, countryCode):
    conn = http.client.HTTPSConnection(
        "community-open-weather-map.p.rapidapi.com")

    headers = {
        'x-rapidapi-key': "a27170578fmsh27610de55ba0128p1beb08jsn19df35ecf23a",
        'x-rapidapi-host': "community-open-weather-map.p.rapidapi.com"
    }

    url = str("/weather?q=")+city+str("%2C")+countryCode + \
        str("&lat=0&lon=0&callback=test&id=2172797&lang=null&units=%22metric%22%20or%20%22imperial%22&mode=xml%2C%20html")

    conn.request("GET", url, headers=headers)

    res = conn.getresponse()
    data = res.read()
    decodeData = data.decode("utf-8")

    def _searchXml(find, type=str):
        if type == int:
            pattern = "(?<={}\":)([\.\d]+)"
        else:
            pattern = "(?<={}\":\")(.*?)(?=\")"
        return re.search(pattern.format(find), decodeData).group()

    return f"""Local Weather:
\t{_searchXml("main")}: {_searchXml("description")}
\tTemparature: {float("{:.2f}".format(float(_searchXml("temp",int))-273))} Celsuis
\tFeels Like: {float("{:.2f}".format(float(_searchXml("feels_like",int))-273))} Celsuis
\tHumidity: {_searchXml("humidity",int)}%
\tDay Length: {float("{:.2f}".format((int(_searchXml("sunset",int))-int(_searchXml("sunrise",int)))/60/60))} Hours 
    """


# print all the functions
def locaterAndWeather():
    print("Your Network IP: {}".format(get_network_ip()))

    computerName, computerIP = get_host()
    print(f"""Your Computer IP: {computerIP}
Your Computer Name: {computerName}""")

    publicIP = get_public_ip()
    print(f"Your public IP: {publicIP}")

    # create address
    address = Get_IP_Address(get_public_ip())
    # make a request for address
    address.makeRequest()
    # print address
    print(f"{address.get_address()}")

    # get city, country code
    city, countryCode = address.get_city_country()
    if city:
        # if city is avaliable thew get weather and print
        print(get_weather(city.lower(), countryCode.lower()))


########################################################################

# Print new line.
# Can have argument to print multiple Lines
def printLine(n=1):
    print("-"*22 + "\n"*n)

# ClearConsole


def clearConsole():
    os.system('cls' if os.name == 'nt' else 'clear')


# this is main function where all calls happens for the script
# User will be asked again and again to play until exits
def main():

    while True:
        # playFunction()
        locaterAndWeather()
        x = input("Do you want to play again.(Y/N):")
        if x.lower().startswith("y"):
            clearConsole()
            continue
        else:
            break

    print("\n\n---------------------\n Thank You :)\nCome Back Soon\n CodedBy:0001\n---------------------")
    printLine(2)
    x = input("Press any key to exit:")


# Start the script if its opened directly
if __name__ == '__main__':
    print(mainIntroText)

    main()


"""



"""




