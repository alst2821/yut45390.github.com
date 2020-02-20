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

output="doc/twitter.rst"
f=open(output,"w")
f.write(const.header)
count=1
for e in sorted_data:
    f.write("   * - %d\n" % count)
    count += 1
    f.write("     - `%s <https://twitter.com/%s>`_\n" % (
        const.change(e['subscription']),e['subscription']))
    f.write("     - %s\n" % e['latest'].strftime(
            "%Y-%m-%d %H:%M:%S"))
f.write("\nUpdated on %s\n" % datetime.datetime.now())
f.write(const.footer)
f.close()
