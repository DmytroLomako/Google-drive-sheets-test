from .settings import *

def connect(name, version):
    creds = None
    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port = 0)
        with open("token.json", "w") as token:
            token.write(creds.to_json())
    service = build(name, version, credentials = creds)
    return service