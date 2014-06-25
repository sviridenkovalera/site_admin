from django.test import TestCase
from models.py import BlogRecord
# Create your tests here.

#add new record

def main ():
	print ( "Add new record" )
	new_record = BlogRecord ()
	new_record.title = u"init record"
	new_record.content = u"init_content"
	new_record.save ()

if __name__ == "__main__":
	main ()
