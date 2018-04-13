from django.http import HttpResponse
from django.shortcuts import render
# from django.http import HttpResponse
from django.utils import timezone
from .models import StubInfo, BoardInfo, TestType, Record
import json
import sys
from django.views.decorators.csrf import csrf_exempt
from django.db import connection
from django.db.models import Count
import collections


@csrf_exempt
def index(request):
    select = {'day': connection.ops.date_trunc_sql('day', 'pub_date')}
    #records = Record.objects.extra(select=select).values('day').annotate(number=Count('id'))
    reportType = TestType.objects.get(name_text='安规')
    records = Record.objects.extra(select=select).values('day').annotate(number=Count('id')).order_by('day')
    print(request.user.username)
    response_packet = {"response": "cmd", "data": " ", "status": "error"}
    print(records)
    data={}
    for record in records:
        data[record['day']]=record['number']
    #response_packet['data'] = {"user1":"name1","user2":"name2"}
    response_packet['data']=data
    return HttpResponse(json.dumps(response_packet), content_type="application/json")

@csrf_exempt
def getDataAnalysis(request):
    select = {'day': connection.ops.date_trunc_sql('day', 'pub_date')}
    #records = Record.objects.extra(select=select).values('day').annotate(number=Count('id'))
    #reportType = TestType.objects.get(name_text='安规')
    #records = Record.objects.filter(test_type=reportType).extra(select=select).values('day').annotate(number=Count('id'))
    records = Record.objects.extra(select=select).values('day').annotate(number=Count('id')).order_by('day')
    angui = TestType.objects.get(name_text='安规')
    anguiRecords = Record.objects.all().filter(test_type=angui).extra(select=select).values('day').annotate(number=Count('id'))
    board = TestType.objects.get(name_text='板级')
    boardRecords = Record.objects.all().filter(test_type=board).extra(select=select).values('day').annotate(number=Count('id'))
    #print(boardRecords)
    intege = TestType.objects.get(name_text='整机')
    integeRecords = Record.objects.all().filter(test_type=intege).extra(select=select).values('day').annotate(number=Count('id'))
    #print(request.user.username)
    response_packet = {"response": "cmd", "data": {"全部": "", "整机": "", "板级": "", "安规": ""}, "status": "error"}
    #print(records)
    dataAll=collections.OrderedDict()
    dataIntege=collections.OrderedDict()
    dataAngui=collections.OrderedDict()
    dataBoard=collections.OrderedDict()
    for record in records:
        #print(record)
        dataAll[record['day']] = record['number']
        dataIntege[record['day']] = 0
        dataAngui[record['day']] = 0
        dataBoard[record['day']] = 0

    #print(dataAll)
    for record in integeRecords:
        dataIntege[record['day']]=record['number']


    for record in anguiRecords:
        dataAngui[record['day']]=record['number']

    for record in boardRecords:
        dataBoard[record['day']]=record['number']

    response_packet['data']['全部'] = dataAll
    response_packet['data']['整机'] = dataIntege
    response_packet['data']['板级'] = dataBoard
    response_packet['data']['安规'] = dataAngui
    return HttpResponse(json.dumps(response_packet), content_type="application/json")


@csrf_exempt
def report(request):
    if request.method == 'POST':
        request_packet = json.loads(request.body.decode('utf-8'))
        response_packet = {"response": "cmd", "data": " ", "status": "error"}
        try:
            response_packet['response'] = request_packet['request']

            if request_packet['request'] != "report":
                return HttpResponse(json.dumps(response_packet), content_type="application/json")

            request_data = request_packet['data']

            reportType = TestType.objects.get(name_text=request_data['type'])
            #reportResult = True if request_data['result'] == 'True' else False
            newReportSet = Record.objects.filter(sn_text=request_data['sn'], test_type=reportType)
            if newReportSet.exists() == True:
                newReport = newReportSet[0]
            else:
                newReport = Record()
            newReport.sn_text = request_data["sn"]
            newReport.test_type = reportType
            newReport.result_integer = 100
            newReport.report_text = request_data['report']
            newReport.pub_date = timezone.now()
            newReport.factory_text = request_data['factory']
            newReport.person_text = request_data['person']
            newReport.approved_bool = False
            newReport.save()
            response_packet['data'] = {"reportid": newReport.id}
            response_packet['status'] = "success"
            # try:
            #    device = Dev.objects.get(sn_text=request_data["sn"]);
            #    devTest = DevTest(testtype=reportType,dev=device,record=newReport);
            #    devTest.save();
            # except:
            #    print("------------Unexpected error:", sys.exc_info())
            #    newReport.delete()
            #    response_packet['data']="create dev or testType first"
            #    return HttpResponse(json.dumps(response_packet), content_type="application/json")
            # 关联被测设备和报表
            # response_packet['data']={"reportid":newReport.id,"devTestId":devTest.id}
            # response_packet['status']="success";

        except:
            print("Unexpected error:", sys.exc_info())
            return HttpResponse(json.dumps(response_packet), content_type="application/json")
        return HttpResponse(json.dumps(response_packet), content_type="application/json")
    return HttpResponse("not post")


@csrf_exempt
def stubInfo(request):
    if request.method == 'POST':
        request_packet = json.loads(request.body.decode('utf-8'))
        response_packet = {"response": "cmd", "data": " ", "status": "error"}
        try:
            response_packet['response'] = request_packet['request']
            # print(request_packet)
            if request_packet['request'] != "stubinfo":
                return HttpResponse(json.dumps(response_packet), content_type="application/json")
            request_data = request_packet['data']
            # TODO BEGIN

            # print(StubInfo.objects.all())
            infoSet = StubInfo.objects.filter(stub_text=request_data['stub'])
            if infoSet.exists() == True:
                stubInfo = infoSet[0]
            else:
                stubInfo = StubInfo()
            stubInfo.stub_text = request_data['stub']
            stubInfo.sim_text = request_data['sim']
            stubInfo.board_text = request_data['board']
            stubInfo.ammeter1_text = request_data['ammeter1']
            stubInfo.ammeter2_text = request_data['ammeter2']
            stubInfo.gun1_text = request_data['gun1']
            stubInfo.gun2_text = request_data['gun2']
            stubInfo.gun_vendor_text = request_data['vendor']
            stubInfo.power_module_text = request_data['power']

            stubInfo.save()
            response_packet['data'] = {"id": stubInfo.id}
            response_packet['status'] = "success";
            # END

        except:
            print("Unexpected error:", sys.exc_info())
            return HttpResponse(json.dumps(response_packet), content_type="application/json")
        return HttpResponse(json.dumps(response_packet), content_type="application/json")
    return HttpResponse("not post")


@csrf_exempt
def boardInfo(request):
    if request.method == 'POST':
        request_packet = json.loads(request.body.decode('utf-8'))
        response_packet = {"response": "cmd", "data": " ", "status": "error"}
        try:
            response_packet['response'] = request_packet['request']
            # print(request_packet)
            if request_packet['request'] != "boardinfo":
                return HttpResponse(json.dumps(response_packet), content_type="application/json")
            request_data = request_packet['data']
            print(request_data)
            # TODO BEGIN
            infoSet = BoardInfo.objects.filter(board_text=request_data['board'])
            if infoSet.exists() == True:
                info = infoSet[0]
            else:
                info = BoardInfo()
            # info = BoardInfo();
            info.board_text = request_data['board']
            info.dcd_text = request_data['dcd']
            info.dcm_text = request_data['dcm']
            info.pwr_text = request_data['pwr']
            info.cpu_text = request_data['cpu']
            info.g4_text = request_data['g4']
            info.ddb_text = request_data['ddb']
            info.dcr_text = request_data['dcr']
            info.led_text = request_data['led']
            info.save()
            response_packet['data'] = {"id": info.id}
            response_packet['status'] = "success";
            # END

        except:
            print("Unexpected error:", sys.exc_info())
            return HttpResponse(json.dumps(response_packet), content_type="application/json")
        return HttpResponse(json.dumps(response_packet), content_type="application/json")
    return HttpResponse("not post")
