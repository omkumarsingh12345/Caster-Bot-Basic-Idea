Python 3.13.3 (tags/v3.13.3:6280bb5, Apr  8 2025, 14:47:33) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> import random
... 
... commentary_templates = {
...     "kill": [
...         "BOOM! That was an insane shot!",
...         "What a takedown! Flawless execution!"
...     ],
...     "win": [
...         "Victory is theirs! What a match!",
...         "GG! That was a masterclass in domination."
...     ],
...     "low_health": [
...         "Health is dropping fast! This could end badly.",
...         "They’re in the danger zone now!"
...     ]
... }
... 
... def get_commentary(event, tone="Pro"):
...     lines = commentary_templates.get(event, [])
...     if not lines:
...         return ""
...     
...     return random.choice(lines)
