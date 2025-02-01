from datetime import datetime

# get current date and time
now = datetime.now()

# format and display the result
print(f"Current date and time: {now.strftime('%Y-%m-%d %H:%M:%S')}")