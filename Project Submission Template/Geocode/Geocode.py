import sys
import geocoder
import requests
import json
import csv
import os
import time 

_key = 'AIzaSyCjh0v3nbkXiDN8bNdRvMxHDbJL18N62PY'
_places_key = 'AIzaSyDVR_w2Radkfe4pN8YJLP6Hdsq6IjbxKJU' #'AIzaSyDN3L_hzHv-cun20ofuig11rG4Y-obDGIM'
city_state = 'Peoria IL'

kml_start = """<?xml version=\"1.0\" encoding=\"UTF-8\" ?>
<kml xmlns=\"http://earth.google.com/kml/2.2\">
<Document>
<name>Construction</name>
<description>Completed on 9/31/2017</description>
<Style id=\"style5\">
<LineStyle>
<color>6414F0FF</color>
<width>30</width>
</LineStyle>
</Style>
<Style id=\"style6\">
<LineStyle>
<color>64FF78F0</color>
<width>30</width>
</LineStyle>
</Style>
<Style id="icon"> <IconStyle> <Icon> <href>OrangeCone_Hackathon-02.png</href> </Icon> </IconStyle> </Style>"""

kml_open = """<Placemark>
<name>Optimal Path</name>
<description>Optimal Path</description>
<styleUrl>#style5</styleUrl>
<LineString>
<tessellate>1</tessellate>
<coordinates>\n"""

kml_open_future = """<Placemark>
<name>Optimal Path</name>
<description>Optimal Path</description>
<styleUrl>#style6</styleUrl>
<LineString>
<tessellate>1</tessellate>
<coordinates>\n"""

kml_middle = """</coordinates>
</LineString>
</Placemark>
<Placemark>
<name>TSP Path</name>
<description>TSP Approximation Path</description>
<styleUrl>#style6</styleUrl>
<LineString>
<tessellate>1</tessellate>
<coordinates>"""

kml_term = """</coordinates>
</LineString>
</Placemark>"""
kml_end = """</Document>
</kml>"""

place_mark_start = """<Placemark>
<styleUrl>#icon</styleUrl>
<Point>
<coordinates>"""

place_mark_end = """</coordinates>
</Point>
</Placemark>"""

def get_lat_lng(address):
    """Given a US Street Address returns a two-element list with the latitude and longitude"""
    results = geocoder.google(address, key=_key)
    return results.latlng


def get_address(coordinates):
    """Given a two element list with the latatude and longitude returns a Street Address"""
    results = geocoder.google(coordinates, method='reverse', key=_key)
    return results

def get_intersection(road_1, road_2):
    """ Given the names of two Peoria Roads as Strings returns the Latatude and Longitude of their intersection"""
    query = 'Intersection of ' + road_1 + ' and ' + road_2 + city_state
    coords = get_lat_lng(query)
    return coords

def get_start_stop(road_name, start_branch, stop_branch):
    """Given a project street a start street name and a stop street name
    returns a two element list with the coordinates of the starting intersection and ending intersection"""
    start_coords = get_intersection(road_name, start_branch)
    stop_coords = get_intersection(road_name, stop_branch)
    return [start_coords, stop_coords]

def add_place(name, address, coords, website, type):
    """ Adds a place with place name lat and lng coords website and type to google maps
    returns a google maps place id"""
    url = 'https://maps.googleapis.com/maps/api/place/add/json?key=AIzaSyDVR_w2Radkfe4pN8YJLP6Hdsq6IjbxKJU'
    data = {"location": {"lat": coords[0] , "lng":coords[1]}, "accuracy": 10, "name": name, "address":address,"types":[type], "website":website, "language": "en-US"}
    data_json = json.dumps(data)
    print(data_json)
    r = requests.post(url, data=data_json)
    results = r.json()['place_id']
    return results

def get_details(place_id):
    """Returns the details of a google maps place id"""
    url = 'https://maps.googleapis.com/maps/api/place/details/json'
    params = {"key":_places_key, "placeid":place_id}
    r = requests.get(url, params)
    print(r.json())

def create_two_point_kml(coords, coords_end):
    """Creates the kml for a two point constructions segment given two pairs of coordinates"""
    kml_str = ""
    kml_str = kml_str + str(coords[1]) + ',' + str(coords[0]) + ',0.0\n'
    kml_str = kml_str + str(coords_end[1]) + ',' + str(coords_end[0]) + ',0.0\n'
    place_mark = place_mark_start
    place_mark = place_mark + str(coords[1]) + ',' + str(coords[0]) + ',0.0\n'
    place_mark = place_mark + place_mark_end
    place_mark = place_mark + place_mark_start
    place_mark = place_mark + str(coords_end[1]) + ',' + str(coords_end[0]) + ',0.0\n'
    place_mark = place_mark + place_mark_end
    kml_final = kml_open + kml_str + kml_middle + kml_term + place_mark
    return kml_final

def create_two_point_kml_future(coords, coords_end):
    """Creates the kml for a two point constructions segment given two pairs of coordinates"""
    kml_str = ""
    kml_str = kml_str + str(coords[1]) + ',' + str(coords[0]) + ',0.0\n'
    kml_str = kml_str + str(coords_end[1]) + ',' + str(coords_end[0]) + ',0.0\n'
    place_mark = place_mark_start
    place_mark = place_mark + str(coords[1]) + ',' + str(coords[0]) + ',0.0\n'
    place_mark = place_mark + place_mark_end
    place_mark = place_mark + place_mark_start
    place_mark = place_mark + str(coords_end[1]) + ',' + str(coords_end[0]) + ',0.0\n'
    place_mark = place_mark + place_mark_end
    kml_final = kml_open_future + kml_str + kml_middle + kml_term + place_mark
    return kml_final

def create_one_point_kml(coords):
    """Creates the kml for a singe construction event"""
    place_mark = place_mark_start
    place_mark = place_mark + str(coords[1]) + ',' + str(coords[0]) + ',0.0\n'
    place_mark = place_mark + place_mark_end
    return place_mark

kml_str = kml_start


with open('c:\\geocode\\roads.csv', 'r') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    skip = 1
    for row in reader:
        if not skip:
            ## dd/mm/yyyy format print 
            today = (time.strftime("%Y"))
            next = get_start_stop(row[0], row[1], row[2])
            if row[3] > today:
                kml_str = kml_str + create_two_point_kml_future(next[0], next[1])
            else:
                kml_str = kml_str + create_two_point_kml(next[0], next[1])
        else:
            skip = 0

kml_str = kml_str + kml_end
with open('c:\\geocode\\alta.kml', 'w') as f:
    f.write(kml_str)
os.startfile('c:\\geocode\\alta.kml')