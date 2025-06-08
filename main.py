import logging

from json2video import Movie, Scene, Image, Video, Audio, Subtitles, run_movie_creation

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def create_task_1():
    movie = Movie(
        resolution="custom",
        quality="low",  
        width=1080,
        height=1920,
        scenes=[
            Scene(
                duration=14,
                transition={
                    "style": "fade",
                    "duration": 1
                },
                elements=[
                    Video(
                        type="video",
                        src='https://files2.heygen.ai/aws_pacific/avatar_tmp/20a7d8a053674a70b6e6ff024f1baa9d/c6a52cad66414a7faedec8ec70158a34.mp4?Expires=1749911689&Signature=AwrkWOr6u1gzV2k2-jHbNvWnkzLfz0jvF441StXXcTRFlnqGfdHaslvkBIDipoE5-bgTMar2EJKKhxX6eRTNNCGWS4oN9pNU9fTD620aElfdWgidTPTyuBA2oPQEhjtdWrsmR52tWI2Re0l3G7L0TcxPycZccje8sWHGTwAukaap6~s78HzGaIUtKiIqVGs0J8mpokdN8RuVb1EyX3ZUCxHfC5F6euKquxxBu7XWdaH8xeH-DKdgn23S-0niVc620Y9K1q4C2ZwJ16OHyrK18Qyez1rLKeMFI8V8nwozXNDfZ0qj8KgCpnT4EpXBucYDeY0pDHglEmf2gtzDjazDsQ__&Key-Pair-Id=K38HBHX5LX3X2H',
                        x=0,
                        y=0,
                        muted=False
                    ),
                    Video(
                        type="video",
                        src='https://dl.dropboxusercontent.com/scl/fi/38kz4nui2n5l7qo4adknn/file_26.mp4?rlkey=tsjvsyeqrlzbg04tq15ljzetr&dl=1',
                        width=1080,
                        height=1080,
                        x=0,
                        y=960,
                        muted=True
                    ),
                    Audio(
                        type="audio",
                        src='https://dl.dropboxusercontent.com/scl/fi/wfaq8fy3ptuars8hnt150/file_29.MP3?rlkey=9236cggfg86jb9ng6ulnb7c94&dl=1',
                        volume=1.0
                    )
                ]  
            )
        ],
        elements=[
            Subtitles(
                type="subtitles",
                language="ru",
                settings={
                    'position': 'center-center',
                    'font-size': 64,
                }
            )
        ]
    )
    result = run_movie_creation(movie)
    
    
def create_task_2():
    images = [
        "https://im.runware.ai/image/ws/2/ii/ce00de5e-4061-4a89-9c4e-f200a9130bd7.jpg",
        "https://im.runware.ai/image/ws/2/ii/dbd10a98-161f-451a-9c8c-cd3a20e746a5.jpg",
        "https://im.runware.ai/image/ws/2/ii/a251d422-203a-4aed-bf6d-bbe2b7cb5504.jpg",
    ]


    scenes = []
    for image in images:
        scenes.append(
            Scene(
                elements=[
                    Image(
                        type="image",
                        src=image,
                        width=1920,
                        height=1920,
                        x=0,
                        y=0,
                        zoom=0
                    ),
                    Image(
                        type="image",
                        src=image,
                        width=1080,
                        height=1080,
                        x=0,
                        y=420,
                        zoom=1
                    )
                ],
                transition={
                    "style": "fade",
                    "duration": 1
                },
                duration=4
            )
        )
        
    movie = Movie(
        resolution="custom",
        quality="low",  
        width=1080,
        height=1920,
        scenes=scenes
    )

    result = run_movie_creation(movie)


def create_task_3():
    movie = Movie(
        resolution="custom",
        quality="low",  
        width=1080,
        height=1920,
        scenes=[
            Scene(
                duration=20,
                transition={
                    "style": "fade",
                    "duration": 1
                },
                elements=[
                    Video(
                        type="video",
                        src='https://www.dropbox.com/scl/fi/zvnniekpcmguid3k2l916/b838fafe-35e0-4657-9b08-6c4d50e35c49-video.mp4?rlkey=6ctiy1tmkyojvcpzv38n8nh62&st=9vbbzkx8&dl=1',
                        muted=True,
                        width=1080,
                        height=1920,
                        x=0,
                        y=0,
                    ),
                    Video(
                        type="video",
                        src='https://dl.dropboxusercontent.com/scl/fi/38kz4nui2n5l7qo4adknn/file_26.mp4?rlkey=tsjvsyeqrlzbg04tq15ljzetr&dl=1',
                        width=1024,
                        height=1024,
                        x=0,
                        y=0,
                        position="center-center",
                        mask='https://www.dropbox.com/scl/fi/dta9mqdq6yr5peelct0jr/476_resized_1024x1024.png?rlkey=3srarkslhfsji8nbasa0lzmbp&st=svir2tt7&dl=1'
                    )
                ]
            )
        ]
    )
    result = run_movie_creation(movie)


if __name__ == "__main__":
    print('============= Start Task 1 =============')
    create_task_1()
    print('============= Start Task 2 =============')
    create_task_2()
    print('============= Start Task 3 =============')
    create_task_3()
