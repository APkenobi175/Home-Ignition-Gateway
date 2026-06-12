def getStuff():
	query = """
	select * from core_session
	"""
	args = []
	
	data = system.db.runPrepQuery(query, args, "astrophoto_user")
	
	return data
	
def writeStuff():
	stuff = getStuff()
	
	system.tag.writeBlocking(["[default]Sessions"], [stuff])