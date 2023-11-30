import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

def uploadFile(path, cfg):
    # Set the path to your JSON key file
    credentials_path = cfg["service-account-key-path"]

    # Set the ID of the Google Drive folder where you want to upload the file
    folder_id = cfg["google-drive-folder-id-upload"]

    # Authenticate using the service account credentials
    credentials = service_account.Credentials.from_service_account_file(
        credentials_path,
        scopes=['https://www.googleapis.com/auth/drive.file']
    )

    # Build the Drive API service
    drive_service = build('drive', 'v3', credentials=credentials)

    # Create file metadata
    file_metadata = {
        'name': os.path.basename(path),
        'parents': [folder_id]
    }

    # Upload the file
    media_body = media = MediaFileUpload(path, resumable=True)
    request = drive_service.files().create(body=file_metadata, media_body=media_body)
    response = None

    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"Uploaded {int(status.progress() * 100)}%")

    print(f"File ID: {response['id']}")
