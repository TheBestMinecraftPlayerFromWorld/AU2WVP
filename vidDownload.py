from pytube.download_helper import download_video
urls = ["https://www.youtube.com/shorts/f_A440qj3SE","https://www.youtube.com/shorts/xZSUIOeRJJM","https://www.youtube.com/shorts/Ga3MMFcnmY0","https://www.youtube.com/watch?v=d16qT44HNaE","https://www.youtube.com/shorts/isy8pPes5KA","https://www.youtube.com/shorts/BH9b46Sy7jM","https://www.youtube.com/shorts/f5eTT5cx6J0"]

print(len(urls))
for url in urls:
    try:
        download_video(url=url)
    except:pass