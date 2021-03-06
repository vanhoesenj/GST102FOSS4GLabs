##Helipad Site Selection=name
##vectorlayer_countieslyr=vector
##tablefield_countynameattr=field vectorlayer_countieslyr
##vectorlayer_airportslyr=vector
##vectorlayer_cityboundarieslyr=vector
##tablefield_cityboundariesattr=field vectorlayer_cityboundarieslyr
##vectorlayer_roadslyr=vector
##tablefield_roadsattr=field vectorlayer_roadslyr
##vectorlayer_waterlyr=vector
##result_alg0=output vector
##output_alg8=output vector
##output_alg9=output vector
outputs_0=processing.runalg("qgis:extractbyattribute", vectorlayer_countieslyr, tablefield_countynameattr, 0, Nueces, result_alg0)
outputs_1=processing.runalg("qgis:clip", vectorlayer_airportslyr, outputs_0['RESULT'], None)
outputs_2=processing.runalg("qgis:extractbyattribute", vectorlayer_cityboundarieslyr, tablefield_cityboundariesattr, 0, Corpus Christi, None)
outputs_3=processing.runalg("qgis:fixeddistancebuffer", outputs_2['RESULT'], 4828.03, 5, True, None)
outputs_4=processing.runalg("qgis:difference", outputs_3['OUTPUT'], outputs_2['RESULT'], None)
outputs_5=processing.runalg("qgis:extractbyattribute", vectorlayer_roadslyr, tablefield_roadsattr, 0, C, None)
outputs_6=processing.runalg("qgis:fixeddistancebuffer", outputs_5['RESULT'], 1609.34, 5, True, None)
outputs_7=processing.runalg("qgis:fixeddistancebuffer", vectorlayer_waterlyr, 804.67, 5, True, None)
outputs_8=processing.runalg("qgis:intersection", outputs_4['OUTPUT'], outputs_6['OUTPUT'], output_alg8)
outputs_9=processing.runalg("qgis:clip", vectorlayer_airportslyr, outputs_8['OUTPUT'], output_alg9)