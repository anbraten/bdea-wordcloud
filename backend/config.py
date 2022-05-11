def get():
    config = {}
    config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
    config['UPLOAD_EXTENSIONS'] = ['.txt']
    config['UPLOAD_PATH'] = 'fake-hdfs/uploads'
    return config