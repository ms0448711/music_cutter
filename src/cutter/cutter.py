import os
from pathlib import Path
from typing import Union, List
from pydub import AudioSegment
from src.schemas.segment import Segment

class Cutter():

    def __init__(self,):
        pass

    def cut(self,audio_file:Union[Path,os.PathLike], audio_segment_definition:List[Segment], output_dir = Path('output/')):
        file_type = audio_file.suffix
        if file_type ==  '.mp3':
            song = AudioSegment.from_mp3( audio_file )
        elif file_type == '.wav':
            song = AudioSegment.from_wav( audio_file )
        else:
            raise Exception("Cannot support file type:", file_type)

        for i,s in enumerate(audio_segment_definition):
            extract = song[ s.start_time*1000: s.end_time*1000 ]
            # Saving

            if file_type == '.mp3':
                extract.export( output_dir/(s.title+'.mp3'), format="mp3")
            elif file_type == '.wav':
                extract.export( output_dir/(s.title+'.wav'), format="wav")
