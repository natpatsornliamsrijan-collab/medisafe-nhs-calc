import time
from datetime import datetime, timedelta

# --- 1. Medication Data Configuration ---
# 'orig' = บรรจุภัณฑ์เดิมจากโรงงานหลังเปิดใช้
# 'repack' = ยาแบ่งบรรจุใส่ตลับ/ขวดใหม่/ซองยา
CATEGORIES = {
    "1": {
        "en_de": "MDS / Tablets / Capsules (Tabletten / Kapseln)", 
        "th": "ยาเม็ด / แคปซูล", 
        "days_nhs": {"orig": 3650, "repack": 56}, 
        "days_thai": {"orig": 3650, "repack": 180}
    },
    "2": {
        "en_de": "Oral Liquid / Syrup (Saft oder Sirup)", 
        "th": "ยาน้ำทั่วไป / ยาน้ำเชื่อม", 
        "days_nhs": {"orig": 180, "repack": 30}, 
        "days_thai": {"orig": 180, "repack": 14}
    },
    "3": {
        "en_de": "Antibiotic Syrup (Antibiotika - Saft)", 
        "th": "ยาปฏิชีวนะผสมน้ำ (หลังผสม)", 
        "is_antibiotic": True # เคสพิเศษแยกอุณหภูมิ
    },
    "4": {
        "en_de": "Cream (Aqueous) / Jar (Creme im Tiegel)", 
        "th": "ยาครีม (สูตรน้ำ) / ยาทากระปุก", 
        "days_nhs": {"orig": 30, "repack": 30}, 
        "days_thai": {"orig": 180, "repack": 90}
    },
    "5": {
        "en_de": "Ointment / Tube (Salbe in der Tube)", 
        "th": "ยาขี้ผึ้ง / ยาทาหลอด", 
        "days_nhs": {"orig": 90, "repack": 90}, 
        "days_thai": {"orig": 180, "repack": 90}
    },
    "6": {
        "en_de": "Eye / Ear Drops (Augen- / Ohrentropfen)", 
        "th": "ยาหยอดตา / หู (Sterile)", 
        "days_nhs": {"orig": 28, "repack": 0},      
        "days_thai": {"orig": 30, "repack": 0}      
    },
    "7": {
        "en_de": "Insulin - In Use (Insulin - im Gebrauch)", 
        "th": "อินซูลินที่กำลังใช้งาน", 
        "days_nhs": {"orig": 28, "repack": 28}, 
        "days_thai": {"orig": 28, "repack": 28}
    },
    "8": {
        "en_de": "Inhaler / MDI (Inhalator)", 
        "th": "ยาพ่น (Inhaler)", 
        "days_nhs": {"orig": 3650, "repack": 3650}, 
        "days_thai": {"orig": 3650, "repack": 3650}
    }
}

def start_app():
    print("========================================")
    print("    💊 MED-TRACKER: GLOBAL STANDARDS    ")
    print("========================================")
    print("Choose Language / Sprache wählen:")
    print("1. English / Deutsch (NHS Standard)")
    print("2. ภาษาไทย (Thai FDA / USP Standard)")
    
    lang_choice = input("\nSelect (1/2): ")
    is_thai = lang_choice == "2"

    while True:
        menu_title = "--- 📋 SELECT CATEGORY ---" if not is_thai else "--- 📋 เลือกหมวดหมู่ยา ---"
        print(f"\n{menu_title}")
        
        for key, val in CATEGORIES.items():
            name = val['th'] if is_thai else val['en_de']
            print(f"  [{key}] {name}")

        choice = input("\nChoice (1-8) [or 'q' to quit]: ")
        
        if choice.lower() == 'q':
            break

        if choice in CATEGORIES:
            item = CATEGORIES[choice]
            days = 0
            pkg_label_detail = ""
            pkg_label_thai = ""

            # --- กรณีพิเศษ: ยาปฏิชีวนะ (Antibiotic) แยกตามอุณหภูมิ ---
            if item.get("is_antibiotic"):
                print("\n🌡️ " + ("Storage Temperature:" if not is_thai else "การเก็บรักษา:"))
                print("  [1] " + ("Room Temperature (7 days)" if not is_thai else "อุณหภูมิห้อง (7 วัน)"))
                print("  [2] " + ("Refrigerator 2-8°C (14 days)" if not is_thai else "ในตู้เย็น 2-8°C (14 วัน)"))
                temp_choice = input("Select (1/2): ")
                days = 7 if temp_choice == "1" else 14
                pkg_label_detail = "Room Temp" if temp_choice == "1" else "Fridge"
                pkg_label_thai = "อุณหภูมิห้อง" if temp_choice == "1" else "แช่เย็น"
            
            else:
                # --- เลือกประเภทบรรจุภัณฑ์สำหรับยาทั่วไป ---
                print("\n📦 " + ("Packaging Type:" if not is_thai else "ประเภทบรรจุภัณฑ์:"))
                print("  [1] " + ("Original Packaging" if not is_thai else "บรรจุภัณฑ์เดิม (จากโรงงาน)"))
                print("  [2] " + ("Repacked / Divided" if not is_thai else "ยาแบ่งบรรจุ (แบ่งใส่ตลับ/ขวดใหม่)"))
                pkg_choice = input("Select (1/2): ")
                pkg_key = "orig" if pkg_choice == "1" else "repack"
                
                if choice == "6" and pkg_key == "repack":
                    print("\n❌ " + ("CRITICAL: Sterile drops must NOT be repacked!" if not is_thai else "อันตราย: ยาหยอดตาห้ามแบ่งบรรจุเอง!"))
                    continue

                days_data = item['days_thai'] if is_thai else item['days_nhs']
                days = days_data.get(pkg_key, 0)
                pkg_label_detail = pkg_key.upper()
                pkg_label_thai = "ขวดเดิม" if pkg_key=="orig" else "แบ่งบรรจุ"

            # --- ส่วนการคำนวณและแสดงผล ---
            if days > 1000:
                msg = ">>> ⚠️ Follow Manufacturer's Expiry <<<" if not is_thai else ">>> ⚠️ ใช้ตามวันหมดอายุบนกล่อง/แผงยา <<<"
                print(f"\n{msg}")
            else:
                try:
                    # --- กรอกวันที่แบบทีละขั้นตอน (Enter แยกบรรทัด) ---
                    print("\n📅 " + ("Enter Opening Date:" if not is_thai else "กรอกวันที่เริ่มเปิด/แบ่งยา:"))
                    d = int(input("  Day (DD): " if not is_thai else "  กรอกวัน (วว): "))
                    m = int(input("  Month (MM): " if not is_thai else "  กรอกเดือน (ดด): "))
                    y = int(input("  Year (YYYY): " if not is_thai else "  กรอกปี (ปปปป): "))
                    
                    open_date = datetime(y, m, d)
                    expiry_date = open_date + timedelta(days=days)
                    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
                    days_left = (expiry_date - today).days

                    print("\n" + "⭐"*40)
                    print(" " + (f"Type: {pkg_label_detail}" if not is_thai else f"รูปแบบ: {pkg_label_thai}"))
                    
                    if days_left < 0:
                        status = "!!! 🛑 EXPIRED (ABGELAUFEN) !!!" if not is_thai else "!!! 🛑 ยาหมดอายุแล้ว !!!"
                        print(f" {status}")
                        print(f" Expired on: {expiry_date.strftime('%d/%m/%Y')}")
                    else:
                        status = "✅ STATUS: SAFE TO USE" if not is_thai else "✅ สถานะ: ยังใช้ได้"
                        print(f" {status}")
                        print(f" Expiry (BUD): {expiry_date.strftime('%d/%m/%Y')}")
                        print(f" Remaining: {days_left} Days")
                    print("⭐"*40)

                except ValueError:
                    print("\nError: " + ("Invalid input! Use numbers only." if not is_thai else "กรอกข้อมูลผิด! กรุณาใช้เฉพาะตัวเลข"))
                except Exception:
                    print("\nError: " + ("Invalid date!" if not is_thai else "วันที่ไม่ถูกต้อง!"))
            
            again = input("\nCheck another? (y/n): " if not is_thai else "\nตรวจสอบยาอื่นต่อไหม? (y/n): ")
            if again.lower() != 'y': break
        else:
            print("\nInvalid choice!")

    print("\n👋 Goodbye! / ขอบคุณที่ใช้งานค่ะ!")

if __name__ == "__main__":
    start_app()
