import streamlit as st

def social_icons(width=24, height=24, **kwargs):
    icon_template = '''
    <a href="{url}" target="_blank" style="margin-right: 20px;">
        <img src="{icon_src}" alt="{alt_text}" width="{width}" height="{height}">
    </a>
    '''

    icons_html = ""
    for name, url in kwargs.items():
        icon_src = {
            "linkedin": "https://www.pinclipart.com/picdir/big/574-5743993_linkedin-icon-white-png-clipart.png",
            "github": "https://www.pinclipart.com/picdir/big/158-1581614_github-clipart.png",
            "medium": "https://miro.medium.com/v2/resize:fit:720/format:webp/1*psYl0y9DUzZWtHzFJLIvTw.png"
        }.get(name.lower())

        if icon_src:
            icons_html += icon_template.format(url=url, icon_src=icon_src, alt_text=name.capitalize(), width=width, height=height)
    return icons_html
