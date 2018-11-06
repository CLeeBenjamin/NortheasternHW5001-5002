'''
CS5001
HW4
kmeans_driver.py
FALL 2018
CASTON BOYD
'''

import random
import math
from kmeans_viz import draw_centroids
from kmeans_viz import draw_assignment

DATA = [ [-32.97, -21.06], [9.01, -31.63], [-20.35, 28.73], [-0.18, 26.73],
         [-25.05, -9.56], [-0.13, 23.83], [19.88, -18.32], [17.49, -14.09],
         [17.85, 27.17], [-30.94, -8.85], [4.81, 42.22], [-4.59, 11.18],
         [9.96, -35.64], [24.72, -11.39], [14.44, -43.31], [-10.49, 33.55],
         [4.24, 31.54], [-27.12, -17.34], [25.24, -12.61], [20.26, -4.7],
         [-16.4, -19.22], [-15.31, -7.65], [-26.61, -20.31], [15.22, -30.33],
         [-29.3, -12.42], [-50.24, -21.18], [-32.67, -13.11], [-30.47, -17.6],
         [-23.25, -6.72], [23.08, -9.34], [-25.44, -6.09], [-37.91, -4.55],
         [0.14, 34.76], [7.93, 49.21], [-6.76, 12.14], [-19.13, -2.24],
         [12.65, -7.23], [11.25, 25.98], [-9.03, 22.77], [9.29, -26.2],
         [15.83, -1.45], [-22.98, -27.37], [-25.12, -23.35], [21.12, -26.68],
         [20.39, -24.66], [26.69, -28.45], [-45.42, -25.22], [-8.37, -21.09],
         [11.52, -16.15], [7.43, -32.89], [-31.94, -11.86], [14.48, -10.08],
         [0.63, -20.52], [9.86, 13.79], [-28.87, -17.15], [-29.67, -22.44],
         [-20.94, -22.59], [11.85, -9.23], [30.86, -21.06], [-3.8, 22.54],
         [-5.84, 21.71], [-7.01, 23.65], [22.5, -11.17], [-25.71, -14.13],
         [-32.62, -15.93], [-7.27, 12.77], [26.57, -13.77], [9.94, 26.95],
         [-22.45, -23.18], [-34.7, -5.62], [29.53, -22.88], [0.7, 31.02],
         [-22.52, -10.02], [-23.36, -14.54], [-19.44, -12.94], [-0.5, 23.36],
         [-45.27, -19.8], [8.95, 13.63], [47.16, -14.46], [5.57, 4.85],
         [-19.03, -25.41], [28.16, -13.86], [-15.42, -14.68], [10.19, -25.08],
         [0.44, 23.65], [-20.71, -20.94], [35.91, -20.07], [42.81, -21.88],
         [5.1, 9.33], [-15.8, -18.47], [5.39, -26.82], [-40.53, -17.16],
         [-29.54, 23.72], [7.8, 23.4], [-22.19, -27.76], [-23.48, -25.01],
         [-21.2, -21.74], [23.14, -24.14], [-28.13, -13.04], [-24.38, -6.79] ]



def k_means_cluster():
    ''' Function k_means_cluster
        Input: void
        Returns: Nothing
        Does: Takes unassorted data and sorts it by distance
        
    '''

    # data, k = number of centroids 
    data = DATA
    k = 4
    # list for randomly selected numbers 
    rand_centroid = []
    colors = ["green", "blue", "red", "purple"]

    # centroid and shortest distance list
    # use to store in another list 
    data_centroid = []

    # two values for data point and centroid 
    val_one = 0
    val_two = 0

    # list of lists 
    assignments = []

    # value to start equality operation
    min_val = 100


    # for loop iterates through k and places
    # random values in list 
    for i in range(k):
        rand_centroid.append(random.choice(DATA))
        
    # print list using imported turtles methods from
    # kmeans_viz
    draw_centroids(rand_centroid, colors)


    # nested for loop used to iterate through to list
    # first list: list of data
    # second list: random number values from list 
    for i in data:
        
        for j in rand_centroid:
            # Euclidean distance method 
            distance = abs(math.sqrt(((i[0] - j[0])**2) + ((i[1] - j[1])**2)))

            #assigns shortest distance to variables by index 
            if (distance != 0) and (distance < min_val):
                min_val = distance
                val_one = data.index(i)
                val_two = rand_centroid.index(j)
                
        # two variables are stored in list to be placed in
        # larger list 
        data_centroid.append(val_one)
        data_centroid.append(val_two)

        # larger list 
        assignments.append(data_centroid)

        
        # reset values after every loop is ran
        min_val = 100
        val_one = 0
        val_two = 0
        data_centroid = []

    # run imported turtle method        
    draw_assignment(rand_centroid, data, assignments, colors)      
            
                
     
k_means_cluster()
