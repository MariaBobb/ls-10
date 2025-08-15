
def analyze_log(file_name):
    counter = {"NEC":0,"SHARP":0,"SONY":0}
    
    try:
        with open (file_name) as file:
            for line in file:
                if "NEC" in line:
                    counter["NEC"] +=1
                elif "SHARP" in line:
                    counter["SHARP"] +=1
                elif "SONY" in line:
                    counter["SONY"] +=1
        for k,v in counter.items():
            print(f"{k}:{v}")    
    except FileNotFoundError:
        print("Файл не найден")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")
analyze_log("Demo.log")