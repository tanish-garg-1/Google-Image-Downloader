import os
from google_images_search import GoogleImagesSearch
import zipfile

GCS_DEVELOPER_KEY = 'your_google_api_key'  # Replace with your API key
GCS_CX = 'your_search_engine_id'  # Replace with your search engine ID

def download_images(keyword, num_images):
    gis = GoogleImagesSearch(GCS_DEVELOPER_KEY, GCS_CX)
    search_params = {
        'q': keyword,
        'num': num_images,
        'fileType': 'jpg',
        'safe': 'off'
    }

    # Create a directory for images
    if not os.path.exists("downloads"):
        os.makedirs("downloads")

    # Clear previous images
    for file in os.listdir("downloads"):
        os.remove(os.path.join("downloads", file))

    # Search and download
    gis.search(search_params=search_params, path_to_dir="downloads")

    # Zip the images
    zip_path = f"downloads/{keyword}_images.zip"
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, _, files in os.walk("downloads"):
            for file in files:
                zipf.write(os.path.join(root, file), file)

    return zip_path
