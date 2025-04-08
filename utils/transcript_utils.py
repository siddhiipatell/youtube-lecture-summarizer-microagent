from youtube_transcript_api import YouTubeTranscriptApi

def get_transcript(video_url):
    video_id = video_url.split("v=")[-1].split("&")[0]
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    text = " ".join([t["text"] for t in transcript])
    return text
