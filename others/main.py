from datetime import datetime, timedelta


dateCreated = datetime(2022, 1, 1).strftime('%Y-%m-%d')



dateFinal = datetime.now().strftime('%Y-%m-%d')



tempo  = dateFinal - timedelta(days= '100')




