async def write_image(file) -> str:
    """Записывает файл на сервер и вовзращает путь к нему"""
    contents = await file.read()
    with open(f'/code/files/{file.filename}', "wb") as f:
        f.write(contents)
    return f'/files/{file.filename}'