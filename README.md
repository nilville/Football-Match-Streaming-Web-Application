# Football Match Streaming Web Application

A Flask-based web application that fetches and displays live football matches with working stream links. The app automatically checks stream availability and only shows matches with active, working streams.

## Features

- 🏈 **Live Football Matches**: Fetches popular football matches from the streamed.pk API
- ✅ **Stream Validation**: Automatically checks and validates stream links before displaying
- 🎨 **Modern UI**: Beautiful, responsive dark-themed interface with glassmorphism effects
- 📱 **Responsive Design**: Works seamlessly on desktop and mobile devices
- 🔍 **Multiple Streams**: Shows all available working streams for each match

## Project Structure

```
.
├── dkdkdk.py              # Main Flask application
├── templates/
│   ├── index.html         # Homepage with match listings
│   ├── watch.html         # Stream player page
│   └── 888.png           # Favicon
└── README.md             # This file
```

## Requirements

- Python 3.6+
- Flask
- requests

## Installation

1. Clone or download this repository

2. Install the required dependencies:

```bash
pip install flask requests
```

Or create a `requirements.txt` file:

```
Flask==2.3.0
requests==2.31.0
```

Then install:

```bash
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:

```bash
python dkdkdk.py
```

2. Open your web browser and navigate to:

```
http://localhost:5000
```

3. Browse available matches and click on any stream to watch.

## How It Works

1. **Match Fetching**: The app fetches football matches from the streamed.pk API
2. **Stream Validation**: For each match, it checks all available stream sources by making HEAD requests to verify they're accessible
3. **Filtering**: Only matches with at least one working stream are displayed
4. **Streaming**: Users can click on any working stream to watch it in an embedded player

## API Endpoints

- `GET /` - Homepage displaying all matches with working streams
- `GET /watch/<source>/<stream_id>` - Watch page for a specific stream

## Configuration

You can modify the following variables in `dkdkdk.py`:

- `website`: The base website URL (default: 'streamed.pk')
- `api`: The API endpoint for fetching matches (default: 'https://streamed.pk/api/matches/football')
- `host`: Server host (default: '0.0.0.0')
- `port`: Server port (default: 5000)
- `debug`: Debug mode (default: True)

## Notes

- Stream availability is checked in real-time, so some streams may become unavailable after the initial check
- The app uses HEAD requests to quickly validate stream URLs
- Streams are embedded from embedsports.top

## License

This project is provided as-is for educational purposes.

## Disclaimer

This application is for educational purposes only. Please ensure you have the right to access and stream the content in your jurisdiction.

