"""
google_drive_integration.py
--------------------------
Moduł pozwalający użytkownikowi połączyć konto Google Drive z AI. Umożliwia autoryzację, pobieranie plików i przeszukiwanie zasobów Dysku Google.
Wymaga interakcji użytkownika i pliku credentials.json (Google Cloud OAuth2).
"""

import os
import importlib
from typing import List

try:
    _gapiclient = importlib.import_module('googleapiclient.discovery')
    build = _gapiclient.build
    _gapiclient_http = importlib.import_module('googleapiclient.http')
    MediaIoBaseDownload = getattr(_gapiclient_http, 'MediaIoBaseDownload', None)
    _oauth_flow = importlib.import_module('google_auth_oauthlib.flow')
    InstalledAppFlow = getattr(_oauth_flow, 'InstalledAppFlow', None)
    _gauth_requests = importlib.import_module('google.auth.transport.requests')
    Request = getattr(_gauth_requests, 'Request', None)
    import pickle  # noqa: F401
except Exception:
    build = None  # Google API nie jest zainstalowane
    MediaIoBaseDownload = None  # type: ignore
    InstalledAppFlow = None  # type: ignore
    Request = None  # type: ignore
    pickle = None  # type: ignore

SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
CREDENTIALS_FILE = 'credentials.json'
TOKEN_FILE = 'token.pickle'

class GoogleDriveAI:
    def __init__(self):
        self.service = None
        self.authorize()

    def authorize(self):
        """Autoryzuje użytkownika i zapisuje token dostępu."""
        if build is None:
            print("[AI] Moduł Google API nie jest zainstalowany. Zainstaluj: pip install google-api-python-client google-auth-httplib2 google-auth-oauthlib")
            return
        creds = None
        if os.path.exists(TOKEN_FILE):
            with open(TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(CREDENTIALS_FILE, SCOPES)
                creds = flow.run_local_server(port=0)
            with open(TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)
        self.service = build('drive', 'v3', credentials=creds)
        print("[AI] Połączono z Google Drive!")

    def list_files(self, query: str = None, max_results: int = 20) -> List[dict]:
        """Zwraca listę plików na Dysku Google użytkownika."""
        if not self.service:
            print("[AI] Brak połączenia z Google Drive.")
            return []
        results = self.service.files().list(q=query, pageSize=max_results, fields="files(id, name, mimeType)").execute()
        return results.get('files', [])

    def download_file(self, file_id: str, dest_path: str):
        """Pobiera plik z Google Drive na dysk lokalny."""
        if not self.service:
            print("[AI] Brak połączenia z Google Drive.")
            return
        request = self.service.files().get_media(fileId=file_id)
        with open(dest_path, 'wb') as f:
            downloader = MediaIoBaseDownload(f, request)
            done = False
            while not done:
                status, done = downloader.next_chunk()
                print(f"[AI] Pobieranie: {int(status.progress() * 100)}%")
        print(f"[AI] Plik pobrany: {dest_path}")

# Przykład użycia:
# drive = GoogleDriveAI()
# pliki = drive.list_files()
# for f in pliki:
#     print(f["name"], f["id"])