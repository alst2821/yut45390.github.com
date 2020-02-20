from secret import consumer_key, consumer_secret, \
                   access_token, access_token_secret

subscriptions = [
    "radleysports", "radleymusic", "radleyasocial", "radleybsocial",
    "radleycsocial", "radleydsocial", "radleyesocial", "radleyfsocial",
    "radleygsocial", "radleyhsocial", "radleyjsocial", "radleyksocial",
    "radleylsocial", "radleyprecentor", "succentor", "radley_warden",
    "radleycocurr", "radleycollege", "radleyrugby", "radleychorister",
    "radleyarchives", "passionforpiano", "radleycampus", "radleyenrich",
    "radleylinks", "radleybiology", "radleyphysics", "radleyemploy",
    "radleyswimming", "radleyshooting", "radleygerman", "radleyfrench",
    "radleygehandu", "radleygovtpol", "radleycharities", "radleychemistry",
    "radleypshe", "radleygolf", "radley_stem", "radleyentry",
    "radleychapel", "radleymedical", "radleyfives", "radleyathletics",
    "radleylibrary", "radleyit", "radleytheatre", "radleyacadsupp",
    "radleysubwarden", "radleyenglish", "radleygallery", "radleytheology",
    "radleygeography", "radleymaths",
    "radleygallery", "radleyartdept", "radleybc", "radleycatering",
    "radleyhockey", "radleystrength", "radleysportscen", "radleytheatre",
    "radleyrackets", "rccoffeeshop", "radleiansociety", "radleyshop",
    "radleyccf", "radleyacademic", "radleyhistory", "radleydesign",
    "ianyorston", "radleypolo", "radleyxcountry", "radleyfencing",
    "radleybadminton", "radleytech", "radleyadventure",
    "radleycoding", "radleydigital", "radleyclassics",
    "radleyeconomics", "radleypolo", "radleymandarin",
    "radleycricket", "radleychronicle", "radleyisocial", "radleyuni" ]

def change(s):
    a = s.replace("radley","")
    b = a.replace("social","Social")
    return b

header="""======================
 Twitter links Radley
======================

.. list-table::
   :widths: auto
	    
"""
footer="""

.. code-block:: python
                
    import tweepy
    import datetime
    import const
    
    def sort_by_date(e):
        return e['latest']
    
    mintime=datetime.datetime.strptime("2001-01-01 01:01:01",
                "%Y-%m-%d %H:%M:%S")
    auth = tweepy.OAuthHandler(const.consumer_key,
                const.consumer_secret)
    auth.set_access_token(const.access_token,
                const.access_token_secret)
    api = tweepy.API(auth,wait_on_rate_limit=True,
                wait_on_rate_limit_notify=True)
    
    alldata =[]
    for s in const.subscriptions:
        user = api.get_user(s)
        latest = mintime
        public_tweets = api.user_timeline(s)
        if len(public_tweets) > 0:
            tweet = public_tweets[0]
            latest=tweet.created_at
        alldata.append(
            {'subscription': s,
             'name'        : user.name,
             'description' : user.description,
             'latest'      : latest
            }
        )
        
    sorted_data = sorted(alldata, key=sort_by_date, reverse=True)
    
    output="data.rst"
    f=open(output,"w")
    f.write(const.header)
    count=1
    for e in sorted_data:
        f.write("   * - %d\\n" % count)
        count += 1
        f.write("     - `%s <https://twitter.com/%s>`_\\n" % (
            const.change(e['subscription']),e['subscription']))
        f.write("     - %s\\n" % e['latest'].strftime(
                "%Y-%m-%d %H:%M:%S"))
    
    f.close()

"""
