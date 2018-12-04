from flask import request, abort


class requestValidate():
    def __init__(self, request):
        if request.content_length == 0:
            abort(401)
        postData = request.get_json()
        keys = sorted(postData)
        for key in keys:
            print("%s=%s" % (key, postData[key]))
