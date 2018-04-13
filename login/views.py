from django.http import HttpResponse
import json
import sys
from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def index(request):
    print(request.user.username)
    response_packet = {"response": "cmd", "data": " ", "status": "error"}
    response_packet['data'] = request.user.username
    return HttpResponse(json.dumps(response_packet), content_type="application/json")


@csrf_exempt
def mylogin(request):
    if request.method == 'POST':
        request_packet = json.loads(request.body.decode('utf-8'))
        response_packet = {"response": "cmd", "data": " ", "status": "error"}
        try:
            response_packet['response'] = request_packet['request']

            if request_packet['request'] != "login":
                return HttpResponse(json.dumps(response_packet), content_type="application/json")
            request_data = request_packet['data']
            print(request_data)
            # TODO BEGIN
            username = request_data['username']
            password = request_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                #login(user)
                # Redirect to a success page.
                login(request, user)
                response_packet['data'] = {"username": username}
                response_packet['status'] = "success"
            else:
                response_packet['data'] = {"username": username}
                response_packet['status'] = "fail"
            # END

        except:
            print("Unexpected error:", sys.exc_info())
            return HttpResponse(json.dumps(response_packet), content_type="application/json")
        return HttpResponse(json.dumps(response_packet), content_type="application/json")
    return HttpResponse("not post")
