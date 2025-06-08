import logging
import subprocess
import os
import requests
import time

from .types import Movie, Scene, Image, Video, Audio,Subtitles, CreateMovieResponse
from settings import settings

logger = logging.getLogger(__name__)

def download_and_convert_to_mp4(url: str, output_path: str):
    temp_path = "temp_downloaded_video"

    # Step 1: Download the file
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(temp_path, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    
    # Step 2: Convert to mp4 with H.264 codec using ffmpeg
    command = [
        "ffmpeg",
        "-i", temp_path,           # input file
        "-c:v", "libx264",         # use H.264 video codec
        "-preset", "fast",         # encoding speed/quality trade-off
        "-crf", "23",              # quality (lower = better, typical range: 18–28)
        "-c:a", "aac",             # audio codec
        "-b:a", "128k",            # audio bitrate
        "-y",                      # overwrite output if exists
        output_path
    ]

    subprocess.run(command, check=True)

    # Step 3: Clean up temporary file
    os.remove(temp_path)
    logger.info(f"Saved converted video to: {output_path}")


def create_movie(movie: Movie) -> CreateMovieResponse:
    """
    Создает видео на основе переданного объекта Movie.

    :param movie: Объект Movie, содержащий информацию о видео.
    :return: Ответ от API в виде словаря.
    """
    response = requests.post(
        url=f'{settings.json2video_base_url}/movies',
        headers={
            'x-api-key': settings.json2video_api_key,
            'Content-Type': 'application/json'
        },
        data=movie.model_dump_json()
    )

    if response.status_code == 200:
        response = CreateMovieResponse.model_validate(response.json())
        return response
    else:
        response.raise_for_status()  # Вызывает исключение при ошибке запроса
        
        
def get_movie(project_id: str) -> dict:
    """
    Получает информацию о видео по его ID.

    :param movie_id: ID видео.
    :return: Ответ от API в виде словаря.
    """
    response = requests.get(
        url=f'{settings.json2video_base_url}/movies/?project={project_id}',
        headers={
            'x-api-key': settings.json2video_api_key
        }
    )

    if response.status_code == 200:    
        return response.json()
    else:
        response.raise_for_status()  # Вызывает исключение при ошибке запроса
        
        
def run_movie_creation(movie: Movie) -> dict:
    """
    Запускает процесс создания видео.

    :param movie: Объект Movie, содержащий информацию о видео.
    :return: Ответ от API в виде словаря.
    """
    create_response = create_movie(movie)
    logger.info(f"Create movie: {create_response.model_dump_json()}")
    logger.info(f"Get movie {create_response.project} status")
    while True:
        get_response = get_movie(create_response.project)
        logger.info(f"{create_response.project}: {get_response['movie']['status']}")
        
        if get_response['movie']['status'] == 'done':
            logger.info(f"{create_response.project} url: {get_response['movie']['url']}")
            download_and_convert_to_mp4(
                url=get_response['movie']['url'],
                output_path=f"output/{create_response.project}.mp4"
            )
            return get_response
        elif get_response['movie']['status'] == 'error':
            logger.info(f"{create_response.project} error: {get_response['movie']['message']}")
            return get_response
        
        time.sleep(1)
        
