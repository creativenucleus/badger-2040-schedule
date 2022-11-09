"""
This file specifies the sessions that will appear on the Badger.
"""
event_title = "The Badger2040 Event"

# The session array is expected by the code that imports this file
sessions = []

# You can add as many of these as you like
# images will be converted from imagename.ext into imagename.bin. ImageMagick should handle all popular formats...
sessions.append({
    'title': "The Session's Title",
    'speaker': "James Rutherford",
    'sub': "An extra subheading",
    'description': "This is a description of the session. There's a limited amount of space for this, so go easy champ!",
    'start': '10:00',
    'end': '13:00',
    'image_src': "james-1.bin"
})

sessions.append({
    'title': "This is Session 2",
    'speaker': "@jtruk@mastodon.social",
    'sub': "Another subheading",
    'description': "Well, I guess we're on to session two. Enjoy!",
    'start': '14:00',
    'end': '15:30',
    'image_src': "james-2.bin"
})
