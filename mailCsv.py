
import csv


def writecsv(filename, dct):
    keylist = ["Mail", "Status"]
    with open(filename, "w",newline="") as file:
        outfile = csv.DictWriter(file, fieldnames=keylist)
        outfile.writeheader()
        for mail, status in dct.items():
            outfile.writerow({"Mail": mail, "Status": status})
            print(f"Success , {mail} verified ")



