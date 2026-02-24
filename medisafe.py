import time
from datetime import datetime, timedelta

# --- 1. ข้อมูลรายการยา (Data) ---
CATEGORIES = {
    "1": {"en_de": "MDS / Weekly Blister Pack (Wöchentliche Blisterpackung)", "th": "ยาจัดแผงรายสัปดาห์ (MDS)", "days": 56},
    "2": {"en_de": "Original Blister Pack (Originalblister)", "th": "ยาเม็ดในแผงฟอยล์เดิม", "days": 3650},
    "3": {"en_de": "Repacked Medicine (Umgefüllte Medikamente)", "th": "ยาที่แบ่งใส่ขวดใหม่", "days": 30},
    "4": {"en_de": "Oral Liquid / Syrup (Saft oder Sirup)", "th": "ยาน้ำทั่วไป / ยาน้ำเชื่อม", "days": 180},
    "5": {"en_de": "Antibiotic Syrup - Room Temp (Antibiotika - Raumtemp.)", "th": "ยาปฏิชีวนะผสมน้ำ (อุณหภูมิห้อง)", "days": 7},
    "6": {"en_de": "Antibiotic Syrup - Fridge (Antibiotika - Kühlschrank)", "th": "ยาปฏิชีวนะผสมน้ำ (ตู้เย็น)", "days": 14},
    "7": {"en_de": "Cream in Jar (Creme im Tiegel)", "th": "ยาทากระปุก", "days": 30},
    "8": {"en_de": "Cream/Ointment Tube (Creme / Salbe in der Tube)", "th": "ยาทาหลอด (ผิวหนัง)", "days": 90},
    "9": {"en_de": "Eye / Ear Drops (Augen- / Ohrentropfen)", "th": "ยาหยอดตา / หู", "days": 28},
    "10": {"en_de": "Single-dose Eye Drops (Einzeldosis-Augentropfen)", "th": "ยาหยอดตาหลอดเล็ก (SDU)", "days": 1},
    "11": {"en_de": "Insulin - In Use (Insulin - im Gebrauch)", "th": "อินซูลินที่กำลังใช้งาน", "days": 28},
    "12": {"en_de": "Inhaler / MDI (Inhalator)", "th": "ยาพ่น (Inhaler)", "days": 3650}
}

def start_app():
    # เลือกภาษาเพียงครั้งเดียวตอนเริ่มโปรแกรม
    print("========================================")
    print("      MED-TRACKER: EXPIRY HELPER        ")
    print("========================================")
    print("Choose Language / Sprache wählen:")
    print("1. English / Deutsch")
    print("2. ภาษาไทย (Thai)")
    
    lang_choice = input("\nSelect (1/2): ")
    is_thai = lang_choice == "2"

    # เริ่มระบบวนลูปตรวจสอบยา
    while True:
        menu_title = "--- SELECT CATEGORY ---" if not is_thai else "--- เลือกหมวดหมู่ยา ---"
        print(f"\n{menu_title}")
        
        for key, val in CATEGORIES.items():
            name = val['th'] if is_thai else val['en_de']
            print(f"  [{key}] {name}")

        choice = input("\nChoice (1-12) [or 'q' to quit]: ")
        
        # กด q เพื่อออกจากโปรแกรม
        if choice.lower() == 'q':
            break

        if choice in CATEGORIES:
            item = CATEGORIES[choice]
            days = item['days']
            
            if days > 1000:
                msg = ">>> Follow Manufacturer's Expiry Date <<<" if not is_thai else ">>> ใช้ตามวันหมดอายุที่ระบุบนกล่อง <<<"
                print(f"\n{msg}")
            else:
                try:
                    prompt = "Enter Opening Date:" if not is_thai else "กรอกวันที่เริ่มเปิดใช้งาน:"
                    print(f"\n{prompt}")
                    d = int(input("  DD: "))
                    m = int(input("  MM: "))
                    y = int(input("  YYYY: "))
                    
                    open_date = datetime(y, m, d)
                    expiry_date = open_date + timedelta(days=days)
                    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                    days_left = (expiry_date - today).days

                    print("\n" + "*"*45)
                    if days_left < 0:
                        if not is_thai:
                            print("!!! EXPIRED (ABGELAUFEN) !!!")
                            print(f"Status: Please discard. Expired on: {expiry_date.strftime('%d/%m/%Y')}")
                        else:
                            print("!!! ยาหมดอายุแล้ว !!!")
                            print(f"สถานะ: ควรทิ้งทันที (หมดอายุเมื่อ: {expiry_date.strftime('%d/%m/%Y')})")
                    else:
                        if not is_thai:
                            print("STATUS: SAFE TO USE (SICHER)")
                            print(f"EXPIRY (ABLAUFDATUM): {expiry_date.strftime('%d/%m/%Y')}")
                            print(f"REMAINING: {days_left} Days (Tage)")
                        else:
                            print("สถานะ: ✅ ยังใช้ได้")
                            print(f"วันหมดอายุ: {expiry_date.strftime('%d/%m/%Y')}")
                            print(f"เหลืออีก: {days_left} วัน")
                    print("*"*45)

                except ValueError:
                    err = "Invalid date!" if not is_thai else "วันที่ไม่ถูกต้อง!"
                    print(f"\nError: {err}")
            
            # ถามว่าต้องการตรวจสอบยาตัวอื่นต่อไหม
            again_prompt = "\nCheck another item? (y/n): " if not is_thai else "\nตรวจสอบรายการอื่นต่อไหม? (y/n): "
            again = input(again_prompt)
            if again.lower() != 'y':
                break
        else:
            err_choice = "Invalid selection!" if not is_thai else "เลือกไม่ถูกต้อง!"
            print(f"\nError: {err_choice}")

    # ข้อความบอกลา
    bye = "Goodbye! / Auf Wiedersehen!" if not is_thai else "ขอบคุณที่ใช้งานค่ะ!"
    print(f"\n{bye}")

if __name__ == "__main__":
    start_app()
