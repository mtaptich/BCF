import ogr2ogr, os

def to_shp(screenOn, screen, filein, fileout):
  """
  Note: main is expecting sys.argv, where the first argument is the script name
  so, the argument indices in the array need to be offset by 1

  This can be used to prune larger shapefiles into smaller files 

  ======================
  EXAMPLE: 
  to_shp(["", "ogr2ogr", "-f", "ESRI Shapefile", "-where", "state='California'", "CA_roads_10m.shp" "ne_10m_roads_north_america.shp" ])
  """
  if(screenOn):
  	query = ["", "-f", "ESRI Shapefile", "-where", screen, fileout, filein]
  else:
  	query = ["", "-f", "ESRI Shapefile", fileout, filein]
  ogr2ogr.main(query)

def to_json(screenOn, screen, filein, fileout):
  """
  Note: main is expecting sys.argv, where the first argument is the script name
  so, the argument indices in the array need to be offset by 1

  This can be used to prune larger shapefiles into smaller files 

  ======================
  EXAMPLE: 
  to_json(["", "ogr2ogr", "-f", "GeoJSON", "-t_srs", "'EPSG:4326'","-where", "state='California'", "CA_roads_10m.shp" "ne_10m_roads_north_america.shp" ])
  """
  if(screenOn):
    query = ["", "-f", "GeoJSON", "-t_srs", "EPSG:4326","-where", screen, fileout, filein]
  else:
    query = ["", "-f", "GeoJSON", "-t_srs", "EPSG:4326", fileout, filein]
  ogr2ogr.main(query)

def to_CSV(screenOn, screen, filein, fileout):
  """
  Note: main is expecting sys.argv, where the first argument is the script name
  so, the argument indices in the array need to be offset by 1

  This can be used to prune larger shapefiles into smaller files 

  ======================
  ogr2ogr -f CSV  precip_20140107.csv  nws_precip_1day_observed_20140107.shp -lco GEOMETRY=AS_XYZ
  """
  if(screenOn):
    query = ["", "-f", "CSV", "-where", screen, fileout, filein,  "-lco", "GEOMETRY=AS_XYZ","-skipfailures", "-overwrite"]
  else:
    query = ["", "-f", "CSV", fileout, filein, "-lco", "GEOMETRY=AS_XYZ"]
  ogr2ogr.main(query)

def to_topojosn(idproperty, subproperty, filein, fileout):
  query = """
  topojson \
    --id-property %(idproperty)s \
    -p %(subproperty)s \
    -o %(fileout)s \
    %(filein)s
    """
  query = query % {"idproperty": idproperty, "subproperty": subproperty, "filein": filein, "fileout": fileout}
  os.system(query)


