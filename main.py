import requests
import pandas as pd

# Jellyfin server configuration
JELLYFIN_URL = input('Enter the Jellyfin server address & port(x.x.x.x:x).')
API_KEY = input('Enter the API key.')

def get_movies():
    headers = {
        'X-Emby-Token': API_KEY
    }
    response = requests.get(f'{JELLYFIN_URL}/Items', headers=headers, params={'IncludeItemTypes': 'Movie', 'Recursive': True, 'Fields': 'Name,Path'})
    response.raise_for_status()
    return response.json()['Items']

def movies_to_excel(movies, output_file='movies.xlsx'):
    movie_list = []
    for movie in movies:
        movie_list.append({
            'Name': movie['Name'],
            'Path': movie['Path']
        })
    df = pd.DataFrame(movie_list)
    df.to_excel(output_file, index=False)

def main():
    movies = get_movies()
    movies_to_excel(movies)
    print(f'Movie list has been saved to movies.xlsx')

if __name__ == '__main__':
    main()
