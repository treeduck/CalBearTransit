from math import radians, cos, sin, asin, sqrt
import datetime

allcoord = [[37.874379, -122.263606, "Tolman Hall: Hearst Avenue @ Arch Street"],
[37.87482, -122.26403, "North Gate Hall: Hearst Avenue @ Euclid Avenue"],
[37.875209, -122.257919, "Cory Hall: Hearst Avenue @ LeRoy Avenue"],
[37.873346, -122.257512, "Evans Hall: Hearst Mining Circle side"], 
[37.872533, -122.2541, "Gayley @ Stadium Rimway"], 
[37.871364, -122.252887, "Haas School of Business: Piedmont Avenue Side"],
[37.869738, -122.252491, "International House: Piedmont Avenue @ Bancroft Way"], 
[37.867985, -122.252212, "Piedmont Avenue @ Channing Way"], 
[37.867079, -122.25395, "College Avenue @ Haste Street"], 
[37.869408, -122.25484, "Kroeber Hall: Bancroft Way @ College Avenue"], 
[37.869103, -122.257222, "Hearst Memorial Gym: Bancroft Way @ Bowditch Street"], 
[37.868612, -122.261245, "Sproul Hall: Bancroft Way @ Barrow Lane"], 
[37.868209, -122.263606, "RSF: Bancroft Way @ Ellsworth Street"], 
[37.867765, -122.267039, "Banway Building: Bancroft Way @ Shattuck Avenue"], 
[37.868273, -122.267661, "Shattuck Avenue @ Kittredge Street"], 
[37.870178, -122.267876, "Downtown Berkeley Bart Station"], 
[37.872618, -122.265794, "Oxford Street @ University Avenue"]]

allTimes = {"Downtown Berkeley Bart Station":["07:00", "07:30", "08:00", "08:30", "09:00", "09:30", "10:00", "10:30", "11:00", "11:30", "12:00", "12:30", "13:00", "13:30", "14:00", "14:30", "15:00", "15:30", "16:00", "16:30", "17:00", "17:30", "18:00", "18:30", "19:00", "19:30"],
        "Oxford Street @ University Avenue":["07:02", "07:32", "08:02", "08:32", "09:02", "09:32", "10:02", "10:32", "11:02", "11:32", "12:02", "12:32", "13:02", "13:32", "14:02", "14:32", "15:02", "15:32", "16:02", "16:32", "17:02", "17:32", "18:02", "18:32", "19:02"],
        "Tolman Hall: Hearst Avenue @ Arch Street":["07:04", "07:34", "08:04", "08:34", "09:04", "09:34", "10:04", "10:34", "11:04", "11:34", "12:04", "12:34", "13:04", "13:34", "14:04", "14:34", "15:04", "15:34", "16:04", "16:34", "17:04", "17:34", "18:04", "18:34", "19:04"],
        "North Gate Hall: Hearst Avenue @ Euclid Avenue":["07:05", "07:35", "08:05", "08:35", "09:05", "09:35", "10:05", "10:35", "11:05", "11:35", "12:05", "12:35", "13:05", "13:35", "14:05", "14:35", "15:05", "15:35", "16:05", "16:35", "17:05", "17:35", "18:05", "18:35", "19:05"],
        "Cory Hall: Hearst Avenue @ LeRoy Avenue":["07:06", "07:36", "08:06", "08:36", "09:06", "09:36", "10:06", "10:36", "11:06", "11:36", "12:06", "12:36", "13:06", "13:36", "14:06", "14:36", "15:06", "15:36", "16:06", "16:36", "17:06", "17:36", "18:06", "18:36", "19:06"],
        "Evans Hall: Hearst Mining Circle side":["07:08", "07:38", "08:08", "08:38", "09:08", "09:38", "10:08", "10:38", "11:08", "11:38", "12:08", "12:38", "13:08", "13:38", "14:08", "14:38", "15:08", "15:38", "16:08", "16:38", "17:08", "17:38", "18:08", "18:38", "19:08"],
        "Gayley @ Stadium Rimway":["07:10", "07:40", "08:10", "08:40", "09:10", "09:40", "10:10", "10:40", "11:10", "11:40", "12:10", "12:40", "13:10", "13:40", "14:10", "14:40", "15:10", "15:40", "16:10", "16:40", "17:10", "17:40", "18:10", "18:40", "19:10"],
        "Haas School of Business: Piedmont Avenue Side":["07:11", "07:41", "08:11", "08:41", "09:11", "09:41", "10:11", "10:41", "11:11", "11:41", "12:11", "12:41", "13:11", "13:41", "14:11", "14:41", "15:01", "15:41", "16:11", "16:41", "17:11", "17:41", "18:11", "18:41", "19:11"],
        "International House: Piedmont Avenue @ Bancroft Way":["07:12", "07:42", "08:12", "08:42", "09:12", "09:42", "10:12", "10:42", "11:12", "11:42", "12:12", "12:42", "13:12", "13:42", "14:12", "14:42", "15:02", "15:42", "16:12", "16:42", "17:12", "17:42", "18:12", "18:42", "19:12"],
        "Piedmont Avenue @ Channing Way":["07:14", "07:44", "08:14", "08:44", "09:14", "09:44", "10:14", "10:44", "11:14", "11:44", "12:14", "12:44", "13:14", "13:44", "14:14", "14:44", "15:14", "15:44", "16:14", "16:44", "17:14", "17:44", "18:14", "18:44", "19:14"],
        "College Avenue @ Haste Street":["07:18", "07:48", "08:18", "08:48", "09:18", "09:48", "10:18", "10:48", "11:18", "11:48", "12:18", "12:48", "13:18", "13:48", "14:18", "14:48", "15:18", "15:48", "16:18", "16:48", "17:18", "17:48", "18:18", "18:48", "19:18"],
        "Kroeber Hall: Bancroft Way @ College Avenue":["07:20", "07:50", "08:20", "08:50", "09:20", "09:50", "10:20", "10:50", "11:20", "11:50", "12:20", "12:50", "13:20", "13:50", "14:20", "14:50", "15:20", "15:50", "16:20", "16:50", "17:20", "17:50", "18:20", "18:50", "19:20"],
        "Hearst Memorial Gym: Bancroft Way @ Bowditch Street":["07:21", "07:51", "08:21", "08:51", "09:21", "09:51", "10:21", "10:51", "11:21", "11:51", "12:21", "12:51", "13:21", "13:51", "14:21", "14:51", "15:21", "15:51", "16:21", "16:51", "17:21", "17:51", "18:21", "18:51", "19:21"],
        "Sproul Hall: Bancroft Way @ Barrow Lane":["07:23", "07:53", "08:23", "08:53", "09:23", "09:53", "10:23", "10:53", "11:23", "11:53", "12:23", "12:53", "13:23", "13:53", "14:23", "14:53", "15:23", "15:53", "16:23", "16:53", "17:23", "17:53", "18:23", "18:53", "19:23"],
        "RSF: Bancroft Way @ Ellsworth Street":["07:25", "07:55", "08:25", "08:55", "09:25", "09:55", "10:25", "10:55", "11:25", "11:55", "12:25", "12:55", "13:25", "13:55", "14:25", "14:55", "15:25", "15:55", "16:25", "16:55", "17:25", "17:55", "18:25", "18:55", "19:25"],
        "Banway Building: Bancroft Way @ Shattuck Avenue":["07:27", "07:57", "08:27", "08:57", "09:27", "09:57", "10:27", "10:57", "11:27", "11:57", "12:27", "12:57", "13:27", "13:57", "14:27", "14:57", "15:27", "15:57", "16:27", "16:57", "17:27", "17:57", "18:27", "18:57", "19:27"],
        "Shattuck Avenue @ Kittredge Street":["07:28", "07:58", "08:28", "08:58", "09:28", "09:58", "10:28", "10:58", "11:28", "11:58", "12:28", "12:58", "13:28", "13:58", "14:28", "14:58", "15:28", "15:58", "16:28", "16:58", "17:28", "17:58", "18:28", "18:58", "19:28"],
        }


def haversine(lon1, lat1, lon2, lat2):
    """
    Calculate the great circle distance between two points 
    on the earth (specified in decimal degrees)
    """
    # convert decimal degrees to radians 
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    # haversine formula 
    dlon = lon2 - lon1 
    dlat = lat2 - lat1 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a)) 
    km = 6367 * c
    #converts into decimal with two places
    km = float("%.2f" % round(km, 2))
    return km

def closesttime(stationname):
    """
    >>> closesttime("Evans Hall: Hearst Mining Circle side")
    '10:38'
    """
    nowtime = datetime.datetime.time(datetime.datetime.now())
    for i in range(0, 25):
        prevtime = allTimes[stationname][i-1]
        nexttime = allTimes[stationname][i]
        hour = int(prevtime[0:2])
        minute = int(prevtime[3:5])
        if nowtime.hour == hour:
            if nowtime.minute >= minute:
                return nexttime
            if nowtime.minute < minute: 
                return prevtime
    return allTimes[stationname][0][1:]

#returns string
def findcloseststop(curlon, curlat):
    maxdistance = float('inf')
    busstop = ''
    for i in range (0, 16):
        distance = haversine(curlon, curlat, allcoord[i][0], allcoord[i][1])
        if distance < maxdistance:
            maxdistance = distance
            busstop = allcoord[i][2]
            closest = closesttime(busstop)
    return ("Kilometers to nearest stop: "+ str(maxdistance), "Nearest stop: " + busstop, "Next arrival: " + closest)






