from moviepy import VideoFileClip
import ctypes
import os

os.environ["SDL_VIDEO_WINDOWS_POS"] = "0,0"
user32 = ctypes.windll.user32
screen_width = user32.GetSystemMetrics(0)
screen_height = user32.GetSystemMetrics(1)
print(f"Screen resolution: {screen_width}x{screen_height}")

clip = VideoFileClip("videos/B3.mp4")
try:
    clip = clip.resized(height=screen_height)
    clip.preview()
except:
    pass