# -*- coding: utf-8 -*-

import LINETCR
from LINETCR.lib.curve.ttypes import *
from datetime import datetime
import time,random,sys,json,codecs,threading,glob,re
import requests
import urllib
import subprocess



#kk = LINETCR.LINE()
#kk.login(qr=True)
#kk.loginResult()

cl = LINETCR.LINE() ##Shunsui Kyōraku(LINE)
cl.login(qr=True)
cl.loginResult()

ki = LINETCR.LINE() #Ichibē Hyōsube(LINE 1)
ki.login(qr=True)
ki.loginResult()

kk = LINETCR.LINE() #Yoruichi Shihōin(LINE 2)
kk.login(qr=True)
kk.loginResult()

kc = LINETCR.LINE() #Kenpachi Kiganjō(LINE 3)
kc.login(qr=True)
kc.loginResult()

ks = LINETCR.LINE() #Nanao Ise(LINE 4)
ks.login(qr=True)
ks.loginResult()

ka = LINETCR.LINE() #Momo Hinamori(LINE 5)
ka.login(qr=True)
ka.loginResult()

kb = LINETCR.LINE() #Rangiku Matsumoto(LINE 6)
kb.login(qr=True)
kb.loginResult()

ko = LINETCR.LINE() #Chikane Iba(LINE 7)
ko.login(qr=True)
ko.loginResult()

ke = LINETCR.LINE() #Hiyori Sarugaki(LINE 8)
ke.login(qr=True)
ke.loginResult()

ku = LINETCR.LINE() #Lisa Yadōmaru(LINE 9)
ku.login(qr=True)
ku.loginResult()

k1 = LINETCR.LINE() #Kicker(Line 10)
k1.login(qr=True)
k1.loginResult()

k2 = LINETCR.LINE() #Kicker(Line 11)
k2.login(qr=True)
k2.loginResult()

k3 = LINETCR.LINE()
k3.login(qr=True)
k3.loginResult()


print "login success"
reload(sys)
sys.setdefaultencoding('utf-8')

helpMessage =""" [>>>SHINIGAMI BOT<<<]

=====================
[>>Public Command<<]
=====================

[*] Creator
[*] Me
[*] Mymid
[*] Cctv
[*] Ciduk
[*] Sider

=====================
[>>Staff Command<<]
=====================

[*] Absen/Respon
[*] Speed
[*] Nk
[*] Ban:on
[*] Unban:on
[*] Mid @
[*] Ginfo

=====================
[>>Admin Command<<]
=====================

[*] Staff @
[*] Unstaff @
[*] Stafflist
[*] Phewit/Kuy/Join
[*] Hushus/Bye
[*] Kernel
[*] Runtime
[*] Gcancel
[*] Ban @
[*] Unban @

=====================
[>>Owner Command<<]
=====================

[*] Admin @
[*] Unadmin@
[*] Adminlist
[*] Blacklist @
[*] Banned @
[*] Lurk on
[*] Lurk off
=====================
[>>Protect Command<<]
=====================

[*] Protect on
[*] Protect off
[*] Cancel on
[*] Cancel off
[*] Protect Qr on
[*] Protect Qr off
[*] Join on
[*] Join off

 
======================================
Open Jasa Protect Grup 

Minat PM :http://line.me/ti/p/~jhon26__

Nb:List harga
======================================
"""

Setgroup =""" 

List Harga Bisa Langsung Cp ke creator
contact line: jhon26__

http://line.me/ti/p/~jhon26__

By: Jhon
        
"""
KAC=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku,k1,k2,k3]
DEF=[cl,ki,kk,kc,ks,ka,kb,ko,ke,ku,k1,k2,k3]
mid = cl.getProfile().mid
Amid = ki.getProfile().mid
Bmid = kk.getProfile().mid
Cmid = kc.getProfile().mid
Dmid = ks.getProfile().mid
Emid = ka.getProfile().mid
Fmid = kb.getProfile().mid
Gmid = ko.getProfile().mid #Nami
Hmid = ke.getProfile().mid #Robin
Imid = ku.getProfile().mid #Jinbei
mid = cl.getProfile().mid #Akun Utama
mid1 = k1.getProfile().mid #Backup
mid2 = k2.getProfile().mid #Backup
mid3 = k3.getProfile().mid

Bots=[mid,Amid,Bmid,Cmid,Dmid,Emid,Fmid,Gmid,Hmid,Imid,mid1,mid2,mid3,"ud7a8fbcc2af037c2c5bf181b89fda5f7","ue027db6fbfa316a7ec28ed8d2cc2757d","ua398858a0ae7d4b27f42273fc83f05df"]
staff=["ud7a8fbcc2af037c2c5bf181b89fda5f7","ue027db6fbfa316a7ec28ed8d2cc2757d","ua398858a0ae7d4b27f42273fc83f05df"]
admin=["ud7a8fbcc2af037c2c5bf181b89fda5f7","ue027db6fbfa316a7ec28ed8d2cc2757d","ua398858a0ae7d4b27f42273fc83f05df","u4aae4762cdff9c8ee2ea89b615bd07e9"]
owner=["ud7a8fbcc2af037c2c5bf181b89fda5f7","ue027db6fbfa316a7ec28ed8d2cc2757d","ua398858a0ae7d4b27f42273fc83f05df"]
creator=["ud7a8fbcc2af037c2c5bf181b89fda5f7"]
wait = {
    'contact':False,
    'autoJoin':True,
    'autoCancel':{"on":True,"members":1},
    'leaveRoom':True,
    'timeline':False,
    'autoAdd':False,
    'message':"""тerima Kasih Sudah Menambahkan Aku Jadi Teman
≫ Aku Ga Jawab PM Karna aq Cuma Bot Protect ≪
≫ NIGHT RAID BOT PROTECT ≪

Ready:
≫ selfbot ≪
≫ bot protect ≪

Minat? Silahkan PM!
Idline: http://line.me/ti/p/~jhon26__""",
    "lang":"JP",
    "comment":"Thanks for add me",
    "commentOn":False,
    "commentBlack":{},
    "wblack":False,
    "dblack":False,
    "clock":False,
    "cName":"",
    "blacklist":{},
    "wblacklist":False,
    "dblacklist":False,
    "Protectgr":False,
    "Protectjoin":False,
    "Protectcancl":False,
    "protectionOn":True,
    "atjointicket":True,
    "Protectqr":False
    }

wait2 = {
    'readPoint':{},
    'readMember':{},
    'setTime':{},
    'ROM':{}
    }

setTime = {}
setTime = wait2['setTime']

contact = cl.getProfile()
backup = cl.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ki.getProfile()
backup = ki.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kk.getProfile()
backup = kk.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kc.getProfile()
backup = kc.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ks.getProfile()
backup = ks.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = ka.getProfile()
backup = ka.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

contact = kb.getProfile()
backup = kb.getProfile()
backup.dispalyName = contact.displayName
backup.statusMessage = contact.statusMessage
backup.pictureStatus = contact.pictureStatus

def sendMessage(to, text, contentMetadata={}, contentType=0):
    mes = Message()
    mes.to, mes.from_ = to, profile.mid
    mes.text = text
    mes.contentType, mes.contentMetadata = contentType, contentMetadata
    if to not in messageReq:
        messageReq[to] = -1
    messageReq[to] += 1
    
def restart_program():
    python = sys.executable
    Linux.Ubuntu(python, python, * sys.argv)
    
mulai = time.time()  
    
def waktu(secs):
    mins, secs = divmod(secs,60)
    hours, mins = divmod(mins,60)
    return '%02d Jam %02d Menit %02d Detik' % (hours, mins, secs)


def bot(op):
    try:
        if op.type == 0:
            return
        if op.type == 5:
            if wait["autoAdd"] == True:
                cl.findAndAddContactsByMid(op.param1)
                if (wait["message"] in [""," ","\n",None]):
                    pass
                else:
                    cl.sendText(op.param1,str(wait["message"]))
        #------------------------------------#
        if op.type == 13:
            if mid in op.param3:
                if wait["autoJoin"] == True:
                    cl.acceptGroupInvitation(op.param1)
                    cl.sendText(op.param1,"Thanks For Invite Me.Made id line day_hard")
                    print "BOT 1 Joined"
                else:                                                                                        
                    print "autoJoin is Off"

            if Amid in op.param3:
                if wait["autoJoin"] == True:
                    ki.acceptGroupInvitation(op.param1)
                    ki.sendText(op.param1,"Thanks For Invite Me.Made By Zenbot")
                    print "BOT 2 Joined"
                else:
                    print "autoJoin is Off"
        #------------------------------------#            
        if op.type == 17:
          if op.param2 in Bots:
            return
          ginfo = cl.getGroup(op.param1)
          random.choice(KAC).sendText(op.param1, "Selamat Datang Di Grup  " + str(ginfo.name))
          print "MEMBER HAS JOIN THE GROUP"
        if op.type == 15:
          if op.param2 in Bots:
             return
          random.choice(KAC).sendText(op.param1, "Semoga Tenang di Alam Sana!!!")
          print "MEMBER HAS LEFT THE GROUP"            
        #------CCTV-------------===----------#
        if op.type == 55:
          try:
            if op.param1 in wait2['readPoint']:
              Name = cl.getContact(op.param2).displayName
              if Name in wait2['readMember'][op.param1]:
                 pass
              else:
                wait2['readMember'][op.param1] += "\n[•]" + Name
                wait2['ROM'][op.param1][op.param2] = "[•]" + Name
            else:
              cl.sendText
          except:
             pass                

        #------Protect Group Kick start------#
        if op.type == 11:
           if wait["Protectgr"] == True:
               if op.param2 not in Bots + staff + admin + owner + creator:
                   G = ka.getGroup(op.param1)
                   G.preventJoinByTicket = True
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
                   random.choice(DEF).updateGroup(G)
        #------Protect Group Kick finish-----#
        #------Protect QR-------#
        if op.type == 11:
          if wait["Protectqr"] == True:
            if op.param2 not in Bots + staff + admin + owner + creator:
              G = random.choice(KAC).getGroup(op.param1)
              G.preventJoinByTicket = True
              random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
              random.choice(KAC).updateGroup(G)
              random.choice(KAC).sendText(op.param1,random.choice(KAC).getContact(op.param2).displayName + "Jangan Buka Kode QR Njiiir")

        #------Cancel Invite User start------#
        if op.type == 13:
           if wait["Protectcancl"] == True:
               if op.param2 not in Bots + staff + admin + owner + creator:
                  group = ka.getGroup(op.param1)
                  gMembMids = [contact.mid for contact in group.invitee]
                  random.choice(DEF).cancelGroupInvitation(op.param1, gMembMids)
        #------Cancel Invite User Finish------#
            
        if op.type == 13:
            if op.param3 in mid:
                if op.param2 in Amid:
                    G = Amid.getGroup(op.param1)
                    G.preventJoinByTicket = False
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ticket)
                    G.preventJoinByTicket = True
                    Amid.updateGroup(G)
                    Ticket = Amid.reissueGroupTicket(op.param1)

            if op.param3 in Amid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)

            if op.param3 in Bmid:
                if op.param2 in Amid:
                    X = ki.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ki.updateGroup(X)
                    Ti = ki.reissueGroupTicket(op.param1)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)

            if op.param3 in Cmid:
                if op.param2 in Bmid:
                    X = kk.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kk.updateGroup(X)
                    Ti = kk.reissueGroupTicket(op.param1)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                
            if op.param3 in Dmid:
                if op.param2 in Cmid:
                    X = kc.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kc.updateGroup(X)
                    Ti = kc.reissueGroupTicket(op.param1)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                
            if op.param3 in Emid:
                if op.param2 in Dmid:
                    X = ks.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ks.updateGroup(X)
                    Ti = ks.reissueGroupTicket(op.param1)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                
            if op.param3 in Fmid:
                if op.param2 in Emid:
                    X = ka.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ka.updateGroup(X)
                    Ti = ka.reissueGroupTicket(op.param1)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                
            if op.param3 in Gmid:
                if op.param2 in Fmid:
                    X = kb.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    kb.updateGroup(X)
                    Ti = kb.reissueGroupTicket(op.param1)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                
            if op.param3 in Hmid:
                if op.param2 in Gmid:
                    X = ko.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    ko.updateGroup(X)
                    Ti = ko.reissueGroupTicket(op.param1)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    ke.updateGroup(X)
                    Ti = ke.reissueGroupTicket(op.param1)
                    
            if op.param3 in Imid:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    
            if op.param3 in mid1:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    
            if op.param3 in mid2:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1) 
                    
            if op.param3 in mid3:
                if op.param2 in mid:
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)

        if op.type == 13:
            print op.param1
            print op.param2
            print op.param3
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        #------Joined User Kick start------#
        if op.type == 17:
           if wait["Protectjoin"] == True:
               if op.param2 not in Bots + staff + admin + owner + creator:
                   random.choice(DEF).kickoutFromGroup(op.param1,[op.param2])
               
        #------Joined User Kick start------#
        
        if op.type == 19:
           if op.param2 not in Bots + staff + admin + owner + creator:
              kk.kickoutFromGroup(op.param1,[op.param2])
              kc.kickoutFromGroup(op.param1,[op.param2])
              ks.kickoutFromGroup(op.param1,[op.param2])
              ka.kickoutFromGroup(op.param1,[op.param2])
              kb.kickoutFromGroup(op.param1,[op.param2])
              ke.kickoutFromGroup(op.param1,[op.param2])
              ku.kickoutFromGroup(op.param1,[op.param2])
              ko.kickoutFromGroup(op.param1,[op.param2])
              k1.kickoutFromGroup(op.param1,[op.param2])
              k2.kickoutFromGroup(op.param1,[op.param2])
              k3.kickoutFromGroup(op.param1,[op.param2])
              random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
           else: 
               pass

        if op.type == 19:
           if op.param2 not in Bots + staff + admin + owner + creator:
              kk.kickoutFromGroup(op.param1,[op.param2])
              kc.kickoutFromGroup(op.param1,[op.param2])
              ks.kickoutFromGroup(op.param1,[op.param2])
              ka.kickoutFromGroup(op.param1,[op.param2])
              kb.kickoutFromGroup(op.param1,[op.param2])
              ke.kickoutFromGroup(op.param1,[op.param2])
              ku.kickoutFromGroup(op.param1,[op.param2])
              ko.kickoutFromGroup(op.param1,[op.param2])
              k1.kickoutFromGroup(op.param1,[op.param2])
              k2.kickoutFromGroup(op.param1,[op.param2])
              k3.kickoutFromGroup(op.param1,[op.param2])
              random.choice(DEF).inviteIntoGroup(op.param1,[op.param3])
           else:
               pass

        if op.type == 19:
                if mid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Kick regulation or Because it does not exist in the group、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True
                    G = random.choice(KAC).getGroup(op.param1)
                    G.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(G)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    X = cl.getGroup(op.param1)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    Ti = cl.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
 
                if Amid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k2.kickoutFromGroup(op.param1,[op.param2])
                        kk.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ki.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ki.updateGroup(G)
                    Ticket = ki.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Bmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        k1.kickoutFromGroup(op.param1,[op.param2])
                        kc.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kk.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kk.updateGroup(G)
                    Ticket = kk.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True

                if Cmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        kk.kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("clientが蹴り規制orグループに存在しない為、\n["+op.param1+"]\nの\n["+op.param2+"]\nを蹴る事ができませんでした。\nブラックリストに追加します。")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kc.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kc.updateGroup(G)
                    Ticket = kc.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                        
                if Dmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ks.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ks.updateGroup(G)
                    Ticket = ks.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Emid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ka.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ka.updateGroup(G)
                    Ticket = ka.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Fmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = kb.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    kb.updateGroup(G)
                    Ticket = kb.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Gmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                            random.choice(KAC).inviteIntoGroup(op.param1,[op.param3])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ko.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ko.updateGroup(G)
                    Ticket = ko.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True
                        
                if Hmid in op.param3:
                    if op.param2 in Bots:
                        pass
                    try:
                        random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                    except:
                        try:
                            random.choice(KAC).kickoutFromGroup(op.param1,[op.param2])
                        except:
                            print ("client Because it is not in the group or Because it does not exist in the group \n["+op.param1+"]\nOf\n["+op.param2+"]\n I could not kick \n Add it to the black list.")
                        if op.param2 in wait["blacklist"]:
                            pass
                        if op.param2 in wait["whitelist"]:
                            pass
                        else:
                            wait["blacklist"][op.param2] = True

                    X = random.choice(KAC).getGroup(op.param1)
                    X.preventJoinByTicket = False
                    random.choice(KAC).updateGroup(X)
                    Ti = random.choice(KAC).reissueGroupTicket(op.param1)
                    cl.acceptGroupInvitationByTicket(op.param1,Ti)
                    ki.acceptGroupInvitationByTicket(op.param1,Ti)
                    kk.acceptGroupInvitationByTicket(op.param1,Ti)
                    kc.acceptGroupInvitationByTicket(op.param1,Ti)
                    ks.acceptGroupInvitationByTicket(op.param1,Ti)
                    ka.acceptGroupInvitationByTicket(op.param1,Ti)
                    kb.acceptGroupInvitationByTicket(op.param1,Ti)
                    ko.acceptGroupInvitationByTicket(op.param1,Ti)
                    ke.acceptGroupInvitationByTicket(op.param1,Ti)
                    ku.acceptGroupInvitationByTicket(op.param1,Ti)
                    k1.acceptGroupInvitationByTicket(op.param1,Ti)
                    k2.acceptGroupInvitationByTicket(op.param1,Ti)
                    k3.acceptGroupInvitationByTicket(op.param1,Ti)
                    G = ke.getGroup(op.param1)
                    G.preventJoinByTicket = True
                    ke.updateGroup(G)
                    Ticket = ke.reissueGroupTicket(op.param1)
                    if op.param2 in wait["blacklist"]:
                        pass
                    if op.param2 in wait["whitelist"]:
                        pass
                    else:
                        wait["blacklist"][op.param2] = True        
                    
        if op.type == 13:
            if mid in op.param3:
                G = cl.getGroup(op.param1)
                if wait["autoJoin"] == True:
                    if wait["autoCancel"]["on"] == True:
                        if len(G.members) <= wait["autoCancel"]["members"]:
                            cl.rejectGroupInvitation(op.param1)
                        else:
                            cl.acceptGroupInvitation(op.param1)
                    else:
                        cl.acceptGroupInvitation(op.param1)
                elif wait["autoCancel"]["on"] == True:
                    if len(G.members) <= wait["autoCancel"]["members"]:
                        cl.rejectGroupInvitation(op.param1)
            else:
                Inviter = op.param3.replace("",',')
                InviterX = Inviter.split(",")
                matched_list = []
                for tag in wait["blacklist"]:
                    matched_list+=filter(lambda str: str == tag, InviterX)
                if matched_list == []:
                    pass
                else:
                    cl.cancelGroupInvitation(op.param1, matched_list)
                    
        if op.type == 22:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 24:
            if wait["leaveRoom"] == True:
                cl.leaveRoom(op.param1)
        if op.type == 26:
            msg = op.message


            if msg.toType == 1:
                if wait["leaveRoom"] == True:
                    cl.leaveRoom(msg.to)
            if msg.contentType == 16:
                url = msg.contentMetadata("line://home/post?userMid="+mid+"&postId="+"new_post")
                cl.like(url[25:58], url[66:], likeType=1001)
        if op.type == 26:
            msg = op.message
            if msg.contentType == 13:
               if wait["wblack"] == True:
                    if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        cl.sendText(msg.to,"already")
                        wait["wblack"] = False
                    else:
                        wait["commentBlack"][msg.contentMetadata["mid"]] = True
                        wait["wblack"] = False
                        cl.sendText(msg.to,"decided not to comment")

               elif wait["dblack"] == True:
                   if msg.contentMetadata["mid"] in wait["commentBlack"]:
                        del wait["commentBlack"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblack"] = False

                   else:
                        wait["dblack"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["wblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        cl.sendText(msg.to,"already")
                        wait["wblacklist"] = False
                   else:
                        wait["blacklist"][msg.contentMetadata["mid"]] = True
                        wait["wblacklist"] = False
                        cl.sendText(msg.to,"Sukses")

               elif wait["dblacklist"] == True:
                   if msg.contentMetadata["mid"] in wait["blacklist"]:
                        del wait["blacklist"][msg.contentMetadata["mid"]]
                        cl.sendText(msg.to,"deleted")
                        wait["dblacklist"] = False

                   else:
                        wait["dblacklist"] = False
                        cl.sendText(msg.to,"It is not in the black list")
               elif wait["contact"] == True:
                    msg.contentType = 0
                    cl.sendText(msg.to,msg.contentMetadata["mid"])
                    if 'displayName' in msg.contentMetadata:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + msg.contentMetadata["displayName"] + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
                    else:
                        contact = cl.getContact(msg.contentMetadata["mid"])
                        try:
                            cu = cl.channel.getCover(msg.contentMetadata["mid"])
                        except:
                            cu = ""
                        cl.sendText(msg.to,"[displayName]:\n" + contact.displayName + "\n[mid]:\n" + msg.contentMetadata["mid"] + "\n[statusMessage]:\n" + contact.statusMessage + "\n[pictureStatus]:\nhttp://dl.profile.line-cdn.net/" + contact.pictureStatus + "\n[coverURL]:\n" + str(cu))
            elif msg.contentType == 16:
                if wait["timeline"] == True:
                    msg.contentType = 0
                    if wait["lang"] == "JP":
                        msg.text = "post URL\n" + msg.contentMetadata["postEndUrl"]
                    else:
                        msg.text = "URLâ†’\n" + msg.contentMetadata["postEndUrl"]
                    cl.sendText(msg.to,msg.text)
            elif msg.text is None:
                return
            elif msg.text in ["Key","help","Help"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,helpMessage)
                    
            elif msg.text in ["List harga"]:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,Setgroup)
                    
            elif ("Gn " in msg.text):
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.name = msg.text.replace("Gn ","")
                    cl.updateGroup(X)
                else:
                    cl.sendText(msg.to,"It can't be used besides the group.")
            elif "Kick " in msg.text:
              if msg.from_ in staff + admin + owner + creator:
                midd = msg.text.replace("Kick ","")
                ki.kickoutFromGroup(msg.to,[midd])
            elif "Invite " in msg.text:
              if msg.from_ in staff + admin + owner + creator:
                midd = msg.text.replace("Invite ","")
                cl.findAndAddContactsByMid(midd)
                cl.inviteIntoGroup(msg.to,[midd])
            elif "invite " in msg.text:
              if msg.from_ in staff + admin + owner + creator:
                midd = msg.text.replace("sinvite ","")
                ki.findAndAddContactsByMid(midd)
                ki.inviteIntoGroup(msg.to,[midd])
                
            elif msg.text in ["Bot?"]: #Ngirim Semua Kontak Bot
              if msg.from_ in staff + admin + owner + creator:
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid1}
                cl.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Amid}
                ki.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Bmid}
                kk.sendMessage(msg)

                msg.contentType = 13
                msg.contentMetadata = {'mid': Cmid}
                kc.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Dmid}
                ks.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Emid}
                ka.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Fmid}
                kb.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Gmid}
                ko.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Hmid}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': Imid}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid2}
                ke.sendMessage(msg)
                
                msg.contentType = 13
                msg.contentMetadata = {'mid': mid3}
                ke.sendMessage(msg)
            elif msg.text in ["Me"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': msg.from_}
                random.choice(KAC).sendMessage(msg)
                
                
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '5'}
                msg.text = None
                cl.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv1 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '6'}
                msg.text = None
                ki.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv2 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '8'}
                msg.text = None
                kk.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","Cv3 gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '10'}
                msg.text = None
                kc.sendMessage(msg)
            elif msg.text in ["æ„›ã�®ãƒ—ãƒ¬ã‚¼ãƒ³ãƒˆ","All gift"]:
                msg.contentType = 9
                msg.contentMetadata={'PRDID': 'a0768339-c2d3-4189-9653-2909e9bb6f58',
                                    'PRDTYPE': 'THEME',
                                    'MSGTPL': '12'}
                msg.text = None
                ki.sendMessage(msg)
                kk.sendMessage(msg)
                kc.sendMessage(msg)
            elif msg.text in ["Cancel","cancel"]:
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    if X.invitee is not None:
                        gInviMids = [contact.mid for contact in X.invitee]
                        cl.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"No one is inviting")
                        else:
                            cl.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif msg.text in ["Cv cancel","Bot cancel"]:
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    G = k3.getGroup(msg.to)
                    if G.invitee is not None:
                        gInviMids = [contact.mid for contact in G.invitee]
                        k3.cancelGroupInvitation(msg.to, gInviMids)
                    else:
                        if wait["lang"] == "JP":
                            k3.sendText(msg.to,"No one is inviting")
                        else:
                            k3.sendText(msg.to,"Sorry, nobody absent")
                else:
                    if wait["lang"] == "JP":
                        k3.sendText(msg.to,"Can not be used outside the group")
                    else:
                        k3.sendText(msg.to,"Not for use less than group")
            #elif "gurl" == msg.text:
                #print cl.getGroup(msg.to)
                ##cl.sendMessage(msg)
            elif msg.text in ["Open url","open url"]:
              if msg.from_ in staff + admin + owner + creator:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = False
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link open")
                    else:
                        cl.sendText(msg.to,"Already open")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            elif msg.text in ["Close url","close url"]:
              if msg.from_ in staff + admin + owner + creator:
                if msg.toType == 2:
                    X = cl.getGroup(msg.to)
                    X.preventJoinByTicket = True
                    cl.updateGroup(X)
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Invite by link Close")
                    else:
                        cl.sendText(msg.to,"Already close")
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            elif "jointicket " in msg.text.lower():
              if msg.from_ in admin + owner + creator:
		rplace=msg.text.lower().replace("jointicket ")
		if rplace == "on":
			wait["atjointicket"]=True
		elif rplace == "off":
			wait["atjointicket"]=False
		cl.sendText(msg.to,"Auto Join Group by Ticket is %s" % str(wait["atjointicket"]))
            elif '/ti/g/' in msg.text.lower():
		link_re = re.compile('(?:line\:\/|line\.me\/R)\/ti\/g\/([a-zA-Z0-9_-]+)?')
		links = link_re.findall(msg.text)
		n_links=[]
		for l in links:
			if l not in n_links:
				n_links.append(l)
		for ticket_id in n_links:
			if wait["atjointicket"] == True:
				group=cl.findGroupByTicket(ticket_id)
				cl.acceptGroupInvitationByTicket(group.mid,ticket_id)
				cl.sendText(msg.to,"Sukses join ke grup %s" % str(group.name))
            elif msg.text == "Ginfo":
              if msg.from_ in admin + staff + owner + creator:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        gCreator = ginfo.creator.displayName
                    except:
                        gCreator = "Error"
                    if wait["lang"] == "JP":
                        if ginfo.invitee is None:
                            sinvitee = "0"
                        else:
                            sinvitee = str(len(ginfo.invitee))
                        if ginfo.preventJoinByTicket == True:
                            u = "close"
                        else:
                            u = "open"
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus + "\nmembers:" + str(len(ginfo.members)) + "members\npending:" + sinvitee + "people\nURL:" + u + "it is inside")
                    else:
                        cl.sendText(msg.to,"[group name]\n" + str(ginfo.name) + "\n[gid]\n" + msg.to + "\n[group creator]\n" + gCreator + "\n[profile status]\nhttp://dl.profile.line.naver.jp/" + ginfo.pictureStatus)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can not be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            elif "Id Group" == msg.text:
              if msg.from_ in admin + staff + owner + creator:
                kk.sendText(msg.to,msg.to)
            elif "Mymid" == msg.text:
              if msg.from_ in admin + staff + owner + creator:
                random.choice(KAC).sendText(msg.to, msg.from_)
            
            elif msg.text in ["Wkwkwk","Wkwk","Wk","wkwkwk","wkwk","wk"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "100",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                cl.sendMessage(msg)
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hehehe","Hehe","He","hehehe","hehe","he"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "10",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Galau"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "9",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["You"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "7",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hadeuh"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "6",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Please"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "4",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Haaa"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "3",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Lol"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "110",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["Hmmm","Hmm","Hm","hmmm","hmm","hm"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "101",
                                     "STKPKGID": "1",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
            elif msg.text in ["Welcome"]:
                msg.contentType = 7
                msg.text = None
                msg.contentMetadata = {
                                     "STKID": "247",
                                     "STKPKGID": "3",
                                     "STKVER": "100" }
                ki.sendMessage(msg)
                kk.sendMessage(msg)
            elif msg.text in ["TL: "]:
              if msg.from_ in creator:
                tl_text = msg.text.replace("TL: ","")
                cl.sendText(msg.to,"line://home/post?userMid="+mid+"&postId="+cl.new_post(tl_text)["result"]["post"]["postInfo"]["postId"])
            elif msg.text in ["Cn "]:
              if msg.from_ in creator:
                string = msg.text.replace("Cn ","")
                if len(string.decode('utf-8')) <= 20:
                    profile = cl.getProfile()
                    profile.displayName = string
                    cl.updateProfile(profile)
                    cl.sendText(msg.to,"name " + string + " done")
            
            elif msg.text in ["Mc "]:
              if msg.from_ in owner + creator:
                mmid = msg.text.replace("Mc ","")
                msg.contentType = 13
                msg.contentMetadata = {"mid":mmid}
                cl.sendMessage(msg)
            elif msg.text in ["Join on","join on"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectjoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Join off","join off"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectjoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectjoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"kick Joined Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel on","cancel on"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectcancl"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Cancel off","cancel off"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectcancl"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectcancl"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cancel All Invited Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect on","protect on"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectgr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Protect off","protect off"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectgr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectgr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect Group Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact On","Contact on","contact on"]:
              if msg.from_ in admin + owner + creator:
                if wait["contact"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Contact Off","Contact off","contact off"]:
              if msg.from_ in admin + owner + creator:
                if wait["contact"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["contact"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Cek Mid Send Contact Off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ³","Join on","Auto join:on","è‡ªå‹•å�ƒåŠ ï¼šé–‹"]:
                if wait["autoJoin"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["è‡ªå‹•å�‚åŠ :ã‚ªãƒ•","Join off","Auto join:off","è‡ªå‹•å�ƒåŠ ï¼šé—œ"]:
                if wait["autoJoin"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoJoin"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Gcancel:"]:
              if msg.from_ in admin + owner + creator:
                try:
                    strnum = msg.text.replace("Gcancel:","")
                    if strnum == "off":
                        wait["autoCancel"]["on"] = False
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,"Invitation refused turned off\nTo turn on please specify the number of people and send")
                        else:
                            cl.sendText(msg.to,"å…³äº†é‚€è¯·æ‹’ç»�ã€‚è¦�æ—¶å¼€è¯·æŒ‡å®šäººæ•°å�‘é€�")
                    else:
                        strnum =  int(strnum)
                        wait["autoCancel"]["on"] = True
                        if wait["lang"] == "JP":
                            cl.sendText(msg.to,strnum + "The group of people and below decided to automatically refuse invitation")
                        else:
                            cl.sendText(msg.to,strnum + "ä½¿äººä»¥ä¸‹çš„å°�ç»„ç”¨è‡ªåŠ¨é‚€è¯·æ‹’ç»�")
                except:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Value is wrong")
                    else:
                        cl.sendText(msg.to,"Bizarre ratings")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ³","Leave on","Auto leave:on","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé–‹"]:
              if msg.from_ in admin + owner + creator:
                if wait["leaveRoom"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å¼·åˆ¶è‡ªå‹•é€€å‡º:ã‚ªãƒ•","Leave off","Auto leave:off","å¼·åˆ¶è‡ªå‹•é€€å‡ºï¼šé—œ"]:
              if msg.from_ in admin + owner + creator:
                if wait["leaveRoom"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["leaveRoom"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ³","Share on","Share on"]:
              if msg.from_ in admin + owner + creator:
                if wait["timeline"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["å…±æœ‰:ã‚ªãƒ•","Share off","Share off"]:
              if msg.from_ in admin + owner + creator:
                if wait["timeline"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["timeline"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
                        
            elif msg.text in ["Qr on","Protect Qr on"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectqr"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectqr"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR On")
                    else:
                        cl.sendText(msg.to,"done")
            elif msg.text in ["Qr off","Protect Qr off"]:
              if msg.from_ in admin + staff + owner + creator:
                if wait["Protectqr"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["Protectqr"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Protect QR Off")
                    else:
                        cl.sendText(msg.to,"done")
            
            elif msg.text in ["Set","Status"]:
              if msg.from_ in admin + staff + owner + creator:
                md = "⭐Status Keamanan⭐\n*==============*\n"
                if wait["Protectqr"] == True: md+=" Protect QR  :On\n"
                else: md+=" Protect QR  :Off\n"
                if wait["Protectjoin"] == True: md+="􀔃􀆑lock􏿿  Block Join\n"
                else: md+=" Block Join Off\n"
                if wait["Protectgr"] == True: md+="􀔃􀆑lock􏿿   Block Group\n"
                else: md+=" Block Group Off\n"
                if wait["Protectcancl"] == True: md+="􀔃􀆑lock􏿿 Cancel All Invited\n"
                else: md+=" Cancel All Invited Off\n"
                if wait["contact"] == True: md+=" Contact    : on\n"
                else: md+=" Contact    : off\n"
                if wait["autoJoin"] == True: md+=" Auto join : on\n"
                else: md +=" Auto join : off\n"
                if wait["autoCancel"]["on"] == True:md+=" Group cancel :" + str(wait["autoCancel"]["members"]) + "\n"
                else: md+= " Group cancel : off\n"
                if wait["leaveRoom"] == True: md+=" Auto leave    : on\n"
                else: md+=" Auto leave : off\n"
                if wait["timeline"] == True: md+=" Share   : on\n"
                else:md+=" Share   : off\n"
                if wait["autoAdd"] == True: md+=" Auto add : on\n"
                else:md+=" Auto add : off\n"
                if wait["commentOn"] == True: md+=" Comment : on\n"
                else:md+=" Comment : off\n*============*\n⭐ɴ̷̣̎ɪ̶̚͜ɢ̶̤̄ʜ̶̟́ᴛ̵̩̍ ̶̬͠ʀ̴̲͘ᴀ̸̮̃ɪ̸͙͂ᴅ̴͙́ ̶̲͌ᴛ̷̖̇ᴇ̷͖͘ᴀ̵̆ͅᴍ̴͇̈́⭐\n*============*"
                cl.sendText(msg.to,md)
            elif "album merit " in msg.text:
              if msg.from_ in admin + owner + creator:
                gid = msg.text.replace("album merit ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
                    cl.sendText(msg.to,mg)
            elif "album " in msg.text:
              if msg.from_ in admin + owner + creator:
                gid = msg.text.replace("album ","")
                album = cl.getAlbum(gid)
                if album["result"]["items"] == []:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"There is no album")
                    else:
                        cl.sendText(msg.to,"ç›¸å†Œæ²¡åœ¨ã€‚")
                else:
                    if wait["lang"] == "JP":
                        mg = "The following is the target album"
                    else:
                        mg = "ä»¥ä¸‹æ˜¯å¯¹è±¡çš„ç›¸å†Œ"
                    for y in album["result"]["items"]:
                        if "photoCount" in y:
                            mg += str(y["title"]) + ":" + str(y["photoCount"]) + "sheet\n"
                        else:
                            mg += str(y["title"]) + ":0sheet\n"
            elif "album remove " in msg.text:
              if msg.from_ in admin + owner + creator:
                gid = msg.text.replace("album remove ","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Deleted albums")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["Group id"]:
                gid = cl.getGroupIdsJoined()
                h = ""
                for i in gid:
                    h += "[%s]:\n%s\n" % (cl.getGroup(i).name,i)
                cl.sendText(msg.to,h)
            elif msg.text in ["Cancelall"]:
              if msg.from_ in admin + staff + owner + creator:
                gid = cl.getGroupIdsInvited()
                for i in gid:
                    cl.rejectGroupInvitation(i)
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"All invitations have been refused")
                else:
                    cl.sendText(msg.to,"æ‹’ç»�äº†å…¨éƒ¨çš„é‚€è¯·ã€‚")
            elif "album removeat’" in msg.text:
              if msg.from_ in admin + owner + creator:
                gid = msg.text.replace("album removeat’","")
                albums = cl.getAlbum(gid)["result"]["items"]
                i = 0
                if albums != []:
                    for album in albums:
                        cl.deleteAlbum(gid,album["id"])
                        i += 1
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,str(i) + "Albums deleted")
                else:
                    cl.sendText(msg.to,str(i) + "åˆ é™¤äº†äº‹çš„ç›¸å†Œã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ³","Add on","Auto add:on","è‡ªå‹•è¿½åŠ ï¼šé–‹"]:
              if msg.from_ in admin + owner + creator:
                if wait["autoAdd"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already on")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["è‡ªå‹•è¿½åŠ :ã‚ªãƒ•","Add off","Auto add:off","è‡ªå‹•è¿½åŠ ï¼šé—œ"]:
              if msg.from_ in admin + owner + creator:
                if wait["autoAdd"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"already off")
                    else:
                        cl.sendText(msg.to,"done")
                else:
                    wait["autoAdd"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif "Message change: " in msg.text:
              if msg.from_ in admin + owner + creator:
                wait["message"] = msg.text.replace("Message change: ","")
                cl.sendText(msg.to,"message changed")
            elif "Message add: " in msg.text:
              if msg.from_ in admin + owner + creator:
                wait["message"] = msg.text.replace("Message add: ","")
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message changed")
                else:
                    cl.sendText(msg.to,"doneã€‚")
            elif msg.text in ["Message","è‡ªå‹•è¿½åŠ å•�å€™èªžç¢ºèª�"]:
              if msg.from_ in admin + owner + creator:
                if wait["lang"] == "JP":
                    cl.sendText(msg.to,"message change to\n\n" + wait["message"])
                else:
                    cl.sendText(msg.to,"The automatic appending information is set as followsã€‚\n\n" + wait["message"])
            elif "Comment:" in msg.text:
              if msg.from_ in admin + owner + creator:
                c = msg.text.replace("Comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"message changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif "Add comment:" in msg.text:
              if msg.from_ in admin + owner + creator:
                c = msg.text.replace("Add comment:","")
                if c in [""," ","\n",None]:
                    cl.sendText(msg.to,"String that can not be changed")
                else:
                    wait["comment"] = c
                    cl.sendText(msg.to,"changed\n\n" + c)
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ³","Comment on","Comment:on","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé–‹"]:
              if msg.from_ in admin + owner + creator:
                if wait["commentOn"] == True:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already on")
                else:
                    wait["commentOn"] = True
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å¼€ã€‚")
            elif msg.text in ["ã‚³ãƒ¡ãƒ³ãƒˆ:ã‚ªãƒ•","Comment on","Comment off","è‡ªå‹•é¦–é �ç•™è¨€ï¼šé—œ"]:
              if msg.from_ in admin + owner + creator:
                if wait["commentOn"] == False:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"already off")
                else:
                    wait["commentOn"] = False
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"done")
                    else:
                        cl.sendText(msg.to,"è¦�äº†å…³æ–­ã€‚")
            elif msg.text in ["Comment","ç•™è¨€ç¢ºèª�"]:
                cl.sendText(msg.to,"message changed to\n\n" + str(wait["comment"]))
            elif msg.text in ["Gurl"]:
              if msg.from_ in staff + admin + owner + creator:
                if msg.toType == 2:
                    x = cl.getGroup(msg.to)
                    if x.preventJoinByTicket == True:
                        x.preventJoinByTicket = False
                        cl.updateGroup(x)
                    gurl = cl.reissueGroupTicket(msg.to)
                    cl.sendText(msg.to,"line://ti/g/" + gurl)
                else:
                    if wait["lang"] == "JP":
                        cl.sendText(msg.to,"Can't be used outside the group")
                    else:
                        cl.sendText(msg.to,"Not for use less than group")
            
            elif msg.text in ["Comment bl "]:
              if msg.from_ in admin + owner + creator:
                wait["wblack"] = True
                cl.sendText(msg.to,"add to comment bl")
            elif msg.text in ["Comment wl "]:
              if msg.from_ in admin and owner and creator:
                wait["dblack"] = True
                cl.sendText(msg.to,"wl to comment bl")
            elif msg.text in ["Comment bl confirm"]:
              if msg.from_ in admin + owner + creator:
                if wait["commentBlack"] == {}:
                    cl.sendText(msg.to,"confirmed")
                else:
                    cl.sendText(msg.to,"Blacklist")
                    mc = ""
                    for mi_d in wait["commentBlack"]:
                        mc += "" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    
        

         #------------------------------- CHECK SIDER --------------------------------
            elif msg.text == "Cctv":
                cl.sendText(msg.to, "Mencari")
                try:
                  del wait2['readPoint'][msg.to]
                  del wait2['readMember'][msg.to]
                except:
                  pass
                now2 = datetime.now()
                wait2['readPoint'][msg.to] = msg.id
                wait2['readMember'][msg.to] = ""
                wait2['setTime'][msg.to] = datetime.strftime(now2,"%H:%M")
                wait2['ROM'][msg.to] = {}
                #print wait2
              
            elif msg.text == "Ciduk":
                    if msg.to in wait2['readPoint']:
                        if wait2["ROM"][msg.to].items() == []:
                            chiya = ""
                        else:
                            chiya = ""
                            for rom in wait2["ROM"][msg.to].items():
                                #print rom
                                chiya += rom[1] + "\n"

                        cl.sendText(msg.to, "||Di Read Oleh||%s\n||By : NIGHT RAID BOT||\n\n>DAFTAR SIDER<\n%s-=SIDER=-\n•\n[%s]" % (wait2['readMember'][msg.to],chiya,setTime[msg.to]))
                    else:
                        cl.sendText(msg.to, "Ketik Cctv dulu\nBaru Ketik Ciduk")

#-------------------------------------------------
            elif "/lirik " in msg.text.lower():
                songname = msg.text.replace("/lirik ","")
                params = {"songname":songname}
                r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                data = r.text
                data = json.loads(data)
                for song in data:
                    cl.sendText(msg.to,song[5])
                    print "[Command] Lirik"
#---------------------------------------------------
            elif 'music ' in msg.text.lower():
                try:
                    songname = msg.text.lower().replace('music ','')
                    params = {'songname': songname}
                    r = requests.get('http://ide.fdlrcn.com/workspace/yumi-apis/joox?' + urllib.urlencode(params))
                    data = r.text
                    data = json.loads(data)
                    for song in data:
                        hasil = 'This is Your Music\n'
                        hasil += 'Judul : ' + song[0]
                        hasil += '\nDurasi : ' + song[1]
                        hasil += '\nLink Download : ' + song[4]
                        cl.sendText(msg.to, hasil)
                        cl.sendText(msg.to, "Please Wait for audio...")
                        cl.sendAudioWithURL(msg.to, song[4])
		except Exception as njer:
		        cl.sendText(msg.to, str(njer))


         #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Phewit","Kuy","Join"]:
              if msg.from_ in admin + owner + creator:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kb.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ko.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ke.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ku.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k1.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k2.acceptGroupInvitationByTicket(msg.to,Ticket)
                        k3.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
    #-------------Fungsi Leave Group Start---------------#
    
    #----------------Fungsi Join Group Start-----------------------#
            elif msg.text in ["Masuk1"]:
              if msg.from_ in staff + admin + owner + creator:
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = False
                        cl.updateGroup(G)
                        Ticket = cl.reissueGroupTicket(msg.to)
                        ki.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kk.acceptGroupInvitationByTicket(msg.to,Ticket)
                        kc.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ka.acceptGroupInvitationByTicket(msg.to,Ticket)
                        ks.acceptGroupInvitationByTicket(msg.to,Ticket)
                        G = cl.getGroup(msg.to)
                        ginfo = cl.getGroup(msg.to)
                        G.preventJoinByTicket = True
                        cl.updateGroup(G)
                        print "Semua Sudah Lengkap"
                        G.preventJoinByTicket(G)
                        random.choice(KAC).updateGroup(G)
    #------------------Finish------------------------#
            elif msg.text in ["Keluar1"]:
              if msg.from_ in staff + admin + owner + creator:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                    except:
                        pass
    
            elif msg.text in ["Keluar"]:
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                    except:
                        pass
                    
            elif msg.text in ["Hushus","Bye"]:
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                        ka.leaveGroup(msg.to)
                        kb.leaveGroup(msg.to)
                        ko.leaveGroup(msg.to)
                        ke.leaveGroup(msg.to)
                        ku.leaveGroup(msg.to)
                        cl.leaveGroup(msg.to)
                        k1.leaveGroup(msg.to)
                        k2.leaveGroup(msg.to)
                        k3.leaveGroup(msg.to)
                    except:
                        pass
                    
            elif msg.text in ["Keluar all1"]:
              if msg.from_ in staff + admin + owner + creator:
                if msg.toType == 2:
                    ginfo = cl.getGroup(msg.to)
                    try:
                        ki.leaveGroup(msg.to)
                        kk.leaveGroup(msg.to)
                        kc.leaveGroup(msg.to)
                        ks.leaveGroup(msg.to)
                    except:
                        pass
            
            
    
    #-------------Fungsi Tag All Start---------------#
            elif msg.text in ["Tag all","Tagall"]:
              if msg.from_ in staff + admin + owner + creator:
                  group = cl.getGroup(msg.to)
                  nama = [contact.mid for contact in group.members]

                  cb = ""
                  cb2 = ""
                  strt = int(0)
                  akh = int(0)
                  for md in nama:
                      akh = akh + int(6)

                      cb += """{"S":"""+json.dumps(str(strt))+""","E":"""+json.dumps(str(akh))+""","M":"""+json.dumps(md)+"},"""

                      strt = strt + int(7)
                      akh = akh + 1
                      cb2 += "@nrik \n"

                  cb = (cb[:int(len(cb)-1)])
                  msg.contentType = 0
                  msg.text = cb2 + "\n Total:" + str(len(nama)) + " Member  \nCreator:Muhammad Fahmi Ridhani\nhttp://line.me/ti/p/~fahmi_077\n"
                  msg.contentMetadata ={'MENTION':'{"MENTIONEES":['+cb+']}','EMTVER':'4'}

                  try:
                      cl.sendMessage(msg)
                  except Exception as error:
                      print error
    #-------------Fungsi Tag All Finish---------------#

         #----------------Fungsi Banned Kick Target Start-----------------------#
            elif msg.text in ["Kill "]:
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    group = ki.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        kk.sendText(msg.to,"Selamat tinggal")
                        kc.sendText(msg.to,"Jangan masuk lagi􀨁􀆷devil smile􏿿")
                        return
                    for jj in matched_list:
                        try:
                            klist=[ki,kk,kc]
                            kicker=random.choice(klist)
                            kicker.kickoutFromGroup(msg.to,[jj])
                            print (msg.to,[jj])
                        except:
                            pass
         #----------------Fungsi Banned Kick Target Finish----------------------#                

            elif "Night raid" in msg.text:
              if msg.from_ in owner + creator:
                if msg.toType == 2:
                    print "ok"
                    _name = msg.text.replace("Night raid","")
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    random.choice(KAC).sendText(msg.to,"Perintah Diterima")
                    random.choice(KAC).sendText(msg.to,"Diproses...")
                    random.choice(KAC).sendText(msg.to,"Laksanakan")
                    msg.contentType = 13
                    msg.contentMetadata = {'Cmid': mid}
                    random.choice(KAC).sendMessage(msg)
                    targets = []
                    for g in gs.members:
                        if _name in g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        random.choice(KAC).sendText(msg.to,"Not found")
                    else:
                        for target in targets:
                          if target not in admin + staff + owner + creator + Bots:
                            try:
                                klist=[kk,kc,ks,ka,kb,ku,ke,ko,k1,k2]
                                kicker=random.choice(klist)
                                kicker.kickoutFromGroup(msg.to,[target])
                                print (msg.to,[g.mid])
                            except:
                                random.choice(KAC).sendText(msg.to,"Sorry Brader")
                                random.choice(KAC).sendText(msg.to,"Sorry Sister")
                                random.choice(KAC).sendText(msg.to,"No Baper")

        #----------------Fungsi Kick User Target Start----------------------#
            elif "Nk " in msg.text:
              if msg.from_ in staff + admin + owner + creator:
                       nk0 = msg.text.replace("Nk ","")
                       nk1 = nk0.lstrip()
                       nk2 = nk1.replace("@","")
                       nk3 = nk2.rstrip()
                       _name = nk3
                       gs = cl.getGroup(msg.to)
                       targets = []
                       for s in gs.members:
                           if _name in s.displayName:
                              targets.append(s.mid)
                       if targets == []:
                           sendMessage(msg.to,"user does not exist")
                           pass
                       else:
                           for target in targets:
                                try:
                                    klist=[ki,kk,kc,ks,ka,kb]
                                    kicker=random.choice(klist)
                                    kicker.kickoutFromGroup(msg.to,[target])
                                    print (msg.to,[g.mid])
                                except:
                                    ki.sendText(msg.to,"Kasian Di Kick....")
                                    kc.sendText(msg.to,"Hehehe")
        #----------------Fungsi Kick User Target Finish----------------------#      
            elif "Blacklist @ " in msg.text:
              if msg.from_ in staff + admin + owner + creator:
                _name = msg.text.replace("Blacklist @ ","")
                _kicktarget = _name.rstrip(' ')
                gs = k2.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _kicktarget == g.displayName:
                        targets.append(g.mid)
                        if targets == []:
                            cl.sendText(msg.to,"Not found")
                        else:
                            for target in targets:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes Cv")
                                except:
                                    ki.sendText(msg.to,"error")
            
            #----------------Fungsi Banned User Target Start-----------------------#
             #--------------------------------------------------------
            elif "Ban @" in msg.text:
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    print "@Ban by mention"
                    _name = msg.text.replace("Ban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        ki.sendText(msg.to,"Not found")
                        kk.sendText(msg.to,"")
                        kc.sendText(msg.to,"")
                    else:
                        for target in targets:
			    if target not in admin + staff + owner + creator + Bots:
                                try:
                                    wait["blacklist"][target] = True
                                    f=codecs.open('st2__b.json','w','utf-8')
                                    json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                    ki.sendText(msg.to,"Succes")
                                    kk.sendText(msg.to,"")
                                    kc.sendText(msg.to,"")
                                except:
                                    ki.sendText(msg.to,"Error")
                                    kk.sendText(msg.to,"")
                                    kc.sendText(msg.to,"")
			    else:
				cl.sendText(msg.to,"Staff Detected~")
#--------------------------------------------------------
#----------------Fungsi Banned User Target Start(lebih dari satu)-----------------------#
            elif "Banned @" in msg.text:
              if msg.from_ in owner + creator:
                key = eval(msg.contentMetadata["MENTION"])
                key["MENTIONEES"][0]["M"]
                targets = []
                for x in key["MENTIONEES"]:
                    targets.append(x["M"])
                for target in targets:
                   try:
                      wait["blacklist"][target] = True
                      f=codecs.open('st2__b.json','w','utf-8')
                      json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                      cl.sendText(msg.to,"Succes Banned")
                   except:
                      pass
#------------------------------------------------------------#
            
            #----------------Fungsi Unbanned User Target Start-----------------------#
            elif "Unban @" in msg.text:
              if msg.from_ in admin + owner + creator:
                if msg.toType == 2:
                    print "[Unban] Sukses"
                    _name = msg.text.replace("Unban @","")
                    _nametarget = _name.rstrip('  ')
                    gs = cl.getGroup(msg.to)
                    gs = ki.getGroup(msg.to)
                    gs = kk.getGroup(msg.to)
                    gs = kc.getGroup(msg.to)
                    targets = []
                    for g in gs.members:
                        if _nametarget == g.displayName:
                            targets.append(g.mid)
                    if targets == []:
                        cl.sendText(msg.to,"Tidak Ditemukan.....")
                        ki.sendText(msg.to,"")
                        kk.sendText(msg.to,"")
                        kc.sendText(msg.to,"")
                    else:
                        for target in targets:
                            try:
                                del wait["blacklist"][target]
                                f=codecs.open('st2__b.json','w','utf-8')
                                json.dump(wait["blacklist"], f, sort_keys=True, indent=4,ensure_ascii=False)
                                cl.sendText(msg.to,"Akun Bersih Kembali")
                            except:
                                ki.sendText(msg.to,"Error")
           #----------------Fungsi Unbanned User Target Finish-----------------------#
           
        #-------------Fungsi Broadcast Start------------#
            elif "Bc " in msg.text: #NgeBC Ke semua Group yang di Join :D
              if msg.from_ in owner + creator:
                 bctxt = msg.text.replace("Bc ","")
                 a = cl.getGroupIdsJoined()
                 for taf in a:
                     cl.sendText(taf, (bctxt))
       #--------------Fungsi Broadcast Finish-----------#
       #VPS STUFF - VPS NEEDED TO RUN THIS COMMAND :)
            elif msg.text in ["Kernel","kernel"]:
                 if msg.from_ in admin + owner + creator:
                     botKernel = subprocess.Popen(["uname","-svmo"], stdout=subprocess.PIPE).communicate()[0]
                     cl.sendText(msg.to, botKernel)
                     print "[Command]Kernel executed"
                 else:
                     cl.sendText(msg.to,"Command denied.")
                     cl.sendText(msg.to,"Admin permission required.")
                     print "[Error]Command denied - Admin permission required"
#------------------------------------------------
            elif msg.text.lower() == 'runtime':
              if msg.from_ in admin + owner + creator:
                eltime = time.time() - mulai
                van = "Bot sudah berjalan selama "+waktu(eltime)
                cl.sendText(msg.to,van)
#-----------------------------------------------                      
            elif msg.text in ["Creator"]:
                msg.contentType = 13
                msg.contentMetadata = {'mid': 'ua35835da9375cdfc874eaa9b279997da'}
                cl.sendMessage(msg)
                cl.sendText(msg.to,"Itu Creator Kami")
#-----------------------------------------------
            elif msg.text in ["Bot:restart"]:
		if msg.from_ in creator:
		    cl.sendText(msg.to, "Bot has been restarted")
		    restart_program()
		    print "@Restart"
		else:
		    cl.sendText(msg.to, "No Access")
#----------------------------------------------
            elif ("Cek " in msg.text):
               if msg.from_ in admin + owner + creator:
                   key = eval(msg.contentMetadata["MENTION"])
                   key1 = key["MENTIONEES"][0]["M"]
                   key = cl.getContact(key1)
                   cl.sendText(msg.to,"Mid:" +  key1)     
                    
#-----------------------------------------------

            elif "Allbio:" in msg.text:
              if msg.from_ in creator:
                string = msg.text.replace("Allbio:","")
                if len(string.decode('utf-8')) <= 500:
                    profile = cl.getProfile()
                    profile.statusMessage = string
                    cl.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ki.getProfile()
                    profile.statusMessage = string
                    ki.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kk.getProfile()
                    profile.statusMessage = string
                    kk.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kc.getProfile()
                    profile.statusMessage = string
                    kc.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ks.getProfile()
                    profile.statusMessage = string
                    ks.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ka.getProfile()
                    profile.statusMessage = string
                    ka.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = kb.getProfile()
                    profile.statusMessage = string
                    kb.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ku.getProfile()
                    profile.statusMessage = string
                    ku.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ke.getProfile()
                    profile.statusMessage = string
                    ke.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    ko.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    k1.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    k2.updateProfile(profile)
                if len(string.decode('utf-8')) <= 500:
                    profile = ko.getProfile()
                    profile.statusMessage = string
                    k3.updateProfile(profile)
                    cl.sendText(msg.to,"Bio berubah menjadi " + string + "")
    #--------------=Finish=----------------
#--------------- SC Add staff ---------
            elif "Staff @" in msg.text:
              if msg.from_ in admin + owner + creator:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Staff @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            staff.append(target)
                            ki.sendText(msg.to," Staff Succes~")
                        except:
                            pass
                print "[Command]Staff add executed"
              else:
                ki.sendText(msg.to,"Command denied.")
                ki.sendText(msg.to,"Admin permission required.")
                
            elif "Unstaff @" in msg.text:
              if msg.from_ in admin + owner + creator:
                print "[Command]Staff remove executing"
                _name = msg.text.replace("Unstaff @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            staff.remove(target)
                            ki.sendText(msg.to,"Deleted Succes~")
                        except:
                            pass
                print "[Command]Staff remove executed"
              else:
                ki.sendText(msg.to,"Command denied.")
                ki.sendText(msg.to,"Staff permission required.")
                
            elif msg.text in ["Stafflist","stafflist"]:
                if admin + staff + owner + creator == []:
                    cl.sendText(msg.to,"The stafflist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in staff:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Stafflist executed"
                  
#--------------- SC Add Admin ---------
            elif "Admin @" in msg.text:
              if msg.from_ in owner + creator:
                print "[Command]Staff add executing"
                _name = msg.text.replace("Admin @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.append(target)
                            ki.sendText(msg.to,"Admin Succes~")
                        except:
                            pass
                print "[Command]Admin add executed"
              else:
                ki.sendText(msg.to,"Command denied.")
                
            elif "Unadmin @" in msg.text:
              if msg.from_ in owner + creator:
                print "[Command]Admin remove executing"
                _name = msg.text.replace("Unadmin @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            admin.remove(target)
                            ki.sendText(msg.to,"Deleted Succes~")
                        except:
                            pass
                print "[Command]Admin remove executed"
              else:
                ki.sendText(msg.to,"Command denied.")
                
            elif msg.text in ["Adminlist","adminlist"]:
                if admin + staff + owner + creator == []:
                    cl.sendText(msg.to,"The Adminlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in admin:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Adminlist executed"
                  
#--------------- SC Add staff ---------
            elif "Owner @" in msg.text:
              if msg.from_ in creator:
                print "[Command]OWner add executing"
                _name = msg.text.replace("Owner @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.append(target)
                            ki.sendText(msg.to,"Owner Succes~")
                        except:
                            pass
                print "[Command]Owner add executed"
              else:
                ki.sendText(msg.to,"Command denied.")
                
            elif "Unowner @" in msg.text:
              if msg.from_ in creator:
                print "[Command]Owner remove executing"
                _name = msg.text.replace("Unowner @","")
                _nametarget = _name.rstrip('  ')
                gs = cl.getGroup(msg.to)
                gs = ki.getGroup(msg.to)
                gs = kk.getGroup(msg.to)
                gs = kc.getGroup(msg.to)
                gs = ks.getGroup(msg.to)
                targets = []
                for g in gs.members:
                    if _nametarget == g.displayName:
                        targets.append(g.mid)
                if targets == []:
                   random.choice(KAC).sendText(msg.to,"Contact not found")
                else:
                   for target in targets:
                        try:
                            owner.remove(target)
                            ki.sendText(msg.to,"Deleted Succes~")
                        except:
                            pass
                print "[Command]Owner remove executed"
              else:
                ki.sendText(msg.to,"Command denied.")
                
            elif msg.text in ["Ownerlist","ownerlist"]:
                if admin + owner + creator == []:
                    cl.sendText(msg.to,"The Ownerlist is empty")
                else:
                    cl.sendText(msg.to,"Tunggu...")
                    mc = ""
                    for mi_d in owner:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
                    print "[Command]Ownerlist executed"
                    
#-----------------------------------------------                    
            elif "lurk on" == msg.text.lower():
              if msg.from_ in owner:
                if msg.to in wait2['readPoint']:
                        try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                        except:
                            pass
                        wait2['readPoint'][msg.to] = msg.id
                        wait2['readMember'][msg.to] = ""
                        wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                        wait2['ROM'][msg.to] = {}
                        with open('sider.json', 'w') as fp:
                         json.dump(wait2, fp, sort_keys=True, indent=4)
                         cl.sendText(msg.to,"Lurking already on")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    wait2['readPoint'][msg.to] = msg.id
                    wait2['readMember'][msg.to] = ""
                    wait2['setTime'][msg.to] = datetime.now().strftime('%H:%M:%S')
                    wait2['ROM'][msg.to] = {}
                    with open('sider.json', 'w') as fp:
                     json.dump(wait2, fp, sort_keys=True, indent=4)
                     cl.sendText(msg.to, "Set reading point:\n" + datetime.now().strftime('%H:%M:%S'))
                     print wait2
            
            elif "lurk off" == msg.text.lower():
              if msg.from_ in owner:
                if msg.to not in wait2['readPoint']:
                    cl.sendText(msg.to,"Lurking already off")
                else:
                    try:
                            del wait2['readPoint'][msg.to]
                            del wait2['readMember'][msg.to]
                            del wait2['setTime'][msg.to]
                    except:
                          pass
                    cl.sendText(msg.to, "Delete reading point:\n" + datetime.now().strftime('%H:%M:%S'))

#-----------------------------------------------

       #-------------Fungsi Respon Start---------------------#
            elif msg.text in ["Absen","SHINIGAMI","Respon"]:
              if msg.from_ in staff + admin + owner:
                ko.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 1]")
                ki.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 2]")
                kk.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 3]")
                kc.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 4]")
                ks.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 5]")
                ka.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 6]")
                kb.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 7]")
                cl.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 8]")
                ke.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 9]")
                ku.sendText(msg.to," ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 10]")
                k1.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 11]")
                k2.sendText(msg.to,"ɴɪɢʜᴛ ʀᴀɪᴅ [BOT 12]")
                k1.sendText(msg.to,"[ɴɪɢʜᴛ ʀᴀɪᴅ] ¤Ôñ ßõT¤")
      #-------------Fungsi Respon Finish---------------------#
      #-------------Fungsi Balesan Respon Start---------------------#
            elif msg.text in ["Ini Apa","ini apa","Apaan Ini","apaan ini"]:
                ki.sendText(msg.to,"Ya gitu deh intinya mah 􀨁􀅴questioning􏿿")

      #-------------Fungsi Balesan Respon Finish---------------------#

       #-------------Fungsi Speedbot Start---------------------#
            elif msg.text in ["Speed","Sp"]:
              if msg.from_ in staff + admin + owner:
                start = time.time()
                cl.sendText(msg.to, "Memproses....")
                elapsed_time = time.time() - start
                cl.sendText(msg.to, "%sDetik" % (elapsed_time))
      #-------------Fungsi Speedbot Finish---------------------#

      #-------------Fungsi Banned Send Contact Start------------------#
            elif msg.text in ["Ban:on"]:
              if msg.from_ in staff + admin + owner:
                wait["wblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"")
                kk.sendText(msg.to,"")
                kc.sendText(msg.to,"")
            elif msg.text in ["Unban:on"]:
              if msg.from_ in staff + admin + owner:
                wait["dblacklist"] = True
                cl.sendText(msg.to,"send contact")
                ki.sendText(msg.to,"")
                kk.sendText(msg.to,"")
                kc.sendText(msg.to,"")
      #-------------Fungsi Banned Send Contact Finish------------------#
      #----------------Mid via Tag--------------
            elif "Mid @" in msg.text:
              if msg.from_ in staff + admin + owner:
                _name = msg.text.replace("Mid @","")
                _nametarget = _name.rstrip(' ')
                gs = cl.getGroup(msg.to)
                for g in gs.members:
                    if _nametarget == g.displayName:
                        random.choice(KAC).sendText(msg.to, g.mid)
                    else:
                        pass
            #-----------------------------------------
      
      #-------------Fungsi Bannlist Start------------------#          
            elif msg.text in ["Banlist"]:
              if msg.from_ in staff + admin + owner:
                if wait["blacklist"] == {}:
                    cl.sendText(msg.to,"Tidak Ada Akun Terbanned")
                else:
                    ki.sendText(msg.to,"Blacklist user")
                    mc = ""
                    for mi_d in wait["blacklist"]:
                        mc += "->" +cl.getContact(mi_d).displayName + "\n"
                    cl.sendText(msg.to,mc)
      #-------------Fungsi Bannlist Finish------------------#  
      
            elif msg.text in ["Cek ban"]:
              if msg.from_ in staff + admin + owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    cocoa = ""
                    for mm in matched_list:
                        cocoa += mm + "\n"
                    cl.sendText(msg.to,cocoa + "")
            elif msg.text in ["Kill ban"]:
              if msg.from_ in staff + admin + owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.members]
                    matched_list = []
                    for tag in wait["blacklist"]:
                        matched_list+=filter(lambda str: str == tag, gMembMids)
                    if matched_list == []:
                        cl.sendText(msg.to,"There was no blacklist user")
                        return
                    for jj in matched_list:
                        ki.kickoutFromGroup(msg.to,[jj])
                        kk.kickoutFromGroup(msg.to,[jj])
                        kc.kickoutFromGroup(msg.to,[jj])
                    cl.sendText(msg.to,"Blacklist emang pantas tuk di usir")
            elif msg.text in ["Clear"]:
              if msg.from_ in owner:
                if msg.toType == 2:
                    group = cl.getGroup(msg.to)
                    gMembMids = [contact.mid for contact in group.invitee]
                    for _mid in gMembMids:
                        cl.cancelGroupInvitation(msg.to,[_mid])
                    cl.sendText(msg.to,"I pretended to cancel and canceled.")
            elif "albumat'" in msg.text:
              if msg.from_ in owner:
                try:
                    albumtags = msg.text.replace("albumat'","")
                    gid = albumtags[:6]
                    name = albumtags.replace(albumtags[:34],"")
                    cl.createAlbum(gid,name)
                    cl.sendText(msg.to,name + "created an album")
                except:
                    cl.sendText(msg.to,"Error")
        if op.type == 59:
            print op


    except Exception as error:
        print error


def a2():
    now2 = datetime.now()
    nowT = datetime.strftime(now2,"%M")
    if nowT[14:] in ["10","20","30","40","50","00"]:
        return False
    else:
        return True

def nameUpdate():
    while True:
        try:
        #while a2():
            #pass
            if wait["clock"] == True:
                now2 = datetime.now()
                now2 = datetime.strftime(now2,"(%H:%M)")
                profile = cl.getProfile()
                profile.displayName = wait["cName"]
                cl.updateProfile(profile)

                profile2 = ki.getProfile()
                profile2.displayName = wait["cName2"]
                ki.updateProfile(profile2)

                profile3 = kk.getProfile()
                profile3.displayName = wait["cName3"]
                kk.updateProfile(profile3)

                profile4 = kc.getProfile()
                profile4.displayName = wait["cName4"]
                kc.updateProfile(profile4)

                profile5 = ks.getProfile()
                profile5.displayName = wait["cName5"]
                ks.updateProfile(profile5)

                profile6 = ka.getProfile()
                profile6.displayName = wait["cName6"]
                ka.updateProfile(profile6)

                profile7 = kb.getProfile()
                profile7.displayName = wait["cName7"]
                kb.updateProfile(profile7)

                profile8 = ko.getProfile()
                profile8.displayName = wait["cName8"]
                ko.updateProfile(profile8)
                
                profile9 = ke.getProfile()
                profile9.displayName = wait["cName9"]
                ke.updateProfile(profile9)
                
                profile10 = ku.getProfile()
                profile10.displayName = wait["cName10"]
                ku.updateProfile(profile10)
            time.sleep(600)
        except:
            pass
thread2 = threading.Thread(target=nameUpdate)
thread2.daemon = True
thread2.start()



def findLyric(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = data.encode('utf-8')
    data = json.loads(data)
    for song in data:
        ki.sendText(to,"Lyrics Of " + song[0] + ":\n\n"+ song[5])
    time.sleep(100)
thread2 = threading.Thread(target=findLyric)
thread2.daemon = True
thread2.start()

def findMusic(to,song):
    params = {'songname':song}
    r = requests.get('https://ide.fdlrcn.com/workspace/yumi-apis/joox?'+urllib.urlencode(params))
    data = r.text
    data = data.encode('utf-8')
    data = json.loads(data)
    for song in data:
        ki.sendText(to,"This Your Music.\n\nJudul: " + song[0] + "\nWaktu: " + song[1] + "\nLink: " + song[3] + "\nDownload: " + song[4])
    time.sleep(100)
thread2 = threading.Thread(target=findMusic)
thread2.daemon = True
thread2.start()

while True:
    try:
        Ops = cl.fetchOps(cl.Poll.rev, 5)
    except EOFError:
        raise Exception("It might be wrong revision\n" + str(cl.Poll.rev))

    for Op in Ops:
        if (Op.type != OpType.END_OF_OPERATION):
            cl.Poll.rev = max(cl.Poll.rev, Op.revision)
            bot(Op)

