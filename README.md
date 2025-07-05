# 📂 CSV to Excel Multi-Sheet Converter

## 📝 **Project Overview**

This Python script **combines multiple CSV files from a folder into a single Excel workbook**, saving each CSV as a separate sheet. Designed for small businesses or individuals needing to compile data efficiently.

---

## ⚙️ **Requirements**

- Python 3.x
- Libraries: pandas, openpyxl

---

## 🛠️ **Installation Guide**

### **1. Install Python**

**Windows:**
- Download from [python.org](https://www.python.org/downloads/windows/)
- During setup, ensure **“Add Python to PATH”** is checked.

**macOS:**
- Check if installed:  
  `python3 --version`  
- If not, install via [Homebrew](https://brew.sh/):  
  `brew install python`

---

### **2. Install required libraries**

**Windows:**

Open **Command Prompt** and run:  
`pip install pandas openpyxl`

**macOS:**

Open **Terminal** and run:  
`pip3 install pandas openpyxl`

---

## 🚀 **How to Use**

1. Place your CSV files into a folder (e.g. `data/`).
2. In the script file, update these variables to your folder and desired output file:

```python
folder_path = r'YOUR_FOLDER_PATH_HERE'
output_file = 'combined.xlsx'
```

For example:

```python
folder_path = r'C:\Users\dylan\OneDrive\Documents\Sample_CSV_Data'
output_file = 'combined.xlsx'
```

✅ **Tip:** Use `r'path'` for Windows paths to avoid escape character errors.

3. Run the script:

**Windows:**  
`python csv_to_excel.py`

**macOS:**  
`python3 csv_to_excel.py`

---

## 📂 **Output**

- Generates an Excel workbook (`.xlsx`)  
- Each sheet is named after the corresponding CSV file  
- Saves to the same directory unless an absolute output path is provided

---

## 📸 **Screenshots**

*(Add your screenshots here for clarity in your portfolio)*

### 🔹 **Input Folder Example**

![Input CSV files](images/input_folder.png)

### 🔹 **Excel Output Example**

![Excel output file](images/script_output.png)

---

## 🔑 **Notes**

- All CSV files must have a `.csv` extension and valid headers.  
- The script uses **pandas** for reading CSVs and **openpyxl** as the Excel writer engine.  
- You can change the output folder by specifying a different `output_file` path.

---

## 👨‍💻 **Author**

Dylan Cleal – Python Developer | Data Automation & Web Scraping Specialist

---

