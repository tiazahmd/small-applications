import sys
import csv
import pandas as pd

def mainLoop(sourceFile):
    count = 0
    tempSourceFile = sourceFile
    
    splitSource = tempSourceFile.split(".csv")
    excerptOutFile = "- 2.csv".join(splitSource)
    outputFile = " - FINAL.csv".join(splitSource)

    # Extracting Excerpt
    with open(sourceFile, encoding="mbcs", newline='') as csvfile:
        lineReader = csv.reader(csvfile, delimiter=',')
        with open(excerptOutFile, 'w', encoding="mbcs", newline='') as outF:
            lineWrite = csv.writer(outF)
            for row in lineReader:
                if count == 0:
                    count += 1
                    row.append("JD Excerpt")
                    lineWrite.writerow(row)
                elif "tuition" in row[8]:
                    fTuition = row[8].find("tuition")
                    fTString = row[8][fTuition-60:fTuition+67]
                    row.append(fTString)
                    lineWrite.writerow(row)
                elif "Tuition" in row[8]:
                    fTuition = row[8].find("Tuition")
                    fTString = row[8][fTuition-60:fTuition+67]
                    row.append(fTString)
                    lineWrite.writerow(row)
    
    # Remove duplicates
    df = pd.read_csv(excerptOutFile, encoding="unicode_escape")
    df.drop_duplicates(inplace=True, subset='Employer', keep="first")
    df.to_csv(outputFile, index=False)

def main():
    argc = len(sys.argv)
    if argc < 2 or argc > 2:
        print("Usage: taylor.py xxxxx.csv")
    elif ".csv" not in sys.argv[1]:
        print("Error: Incorrect file type")
    else:
        mainLoop(sys.argv[1])

if __name__ == "__main__":
    main()