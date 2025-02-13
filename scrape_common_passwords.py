import json
import csv

list_of_pw = []
def read_json():    
    with open('all.json', "r") as f:  # Use 'with' to ensure proper file closing
        data = json.load(f)  # Load JSON file
    for entry in data:  
        list_of_pw.append(entry['Password'])

def write_to_csv():
    with open('data.csv', 'a', newline='') as f:
        writer = csv.writer(f)
        for pw in list_of_pw:
            writer.writerow([pw, 0])  # Writing as ["password", 0]

# Execute functions
read_json()
write_to_csv()   