# 💊 MediSafe: NHS-Standard Medication Expiry Calculator

A Python tool designed to improve patient safety by calculating the precise expiry date of medications after they have been opened. This project is specifically tailored for care home settings and individuals managing multiple medications (Polypharmacy).

## 💡 Why I built this
During my experience in pharmacy, I noticed that many patients were unsure about how long medicines remain safe after opening. Especially in care homes where multiple medications are used, incorrect expiry tracking can pose risks. This project combines my healthcare background with my interest in software development to create a practical safety tool.

## 📋 Project Overview
Many medications have a shortened shelf life once the original seal is broken. This tool helps users:
1. **Select** the correct medication category (supports English, Thai, and German terms).
2. **Enter** the date of opening (Day/Month/Year).
3. **Receive** an instant expiry date calculation and voice notification (Text-to-Speech).

## 📖 NHS Guidance & Medical Reference
The logic in this software is based on **NHS Guidance Sheet 6: Storage and Expiry Dates**.

### ⏳ Table of Suggested Expiry (After Opening)
| Formulation | Suggested Expiry | Deutsch (German) |
| :--- | :--- | :--- |
| **MDS / Weekly Blister Pack** | 56 Days (8 Weeks) | Wöchentliche Blisterpackung |
| **Oral Liquids / Syrup** | 6 Months (180 Days) | Saft oder Sirup |
| **Eye, Ear, Nose Drops** | 1 Month (28 Days) | Augen-, Ohren-, Nasentropfen |
| **Topical Tubes (Skin)** | 3 Months (90 Days) | Tube für die Haut |
| **Insulin (In-use)** | 4 Weeks (28 Days) | Insulin im Gebrauch |
| **Inhalers** | Manufacturer's Expiry | Inhalator |

### ⚠️ Handling Uncertainty (If Date is Forgotten)
Safety is our top priority. If the opening date is unknown:
* **Use Dispensed Date:** Use the date the medicine was received as a starting point.
* **Physical Inspection:** Discard if appearance, color, or smell has changed.
* **Consult a Professional:** When in doubt, contact a community pharmacist immediately.
* **Proactive Tracking:** Always write the opening date on the label upon opening.

## 🌡️ Key Storage Principles
* **Original Packaging:** Keep medicines in their original outer packaging to protect from sunlight.
* **Temperature Control:** Store in a cool, dry place (below 25°C) unless refrigeration is required (2°C - 8°C).
* **Batch Integrity:** Never mix different batches of medication.

## 🚀 How to Use
1. Run the Python script `medisafe.py`.
2. Listen to the voice options (TTS enabled).
3. Select your medication type (1-12).
4. Enter the opening date in **DD/MM/YYYY** format.
5. The system will alert you if the medicine is safe or must be discarded.

---
**Data Sources:**
* NHS Gloucestershire Health and Care: Good Practice Guidance for Expiry Dates.
* NHS Cheshire Formulary: Storage and Expiry Dates Guidance (Sheet 6).

**Disclaimer:** This tool is for educational purposes. Always verify with the physical label provided by your pharmacist and the manufacturer's instructions.
---
**Disclaimer:** This tool is for educational purposes and to assist in tracking. Always verify with the physical label provided by your pharmacist and the manufacturer's instructions.
