from yt_concate.pipeline.steps.get_video_list import GetVideoList
from yt_concate.pipeline.steps.download_captions import DownloadCaptions
from yt_concate.pipeline.steps.read_caption import ReadCaption
from yt_concate.pipeline.steps.preflight import Preflight
from yt_concate.pipeline.steps.postflight import Postlight
from yt_concate.pipeline.steps.step import StepException
from yt_concate.pipeline.pipeline import Pipeline
from yt_concate.utils import Utils
CHANNEL_ID = 'UCOnTV13iZ-Gb351nz9-9tOA'

def main():
    inputs = {
        'channel_id': CHANNEL_ID
    }
    steps = [
        Postlight(),
        Preflight(),
        GetVideoList(),
        DownloadCaptions(),
        ReadCaption(),
        ]

    utils = Utils()
    p = Pipeline(steps)
    p.run(inputs, utils)


if __name__ == '__main__':
    main()
