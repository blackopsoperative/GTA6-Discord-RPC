import time
from pypresence import Presence

gta6 = Presence('YOUR_APP_ID') # Would be smart to name this 'Grand Theft Auto VI'
gta6.connect()
gta6.update(start=time.time(),
            details='Playing as Jason',
            state='Story Mode',
            large_image='https://i.imgur.com/egNblmR.png',
            large_text='v0.861 Beta',
            small_image='https://i.imgur.com/d4Mbttt.jpeg',
            buttons=[{"label": "Get GTA VI", "url": "https://bit.ly/gta-6-join-game"}, {"label": "Join Beta", "url": "https://bit.ly/gta-6-join-game"}]
while True:
  time.sleep(15)
