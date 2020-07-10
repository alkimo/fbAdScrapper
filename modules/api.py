from __future__ import print_function
import pickle
import os.path
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaFileUpload
import getpass


# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly',
          'https://www.googleapis.com/auth/drive.file', 'https://www.googleapis.com/auth/drive']


def create_folder(service, name):
    file_metadata = {
        'name': name,
        'mimeType': 'application/vnd.google-apps.folder',
    }

    file = service.files().create(body=file_metadata, fields='id').execute()
    return file


def iterate_files(service, path, file_id):

    for filename in os.listdir(path):
        print(filename)
        if(filename.endswith(".png")):
            file_metadata = {'name': filename, 'parents': [file_id['id']]}
            media = MediaFileUpload(path + filename, mimetype='image/png')
            file = service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()
            continue
        elif filename.endswith(".html"):
            file_metadata = {'name': filename, 'parents': [file_id['id']]}
            media = MediaFileUpload(path + filename, mimetype='text/html')
            file = service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()
            continue
        elif filename.endswith(".pdf"):
            file_metadata = {'name': filename, 'parents': [file_id['id']]}
            media = MediaFileUpload(path + filename, mimetype='application/pdf')
            file = service.files().create(body=file_metadata,
                                                media_body=media,
                                                fields='id').execute()
            continue

def upload(name, folder_path):
    """Shows basic usage of the Drive v3 API.

    Prints the names and ids of the first 10 files the user has access
    to.
    """
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('/home/' + getpass.getuser() +  '/Desktop/fbScrapper/token.pickle'):
        with open('/home/' + getpass.getuser() +  '/Desktop/fbScrapper/token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                '/home/' + getpass.getuser() +  '/Desktop/fbScrapper/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('/home/' + getpass.getuser() +  '/Desktop/fbScrapper/token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('drive', 'v3', credentials=creds)

    # Creates folder on Google Drive
    file_id = create_folder(service, name)
    iterate_files(service, folder_path, file_id)
