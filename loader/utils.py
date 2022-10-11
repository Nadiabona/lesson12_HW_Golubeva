def save_picture(picture) -> str: #будем возращать путь, чтобы его записать
    filename = picture.filename
    path = f'uploads/images/{filename}'
    picture.save(path)
    return f'/{path}'

