with open("sample_logs.txt", 'r') as file:
        for line in file:
            if "ERROR" in line:
                time = line.split(']')[0].strip('[')
                ermsg= line.split('ERROR:')[1].strip()
                print(f"Timestamp: {time}, Error Message: {ermsg}")
