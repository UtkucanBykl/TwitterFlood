import argparse
from TwitterFlood.base import TweetFlood

parser = argparse.ArgumentParser()

# add long and short argument
parser.add_argument("--flood", "-f", help="set flood text tweet")
parser.add_argument("--count", "-c", help="set split count")
parser.add_argument("--consumer", "-ck", help="add consumer key")
parser.add_argument("--consumer_secret", "-cs", help="add consumer secret key")
parser.add_argument("--access", "-a", help="add access key")
parser.add_argument("--access_secret", "-ak", help="add access secret key")

args = parser.parse_args()

if args.flood and args.count and args.consumer and args.consumer_secret and args.access and args.access_secret:

    c_key = args.consumer
    c_secret = args.consumer_secret
    a_key = args.access
    a_secret = args.access_secret
    tw = TweetFlood(args.flood, int(args.count))
    tw.auth(c_key, c_secret, a_key, a_secret)
    tw.send_tweet()
