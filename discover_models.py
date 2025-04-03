import os
import importlib

def import_models():
    models_directory = os.path.join(os.path.dirname(__file__), 'model')

    for filename in os.listdir(models_directory):
        if filename.endswith('.py') and filename != '__init__.py':
            module_name = f"model.{filename[:-3]}"
            importlib.import_module(module_name)
