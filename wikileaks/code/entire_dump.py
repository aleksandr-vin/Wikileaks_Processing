import codecs 
import re
fi=codecs.open('please', 'r', encoding='utf-8')
fi2=codecs.open('output.txt', 'w', encoding='utf-8')
fg=fi.read()
fi.close()
fg=fg.replace('\\"',"%QUOTES%")
fg=fg.replace("\\'","%SINGLEQUOTES%")
fg=fg.replace('","',"%colseparator%")
fg=fg.replace('"\r\n"',"%lineseparator%")
fg=fg.split("#lineseparator#")
for recordindex,record in enumerate(fg):
	print(str(recordindex)+record)
	if recordindex>=1:
		
	#	print()"
		#print("helli")
#		output='output'+str(recordindex+2)
#		fi=codecs.open(output, 'w', encoding='utf-8')
#		fi.write(record)
#		fi.close
		record2=record.split("%colseparator%")
		for index,j in enumerate(record2):	
			if index==3:
				print(record)
				fi=codecs.open('/home/hp/Downloads/nlp_phase1/iitd_nlp/oct28/output_json/'+j, 'a+', encoding='utf-8')
				record=record.replace("%SINGLEQUOTES%","\\'")
				record=record.replace("%QUOTES%",'\\"')
				record=record.replace("%colseparator%",'","')
				fi.write('\n'+'"'+record+'"')
				fi.close
#		if(index==6):
#			temporary=j
#			temporary1=temporary.split("\n")
#			fromembassy=temporary1[1]
#			fmembassy0=fromembassy.split(" ")
#			temporary2=temporary.split("\n")
#			toembassy=temporary2[2]
#			toembassy0=toembassy.split(" ")
#			originembassy=fmembassy0[2]
#			toembassy0=toembassy0[2]
#			targetembassy=toembassy0
#			output=originembassy+'2'+targetembassy
#			fi=codecs.open(output, 'a+', encoding='utf-8')
#			record=record.replace("%SINGLEQUOTES%","\\'")
#			record=record.replace("%QUOTES%",'\\"')
#			record=record.replace("%colseparator%",'","')
#			fi.write('\n'+'"'+record+'"')
#			fi.close
#			print('from'+originembassy)
#			print('target'+targetembassy)

