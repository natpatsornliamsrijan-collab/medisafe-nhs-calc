# 💊 Med-Tracker: Medication Expiry Helper (NHS-Based)

Med-Tracker is a small Python project I built while learning programming. It helps calculate how long medicines remain safe to use after opening.

The idea connects my background in pharmacy with my current journey into software development.

---

## 💡 Why I Built This
During my time working in pharmacy, I noticed that many people were unsure about one important detail:

**The expiry date printed on the box is not always the same as the safe period after opening.**

For example, eye drops may show a manufacturer expiry date years in the future, but once opened they are usually only safe for around 28 days. The same applies to insulin, oral liquids, and certain creams.

Even when pharmacists explain this clearly, patients or caregivers may forget the details later at home. Labels can fade, opening dates may not be written down, and confusion can happen easily — especially in elderly patients managing multiple medications (polypharmacy).

I built this project as a simple way to turn medical guidance into something practical and easy to check again later.

---

## 📋 Project Overview
This is a simple command-line tool that allows users to:
1. **Select a medication category** (English, Thai, and German terms supported)
2. **Enter the opening date** (DD/MM/YYYY)
3. **Receive a calculated expiry date**
4. **See a clear status message** (Safe / Near Expiry / Expired)

The focus is clarity and safety rather than complexity.

---

## 📖 Medical Reference
The expiry logic is based on:
> **NHS Guidance Sheet 6 – Storage and Expiry Dates**

This helped me translate real healthcare rules into program logic.

### ⏳ Example Expiry Rules After Opening
| Formulation | Suggested Expiry |
| :--- | :--- |
| MDS / Weekly Blister Pack | 56 Days |
| Oral Liquids / Syrup | 6 Months |
| Eye, Ear, Nose Drops | 28 Days |
| Topical Cream (Tube) | 3 Months |
| Insulin (In Use) | 28 Days |
| Inhalers | Manufacturer’s Expiry Date |

---

## ⚠️ If the Opening Date Is Unknown
If someone does not remember the opening date:
* Use the dispensing date as a rough reference.
* Discard the medicine if appearance or smell has changed.
* Ask a pharmacist if unsure.
* Write the opening date clearly on the label next time.

**Safety should always come first.**

---

## 🌡️ Storage Principles Reflected in the Tool
* Store below 25°C unless refrigeration is required.
* Keep medicines in original packaging.
* Do not mix different batches.
* Follow manufacturer instructions when in doubt.

---

## 🚀 How to Use
1. Run the Python script `medisafe.py`.
2. Select your medication type from the menu (1-12).
3. Enter the opening date in **DD/MM/YYYY** format.
4. The system will calculate the expiry and alert you if the medicine is safe or must be discarded.

---

## 🛠 Technical Stack
* **Python 3**
* **`datetime` module** (For accurate date calculations)
* **Command-line interface** (Simple CLI interaction)
* **Dictionary-based data structure**

---

## 📌 What I Learned
Through this project, I practiced:
* Turning written healthcare guidelines into logical conditions.
* Working with date calculations in Python.
* Structuring categorized data clearly.
* Designing a simple and readable user interface.
* Connecting prior professional knowledge with programming.

**Development Note:**
I used AI as a coding assistant while learning. The project idea, structure, and medical reasoning are based on my own experience and research.

---

## 📚 Sources
* **NHS Gloucestershire Health and Care** – Good Practice Guidance for Expiry Dates
* **NHS Cheshire Formulary** – Storage and Expiry Dates Guidance (Sheet 6)

---

## ⚖️ Disclaimer
This tool is for educational purposes only. Always verify information using official pharmacy labels and manufacturer instructions.
