from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

website = 'streamed.pk'
api = 'https://streamed.pk/api/matches/football'

def get_football_matches_with_working_streams():
    """Fetch football matches and check which streams are working."""
    try:
        response = requests.get(api, timeout=10)
        data = response.json()
    except Exception as e:
        print(f"Error fetching data: {e}")
        return []
    
    matches = []
    for item in data:
        if item.get('category') == 'football' and item.get('popular') == True:
            working_streams = []
            for source in item.get("sources", []):
                watch_url = f'https://embedsports.top/embed/{source["source"]}/{source["id"]}/1'
                try:
                    res = requests.head(watch_url, timeout=5)
                    if res.status_code == 200:
                        working_streams.append({
                            'url': watch_url,
                            'source': source['source'],
                            'id': source['id']
                        })
                except Exception:
                    pass
            
            if working_streams:
                match_data = {
                    'id': item['id'],
                    'title': item['title'],
                    'poster': f'https://{website}{item.get("poster", "")}',
                    'working_streams': working_streams,
                    'teams': item.get('teams', {})
                }
                matches.append(match_data)
    
    return matches

@app.route('/')
def index():
    """Homepage displaying all football matches with working streams."""
    matches = get_football_matches_with_working_streams()
    return render_template('index.html', matches=matches)

@app.route('/watch/<path:stream_id>')
def watch(stream_id):
    """Watch page for playing a specific stream."""
    parts = stream_id.split('/')
    if len(parts) >= 2:
        source = parts[0]
        stream_id_only = '/'.join(parts[1:])
        watch_url = f'https://embedsports.top/embed/{source}/{stream_id_only}/1'
    else:
        watch_url = f'https://embedsports.top/embed/{stream_id}/1'
    
    return render_template('watch.html', watch_url=watch_url)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
