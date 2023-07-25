import time
def focus_timer(minutes):
    seconds = minutes * 60
    start_time = time.time()
    end_time = start_time + seconds
    
    while time.time() < end_time:
        remaining_seconds = int(end_time - time.time())
        minutes = remaining_seconds // 60
        seconds = remaining_seconds % 60
        
        print(f"Remaining Time: {minutes:02d}:{seconds:02d}", end="\r")
        time.sleep(1)
    
    print("Focus time is up!")
# 设置专注时长为25分钟
focus_timer(int(input("Enter the number of minutes to fucus:")))
