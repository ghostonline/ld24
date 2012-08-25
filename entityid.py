import uuid

def create(name=None):
    if not name:
        name = uuid.uuid4()
    return hash(name)
