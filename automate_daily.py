import twint
import schedule
import time
import os
import datetime
os.environ['TWINT_DEBUG'] = 'debug'


# you can change the name of each "job" after "def" if you'd like.
def jobone():
    
	#time15minago=(datetime.datetime.now() - datetime.timedelta(minutes = 10))
	#current_time = time15minago.strftime(f"%Y-%m-%d %H:%M:%S")
	#current_timestamp = time15minago.strftime(f"%Y%m%d%H%M%S")
	day_current = datetime.datetime.now()
	while True: 	
		current_timestamp = day_current.strftime(f"%Y%m%d%H%M%S")
		day_2_before = (day_current - datetime.timedelta(days = 3))
		day_before = (day_current - datetime.timedelta(days = 1))

		print("current date ", day_current, " before date ",day_before)
		c = twint.Config()
		#c.Username = "shahzadsaeed240"
		c.User_id = "3723347053"
		c.Limit = 1000
		c.Store_csv = True
		c.Output = "file"+current_timestamp+".csv"	
		#c.Retweets = True
		c.Since = day_2_before.strftime(f"%Y-%m-%d %H:%M:%S")
		#c.Since = "2021-03-01"
		#c.Until = current_time
		c.Until = day_current.strftime(f"%Y-%m-%d %H:%M:%S")
		#c.Show_hashtags = True
		#c.Show_cashtags = True
		#c.Stats = True
		#c.Debug = True
		#c.Pandas = True
		#c.All="shahzadsaeed240"
		twint.run.Search(c)
		day_current = day_before
jobone()

# run every minute(s), hour, day at, day of the week, day of the week and time. Use "#" to block out which ones you don't want to use.  Remove it to active. Also, replace "jobone" and "jobtwo" with your new function names (if applicable)

# schedule.every(5).minutes.do(jobone)
#schedule.every().hour.do(jobone)
# schedule.every().day.at("10:30").do(jobone)
# schedule.every().monday.do(jobone)
# schedule.every().wednesday.at("13:15").do(jobone)

#schedule.every(1).minutes.do(jobone)
#schedule.every().hour.do(jobtwo)
# schedule.every().day.at("10:30").do(jobtwo)
# schedule.every().monday.do(jobtwo)
# schedule.every().wednesday.at("13:15").do(jobtwo)

#while True:
#  schedule.run_pending()
#  time.sleep(1)
