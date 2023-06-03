# Required Imports
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform
import requests

class RedNoticeByPhraseFaceSearch(DiscoverableTransform):

	@classmethod
	def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
	
		# Obtain Target Information from Entity
		request_phrase = request.getProperty("text")
		if bool(request_phrase) == False:
			request_phrase = ''
			
		# Search for Target Information via Interpol Red Notice API
		red_notice_url = 'https://ws-public.interpol.int/notices/v1/red?&freeText=' + request_phrase
		
		api_response = requests.get(red_notice_url)
		red_notices = api_response.json()
		red_notices = (red_notices['_embedded']['notices'])
		
		# Iterate through all returned Red Notices
		for i in red_notices:

			red_notice_entity = response.addEntity("maltego.SearchFace")
		
			response_firstname = i.get("forename", '')
			if response_firstname:
				red_notice_entity.addProperty("firstname", value = response_firstname)
			
			response_lastname = i.get("name", '')
			if response_lastname:
				red_notice_entity.addProperty("lastname", value = response_lastname)
			
			red_notice_entity.addProperty("fullname", value = response_firstname + " " + response_lastname)

			# red_notice_entity.addProperty("Full Name / Alias", response_firstname + response_lastname)

			response_photo = i['_links'].get('thumbnail')
			if response_photo:
				photo_url = response_photo['href']
				photo_url_id = photo_url.split('/')[-1]
				full_photo_url_id = int(photo_url_id) -1 
				full_photo_url = photo_url.rsplit('/', 1)[0] + '/' + str(full_photo_url_id)

				red_notice_entity.addProperty("photo", value = full_photo_url)
			
