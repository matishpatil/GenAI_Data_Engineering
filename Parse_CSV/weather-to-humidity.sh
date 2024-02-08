#!/bin/bash

# Run first awk command to reformat weatherHistory.csv
awk -F, '{print $1","$2","$3","$4","$5","$6","$7","$8","$9","$11","$12}' weatherHistory.csv > new_weatherHistory.csv

# Run second awk command to filter rows with humidity >= 0.85
awk -F, '$6 >= 0.85' new_weatherHistory.csv > high_humidity.csv