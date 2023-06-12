import os

from django.core.files.storage import FileSystemStorage
from django.utils.crypto import get_random_string


class RandomFilenameStorage(FileSystemStorage):
    @classmethod
    def get_file_name(cls, ext, length):
        return f'{get_random_string(length=length)}{ext}'

    @classmethod
    def get_path(cls, path, name, length=32):
        _, ext = os.path.splitext(name)
        name = cls.get_file_name(ext, length)
        while os.path.exists(os.path.join(path, name)):
            name = cls.get_file_name(ext, length)
        return os.path.join(path, name).lower()

    def get_available_name(self, name, *args, **kwargs):
        """For imagekit cache a thumbnail name must be no changed"""
        source = super().get_available_name(name, *args, **kwargs)
        path, name = os.path.split(source)
        return self.get_path(path, name)
