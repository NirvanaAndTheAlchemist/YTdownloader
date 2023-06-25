from types import FunctionType
from pytube import YouTube
from typing import Any, Callable, Dict, List, Optional

#Place the URL in this field
url = input('Enter youtube URL here...')

#Create a Youtube object
video = YouTube(url)

#Get the highest resolution of the video
stream = video.streams.get_highest_resolution()

#Download the video to this directory
folder = input("Enter save location here...")
stream.download(folder)

#Download Progress (work in progress...)
#def register_on_progress_callback(self, function: Callable[[Any, Optional[str]], None]):
 #   self.stream_monostate.on_complete = FunctionType