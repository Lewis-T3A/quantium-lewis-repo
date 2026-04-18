import csv
import os

DATA_DIR = "./data"
OUTPUT_PATH = "./formatted.csv"

with open(OUTPUT_PATH, "w", newline="") as output_file:
    writer = csv.writer(output_file)

    header = ["sales", "date", "region"]
    writer.writerow(header)

    for file_name in os.listdir(DATA_DIR):
        with open(f"{DATA_DIR}/{file_name}", "r") as input_file:
            reader = csv.reader(input_file)
            index = 0

            for input_row in reader:
                if index > 0:
                    product = input_row[0]
                    raw_price = input_row[1]
                    quantity = input_row[2]
                    date = input_row[3]
                    region = input_row[4]

                    if product == "pink morsel":
                        price = float(raw_price[1:])
                        sale = price * int(quantity)
                        output_row = [sale, date, region]
                        writer.writerow(output_row)

                index += 1