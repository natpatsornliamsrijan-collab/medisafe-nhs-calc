# 💊 Med-Tracker: Medication Expiry Helper (Multi-Standard)

**Med-Tracker** is a Python-based project I developed to bridge my professional background in pharmacy with my journey into software development. It calculates the **Beyond-Use Date (BUD)** to ensure medicines remain safe and effective after being opened or repacked.

---

## 💡 Why I Built This
In pharmacy practice, I observed a common risk: **The expiry date on the box is not the same as the safe period after opening.**

Factors like humidity, microbial exposure, and oxidation start affecting the medicine the moment the seal is broken. While pharmacists explain this, labels fade and dates are forgotten—especially for elderly patients managing multiple medications (polypharmacy). I built this tool to turn complex medical guidelines into a practical, digital safety check.

---

## 📋 Project Overview
This command-line tool allows users to:
* **Select a Language/Standard:** Switch between English-Deutsch (NHS Standard) and ภาษาไทย (Thai FDA/USP Standard).
* **Select a Medication Category:** Choose from 12 specific categories with terminology in all three languages.
* **Enter the Opening Date:** Simply input the date in DD/MM/YYYY format.
* **Receive a Calculated Status:** Instant feedback: ✅ SAFE, ⚠️ NEAR EXPIRY, or ❌ EXPIRED.

---

## 📖 Medical Reference & Guideline Comparison
The logic in this tool is inspired by publicly available guidance documents:

### ⚖ Scope & Regulatory Clarification

This tool is designed as an educational comparison of publicly available guidance (NHS and Thai FDA/USP-based frameworks). 

It does not replace:
• Product-specific Summary of Product Characteristics (SPC / Fachinformation)
• National pharmacy compounding standards (e.g., DAC/NRF in Germany)
• Individual manufacturer storage instructions

Expiry rules may vary depending on formulation, preservatives, packaging type, and national regulation. 

The implemented logic represents simplified safety-oriented interpretations for learning and demonstration purposes.

### 🔬 Comparative Analysis: NHS vs. Thai FDA (USP 795)
As a pharmacist, I understand that stability guidelines must adapt to local contexts:

* **NHS (UK/Europe):** Optimized for Climate Zone I/II (Temperate). It offers a balanced approach for stable environments.
* **Thai FDA (Thailand):** Based on USP 795 and adapted for Climate Zone IVb (Hot & Very Humid).
    * **The Liquid Paradox:** Unlike the NHS, the Thai FDA is significantly stricter on Repacked Oral Liquids (14 days) because high humidity and temperature dramatically increase the risk of microbial growth.
    * **Repacked Solids:** Conversely, it allows up to 6 months (180 days) for tablets/powders in certain conditions, whereas European standards often suggest stricter limits for MDS packs.

### ⏳ Example Expiry Rules (Implemented Logic)

| Formulation | NHS (UK/EU) | Thai FDA (USP) | Note |
| :--- | :--- | :--- | :--- |
| MDS / Weekly Blister | 56 Days | 180 Days | Based on local solid stability |
| Oral Liquids (Repacked) | 180 Days | 14 Days | Strict microbial control (Zone IVb) |
| Decanted Medicine | 30 Days | 180 Days | Standard vs. Safety Choice |
| Eye / Ear Drops | 28 Days | 30 Days | Global standard for multi-dose |
| Creams (Aqueous) | 30 Days | 30 Days | High water activity limits |
| Insulin (In Use) | 28 Days | 28 Days | Standard protein stability |

---

## ⚠️ If the Opening Date Is Unknown
* Use the dispensing date as a rough reference point.
* **Observe Physical Changes:** Discard immediately if the smell, color, or texture has changed.
* **Write it down:** Always record the opening date on the label for future safety.
* **Consult a Pharmacist:** When in doubt, safety always comes first.

---

## 🚀 How to Use
1.  Run the Python script:
    
bash
    python med_tracker.py
    

2.  Choose your preferred standard/language:
    * 1 for English-Deutsch (NHS-EU)
    * 2 for ภาษาไทย (Thai FDA-USP)
3.  Select the medication type from the menu (1-12).
4.  Enter the opening date (`DD/MM/YYYY`).
5.  The system will calculate the remaining days and display the safety status.

---

## 🛠 Technical Stack
* **Language:** Python 3
* **Modules:** datetime (For precise date arithmetic).
* **Data Structure:** Dictionary-based dual-logic engine.
* **Localization:** Fully supports English (EN), German (DE), and Thai (TH).

---

## 📌 What I Learned
* **Domain-Driven Design:** Translating complex medical PDFs and regulatory documents into functional code logic.
* **Global Regulatory Analysis:** Comparing international pharmaceutical standards and understanding the "why" behind different safety margins (Climate factors).
* **User-Centric Programming:** Designing a CLI that handles user errors (invalid dates) gracefully.

> **Development Note:**
> I used AI as a coding assistant while learning. The project idea, multilingual structure, and comparative medical reasoning are based on my professional experience as a pharmacist and research into global stability standards.

---

## 📚 Sources
* **Thai FDA:** Guidelines for Assigning Beyond-Use Dates (BUD) for Medicinal Products in Healthcare Facilities (Ref: USP 795).
* **NHS England:** Guidance Sheet 6 – Storage and Expiry Dates.
* **ICH Q1A (R2):** Stability Testing Reference for Climate Zones.

---

## ⚖️ Disclaimer
This tool is for educational purposes only. Always verify information using official pharmacy labels and manufacturer instructions.
