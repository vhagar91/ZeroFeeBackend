from importlib import import_module
import os


def asset_upload(instance, filename):



    output = 'users/%s' % filename


    return output

def asset_upload_property(instance, filename):



    output = 'listing/%s' % filename


    return output