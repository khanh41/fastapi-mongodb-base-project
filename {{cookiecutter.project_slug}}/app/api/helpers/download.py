from app.api.helpers import base_file_download
from app.core.constant import VIDEO_TEMPLATE


def download_video_template():
    base_file_download(VIDEO_TEMPLATE["path"], VIDEO_TEMPLATE["url"])
