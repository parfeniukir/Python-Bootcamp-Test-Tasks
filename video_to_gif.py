'''
Because of "TikTok example" is not working, I have taken another one.
My example URL: 
https://rr5---sn-4g5lzner.googlevideo.com/videoplayback?expire=1659446515&ei=k9DoYo3xB9SDp-oPq92SuAI&ip=216.131.108.27&id=o-ABMiOVej6yR9RNKAKQWMDYAZOmfmxRXdtqKK0JMbFIz_&itag=18&source=youtube&requiressl=yes&spc=lT-KhpyzfXMcUj8xiFH7U4e18Z-Amqw&vprv=1&mime=video%2Fmp4&ns=Qr3TDHtMJdHohzjtFbKMCEIH&gir=yes&clen=400307&ratebypass=yes&dur=7.337&lmt=1625908751367810&fexp=24001373,24007246&c=WEB&rbqsm=fr&txp=1319222&n=IUsspaaC_SfBUQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgfZ5om3WuXnSEnALOtNGEMiy4L35KFuxmkPnnV8uUb5UCIANsXR2he-L-1Hciso2JNEGY1VbPbYNs_77t2AifCBYi&redirect_counter=1&cm2rm=sn-1gie67z&req_id=7187eeafadb5a3ee&cms_redirect=yes&cmsv=e&mh=3a&mip=143.244.46.232&mm=34&mn=sn-4g5lzner&ms=ltu&mt=1659424622&mv=u&mvi=5&pl=24&lsparams=mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIhAJddc28bWFMy028_FRRV-60qmEScLkcL3AAvzCTmbcu9AiAeVHvUNPDS_efmdhSCGQv7lb_fPchXWMOPVZ4UNSqcbQ%3D%3D
'''

import os
import urllib.request
from moviepy.editor import VideoFileClip


def video_for_url_to_gif():
    '''
    Function that input a video url address and return a path to GIF image.
    '''
    url = input("Enter the URL\n")
    video_name = input("Enter the name for the video\n")
    video_name_mp4 = video_name + ".mp4"
    try:
        print("Downloading start...\n")
        urllib.request.urlretrieve(url, video_name_mp4)
        print("Download completed!")
    except Exception as e:
        print(e)

    video_clip = VideoFileClip(video_name_mp4)
    video_clip.write_gif(f"{video_name}.gif")
    print(os.path.abspath(f'{video_name}.gif'))


if __name__ == "__main__":
    video_for_url_to_gif()
