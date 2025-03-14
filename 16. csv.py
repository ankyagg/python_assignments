import csv
import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + 
                     (p1[1] - p2[1])**2 + 
                     (p1[2] - p2[2])**2)

def find_closest_points(csv_filename):
    points = []

    with open(csv_filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            points.append((float(row[0]), float(row[1]), float(row[2])))

    min_distance = float('inf')
    closest_pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            dist = euclidean_distance(points[i], points[j])
            if dist < min_distance:
                min_distance = dist
                closest_pair = (points[i], points[j])

    print(f"Closest Points: {closest_pair[0]} and {closest_pair[1]}")
    print(f"Minimum Distance: {min_distance:.4f}")

csv_filename = "coordinates.csv"
find_closest_points(csv_filename)
