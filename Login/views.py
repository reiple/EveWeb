from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from Login.models import APIKey

import time
import tempfile
import cPickle
import zlib
import os
from os.path import join, exists
from httplib import HTTPException
import eveapi
from bs4 import BeautifulSoup
import urllib2


#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext

from models import APIKey


def LoginTest(request):
    
    listAPIKey = APIKey.objects.all()
    
    strText = ""
    for keyInfo in listAPIKey:
        strUserName = keyInfo.UserName
        strKeyID = keyInfo.KeyID
        strVCode = keyInfo.VCode
        api = eveapi.EVEAPIConnection()
        print strKeyID
        print strVCode
        auth = api.auth(keyID=strKeyID, vCode = strVCode)
        result = auth.account.Characters()
        
        try:
            strText = strText + "User Name: "  + strUserName + "<br />"
            for character in result.characters:
                wallet = auth.char.AccountBalance(characterID=character.characterID)
                isk = wallet.accounts[0].balance
                strText = strText + "ISK: " + str(isk) + "<br />"
        except StandardError, e:
            strText = str(e)
            print e            
        
    return HttpResponse(strText)



def GetMemberList(request):
    site = "http://api.eveonline.com"
    keyID = '3135538'
    vCode = 'etKjrz1h0XE5gKqim5B2RdmXLJZ5hb9Cv6qY0NLLUZ44UKeYhvXJlNHPRWzbntSt'
    
    requestURL = site + "/corp/MemberTracking.xml.aspx?keyID=" + keyID + "&vCode=" + vCode + "&extended=1"
    
    try:
        #request = urllib2.Request(requestURL, headers=hdr)
        request = urllib2.urlopen(requestURL)
        if request == None:
            print 'REQUEST NONE'
            
    except urllib2.HTTPError, e:
        print "HTTP Error: %d" % e.code
    except urllib2.URLError, e:
        print "Network Error: %s" % e.reason.args[1]
            
    soup = BeautifulSoup(request)
    rows = soup.find_all('row')
    
    strText = ""
    strWormholeChar = ""
    for currentRow in rows:
        location = currentRow['location']
        characterid = currentRow['characterid']
        name = currentRow['name']
        #print currentRow
        print name + ": " + location + "<br />"
        strText = strText + name + ": " + location + "<br />"
        if location == 'J162437':
            strWormholeChar = strWormholeChar + name + "<br />"
        
        
    #return HttpResponse(strText)
    return HttpResponse(strWormholeChar)


def GetWormholeMemberList(request):
    site = "http://api.eveonline.com"
    
    listAPIKey = APIKey.objects.all()
    corpKey = APIKey.objects.get(UserName='corp_wormhole')
    
    #requestURL = site + "/corp/MemberTracking.xml.aspx?keyID=" + keyID + "&vCode=" + vCode + "&extended=1"
    requestURL = site + "/corp/MemberTracking.xml.aspx?keyID=" + corpKey.KeyID + "&vCode=" + corpKey.VCode + "&extended=1"
    
    try:
        #request = urllib2.Request(requestURL, headers=hdr)
        request = urllib2.urlopen(requestURL)
        if request == None:
            print 'REQUEST NONE'
            
    except urllib2.HTTPError, e:
        print "HTTP Error: %d" % e.code
    except urllib2.URLError, e:
        print "Network Error: %s" % e.reason.args[1]
            
    soup = BeautifulSoup(request)
    rows = soup.find_all('row')
    
    strText = ""
    strWormholeChar = ""
    for currentRow in rows:
        location = currentRow['location']
        characterid = currentRow['characterid']
        name = currentRow['name']
        
        #print currentRow
        strText = strText + name + ": " + location + "<br />"
        if location == 'J162437':
            strWormholeChar = strWormholeChar + name + "<br />"
        
    #return HttpResponse(strText)
    return HttpResponse(strWormholeChar)
    