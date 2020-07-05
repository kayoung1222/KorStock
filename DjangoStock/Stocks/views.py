from django.shortcuts import render
import requests
import xmltodict


def base(request):
    return render(request, 'Stocks/base.html')


def news(request):
    try:
        isinCdNm = request.GET['isinCdNm']
        url = "http://apis.data.go.kr/1160100/service/GetStocIssuInfoService/getItemBasiInfo?pageNo=1&numOfRows=1&resultType=xml&stckIssuCmpyNm=" + isinCdNm + "&fnccmpNm=%EA%B9%80%EC%B2%9C%EC%A0%80%EC%B6%95%EC%9D%80%ED%96%89&serviceKey=T%2BZ9WBogSOHeK9o0cygpwLmkGv3Kqmkx%2FOXFHnTevmyo%2FT%2BUqYsY7M6FSOW04r2tK0R8jeQ9Gtn9TyZBTume9A%3D%3D"

        req = requests.get(url).content
        xmlObject = xmltodict.parse(req)
        allData = xmlObject['response']['body']['items']['item']
    except Exception as e:
        allData = ""

    content = {'allData': allData}

    return render(request, 'Stocks/news.html', content)


def money(request):
    try:
        crno = request.GET['crno']
        url = "http://apis.data.go.kr/1160100/service/GetFinaStatInfoService/getSummFinaStat?pageNo=1&numOfRows=1&resultType=xml&crno=" + crno + "&fnccmpNm=%EA%B9%80%EC%B2%9C%EC%A0%80%EC%B6%95%EC%9D%80%ED%96%89&serviceKey=T%2BZ9WBogSOHeK9o0cygpwLmkGv3Kqmkx%2FOXFHnTevmyo%2FT%2BUqYsY7M6FSOW04r2tK0R8jeQ9Gtn9TyZBTume9A%3D%3D"

        req = requests.get(url).content
        xmlObject = xmltodict.parse(req)
        allData = xmlObject['response']['body']['items']['item']
    except Exception as e:
        allData = ""

    content = {'allData': allData}

    return render(request, 'Stocks/money.html', content)
