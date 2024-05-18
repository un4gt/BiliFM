import os

import typer

from .audio import Audio
from .fav import Fav
from .season import Season
from .series import Series
from .user import User
from .util import Directory, Path, AudioQuality, AudioQualityEnums

app = typer.Typer()


@app.command()
def bv(bv: str, directory: Directory = None, audio_quality: AudioQuality = AudioQualityEnums.k64):
    audio = Audio(bv, audio_quality)
    audio.download()


@app.command()
def uid(uid: str, directory: Directory = None, audio_quality: AudioQuality = AudioQualityEnums.k64):
    user = User(uid)

    for video in user.videos:
        bv = video["bvid"]
        audio = Audio(bv, audio_quality)
        audio.download()

    typer.echo("Download complete")


@app.command()
def fav(
    media_id: str,
    cookies_path: str = Path,
    directory: Directory = None,
    audio_quality: AudioQuality = AudioQualityEnums.k64
):
    with open(cookies_path, "r") as f:
        cookies = f.read()

    fav = Fav(media_id, cookies)

    for bvid in fav.id_list:
        audio = Audio(bvid, audio_quality)
        audio.download()

    typer.echo("Download complete")


@app.command()
def season(uid: str, sid: str, directory: Directory = None, audio_quality: AudioQuality = AudioQualityEnums.k64):
    sea = Season(uid, sid)
    audio_generator = sea.get_videos()
    if not audio_generator:
        typer.Exit(1)
        return

    if not os.path.isdir(sea.name):
        os.makedirs(sea.name)
    os.chdir(sea.name)

    for audios in audio_generator:
        for id in audios:
            audio = Audio(id, audio_quality)
            audio.download()
    typer.echo("Download complete")


@app.command()
def series(uid: str, sid: str, directory: Directory = None, audio_quality: AudioQuality = AudioQualityEnums.k64):
    """Download bilibili video series

    The api of series lacks the series name, executing
    this command will not create a folder for the series
    """
    ser = Series(uid, sid)
    audio_generator = ser.get_videos()
    if not audio_generator:
        typer.Exit(1)
        return

    for audios in audio_generator:
        for id in audios:
            audio = Audio(id, audio_quality)
            audio.download()
    typer.echo("Download complete")
