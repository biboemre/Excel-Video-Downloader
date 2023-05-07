import pandas as pd
import os
import requests
from pytube.exceptions import RegexMatchError, VideoUnavailable
from pytube import YouTube
from pytube import extract
from pytube import request as py_request
from pytube import Stream
from pytube.cli import on_progress
from pytube.helpers import safe_filename
from pytube.__main__ import YouTube as YouTubeDownloader
from PIL import Image
from io import BytesIO

df = pd.read_excel('veriler.xlsx')

for url in df['YouTube URL']:
    try:
        video = YouTube(url)
        video.check_availability()
        video.register_on_progress_callback(on_progress)
        video_streams = video.streams.filter(file_extension='mp4').order_by('resolution').asc()
        video_stream = video_streams.first()
        video_stream.download()

        file_name = safe_filename(video.title) + '.mp4'

        video_stream.download(filename=file_name)

        r = requests.get(df.loc[df['YouTube URL'] == url, 'Upload'].iloc[0])
        image = Image.open(BytesIO(r.content))
        image.save(file_name.replace('.mp4', '.jpg'))

    except RegexMatchError:
        print('Hata: Geçersiz URL ->', url)
    except VideoUnavailable:
        print('Hata: Video mevcut değil veya özel ->', url)
    except Exception as e:
        print(f'Hata: {e} -> {url}')