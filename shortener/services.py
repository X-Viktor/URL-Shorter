def get_short_url(url):
    """Укорачивает ссылку."""
    import pyshorteners
    s = pyshorteners.Shortener()
    return s.tinyurl.short(url)
