import random
from datetime import datetime, timedelta

#define a start and end date range
start_date = datetime(2020, 1, 1) #start from junaury 1, 2020
end_date = datetime(2030, 12, 31) #end at december 31, 2030

# genrate a random number of seconds whithin the range
random_seconds = random.randint(0, int((end_date - start_date).total_seconds()))

#calculate the randome date and time
random_date = start_date + timedelta(seconds=random_seconds)

# display the result
print(f"Random date and time: {random_date.strftime('%Y-%m-%d %H:%M:%S')}")