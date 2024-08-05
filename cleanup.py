import pandas as pd
import re

# Define the path to your Excel file
input_file = 'movies.xlsx'
output_file = 'cleaned_movies.xlsx'

# Read the Excel file
df = pd.read_excel(input_file)

# Clean the data (example cleanup steps)
# Remove leading/trailing whitespaces from column names
df.columns = df.columns.str.strip()

# Remove leading/trailing whitespaces from data
df['Name'] = df['Name'].str.strip()
df['Path'] = df['Path'].str.strip()

# Define common quality markers
quality_markers = ['1080p', '1440p', '2160p', '4K', 'BluRay', 'HDR', 'WEBRip', 'DVDRip', 'x264', 'x265', 'AAC5.1', 'HEVC']

# Extract Name, Release Year, and Quality
def extract_info(name, path):
    # Extract release year
    release_year_match = re.search(r'\((\d{4})\)', path)
    release_year = release_year_match.group(1) if release_year_match else None

    # Extract quality
    quality_match = None
    for marker in quality_markers:
        if re.search(marker, path, re.IGNORECASE):
            quality_match = marker
            break

    # Remove the release year and quality from the name to get the clean movie name
    clean_name = re.sub(r'\s*\(\d{4}\)', '', name)  # Remove year in parentheses
    if quality_match:
        clean_name = re.sub(re.escape(quality_match), '', clean_name, flags=re.IGNORECASE)  # Remove quality keyword
    clean_name = clean_name.strip()  # Remove leading/trailing whitespaces

    return clean_name, release_year, quality_match

# Apply the extraction logic and log what is being parsed
def log_and_extract(row):
    clean_name, release_year, quality = extract_info(row['Name'], row['Path'])
    print(f"Original: {row['Name']}, Name: {clean_name}, Year: {release_year}, Quality: {quality}")
    return pd.Series([clean_name, release_year, quality])

df[['Name', 'Release Year', 'Quality']] = df.apply(log_and_extract, axis=1)

# Remove Path column
df = df.drop(columns=['Path'])

# Remove duplicate entries (if any)
df = df.drop_duplicates()

# Optionally, you can sort the data by Name
df = df.sort_values(by='Name')

# Write the cleaned data to a new Excel file
df.to_excel(output_file, index=False)

print(f'Cleaned data has been saved to {output_file}')
