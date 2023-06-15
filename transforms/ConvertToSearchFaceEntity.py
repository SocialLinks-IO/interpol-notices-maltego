# Required Imports
from maltego_trx.maltego import MaltegoMsg, MaltegoTransform
from maltego_trx.transform import DiscoverableTransform

class ConvertToSearchFaceEntity(DiscoverableTransform):

	@classmethod
	def create_entities(cls, request: MaltegoMsg, response: MaltegoTransform):
	
		# Obtain Target Information from Entity
		request_firstname = request.getProperty("firstname")
		if bool(request_firstname) == False:
			request_firstname = ''
			
		request_lastname = request.getProperty("lastname")
		if bool(request_lastname) == False:
			request_lastname = ''

		photo_url = request.getProperty("photo") or request.getProperty("PhotoURL") or request.getProperty("URL")

		face_search = response.addEntity("maltego.SearchFace")
	
		face_search.addProperty("firstname", value = request_firstname)
		face_search.addProperty("lastname", value = request_lastname)
		face_search.addProperty("fullname", value = request_firstname + " " + request_lastname)
		face_search.addProperty("photo", value = photo_url)
		
