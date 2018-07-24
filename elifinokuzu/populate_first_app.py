import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'elifinokuzu.settings')

import django
django.setup()

## FAKE POPULATE SCRIPT
import random
from faker import Faker

fakegen = Faker()
topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']

def add_topic():  #topic modeline veri giriyor
	t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
	t.save()
	return t

def populate(N=5):	#topic modelindeki veriyi alarak ForeignKey olarak kullaniyor
	for entry in range(N):

		#GET THE TOPIC FOR THE ENTRY
		top = add_topic()

		#CREATE THE FAKE DATA FOR THAT ENTRY
		fake_url = fakegen.url()
		fake_date = fakegen.date()
		fake_name = fakegen.company()
		fake_idea = fakegen.job()

		#CREATE THE NEW WEBPAGE ENTRY
		webpg = Webpage.objects.get_or_create(topic=top, url=fake_url,
								topic_idea=fake_idea, name=fake_name)[0]

		#CREATE A FAKE ACCESS RECORD FOR THAT WEBPAGE
		acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
	print("Populating script!")
	populate(25)
	print("Populating complete")
