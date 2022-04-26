def get():
    config = {}
    config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
    config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
    config['UPLOAD_PATH'] = 'data/uploads'
    return config