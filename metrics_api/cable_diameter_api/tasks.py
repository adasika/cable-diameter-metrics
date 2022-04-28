from celery import shared_task
import requests 
from .models import Cable, Backup_Data

@shared_task
def get_cable_data():
    #we want to delete all previous data from our TEMP DB
    Cable.objects.all().delete()
    r = requests.get("http://takehome-frontend.oden.network/?metric=cable-diameter")
    #create a dict of the json object
    cable_dict = r.json()
    series = cable_dict['series']
    #effectively traversing through the first element of series
    series_list = series[0]
    #Bit of high complexity logic, can be tuned with more time
    #ideally would separate this into separate functions as the runtime of this can be exceedingly high with large amounts of data
    for i in series:
        for j in i:
            if isinstance(j, str):
                time_val = j
                print("Time is:" + time_val)
            else:
                for index, value in enumerate(j):
                    if index == 0:
                        min_val = value
                    elif index == 1:
                        av_val = value
                    else:
                        max_val = value
                        #honestly this could be modularized into different functions
                        Cable.objects.create(
                            time_stamp = time_val,
                            minimum = min_val,
                            average = av_val,
                            maximum = max_val
                        )
                        #this step is to ensure that we don't ever lose data~ there are better ways to do this
                        #due to time limit on assignment, have decided to just create a backup table
                        Backup_Data.objects.create(
                            time_stamp = time_val,
                            minimum = min_val,
                            average = av_val,
                            maximum = max_val
                        )
    #Cleaned up most of my test prints!
    return print("finished saving data")

