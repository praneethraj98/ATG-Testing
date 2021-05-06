import json
import os

import requests

acceptableStatusCodes = [i for i in range(200, 400)]

# The API_KEY & USER_ID have been exposed to ensure proper working upon running,But the better approach would have been to not expose them by using Env vars

API_KEY = "97969dcb3ecab66e4d45ea0c61d0cdf4"
USER_ID = "192909431@N02"

os.system("cls")

"""A function that expects the API_KEY and USER_ID to get the JSON response, In this case it happens to be the flickr.photos.getPopular  """


def getJSONResponseFromFlickr(KEY, USER_ID):
    URL = "https://www.flickr.com/services/rest/?method=flickr.photos.getPopular&api_key={API_KEY}&user_id={USER_ID}&format=json&nojsoncallback=1".format(
        API_KEY=API_KEY, USER_ID=USER_ID
    )
    response = requests.get(URL)
    jsonResponse = response.text
    statusCode = response.status_code
    print("Status Code {statusCode}".format(statusCode=statusCode))
    if int(statusCode) in acceptableStatusCodes:
        print("Status Code :OK(<400)\n")
    else:
        print("Status Code:ERROR(>400),Please try again\n")
    print("JSON response returned is as follows:")
    print(response.text)
    print(5 * "\n")


getJSONResponseFromFlickr(API_KEY, USER_ID)
