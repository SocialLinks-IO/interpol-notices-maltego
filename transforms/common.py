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
		photo_url = response_photo['href']
		# preview
		notice_entity.addProperty("PhotoURL", value = photo_url)
		# full photo
		photo_url_id = photo_url.split('/')[-1]
		full_photo_url_id = int(photo_url_id) -1
		full_photo_url = photo_url.rsplit('/', 1)[0] + '/' + str(full_photo_url_id)

		notice_entity.addProperty("photo", value = full_photo_url)
