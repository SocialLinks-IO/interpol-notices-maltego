import requests

def create_notice_entity(notice_entity, notice_data):
	response_firstname = notice_data.get("forename")
	if response_firstname:
		notice_entity.addProperty("firstname", value = response_firstname)
	
	response_lastname = notice_data.get("name")
	if response_lastname:
		notice_entity.addProperty("lastname", value = response_lastname)
	
	response_dob = notice_data.get("date_of_birth")
	if response_dob:
		notice_entity.addProperty("DateOfBirth", value = response_dob)
	
	response_nationality = notice_data.get("nationalities")
	if response_nationality:
		notice_entity.addProperty("Nationality", value = response_nationality[0])
	
	response_photo = notice_data['_links'].get('thumbnail')
	if response_photo:
		notice_entity.addProperty("PhotoURL", value = response_photo['href'])

