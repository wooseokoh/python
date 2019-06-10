from storages.backends.s3boto3 import S3Boto3Storage
class MediaStorage(S3Boto3Storage):
    location = 'media'
    file_overwrite = False # 오버라이드 금지 ex) 001.jpg , 001GtEEnog.jpg