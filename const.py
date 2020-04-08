from secret import consumer_key, consumer_secret, \
                   access_token, access_token_secret

subscriptions = [
    "radleysports"    , "radleymusic"     , "radleyasocial"   ,
    "radleybsocial"   , "radleyfsocial"   , "radleyksocial"   ,
    "radleycsocial"   , "radleydsocial"   , "radleyesocial"   ,
    "radleygsocial"   , "radleyhsocial"   , "radleyjsocial"   ,
    "radleylsocial"   , "radleyprecentor" , "succentor"       ,
    "radley_warden"   , "radleychorister" , "radleyenrich"    ,
    "radleycocurr"    , "radleycollege"   , "radleyrugby"     ,
    "radleyarchives"  , "passionforpiano" , "radleycampus"    ,
    "radleylinks"     , "radleybiology"   , "radleyphysics"   ,
    "radleyemploy"    , "radleyfrench"    , "radleychemistry" ,
    "radleyswimming"  , "radleyshooting"  , "radleygerman"    ,
    "radleygehandu"   , "radleygovtpol"   , "radleycharities" ,
    "radleypshe"      , "radleygolf"      , "radley_stem"     ,
    "radleyentry"     , "radleycatering"  , "radleysailing"   ,
    "radleychapel"    , "radleymedical"   , "radleyfives"     ,
    "radleyathletics" , "radleyacadsupp"  , "radleyserpentes" ,
    "radleylibrary"   , "radleyit"        , "radleytheatre"   ,
    "radleysubwarden" , "radleyenglish"   , "radleytheology"  ,
    "radleygeography" , "radleymaths"     , "radley_football" ,
    "radleysust"      , "radleyshop"      , "radleydesign"    ,
    "radleygallery"   , "radleyartdept"   , "radleybc"        ,
    "radleyhockey"    , "radleystrength"  , "radleysportscen" ,
    "radleyrackets"   , "rccoffeeshop"    , "radleiansociety" ,
    "radleyccf"       , "radleyacademic"  , "radleyhistory"   ,
    "ianyorston"      , "radleypolo"      , "radleyxcountry"  ,
    "radleybadminton" , "radleytech"      , "radleyadventure" ,
    "radleycoding"    , "radleydigital"   , "radleyclassics"  ,
    "radleyeconomics" , "radleyclimates"  , "radleymandarin"  ,
    "radleycricket"   , "radleychronicle" , "radleyisocial"   ,
    "radleyuni"       , "radleyfencing"   , "radleyarthist"   ,
    "radleyjms"       , "radleygeol"      , "andrewcnorman" ]

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
