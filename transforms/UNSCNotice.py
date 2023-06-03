# Required Imports
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform
import requests

class UNSCNotice(DiscoverableTransform):

	@classmethod
	def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
	
		# Obtain Target Information from Entity
		request_firstname = request.getProperty("firstname")
		if bool(request_firstname) == False:
			request_firstname = ''
			
		request_lastname = request.getProperty("lastname")
		if bool(request_lastname) == False:
			request_lastname = ''

		
		# Search for Target Information via Interpol UNSC Notice API
		red_notice_url = 'https://ws-public.interpol.int/notices/v1/un?&name=' + request_lastname + '&forename=' + request_firstname
		
		api_response = requests.get(red_notice_url)
		red_notices = api_response.json()
		red_notices = (red_notices['_embedded']['notices'])
		
		# Iterate through all returned UNSC Notices
		for i in red_notices:
		
			# Create new UNSC Notice Entity
			red_notice_entity = response.addEntity("yourorganization.InterpolUNSCNotice")
		
			# Add Properties to UNSC Notice Entity
			response_firstname = i.get("forename")
			if response_firstname:
				red_notice_entity.addProperty("firstname", value = response_firstname)
			
			response_lastname = i.get("name")
			if response_lastname:
				red_notice_entity.addProperty("lastname", value = response_lastname)
			
			response_dob = i.get("date_of_birth")
			if response_dob:
				red_notice_entity.addProperty("DateOfBirth", value = response_dob)
			
			response_nationality = i.get("nationalities")
			if response_nationality:
				red_notice_entity.addProperty("Nationality", value = response_nationality[0])
			
			response_photo = i['_links'].get('thumbnail')
			if response_photo:
				red_notice_entity.addProperty("PhotoURL", value = response_photo['href'])
			



