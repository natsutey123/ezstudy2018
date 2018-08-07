from __future__ import print_function
# from future.standard_library import install_aliases
# install_aliases()
from django.views.decorators.csrf import csrf_exempt

from urllib.parse import urlparse, urlencode
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from django.http import JsonResponse, HttpResponse
from var_dump import var_dump

import json
import os

# from flask import Flask
# from flask import request
# from flask import make_response


# Flask app should start in global layout


@csrf_exempt
def webhook(request):
    if request.method == 'POST':
        if request.body:
            json_data = json.loads(request.body)
            result = json_data['queryResult']
            with open('/Desktop/ezstudy2018/ezstudy2018/try.txt', 'w') as file:
                file.write(json.dumps(json_data))
            return JsonResponse(json_data)
    # result = json_data['queryResult']
    # action = queryResult[action]
    # parameters = queryResult[parameters]


    if action != "udemySearchCourse":
        return HttpResponse({})
    else:
        requirement = "parameters"
        r_searchcourse = requests.get('https://www.udemy.com/api-2.0/courses/',
                                  auth=('EvBrZjvwgbY6iXWujMJE1qnNrZTmaOnDVpC57Sl9',
                                        'neaBg8yIevDFSIXZpKZix6QyksQ2707REavzABZ507HjLtlzKKiBdvoqyvVLXWb3DptFnj7D6fGTk3YUbpc1Qtaj6gvMm24S63lSQlq4qiMbzCwiI3tKtOoG6C22IKze'),
                                  params=requirement)
        content = r_searchcourse.json()
        content_data = content['results']
        content_result = content_data[00]
        course_urls = "https://www.udemy.com" + content_result['url']
        course_title = content_result['title']

        speech = "This is your best course" + '\n' + course_title + '\n' + course_urls

        print("Response:")
        print(speech)

    return {
    "speech": speech,
    "fulfillmentText": speech,
    "source": "UdemyApi"
    }
# req = request.get_json(silent=True, force=True)
# print("Request:")
# print(json.dumps(req,indent=4))

# res = processRequest(req)
# res = json.dumps(res, indent=4)

# r = make_response(res)
# r.headers['Content-Type'] = 'application/json'
# return r


# def processRequest(req):
#     print("here I am....")
#     print("starting processRequest...",req.get("queryResult").get("action"))
#     if req.get("queryResult").get("action") != "udemySearchCourse":
#         print("Pls check action name in DialogFlow")
#         return {}
#     print("111111111111")
#     baseurl = "https://query.yahooapis.com/v1/public/yql?"
#     print("1.5 1.5 1.5")
#     yql_query = makeYqlQuery(req)
#     print("2222222222")
#     if yql_query is None:
#         return {}
#     yql_url = baseurl + urlencode({'q': yql_query}) + "&format=json"
#     print("3333333333")
#     print(yql_url)
#     result = urlopen(yql_url).read()
#     data = json.loads(result)
#     # for some the line above gives an error and hence decoding to utf-8 might help
#     # data = json.loads(result.decode('utf-8'))
#     print("44444444444")
#     print(data)
#     res = udemySearchCourses(data)
#     return res

# def makeYqlQuery(req):
#     result = req.get("queryResult")
#     parameters = result.get("parameters")
#     search = parameters.get("search")
#     price = parameters.get("price")
#     instructional_level = parameters.get("instructional_level")

#     if search & price & instructional_level is None:
#         return None
#     return {}


# def udemySearchCourses(data):

#     requirement = data.get('query')
#     r_searchcourse = requests.get('https://www.udemy.com/api-2.0/courses/',
#                                auth=('EvBrZjvwgbY6iXWujMJE1qnNrZTmaOnDVpC57Sl9', 'neaBg8yIevDFSIXZpKZix6QyksQ2707REavzABZ507HjLtlzKKiBdvoqyvVLXWb3DptFnj7D6fGTk3YUbpc1Qtaj6gvMm24S63lSQlq4qiMbzCwiI3tKtOoG6C22IKze'),
#                                   params=requirement)
#     content = r_searchcourse.json()
#     content_data = content['results']
#     content_result = content_data[00]
#     course_urls = "https://www.udemy.com" + content_result['url']
#     course_title = content_result['title']

#     speech = "This is your best course" + '\n' + course_title + '\n' + course_urls

#     print("Response:")
#     print(speech)

#     return {
#         "speech": speech,
#         "displayText":speech,
#         "source": "UdemyApi"
#     }

