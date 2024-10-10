# Importing necessary modules
import yt_dlp  # YouTube downloader library for downloading videos
import os  # Operating system library for file path management

# Function to display available video formats to the user
def display_formats(formats):
    """
    Displays the available video/audio formats to the user.
    
    :param formats: A list of available formats retrieved from the YouTube video.
    """
    print("\nAvailable Formats:")
    for index, fmt in enumerate(formats):
        # Prepare format information for both video and audio formats
        format_info = (
            f"{index + 1}: {fmt['format_id']} - {fmt['ext']} - "
            f"{fmt['resolution'] if 'resolution' in fmt else 'Audio Only'} - "
            f"{fmt['filesize'] / (1024 * 1024):.2f} MB" if 'filesize' in fmt else ''  # Check if filesize is available
        )
        print(format_info)  # Print each format information
    print("\n")

# Function to handle the video download process
def download_video():
    """
    Prompts the user for a YouTube video URL, displays available download formats,
    and allows the user to download the video in a selected format.
    """
    # Asking the user to provide a YouTube video URL
    video_url = input("Enter the YouTube video URL: ")
    
    # Define options for yt-dlp to only fetch information (not download yet)
    options = {
        'format': 'bestvideo/best',  # Default to best video and audio quality
        'noplaylist': True,  # Ensure only a single video is downloaded, not a playlist
    }

    try:
        # Use yt-dlp to retrieve video info without downloading
        with yt_dlp.YoutubeDL(options) as ydl:
            # Fetch video information
            info_dict = ydl.extract_info(video_url, download=False)
            
            # Retrieve available formats for the video
            formats = info_dict['formats']
            display_formats(formats)  # Show formats to the user
            
            # Prompt user to select a format from the displayed list
            format_index = int(input("Select a format by number: ")) - 1
            
            # Validate if the user has selected a valid format
            if format_index < 0 or format_index >= len(formats):
                print("Invalid format selected.")
                return
            
            selected_format = formats[format_index]  # Get the user-selected format

            # Define download options based on the selected format
            download_options = {
                'format': selected_format['format_id'],  # The format selected by the user
                'outtmpl': os.path.join(os.getcwd(), '%(title)s.%(ext)s'),  # Save the file in the current directory
            }

            # Confirm download with the user
            confirm = input(f"Do you want to download {info_dict['title']} in format {selected_format['format_id']}? (y/n): ")
            if confirm.lower() != 'y':
                print("Download canceled.")
                return

            # Start downloading the video using the selected format
            ydl = yt_dlp.YoutubeDL(download_options)
            ydl.download([video_url])  # Download the video
            print("Download completed successfully!")

    # Catch any errors that may occur during the process
    except Exception as e:
        print(f"An error occurred: {e}")

# The script's main function
if __name__ == "__main__":
    download_video()  # Start the video download process when the script is run
