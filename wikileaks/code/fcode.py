import codecs 
import re
fi=codecs.open('final.csv', 'r', encoding='utf-8')
fi2=codecs.open('output.txt', 'w', encoding='utf-8')
fg=fi.read()
fi.close()
fg=fg.replace('\\"',"%QUOTES%")
fg=fg.replace("\\'","%SINGLEQUOTES%")
fg=fg.replace('","',"%colseparator%")
fg=fg.replace('"\r\n"',"%lineseparator%")
fg=fg.split("%lineseparator%")
for recordindex,record in enumerate(fg):
#	if recordindex>=0:
#		output='output'+str(recordindex+2)
#		fi=codecs.open(output, 'w', encoding='utf-8')
#		fi.write(record)
#		fi.close
	record2=record.split("%colseparator%")
	for index,j in enumerate(record2):	
		if(index==6):
			temporary=j
			temporary1=temporary.split("\n")
			#print(temporary[1])
			fromembassy=temporary1[1]
			fmembassy0=fromembassy.split(" ")
			temporary2=temporary.split("\n")
			toembassy=temporary2[2]
			toembassy0=toembassy.split(" ")
			#fmembassy0=fmembassy0[2]
			originembassy=fmembassy0[2]
			#print(originembassy)
			#targetembassy=toembassy0[2]
			toembassy0=toembassy0[2]
			targetembassy=toembassy0
			output2=originembassy+'2'
			output=output2+targetembassy
			fi=codecs.open(output, 'a+', encoding='utf-8')
			record=record.replace("%SINGLEQUOTES%","\\'")
			record=record.replace("%QUOTES%",'\\"')
			record=record.replace("%colseparator%",'","')
			fi.write('\n'+'"'+record+'"')
			fi.close
			print('from'+originembassy)
			print('target'+targetembassy)
