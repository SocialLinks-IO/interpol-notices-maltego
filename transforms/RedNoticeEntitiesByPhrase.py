# Required Imports
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform
from .common import *

class RedNoticeEntitiesByPhrase(DiscoverableTransform):

	@classmethod
	def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
	
		# Obtain Target Information from Entity
		request_phrase = request.getProperty("text")
		if bool(request_phrase) == False:
			request_phrase = ''
			
		# Search for Target Information via Interpol Red Notice API
		url = 'https://ws-public.interpol.int/notices/v1/red?&freeText=' + request_phrase

		api_response = requests.get(url)
		notices = api_response.json()
		notices = (notices['_embedded']['notices'])
		
		# Iterate through all returned Red Notices
		for notice_data in notices:
			notice_entity = response.addEntity("yourorganization.InterpolRedNotice")
			create_notice_entity(notice_entity, notice_data)
