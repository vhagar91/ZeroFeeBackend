from importlib import import_module
import os


def asset_upload(instance, filename):

    username = instance.username

    output = 'user%s/%s' % (username, filename)


    return output