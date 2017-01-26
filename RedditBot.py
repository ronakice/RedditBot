import praw
import time

r = praw.Reddit(user_agent='Comment Extraction',
                     client_id='Ho4Yr54TEqpV2Q', client_secret="EF-80ngO-IbsULqfc_rjsuperfk",
                     username='rbot42', password='abc123')
inapp_users=set()
kind_users=set()
lstk=["thank","please"]
lstin=["shit","stupid","retarded"]
already_seenk=[]
already_seenin=[]
while True:
    inapp_users=set()
    kind_users=set()
    usr_comment_good={}
    usr_comment_bad={}
    msg=""
    ct=0
    for comment in r.subreddit('uwaterloo').stream.comments():
        body=comment.body.lower()
        ct+=1
        print(ct)
        #print(body)
        for wordsk in lstk:
            if body.find(wordsk) != -1:
                if comment.author not in already_seenk:
                    print("GOOOO")
                    usr_comment_good[comment.author]=body
                    kind_users.add(comment.author)
                break
        for wordsin in lstin:
            if body.find(wordsin) != -1:
                if comment.author not in already_seenin:
                    print("ZOODDD")
                    usr_comment_bad[comment.author]=body
                    inapp_users.add(comment.author)
                break
        if ct==100:
            break
    print("HEY")
    if len(kind_users)!=0:
        msg = "Kind users: "
    for user in kind_users:
        #print (user)
        if user not in already_seenk:
            msg+=str(user)+", "
            already_seenk.append(user)
    msg+="\n"
    if len(inapp_users)!=0:
        msg +="Inappropriate users: "
    for user in inapp_users:
        # print (user)
        if user not in already_seenin:
            msg += ", "+ str(user)
            already_seenin.append(user)
        msg +=".\n"
    msg+="\n"
    for i in usr_comment_bad.keys():
        msg+="%s : %s"%(i, usr_comment_bad[i])
        msg+="\n"
    for i in usr_comment_good.keys():
        msg+="%s : %s"%(i, usr_comment_good[i])
        msg+="\n"
    if msg=="":
        print("go")
        r.redditor('rbot42').message('TEST',"Nothing interesting going on right now!")

    else:
        print("lo")
        r.redditor('rbot42').message('TEST',msg)
    time.sleep(15)
