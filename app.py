# John Byron Garin
# 2021-02658

import csv
import random
import math
import matplotlib.pyplot as plt


def readCSVFile():
    # Dictionary to store the data
    data = {}

    with open('Wine.csv', 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        header = next(csvreader)

        # Initialize the dictionary with empty lists for each header key
        for key in header:
            data[key] = []

        # Iterate through each row in the CSV file
        for row in csvreader:
            # Append each value to the corresponding key's list
            for key, value in zip(header, row):
                data[key].append(float(value))

    return data

def calculate_distance(point1, point2):
    return math.sqrt(sum((a - b) ** 2 for a, b in zip(point1, point2)))

def assign_to_cluster(data_point, centroids):
    distances = [calculate_distance(data_point, centroid) for centroid in centroids]
    min_distance = min(distances)
    min_index = distances.index(min_distance)
    return min_index  # Adding 1 to make cluster numbers 1-based

def update_clusters(centroid_array, attribute1_array, attribute2_array):
    grouping_dict = {}
    
    for i, centroid in enumerate(centroid_array, start=0):
        cluster_key = f'Centroid {i}'
        grouping_dict[cluster_key] = []

    for i in range(len(attribute1_array)):
        data_point = [attribute1_array[i], attribute2_array[i]]
        cluster_index = assign_to_cluster(data_point, centroid_array)
        cluster_key = f'Centroid {cluster_index}'
        grouping_dict[cluster_key].append(data_point)

    return grouping_dict

def compute_averages(cluster, feature_vector_length):
    averages = []
    num_arrays = len(cluster)
    counter = 0
    while counter < feature_vector_length:
        sum_value = sum(subarray[counter] for subarray in cluster)
        ave = sum_value / num_arrays
        averages.append(ave)
        counter += 1
    return averages

def write_to_csv(centroids, grouping_dict):
    with open('output.csv', 'w', newline='') as csvfile:
        counter = 0
        while counter < k:
            csvfile.write(f"Centroid {counter} : {centroids[counter]}\n")
            cluster_key = f'Centroid {counter}'
            for value in grouping_dict[cluster_key]:
                csvfile.write(f"{value}\n")
            counter += 1

input_data_set = readCSVFile()
k = int(input('Enter k value: '))
Attr1 = input('Enter Attribute 1: ')
Attr2 = input('Enter Attribute 2: ')
feature_vector_length = 2
k_counter = 0
used_index = []
initial_centroid = []

############################## RANDOMIZED ##############################
# data_set = []
# random_index = 112
# data_set.append(input_data_set[Attr1][random_index])
# data_set.append(input_data_set[Attr2][random_index])
# initial_centroid.append(data_set)

# data_set = []
# random_index = 53
# data_set.append(input_data_set[Attr1][random_index])
# data_set.append(input_data_set[Attr2][random_index])
# initial_centroid.append(data_set)

# print("Initial Centroid")
# print(initial_centroid)

########################################################################

while k_counter < k:
    data_set = []
    random_int_limit = len(input_data_set[Attr1])-1
    random_index = random.randint(0, random_int_limit)
    while random_index in used_index:
        random_index = random.randint(0, random_int_limit)    
    used_index.append(random_index)
    
    print("Random Index")
    print(random_index)
    data_set.append(input_data_set[Attr1][random_index])
    data_set.append(input_data_set[Attr2][random_index])
    initial_centroid.append(data_set)
    k_counter += 1

print("Initial Centroid")
print(initial_centroid)

############################## RANDOMIZED ##############################

attribute1_array = input_data_set[Attr1]
attribute2_array = input_data_set[Attr2]

centroid_counter = 2
done_switch = False
centroid_used = initial_centroid
while done_switch == False:
    grouping_dict = update_clusters(centroid_used, attribute1_array, attribute2_array)
    new_centroid_array = []
    for cluster in grouping_dict.values():
        new_centroid_array.append(compute_averages(cluster, feature_vector_length))

    if new_centroid_array == centroid_used:
        done_switch == True
        break
    else:
        print("Centroid Number ", centroid_counter)
        print(new_centroid_array)
        centroid_used = new_centroid_array

    centroid_counter += 1

# Print the resulting grouping_dict
colors = ["blue", "red", "yellow", "pink", "green", "orange", "purple", "violet"]
coordinate_counter = 0
for keys in grouping_dict:
    x_values = []
    y_values = []
    print("==============")
    print(keys, ":")
    print("==============")
    for v in grouping_dict[keys]:
        x_values.append(v[0])
        y_values.append(v[1])
        print(v)
    plt.scatter(x_values, y_values, c =colors[coordinate_counter])
    coordinate_counter += 1

write_to_csv(new_centroid_array, grouping_dict)
plt.xlabel(Attr1)
plt.ylabel(Attr2)
plt.show()


