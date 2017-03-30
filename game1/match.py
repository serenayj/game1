import json, random, io, os
from game1.models import Pairs, HID
#from py4j.java_gateway import JavaGateway

# json data
######
#user = {"turkid": blah, "Status": False/True}
######
user1 = {"username":'foo1', "Status":False}
user2 = {"username":'foo2', "Status":True}
user3 = {"username":'foo3', "Status":False}

# list of requests
requests = []
requests.append(user1)
requests.append(user2)
requests.append(user3)

def check(request,username):
    # If JSON file is empty -> no requests waitlisted // save the new request
    if (os.stat("waiting.json").st_size == 0):
        to_unicode = unicode     
        with io.open('waiting.json', 'w') as outfile:
            str_ = json.dumps(request, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)
            outfile.write(to_unicode(str_))
    # Else pop the previous request to create the matching
    else:
        with io.open('waiting.json', 'r') as infile:
            data = json.loads(infile.read())
        pair = [data, json.loads(unicode(json.dumps(request, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)))]
        with io.open('waiting.json', 'w') as outfile:
            outfile.write(unicode(''))
        chanid = match(pair)
        entrance = 'http://webchat.freenode.net?nick=' + str(username) + '&channels=' + chanid + '&uio=d4'
        return entrance
        #return chid 
    
# input is a list of two json data
def match(pair):
    #pass
    usr1 = HID.objects.get(username = pair[0]['username'])
    usr1n = usr1.username
    print usr1n
    print type(usr1n)
    usr2 = HID.objects.get(username = pair[1]['username'])
    usr2n = usr2.username
    p = Pairs(user1id = usr1, user2id = usr2)
    p.save()
    print p.pairid
    print type(p.pairid)
    channel = 'NLPChannel' + str(p.pairid)
    url1 = 'http://webchat.freenode.net?nick=' + str(usr1n) + '&channels=' + channel + '&uio=d4'
    url2 = 'http://webchat.freenode.net?nick=' + str(usr2n) + '&channels=' + channel + '&uio=d4'
    p = Pairs(pairid = p.pairid, user1id = usr1, user2id = usr2, channelid = channel, url1 = url1, url2 = url2)
    p.save()
    call_bot(usr1, usr2, channel)
    return channel
    
    
    
# calling the bot
def call_bot(usr1, usr2, channel):
    print "calling bot!!!!"
    #gateway = JavaGateway() 
    #bot = gateway.entry_point.startChannel(usr1, usr2, channel)