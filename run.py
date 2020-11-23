from shutil import copyfile
from os.path import join


## download data from Garmin using API

#!!! uses script downloaded from here using command line actions
# https://github.com/pe-st/garmin-connect-export


## read csv of activities and filter
def select_activities(source='', destination='', activities_to_ignore=[]):
    activities = []

    # read in csv file
    with open(join(source, '/activities.csv')) as a_file:
        headers = a_file.readline().split(',')
        for activity in a_file.readlines():

            # print(activity)
            activity = activity.split(',')
            # print(activity[12])

            if len(activity) > 12 and activity[12] != '"Cycling"':
                # print('TRUE')
                activities.append(activity[2])
            # break

    for activity in activities:
        # ignore activities with GPS errors for example
        if int(activity) in activities_to_ignore:
            pass
        else:
            file = activity.replace('"','')
            try:
                src = join(source,'activity_'+file+'.gpx')
                dst = join(destination,'activity_'+file+'.gpx')

                copyfile(src, dst)
            except:
                pass

    return

ignore = [181229424, 798916912]
source = 'garmin-connect-export/2020-11-22_garmin_connect_export'
destination = 'Strava-local-heatmap-browser-master/Strava-local-heatmap-browser-master/gpx'
select_activities(source, destination, ignore)

## plot heat map with selected activities
#!!!! uses another git repo
# https://hitbuh.com/remisalmon/Strava-local-heatmap-browser
