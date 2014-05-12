## Define the functions used in mapping the dataset of ACMAA
## To avoid having the same function name in different python script files, each function here adds a prefix with "ac_". 
## By Chao on 05-08-2014@ISI 


def ac_objectUri():
	return "object/" + getValue("Accession Number")

def ac_objectIdentifierUri():
	return "object/" + getValue("Accession Number") + "/regno"

def ac_imageUri():
	return ac_objectUri() + "/image"

def ac_imageIdentifierUri():
	return ac_imageUri() + "/identifier"

def ac_titleUri():
        return ac_objectUri() + "/title"

def ac_objectTypeUri():
	return "thesauri/objecttype/" + getValue("Object Type").lower().replace(' ','_')

# return person's URI, if person name includes 'unknown', plus the regno of the related object
def ac_creatorUri():
	personName = getValue("Creator Name").lower()
	if "unknown" in personName:
		return "person-institution/" + personName.replace(' ', '_') + '_' + getValue("Accession Number")
	else:
		return "person-institution/" + personName.replace(' ', '_')

def ac_creatorAppellationUri():
	return ac_creatorUri() + "/appellation"

def ac_productionUri():
	return ac_objectUri() + "/production"

def ac_creatorBirthUri():
	return ac_creatorUri() + "/birth"

def ac_creatorBirthDateUri():
	return ac_creatorBirthUri() + "/date"

def ac_creatorDeathUri():
	return ac_creatorUri() + "/death"

def ac_creatorDeathDateUri():
	return ac_creatorDeathUri() + "/date"

def ac_nationalityUri():
	if getValue("Creator Nationality"):
  		return "thesauri/nationality/" + getValue("Creator Nationality").lower().replace(' ','_')

def ac_genderUri():
	if getValue("Creator Gender"):
  		return "thesauri/gender/" + getValue("Creator Gender").lower()

def ac_roleUri():
	if getValue("Creator Role"):
  		return "thesauri/role/" + getValue("Creator Role").lower().replace(' ','_')

# return the Country, State, County, City of a place, the corresponding index is 0, 1, 2, 3.
# [params] string columnName: the data column name, which value usually has the ',' seperator; 
#          integer index: 0 return Country, 1 return State, 2 return County, 3 return City
def ac_place(columnName, index):
	val = getValue(columnName)
	if val:
		place = val.split(',')
		if len(place) > index:
		    return place[index]

# return the URI of a place, including the Country, State, County and City
# [params] string columnName: the data column name; 
#          string placeType: "country", "state", "county" or "city"
def ac_placeUri(columnName, placeType):
	val = getValue(columnName)
	if val:
		p = val.lower().replace(' ','_')
  		return "thesauri/place/" + placeType.lower() + "/" + p

def ac_placeAppellationUri(columnName, placeType):
	val = ac_placeUri(columnName, placeType)
	if val:
  		return val + "/appellation"

def ac_creatorDeathPlaceUri():
	val = getValue("Creator Death Place")
	if val:
  		return "thesauri/place/death/" + val.lower().replace(' ', '_')

def ac_creatorDeathPlaceAppeUri():
	val = ac_creatorDeathPlaceUri()
	if val:
  		return val + "/appellation"

















