# !/usr/bin/env python
#coding:utf8
import memcache

mc = memcache.Client(['182.245.29.123:11212'], debug=True)

separator = "-"

def flushAll():
    return mc.flush_all()

def getValue(key):
    return mc.get(key)

def setValue(key, value):
    print mc.set(key, value)

def delKey(key):
    print mc.delete(key)

#活动状态
def makePA(activityId):
    return "PA" + separator + activityId

#并发控制
def makePUF(userId):
    return "PUF" + separator + userId

#用户状态
def makePADU(activityId, dayId, userId):
    return "PADU" + separator + activityId + separator + dayId + separator + userId

#用户奖品
def makePAU(activityId, userId):
    return "PAU" + separator + activityId + separator + userId

#奖品池状态
def makePADS(activityId, dayId):
    return "PADS" + separator + activityId + separator + dayId

#用户中奖开关
def makePAUS(userId):
    return "PAUS" + separator + userId

#中奖名单
def makePAA(activityId):
    return "PAA" + separator + activityId

#接口配置
def makePAT(activityId, prizeType):
    return "PAT" + separator + activityId + separator + prizeType

def printAllInfo(activityId, dayId, userId):
    for aId in activityId.split(","):
        print '活动',aId,'状态:', getValue(makePA(aId))
        print '奖品池开关:',getValue(makePADS(aId, dayId))
        print '中奖名单:',getValue(makePAA(aId))
        print '接口配置:',getValue(makePAT(aId, "5"))
        if userId:
            for uId in userId:
                #print uId,'用户并发控制:',getValue(makePUF(uId))
                print uId,'用户开关:',getValue(makePAUS(uId))
                print uId,'用户状态:',getValue(makePADU(aId, dayId, uId))
                #print uId,'用户奖品:',getValue(makePAU(aId, uId))

def deleteAllInfo(activityId, dayId, userId):
    for aId in activityId.split(","):
        print '活动',aId,'状态:', delKey(makePA(aId))
        print '奖品池开关:',delKey(makePADS(aId, dayId))
        print '中奖名单:',delKey(makePAA(aId))
        print '接口配置:',delKey(makePAT(aId, 5))
        if userId:
            for uId in userId:
                #print uId,'用户并发控制:',delKey(makePUF(uId))
                print uId,'用户开关:',delKey(makePAUS(uId))
                print uId,'用户状态:',delKey(makePADU(aId, dayId, uId))
                #print uId,'用户奖品:',delKey(makePAU(aId, uId))

#控制中奖用户
def setPAUS(winerId):
    for uId in winerId:
        setValue(makePAUS(uId), "-1")

#控制活动奖品池
def setPADS(activityId, dayId):
    setValue(makePADS(activityId, dayId), "-1")


# flushAll()

activityId = "15,16,17"
dayId = "20181231"
userId = []

#delKey(makePA(activityId))
#delKey(makePADS(activityId, dayId))
#delKey(makePAA(activityId))
#delKey(makePADU(activityId, dayId, userId[0]))
#delKey(makePAU(activityId, userId[0]))
#delKey(makePAUS(userId[0]))

#print getValue(makePA(activityId))
#setPAUS(userId)
#setPADS(activityId, dayId)
printAllInfo(activityId, dayId, userId)
