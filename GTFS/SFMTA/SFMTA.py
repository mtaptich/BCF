import os, sys, csv
lib_path = os.path.abspath('../../scripts')
sys.path.append(lib_path)
import route2topo

def makeroute(routeid):
	try:
		newpath = "Output/"+str(routeid)
		if not os.path.exists(newpath): os.makedirs(newpath)
		try:
		    os.remove("Output/"+str(routeid)+"/sfmta.json")
		except OSError:
		    pass

		route2topo.to_json(True, "LINE_NAME='"+str(routeid)+"'", "../../data/SFMTA/shapefiles/sfmtaPublicRoutesMarchSignUp2012.shp", "Output/"+str(routeid)+"/sfmta.json")
		route2topo.to_topojosn("SERVICENAM", "PREDOMINAN","Output/"+str(routeid)+"/sfmta.json","Output/"+str(routeid)+"/"+str(routeid)+"_sfmtaTOPO.json")
		makeHTML(routeid)
	except:
		print "Failed to create file for: "+str(routeid)

def makeHTML(routeid):
	template = "../../data/SFMTA/HTML/SFMTA_blank.html"
	fileout = "Output/"+str(routeid)+"/index.html";
	temp = open(template).read();
	topo = str(routeid)+"_sfmtaTOPO.json"
	temp = temp%topo
	html_file = open(fileout, 'w')
	html_file.write(temp);
	html_file.close();


routes = []
with open('../../data/SFMTA/GTFS/routes.csv', 'r') as f:
    next(f)
    reader = csv.reader(f)
    for line in reader:
    	routes.append(line[2])

filein = open("../../admin/blankhome.html", mode="r").read()
li = ""
for route in routes:
	route = route.replace(" ","")
	print route+"."
	print "..........................................\n"
	makeroute(route)
	li = li+"<li><a href='GTFS/SFMTA/Output/"+str(route)+"/index.html'>"+str(route)+"</a></li>\n"

filein = filein%li;
html_file = open("../../admin/index.html", 'w')
html_file.write(filein);
html_file.close();