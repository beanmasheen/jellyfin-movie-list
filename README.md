# Jellyfin Movie Name Export

## Goal of this Project
The main goal of this script is to use the Jellyfin API to extract the list of movies on the given server.

## Explanation of the script:

### Configuration:
    Set the Jellyfin server URL and API key.

### Fetching Movies:
    The get_movies function sends a request to the Jellyfin API to get all items of type 'Movie'.
    It includes fields like 'Name' and 'Path' in the response.

### Saving to Excel:
    The movies_to_excel function converts the movie data into a list of dictionaries, each containing 'Name' and 'Path'.
    It then uses pandas to create a DataFrame and save it to an Excel file.

### Main Function:
    The main function fetches the movie data and saves it to an Excel file named movies.xlsx.

## Required libraries:
**requests** for making API calls.
**pandas** for handling data and writing to Excel.
**openpyxl** for working with Excel files (used by pandas).