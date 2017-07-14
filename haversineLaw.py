
'''
Harversine's Law:
	- find the distance between two points on the Earth, given their longitudes and latitudes.
	- Thank you Raspberry Pi!
'''

import h5py
import numpy as np
from math import radians, cos, sin, asin, sqrt

def haversineLaw(lat1, lon1, lat2, lon2):
    ''' Haversine's Law: find the distance between two GPS locations'''
    
    # convert int to float to avoid errors and convert degrees to radians
    lon1 = radians(float(lon1))
    lat1 = radians(float(lat1))
    lon2 = radians(float(lon2))
    lat2 = radians(float(lat2))
    
    dlon = lon2 - lon1 
    dlat = lat2 - lat1
    
    # haversine formula 
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    
    c = 2 * asin(sqrt(a)) 
    
    # Radius of earth in kilometers
    r = 6371 
    return c * r


def nearest_neighbor(inSituLatutude, inSituLongitude, satelliteLatitude, satelliteLongitude, pollutant):
	''' nearest_neighbor: find the satelite pixel that corresponds to the ground instrument '''
	
	# 20036 km is the longest distance on the Earth's surface
	nearest = 20036
	locationIndex = 0
	
	for satLat, satLon, pm in zip(satelliteLatitude, satelliteLongitude, pollutant):
		
		# haversine(lat1, lon1, lat2, lon2)
		distance = haversineLaw(inSituLatutude, inSituLongitude, satLat, satLon)
		locationIndex += 1
		
		if distance < nearest:
			
			# find the nearest MERRA-2 pixel location
			nearest = distance
			nearestIndex = locationIndex
			
			# Pollutant concentration at that pixel location
			pollutantConcentration = pm
			
			# GPS coordinates for the nearest pixel location
			nearestLatitude = satLat
			nearestLongitude = satLon
			
			# print distance to know if this is working
			print(distance)
			
	# print results
	print('\nPM2.5 = ' + str(pollutantConcentration))
	print('\tLatitude: ' + str(nearestLatitude))
	print('\tLongitude: ' + str(nearestLongitude))
	
	# print the index of the pixel
	print('\tPixel Index: [' + str(nearestIndex - 1) + ':' + str(nearestIndex) + ']')
