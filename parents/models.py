from django.db import models

# Create your models here.
class Entry(models.Model):
    """
    from_who: int
    what: Text
    when: Datetime
    to_who: int
    c_time: created time
    m_time: modified time
    """
    what = models.TextField()
