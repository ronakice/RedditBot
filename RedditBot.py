import praw
import time

r=praw.Reddit('Simple comment parser')
r.login()
inapp_users=set()
kind_users=set()
lstk=["thank","please"]
lstin=["shit","stupid","retarded","fuck"]
usr_comment_good={}
usr_comment_bad={}
already_seenk=[]
already_seenin=[]
while True:
    comments=r.get_comments('askreddit')
    for comment in comments:
        body=comment.body.lower()
        for wordsk in lstk:
            if body.find(wordsk) != -1:
                usr_comment_good[comment.author]=body
                kind_users.add(comment.author)
                break
        for wordsin in lstin:
            if body.find(wordsin) != -1:
                usr_comment_bad[comment.author]=body
                inapp_users.add(comment.author)
                break
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
    r.user.send_message('rbot42', msg)
    time.sleep(15)
