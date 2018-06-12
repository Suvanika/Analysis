# Use shebang here

#Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import time
import csv
import sys

class StdOutListener(StreamListener):

    def __init__(self, api = None):
        self.api = api
        self.filename = sys.argv[1]+'_'+time.strftime('%Y%m%d-%H%M%S')
        csvFile = open(self.filename, 'w')

    def on_status(self, status):
        print(self.filename)
        csvFile = open(self.filename, 'a')

        csvWriter = csv.writer(csvFile)

        if not 'RT @' in status.text:
            try:
                csvWriter.writerow([
                                    status.id,
                                    status.text
                                   ])
            except Exception as e:
                print(e)
                pass

        csvFile.close()

        return

    def on_error(self, status_code):
        print('Encountered error with status code:', status_code)
        return True

    def on_delete(self, status_id, user_id):
        """Called when a delete notice arrives for a status"""
        print("Delete notice")
        return True

    def on_limit(self, track):
        # If too many posts match our filter criteria and only a subset is sent to us
        print("!!! Limitation notice received")
        return True

    def on_timeout(self):
        print(sys.stderr, 'Timeout...')
        time.sleep(10)
        return True

def start_mining():
    #Variables that contains the user credentials to access Twitter API
    consumer_key = 'YZJMzf7bhl4vSwpapzHdLWQtz'
    consumer_secret = 'lrWrrhkf8BKu4eLlJsN8S2Xa7bur9hEA6Fl0PORgkUDGv2pzLe'
    access_token = '1005320917235298306-aP3iXwb5hCQKmhkXlNJQnl7y6rEAUb'
    access_token_secret = 'gUDjxNCff1jMfYbmhofZN81EaHHzbuoGtoLW01uNGLkXk'

    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    while True:
        try:
            stream.filter(track=sys.argv[2:])
        except:
            continue
if __name__ == '__main__':
    start_mining()