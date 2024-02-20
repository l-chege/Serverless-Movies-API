#serverless function implementation using Flask and Azure Cosmos DB and Blob Storage

import os
import json
from flask import Flask, request
from azure.cosmos import CosmosClient
from azure.storage.blob import BlobServiceClient
import openai

app = Flask(__name__)

#initialize azure cosmos db and blob storage clients
cosmos_client = CosmosClient(os.environ['COSMOSDB_CONNECTION_STRING'])
database = cosmos_client.get_database_client(os.environ['COSMOSDB_DB_NAME'])
container = database.get_container_client(os.environ['COSMOSDB_CONTAINER_NAME'])

blob_service_client = BlobServiceClient.from_connection_string(os.environ['AZURE_STORAGE_CONNECTION_STRING'])
blob_container_client = blob_service_client.get_container_client(os.environ['AZURE_STORAGE_CONTAINER_NAME'])

#setup openai GPT-3 (optional)
openai.api_key - os.environ['OPENAI_API_KEY']

#get all movies
@app.route('/api/movies', methods=['GET'])
def get_movies():
    movies = list(container.query_items(query='SELECT * FROM c', enable_cross_partition_query=True))
    movie_list = [{"title": movie['title'], 
                   "year": movie['year'],
                   "genre": movie['genre'],
                   "cover_url": f"/api/movies/cover/{movie['id']}"} for movie in movies]
    return json.dumps(movie_list)

#get movies by year
@app.route('/api/movies/year/<int:year>', methods=['GET'])
def get_movies_by_year(year):
    movies = list(container.query_items(query=f'SELECT * FROM c WHERE c.year={year}', enable_cross_partition_query=True))
    movie_list = [{"title": movie['title'], 
                   "year": movie['year'], 
                   "genre": movie['genre'],
                   "cover_url": f"/api/movies/cover/{movie['id']}"} for movie in movies]
    return json.dumps(movie_list)

#get movie covers
@app.route('/api/movies/cover/<string:movie_id>', methods=['GET'])
def get_movie_cover(movie_id):
    blob_name = f"{movie_id}.jpg"
    blob_url = blob_container_client.get_blob_client(blob_name).url
    return json.dumps({"cover_url": blob_url})

#get movie summary using openai GPT-3 (optional)
@app.route('/api/movies/summary/<string:movie_id>', methods=['GET'])
def get_movie_summary(movie_id):
    movie = container.read_item(item=movie_id)
    prompt = f"Create the movie summary of '{movie['title']}' released in '{movie['year']}' of the genre {movie['genre']}."
    response = openai.Completion.create(engine="text-davinci-002", prompt=prompt, max_tokens=150)
    return json.dumps({"summary": response['choices'][0]['text']})

if __name__ == "__main__":
    app.run()
