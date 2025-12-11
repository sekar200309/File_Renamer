# To run this script we need to install the Pandas using the following command 
# pip install pandas openpyxl run this command in Terminal 
import os
import pandas as pd
import logging

# Setup logging
log_file = "file_renaming.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


# To run this script we need to install the pip install pandas openpyxl


# Paths
folder_path = "C:/Users/Panda/Documents/VD/IGS" 
excel_path = "C:/Users/Panda/Documents/VD/names.xlsx"   # OR .csv

try:
    # Load Excel or CSV
    if excel_path.lower().endswith(".csv"):
        df = pd.read_csv(excel_path)
    else:
        df = pd.read_excel(excel_path)

    # Ensure correct columns exist
    df = df[['EN#', 'MFG PN']]

    # Rename internally for easy use
    df = df.rename(columns={
        "EN#": "EN_number",
        "MFG PN": "original_file_name"
    })

    logging.info("Loaded Excel/CSV file successfully.")

    # Convert to string (avoids errors)
    df['original_file_name'] = df['original_file_name'].astype(str)

    # Process each file in the folder
    for file_name in os.listdir(folder_path):

        if file_name.lower().endswith((".igs", ".pdf")):

            file_path = os.path.join(folder_path, file_name)
            # Extract extension and base name
            file_extension = os.path.splitext(file_name)[1]
            file_base = os.path.splitext(file_name)[0]

            matched_en = None

            # Look for substring match
            for _, row in df.iterrows():

                original = str(row['original_file_name'])

                if original.lower() in file_base.lower():
                    matched_en = row['EN_number']
                    break

            if matched_en:

                new_name = f"{matched_en}{file_extension}"
                new_file_path = os.path.join(folder_path, new_name)

                os.rename(file_path, new_file_path)

                logging.info(f"Renamed: {file_name} -> {new_name}")

            else:
                logging.warning(f"No match found for: {file_name}")

except Exception as e:
    logging.error(f"An error occurred: {str(e)}")
    print("Error:", e)
