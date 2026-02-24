import pyttsx3
import time
from datetime import datetime, timedelta

# --- 1. ตั้งค่าระบบเสียง ---
engine = pyttsx3.init()
engine.setProperty('rate', 135) 

def announce(text):
    print(f"\n>>> {text.upper()} <<<")
    engine.say(text)
    engine.runAndWait()

# --- 2. ข้อมูลยาอ้างอิงจาก NHS (เหลือ 12 รายการ) ---
CATEGORIES = {
    "1": {"name": "MDS / Weekly Blister Pack (ยาเม็ดจัดแผงรายสัปดาห์)", "days": 56},
    "2": {"name": "Original Manufacturer Blister (ยาเม็ดในแผงฟอยล์เดิม)", "days": 365},
    "3": {"name": "Decanted Medicine (ยาที่แบ่งใส่ขวดใหม่)", "days": 30},
    "4": {"name": "Oral Liquid / Syrup (ยาน้ำกินหลังเปิดขวด)", "days": 180},
    "5": {"name": "Reconstituted Antibiotics (ยาปฏิชีวนะผสมน้ำแล้ว)", "days": 7},
    "6": {"name": "Topical Cream in Jar (ยาทากระปุก)", "days": 30},
    "7": {"name": "Topical Tube - SKIN ONLY (ยาทาหลอด-ใช้ทาผิวเท่านั้น)", "days": 90},
    "8": {"name": "Medicated Lotion (โลชั่นยา)", "days": 180},
    
    # --- หมวดหมู่ยาตา (แบบมาตรฐาน) ---
    "9": {"name": "Standard Eye/Ear Drops (ยาหยอดตาหรือหูทั่วไป - 1 เดือน)", "days": 28},
    "10": {"name": "Single-use Units (ยาหยอดตาแบบกระเปาะเล็กรายวัน)", "days": 1},
    
    "11": {"name": "Insulin Pen / Vial - In Use (อินซูลินหลังเริ่มใช้)", "days": 28},
    "12": {"name": "Inhaler / MDI (ยาพ่น)", "days": 365}
}

def start_app():
    print("========================================")
    print("    MEDISAFE: NHS STORAGE GUIDANCE      ")
    print("========================================")
    announce("Welcome. I will help you check your medicine.")
    
    announce("Please listen to the categories:")
    for key, val in CATEGORIES.items():
        print(f"  [{key}] {val['name']}")
        engine.say(f"Option {key}: {val['name']}")
        engine.runAndWait()
        time.sleep(0.05)

    choice = input("\nSELECT NUMBER (1-12): ")

    if choice in CATEGORIES:
        selected = CATEGORIES[choice]
        announce(f"You selected {selected['name']}")
        
        # --- คำเตือนพิเศษ ---
        if choice == "7":
            announce("Warning: This is for skin use only. Do not put in eyes.")
        elif choice == "10":
            announce("Safety Alert: This is preservative-free. Discard within 24 hours.")

        print("\n--- ENTER DATE OF OPENING ---")
        try:
            # ลำดับการกรอก: วัน -> เดือน -> ปี
            d = int(input("DAY   (DD):   "))
            m = int(input("MONTH (MM):   "))
            y = int(input("YEAR  (YYYY): "))
            
            open_date = datetime(y, m, d)
            expiry_date = open_date + timedelta(days=selected['days'])
            days_left = (expiry_date - datetime.now()).days

            print("\n" + "*"*40)
            if days_left < 0:
                print("!!! WARNING: DISCARD IMMEDIATELY !!!")
                announce(f"Warning! This medicine is expired. Please dispose of it safely.")
            elif days_left <= 7:
                print("!!! CAUTION: NEAR EXPIRY !!!")
                announce(f"Be careful. It will expire in {days_left} days.")
            else:
                print("       STATUS: SAFE TO USE      ")
                announce(f"Safe to use. It expires on {expiry_date.strftime('%d/%m/%Y')}.")
                print(f"Days remaining: {days_left}")
            print("*"*40)

        except ValueError:
            announce("Invalid date. Please use numbers only.")
    else:
        announce("Invalid choice.")

if __name__ == "__main__":
    start_app()
