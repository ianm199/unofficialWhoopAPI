# unofficialWhoopAPI

I created a wrapper around the unofficial WHOOP API documented here https://app.swaggerhub.com/apis/DovOps/whoop-unofficial-api/1.0.1#/. As far as I know this is not support officially by WHOOP in anyway. My motivation was that WHOOP users will be able to derive more health insights by being able to access their own data directly.

I used the script provided here as a base https://gist.github.com/jkreileder/459cf1936e099e2e521cee7d2d4b7acb.

With this wrapper you can easily get a dataframe of your cycle data, workout data, sleep data, and heart rate by tick.

# Getting Started

Login by initializing a whoopUser with the same credentials you use on WHOOP.com

`user = whoopUser("youremail", "yourpassword")`

By default for cycle, sleep, and workout data will pull all available data. You can see this done in [examples.py](/examples.py). In order to change the time frame you can pass in alternate parameters like this:

`alternate_timeframe = {'start': '2020-12-10T00:00:00.000Z','end': '2020-12-13T00:00:00.000Z'}
user.get_cycles_df(params=alternate_timeframe)`

Note that when pulling heart rate data the WHOOP API only allows you to pull 8 days worth of data at a time. Additiaonlly my function whoopUser.get_heart_rate_df() converts the 13 second UNIX timestamp to date time, as a result it can take a bit of time ot pull the heart rate data.

# Still to do
I haven't tested this at all outside of just using my own account, there could be many edge cases I'm not aware of. 

I didn't implement all the endpoints possible from the swaggerhub page, most notably the survey data which would be nice to export.

If anyone finds any issues or has any ideas to help please let me know!
