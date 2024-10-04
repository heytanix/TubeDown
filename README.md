# YouTube Video Downloader

This Python script allows you to download videos from YouTube by selecting the desired format. It utilizes the `yt-dlp` library, which is a powerful tool for downloading videos and audio from various streaming platforms, including YouTube.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)

## Features

- **Available Formats**: Lists all the available video and audio formats with details such as format ID, file extension, resolution, and file size.
- **User-Friendly Interface**: Simple command-line interface that guides users through the downloading process.
- **Customizable Downloads**: Allows users to choose the desired format before downloading.
- **Error Handling**: Provides clear error messages to help troubleshoot any issues during the download process.

## Requirements

To run this script, you need to have Python installed on your machine. The script requires the following Python package:

- `yt-dlp`: A fork of `youtube-dl` that supports more sites and additional features.

### Installation

You can install the required package using pip:

```bash
pip install yt-dlp
