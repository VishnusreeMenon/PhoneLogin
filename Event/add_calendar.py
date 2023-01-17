from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from datetime import datetime, timedelta



def add_cal_event(topic,doctor,start_time,end_time,meet_link):
    scopes = ['https://www.googleapis.com/auth/calendar']

    flow = InstalledAppFlow.from_client_secrets_file("Event\client_secret.json", scopes=scopes)

    credentials = flow.run_console()


    service = build("calendar", "v3", credentials=credentials)
    result = service.calendarList().list().execute()

    # print(result['items'][0])

    calendar_id = result['items'][0]['id']
    
    st = start_time.split()
    y,m,d = map(int,st[0].split('-'))

    h,mn,s = map(int,st[1].split(':'))

    start_time = datetime(y,m,d,h,mn,s)
    
    et = end_time.split()
    y,m,d = map(int,et[0].split('-'))

    h,mn,s = map(int,et[1].split(':'))

    end_time = end_time = datetime(y,m,d,h,mn,s)

    # start_time = datetime(2019, 5, 12, 19, 30, 0)
    # end_time = start_time + timedelta(hours=4)
    timezone = 'Asia/Kolkata'
    
    event = {
        'summary': f'{topic}',
        'location': 'India',
        'description': f'Meeting with {doctor}\n Link : {meet_link}',
        'start': {
            'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'end': {
            'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
            'timeZone': timezone,
        },
        'reminders': {
            'useDefault': False,
            'overrides': [
            {'method': 'email', 'minutes': 24 * 60},
            {'method': 'popup', 'minutes': 10},
            ],
        },
    }
    try:
        service.events().insert(calendarId=calendar_id, body=event).execute()
        print("Done")
    except Exception as e:
        print("error ",e)
    

# add_cal_event("test","Aadith1","2023-01-20T17:06:02.000Z","2023-01-20T17:06:02.000Z","https://meet.google.com/cng-ksez-rkt")
# add_cal_event("test","Aadith1","2023-01-20 19:10:00","2023-01-20 19:20:00","https://meet.google.com/cng-ksez-rkt")