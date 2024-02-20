# place your code to clean up the data file below.
import csv

def clean_data(input_file_path, output_file_path):
    with open(input_file_path, mode='r', encoding='utf-8') as infile, \
         open(output_file_path, mode='w', encoding='utf-8', newline='') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        headers = next(reader)
        if 'DBN' in headers:
            dbn_index = headers.index('DBN')
            del headers[dbn_index]
        else:
            dbn_index = None

        headers.append("Exam Pass rate")

        writer.writerow(headers)

        for row in reader:
            if dbn_index is not None:
                del row[dbn_index]
            row = [item.replace('s', '0') for item in row]

            ap_exams_taken = int(row[2]) 
            ap_exams_passed = int(row[3])  
            if ap_exams_taken != 0:
                pass_rate = round(ap_exams_passed / ap_exams_taken, 3)
            else:
                pass_rate = "N/A"
            row.append(pass_rate)

            writer.writerow(row)

if __name__ == "__main__":
    input_file_path = 'data/2012__AP_Results_20240219.csv'  
    output_file_path = 'data/clean_data.csv' 

clean_data(input_file_path, output_file_path)