## Define the functions used in mapping the dataset of ACMAA
## To avoid having the same function name in different python script files, each function here adds a prefix with "ac_". 
## By Chao on 05-08-2014@ISI 


def ac_objectUri():
	return "object/" + getValue("Accession Number")

def ac_objectIdentifierUri():
	return "object/" + getValue("Accession Number") + "/regno"


def ac_imageUri():
#	return ac_objectUri() + "/image"
	imgFile = getValue("Image File")
	if imgFile:
		nPos1 = imgFile.index("_")	
		nPos2 = imgFile.index(".tif")	
		if nPos1 > 0:
			if nPos2 > 0:
				return "http://www.cartermuseum.org/sites/all/files/styles/artwork_full/public/images/" + imgFile[(nPos1 + 1):nPos2] + "_s_0.jpg"

def ac_imageIdentifierUri():
	return ac_imageUri() + "/identifier"

def ac_titleUri():
        return ac_objectUri() + "/title"

def ac_objectTypeUri():
#	return "thesauri/objecttype/" + getValue("Object Type").lower().replace(' ','_')
	if getValue("Object Type"):
		return "thesauri/classification/"+getValue("Object Type").lower().replace(" ","-")
	else:
		return ""

# return person's URI, if person name includes 'unknown', plus the regno of the related object
def ac_creatorUri():
	personName = getValue("Creator Name").lower()
	if "unknown" in personName:
		return "person-institution/" + personName.replace(' ', '_') + '_' + getValue("Accession Number")
	else:
		return "person-institution/" + personName.replace(' ', '_')

def ac_creatorFirstName():
	personName = getValue("Creator Name")
	if personName:
		iPos = personName.index(" ")
		if (iPos > 0):
			return personName[0:iPos]
		else:
			return personName

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
  		return "thesauri/nationality/" + getValue("Creator Nationality").replace(' ','_')

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
		p = val.lower().replace(' ','_').replace(',','')
  		return "thesauri/place/" + placeType.lower() + "/" + p

def ac_placeAppellationUri(columnName, placeType):
	val = ac_placeUri(columnName, placeType)
	if val:
  		return val + "/appellation"

def ac_creatorBirthPlaceUri():
	val = getValue("Creator Birth Place")
	if val:
  		return "thesauri/place/birth/" + val.lower().replace(' ', '_').replace(',','')

def ac_creatorBirthPlaceAppeUri():
#	val = ac_creatorBirthPlaceUri()
#	if val:
 # 		return val + "/appellation"
	val = getValue("Creator Birth Place")
	if val:
		return "thesauri/placetype/City"

def ac_creatorDeathPlaceUri():
	val = getValue("Creator Death Place")
	if val:
  		return "thesauri/place/" + val.lower().replace(' ', '_').replace(',','')

def ac_creatorDeathPlaceAppeUri():
#	val = ac_creatorDeathPlaceUri()
#	if val:
#		return val + "/appellation"
	val = getValue("Creator Death Place")
	if val:
		return "thesauri/placetype/City"

def ac_bibliographyUri():
	return "bibliography/" + getValue("Accession Number")

def ac_publicationUri():
	return ac_bibliographyUri() + "/publication"

def ac_publicationDateUri():
#	return ac_bibliographyUri() + "/publication/date"
	return ac_productionUri() + "/date"

# split the Credit Line column with character ", Texas" to two columns: legalBodyInfo and acquisitionInfo
def ac_legalBodyInfo():
	val = getValue("Credit Line")
	nPos = val.index(", Texas")	
	if nPos == 0:
		return val
	else:
		return val[0:nPos + 7]

def ac_acquisitionInfo():
	val = getValue("Credit Line")
	nPos = val.index(", Texas")	
	if nPos == 0:
		return ""
	else:
		return val[nPos + 9: 1000].lstrip().rstrip()

def ac_legalBodyUri():
#	if getValue("LegalBodyInfo"):
#		return ac_objectUri() + "/creditline"
	return "http://collection.cartermuseum.org/id/the-amon-carter-museum-of-american-art"

def ac_acquisitionUri():
	if getValue("AcquisitionInfo"):
		return ac_objectUri() + "/acquisition"

def ac_copyrightUri():
	if getValue("Copyright"):
		return ac_objectUri() + "/copyright"

def ac_materialUri():
	val = getValue("Medium")
	if val:
		return "thesauri/material/" + val.lower().replace(" ", "_")

def ac_singleKeyword():
	val = getValue("Values")
	if val:
		return val

def ac_subjectKeywordsUri():
	val = getValue("Values").lstrip().rstrip()
	if val:
		return "thesauri/subjectkeyword/" + val.lower().replace(" ", "_")

def ac_informationUri():
	val = getValue("Values")
	if val:
		return ac_objectUri() + "/concept"

def ac_dimensionHeightUri():
	val = getValue("Measurement Height")
	if getValue("Measurement Units"):
		unit = getValue("Measurement Units")
	else:
		unit = ""
	if val:
		if val.lower().find("in")>=0:
			return ac_objectUri() + "/dimension/height/in"
		else:
			return ac_objectUri() + "/dimension/height/cm"


def ac_measureUnitUri():
	val = getValue("Measurement Units")
	if val:
#		if val.lower().strip() == "cm":
		if val.lower().find("cm")>=0:
			return "http://qudt.org/vocab/unit#Centimeter"
		elif val.lower().strip() == "m":
			return "http://qudt.org/vocab/unit#Meter"
		elif val.lower().strip() == "foot":
			return "http://qudt.org/vocab/unit#Foot"
#		elif val.lower().strip() == "inch":
		if val.lower().find("in")>=0:
			return "http://qudt.org/vocab/unit#Inch"

def ac_measureHeightTypeUri():
	val = getValue("Measurement Height")
	if val:
		return "thesauri/dimension/height"
def ac_measureHeightTypeLabel():
	return "Height"

def ac_dimensionWidthUri():
	val = getValue("Measurement Width")
	if getValue("Measurement Units"):
		unit = getValue("Measurement Units")
	else:
		unit = ""
	if val:
		if val.lower().find("in")>=0:
			return ac_objectUri() + "/dimension/width/in"
		else:
			return ac_objectUri() + "/dimension/width/cm"

def ac_measureWidthTypeUri():
	val = getValue("Measurement Width")
	if val:
		return "thesauri/dimension/width"
def ac_measureWidthTypeLabel():
	return "Width"

def ac_dimensionDepthUri():
	val = getValue("Measurement Depth")
	if getValue("Measurement Units"):
		unit = getValue("Measurement Units")
	else:
		unit = ""
	if val:
		if val.lower().find("in")>=0:
			return ac_objectUri() + "/dimension/depth/in"
		else:
			return ac_objectUri() + "/dimension/depth/cm"

def ac_measureDepthTypeUri():
	val = getValue("Measurement Depth")
	if val:
		return "thesauri/dimension/depth"
def ac_measureDepthTypeLabel():
	return "Depth"

def ac_relatedObjectUri():
	val = getValue("Related Object ID")
	if val:
		return "object/" + val

def ac_relatedObjectIdentifierUri():
	val = getValue("Related Object ID")
	if val:
		return "object/" + val + "/regno"

def ac_objectRelationshipUri():
	val = getValue("Related Object Relationship Type")
	if val:
		return "thesauri/objectrelationshiptype/" + val.lower()

