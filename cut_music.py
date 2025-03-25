from pydub import AudioSegment
from pathlib import Path
import re


class Song:
    def __init__(self,title,start_time,part):
        self.title=title
        self.start_t=start_time
        self.part=part
        

def time_str_to_sec(time_str):
    match=re.search(r"(?P<hour>[\d]+):(?P<min>[\d]+):(?P<sec>[\d]+)",time_str)
    match_m=re.search(r"(?P<min>[\d]+):(?P<sec>[\d]+)",time_str)
    if match:
        return int(match.group('hour'))*60*60 + int( match.group('min'))*60 + int(match.group('sec'))
    elif match_m:
        return int( match_m.group('min'))*60 + int(match_m.group('sec'))
    else:
        return 0


if __name__=='__main__':
    x="#6 Maplestory 20 Additional Piano Compilation"
    is_test=False
    file_folder = Path(x)
    file_path = file_folder / (x + ".mp3")
    timestamp_file_path = file_folder/"timestamps.txt"
    with open(timestamp_file_path,'r') as f:
        timestamps_str=f.readlines()
    songs=[]
    part=""
    for line in timestamps_str:
        if "Overture" in line:
            part="Overture"
        if "Finale" in line:
            part="Finale"
        has_timestamp = re.search(r"(\d\d?:)?\d\d:\d\d",line)
        if has_timestamp:
            match1=re.search(r"\((?P<title>[^()]+)\)[^()]+\((?P<time>(\d\d?:)?\d\d:\d\d)\)",line)
            match2=re.search(r"\W(?P<title>[^()]+)[^()]+\((?P<time>(\d\d?:)?\d\d:\d\d)\)",line)
            match=None
            if match1:
                match=match1
            elif match2:
                match=match2
            if match:
                songs.append(Song(
                    title=match.group('title').replace(r"/","_"),
                    start_time=match.group('time'),
                    part=part
                ))
        else:
            
            part_m=re.search(r"\((?P<part>.+)\)",line)
            if part_m:
                part=part_m.group('part')
    if is_test:
        [print(item.part,'-',item.title,'\t\t\t',item.start_t) for item in songs]
        print("Song List Length:",len(songs))
        exit()
    # Opening file and extracting segment
    song = AudioSegment.from_mp3( file_path )
    for i,s in enumerate(songs):
        start_time = time_str_to_sec(s.start_t)*1000
        if i < len(songs)-1:
            end_time = time_str_to_sec(songs[i+1].start_t)*1000
            extract = song[start_time:end_time]
        else:
            extract = song[start_time:]
        # Saving
        print((s.part+'-'+s.title+'.mp3'),'saving')
        extract.export( file_folder/(s.part+' - '+s.title+'.mp3'), format="mp3")
        print((s.part+'-'+s.title+'.mp3'),'saving completed!')
    

    