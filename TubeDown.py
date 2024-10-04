import yt_dlp
import os

def display_formats(formats):
    print("\nAvailable Formats:")
    for index, fmt in enumerate(formats):
        format_info = f"{index + 1}: {fmt['format_id']} - {fmt['ext']} - {fmt['resolution'] if 'resolution' in fmt else 'Audio Only'} - {fmt['filesize'] / (1024 * 1024):.2f} MB" if 'filesize' in fmt else ''
        print(format_info)
    print("\n")

def download_video():
    # Asking for the YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Define options for fetching formats
    options = {
        'format': 'bestvideo/best',  # Default to best quality
        'noplaylist': True,  # Only download single video
    }

    try:
        with yt_dlp.YoutubeDL(options) as ydl:
            # Fetching video information
            info_dict = ydl.extract_info(video_url, download=False)
            formats = info_dict['formats']  # Getting available formats
            display_formats(formats)  # Displaying available formats
            
            # Asking user to select a format
            format_index = int(input("Select a format by number: ")) - 1
            
            if format_index < 0 or format_index >= len(formats):
                print("Invalid format selected.")
                return
            
            selected_format = formats[format_index]

            # Define download options with user-selected format
            download_options = {
                'format': selected_format['format_id'],  # User-selected format
                'outtmpl': os.path.join(os.getcwd(), '%(title)s.%(ext)s'),  # Save file in current directory with video title
            }

            # Confirming download
            confirm = input(f"Do you want to download {info_dict['title']} in {selected_format['format_id']}? (y/n): ")
            if confirm.lower() != 'y':
                print("Download canceled.")
                return

            # Downloading the selected video
            ydl = yt_dlp.YoutubeDL(download_options)
            ydl.download([video_url])  # Download the video
            print("Download completed successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    download_video()