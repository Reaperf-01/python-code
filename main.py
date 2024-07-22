import yt_dlp
import os


def download_youtube_audio(youtube_url):
    """
    Downloads audio from a YouTube video and saves it as an MP3 file.

    Args:
        youtube_url (str): The URL of the YouTube video.
    """

    try:
        # Download audio using yt-dlp
        ydl_opts = {
            "format": "bestaudio[ext=m4a]/best[ext=m4a]/bestaudio",  # Prioritize m4a, fallback to other audio formats
            "outtmpl": "%(title)s.%(ext)s",
            "noplaylist": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(youtube_url, download=False)
            title = info["title"]
            output_filename = os.path.join(os.getcwd(), f"{title}.mp3")
            ydl.download([youtube_url])

        # Convert m4a to mp3 if necessary
        if output_filename.endswith(".m4a"):
            os.rename(
                output_filename, output_filename[:-4] + ".mp3"
            )  # Rename .m4a to .mp3

        print(f"Audio successfully downloaded to {output_filename}")

    except Exception as e:
        print(f"Download failed: {e}")


if __name__ == "__main__":
    # Input YouTube video URL
    youtube_url = input("Please enter YouTube video URL: ")

    # Call download function
    download_youtube_audio(youtube_url)
