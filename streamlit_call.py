from subprocess import Popen

def load_jupyter_server_extension(nbapp):
    """Serve the streamlit app"""
    Popen(["streamlit", "run", "app.ipynb", "--browser.serverAddress=0.0.0.0", "--server.enableCORS=False"])
