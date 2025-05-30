import yt_dlp

# Paste your YouTube video link here
video_urls = [
    "https://www.youtube.com/watch?v=GlvgqliaQaA", 
    "https://www.youtube.com/watch?v=vEUVeCQ63Ew", 
    "https://www.youtube.com/watch?v=xeVZ6QcUb7Q", 
    "https://www.youtube.com/watch?v=0rFNsOx9gUo",  
    "https://www.youtube.com/watch?v=T1U7rniplCE",  
    "https://www.youtube.com/watch?v=iHE4eRksidQ",  
    "https://www.youtube.com/watch?v=tSwH1i1bl7A", 
    "https://www.youtube.com/watch?v=g6XRDzCLzA0",  
    "https://www.youtube.com/watch?v=hqVeBtp7J_E", 
    "https://www.youtube.com/watch?v=skr08dnWXC8", 
    "https://www.youtube.com/watch?v=9LfjL2m8cxM", 
    "https://www.youtube.com/watch?v=PAkvevHCEQU",  
    "https://www.youtube.com/watch?v=QKYd4A1RDss",  
    "https://www.youtube.com/watch?v=VutZ3E55O0o",  
    "https://www.youtube.com/watch?v=8T1dx1sP-X0",  
    "https://www.youtube.com/watch?v=xpyfMLQa6Rk",
    "https://www.youtube.com/watch?v=bLAPFchSH00",
    "https://www.youtube.com/watch?v=ZEV7DNfn-08",
    "https://www.youtube.com/watch?v=T4UGsVn0D_I",
    "https://www.youtube.com/watch?v=Mg-wl_8xL7s"
]




ydl_opts = {
    'outtmpl': 'downloads/%(title)s.%(ext)s',
    'format': 'best'
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download(video_urls)

