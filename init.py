import os
import json
from flask import Flask, request
from azure.cosmos import CosmosClient
from azure.storage.blo import BlobServiceClient
import openai

app = Flask(__name__)

#initialize azure cosmos db and blob storage
