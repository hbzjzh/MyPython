# !/usr/bin/env python
#coding:utf8
import memcache

mc = memcache.Client(['182.245.29.123:11215'], debug=True)

def flushAll():
    return mc.flush_all()

def getValue(key):
    return mc.get(key)

#直播实时
def makeTV(mediaCode, latn, playLine):
    return mediaCode + "@" + latn + "&" + playLine


#flushAll()


userId = "GQ000006209904"
mediaCode = "143"
latn = "870"
playLine = "0"

print getValue(userId)

print getValue(makeTV(mediaCode, latn, playLine))

