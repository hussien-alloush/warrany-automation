# 📊 Excel to PHP Warranty Data Automation

This project is a Python automation script that reads warranty data from an Excel file and converts it into a PHP associative array.

It is useful for automatically generating PHP-ready data from Excel without manual copying or formatting.

## 🔧 What This Script Does

- Reads warranty data from an Excel file using **pandas**
- Cleans and formats the data
- Converts issue dates to `YYYY-MM-DD` format
- Generates a PHP associative array
- Saves the output to a `.php` file ready to be used in a PHP project

## 📁 Input File

The script expects an Excel file with columns similar to:

- `Warranty nbr`
- `Model nbr`
- `Issue date`

## 📤 Output File

The script generates a file called:

warranty_data.php

Example output format:

$warranty = array(
  '123456' => array(
    'brand' => 'test',
    'model' => 'test123',
    'issueDate' => '2024-01-15'
  ),
);

🚀 How to Run the Script
1️⃣ Install dependencies
1- pip install pandas openpyxl

2️⃣ Place your Excel file in the project folder

Update the file name inside the script :

excel_file = 'test.xlsx'

3️⃣ Run the script
python excel_to_php.py

4️⃣ Output

The PHP file will be created in the same directory:
warranty_data.php
