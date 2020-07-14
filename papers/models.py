import datetime 
from django.db import models
from django.utils.formats import get_format

def parse_date(date_str):
    """Parse date from string by DATE_INPUT_FORMATS of current language"""
    for item in get_format('DATE_INPUT_FORMATS'):
        try:
            return datetime.datetime.strptime(date_str, item).date()
        except (ValueError, TypeError) as e:
            # log e
            continue
    return None

class Paper(models.Model):
    cord_uid = models.CharField(max_length=500, blank=True, null=True)
    sha = models.CharField(max_length=500, blank=True, null=True)
    source_x = models.CharField(max_length=500, blank=True, null=True)
    title = models.CharField(max_length=500, blank=True, null=True)
    doi = models.CharField(max_length=500, blank=True, null=True)
    pmcid = models.CharField(max_length=500, blank=True, null=True)
    pubmed_id = models.CharField(max_length=500, blank=True, null=True)
    license = models.CharField(max_length=500, blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)
    # publish_time is a string respresenting a date or a year.
    publish_time = models.CharField(max_length=500,blank=True,null=True)
    authors = models.CharField(max_length=500, blank=True, null=True)
    journal = models.CharField(max_length=500, blank=True, null=True)
    # rename of the column Microsoft Academic Paper ID
    microsoft_pid = models.CharField('Microsoft Academic Paper ID', max_length=500,blank=True, null=True)
    # rename of the column WHO #Covidence
    coevidence = models.CharField('WHO #Covidence', max_length=500, blank=True, null=True)
    has_pdf_parse = models.CharField(max_length=500, blank=True, null=True)
    has_pmc_xml_parse = models.CharField(max_length=500, blank=True, null=True)
    full_text_file = models.CharField(max_length=500, blank=True, null=True)
    url = models.CharField(max_length=500,blank=True, null=True)
    # publish date is the datefied version of publish time. It is used for filtering/ordering
    publish_date = models.DateField(null=True, blank=True)

    def save(self, *args, **kwargs):
        # Cast publish_time into its datefied version publish_date
        if self.publish_time:
            if self.publish_time.isdigit():
                # the value represent a year (2004,2005). The first day of the year is set by convention
                publish_year = int(self.publish_time)
                # Avoid unfortunate mistakes. To be redifined.
                if publish_year > 1900:
                    self.publish_date = datetime.date(int(self.publish_time),1,1)
            else:
                self.publish_date = parse_date(self.publish_time)
        super().save(*args, **kwargs)
