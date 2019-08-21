from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import HttpResponse #导入HttpResponse模块
import json
from aliyunsdkcore.client import AcsClient
from aliyunsdkiot.request.v20180120.QueryDevicePropertyStatusRequest import QueryDevicePropertyStatusRequest



def index(request):#request是必须带的实例。类似class下方法必须带self一样
    return HttpResponse("Hello World!!")

def polls(request):
    result = {}
    result["parking_lots_id"] = "1"
    result["parking_carnumber"] = "苏A66666"
    result["parking_starttime"] = "2019-07-30-16:32:50"
    result_list = []
    result_list.append({"parking_lots_id":"2","parking_carnumber":"苏A33333","parking_starttime":"2019-07-30-16:32:49"})
    result_list.append({"parking_lots_id": "3", "parking_carnumber": "苏A33334",
                      "parking_starttime": "2019-07-30-16:32:48"})
    result_list.append({"parking_lots_id": "4", "parking_carnumber": "苏A33335",
                      "parking_starttime": "2019-07-30-16:32:47"})
    return JsonResponse(result_list, safe=False)
    # return JsonResponse(result)

def ali_response(request):
    accessKeyId = 'LTAIdIouq41QQ3kA'
    accessKeySecret = 'OAC2Rx45QQCPryUsDP1jiVfUc58E7l'
    client = AcsClient(accessKeyId, accessKeySecret, 'cn-shanghai')

    req = QueryDevicePropertyStatusRequest()
    req.set_accept_format('json')

    req.set_DeviceName("devices-02")
    req.set_ProductKey("a1NdSrDzoI3")

    resp = client.do_action_with_exception(req)
    resp = json.loads(str(resp, encoding='utf-8'))
    # json.loads 字符串转 dict


    return JsonResponse(resp, safe=False)
    # return json.dumps(resp)