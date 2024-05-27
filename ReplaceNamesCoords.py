import os
import sys

# Definieer het pad naar de directory
directory = sys.argv[1]

# Zoek naar bestanden eindigend op "_coord_out.txt" in de opgegeven directory
coord_files = [file for file in os.listdir(directory) if file.endswith("_coord_out.txt")]

# Loop door de gevonden "_coord_out.txt" bestanden
for coord_file in coord_files:
    # Zoek naar pdf-bestanden in dezelfde directory
    pdf_files = [file for file in os.listdir(directory) if file.endswith(".pdf")]
    
    # Zoek naar het nummer in de pdf-bestandsnaam
    pdf_number = None
    for pdf_file in pdf_files:
        # Zoek naar het nummer in de pdf-bestandsnaam
        pdfFile = pdf_file.split("_NA_")
        pdfFile2 = pdfFile[1].replace(".pdf", "")
        if coord_file.startswith(pdfFile2):
            pdf_number = pdfFile[0]
            break
    
    # Als een nummer is gevonden
    if pdf_number:
        # Construeer de nieuwe bestandsnaam voor "_coord_out.txt"
        new_filename = f"{pdf_number}_{coord_file}"
        
        # Hernoem het bestand
        os.rename(os.path.join(directory, coord_file), os.path.join(directory, new_filename))
        
    #    print(f"Hernoemd {coord_file} naar {new_filename}")
  #  else:
   #     print(f"Geen nummer gevonden in de pdf-bestandsnaam voor {coord_file}")
