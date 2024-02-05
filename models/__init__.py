#!/user/bin/python3
"""package file"""


from models.engine.file_storage import FileStorage
from models import storage

storage = FileStorage()
storage.reload()
