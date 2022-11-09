"""
This file specifies the sessions that will appear on the Badger.
"""

# The session array is expected by the code that imports this file
sessions = []

# You can add as many of these as you like
# images will be converted from imagename.ext into imagename.bin. ImageMagick should handle all popular formats...
sessions.append({
    'title': "The Session's Title",
    'speaker': "Andrew Name",
    'sub': "An extra subheading",
    'description': "This is a description of the session. There's a limited amount of space for this, so go easy champ!",
    'start': '14:00',
    'end': '17:00',
    'image_src': "default-jr.bin"
})
