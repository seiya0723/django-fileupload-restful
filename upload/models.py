from django.db import models

class PhotoList(models.Model):

    class Meta:
        db_table    = "photolist"

    photo       = models.ImageField(verbose_name="フォト",upload_to="photo/")

class DocumentList(models.Model):

    class Meta:
        db_table    = "documentlist"

    document    = models.FileField(verbose_name="ファイル",upload_to="file/")
