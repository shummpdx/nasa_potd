model_backend='datastore'

if model_backend == 'datastore':
    from .model_datastore import model
else:
    raise ValueError("No appropiate databackend configured.")

appmodel = model()

def get_model():
    return appmodel
