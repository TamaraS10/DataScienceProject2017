from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import tweepy as tp
import sys
from datetime import date
import time as t

access_token="740635692359950336-4rgBW9g1baTzcvX8rVzBBRbS08KIN39"
access_token_secret="KgJ0LlsMeKvEIdJblamLN411HNGo3N3FezBHpJvgmu0Xa"
consumer_key="GT3xrIN0V85UdqPqUZ4E28egE"
consumer_secret="oBzZvyTApKHxP0GSqo9lbRJ1K93CJRIovRN8zdBaic5oANGRvN"


class CustomStreamListener(tp.StreamListener):

    def on_data(self, data):

        until_date = '2017-05-19'
        current_date = str(date.today())
        current_time = t.localtime()
        current = int(t.strftime("%M", current_time)) + 1
        previous = 70

        #open file for recording
        file_name = 'Output_' + current_date + '_NewsSources.json'
        print('Creating output file: ' + file_name)
        output_file = open(file_name, 'a')

        while until_date != current_date:
            #t.sleep(5)
            current_time = t.localtime()
            current = int(t.strftime("%M", current_time)) + 1
            print(str(current))
            print(str(previous))
            if current != previous:
                previous = current
                print(str(current))
                print(str(previous))
                #close output file
                output_file.close()
                #create and open new file
                current_date = str(date.today())
                file_name = 'Output_' + current_date + str(current) + '_NewsSources.json'  #replace current with data when working
                print('Creating new output file: ' + file_name)
                output_file = open(file_name, 'a')
                #continue recording
            else:
                try:
                    output_file.write(data)

                    return True
                except:
                    print('failed on_data')
                    t.sleep(5)
                    pass

    def on_error(self, status_code):
        print >> sys.stderr, 'Encountered error with status code:', status_code
        return True  # Don't kill the stream

    def on_timeout(self):
        print >> sys.stderr, 'Timeout...'
        return True  # Don't kill the stream


until_date = '2017-05-19'
current_date = str(date.today())
print('Current date: ' + current_date)
print('Until date: ' + until_date)
authentication = OAuthHandler(consumer_key,consumer_secret)
authentication.set_access_token(access_token,access_token_secret)
stream = Stream(authentication,CustomStreamListener())
stream.filter(track=['USAToday', 'LATimes', 'USNews', 'Newsweek', 'MSNBC', 'HuffPost', 'CBSNews', 'ABC', 'NPR', 'WashingtonPost', 'TheEconomist', 'AP', 'WSJ', 'BBCWorld', 'TIME', 'Fox News', 'NyTimes', 'CNN'])
