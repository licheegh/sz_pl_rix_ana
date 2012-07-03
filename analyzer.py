# coding:utf-8
import urllib2
import re


def find_target_line(data):
	for line in data:
		if 'housedetail' in line:
			#print line[0:200]
			break
	return line

def abstract_string(string):

	#patterns_erase=['\t',' ','</div>']
	#patterns_erase=['\t',' ','</div>',"</td><tdheight='68'width='140'bgcolor='#EFF6FB'>"]
	key_word_ceng='\xB2\xE3'
	key_word_fang='\xB7\xBF'
	pic_sold='b2.gif'
	pic_under_sale='b1_2.gif'
	pic_pre_signed='b10.gif'
	pic_signed='b3.gif'
	pic_locked='bz1.gif'

	sale_stat={'total':0,'sold':{'total':0},'under_sale':{'total':0},'pre_signed':{'total':0},'signed':{'total':0},'locked':{'total':0}}

	#for pattern in patterns_erase:
		#string=string.replace(pattern,'')
	#data_list=string.split("<divalign=")
	data_list=re.split('\<div align=.center.>',string)

	item_plus_one=''
	for i in range(len(data_list)):
		if key_word_fang in data_list[i]:

			sale_stat['total']+=1

			room=re.findall('\d\w</div>',data_list[i])
			if len(room) is 0:room='unknown'
			else:room=room[0].replace('</div>','')	#get room cat.

			if pic_sold in data_list[i+1]:
				item_plus_one='sold'
			elif pic_under_sale in data_list[i+1]:
				item_plus_one='under_sale'
			elif pic_pre_signed in data_list[i+1]:
				item_plus_one='pre_signed'
			elif pic_signed in data_list[i+1]:
				item_plus_one='signed'
			elif pic_locked in data_list[i+1]:
				item_plus_one='locked'

			if item_plus_one is not '':
				sale_stat[item_plus_one]['total']+=1
				if not sale_stat[item_plus_one].has_key(room):
					sale_stat[item_plus_one][room]=0
				sale_stat[item_plus_one][room]+=1
				item_plus_one=''
			
	#print ord(data_list[2][0])
	#print ord(data_list[2][1])
	#for item in data_list[0:10]:print item
	#sale_stat['data_list']=data_list
	return sale_stat

def szpl_ana(target_url):
	print 'target url:'+target_url
	#sale_stat={'total':1,'sold':2,'under_sale':3,'pre_signed':4,'signed':5,'locked':6}
	try:
		data=urllib2.urlopen(target_url)
	except urllib2.URLError:
		print 'url error'
	else:
		target_line=find_target_line(data)
		sale_stat=abstract_string(target_line)
		#del sale_stat['data_list']
	return sale_stat



if __name__ == '__main__':
	target_url='file:///F:/web_page_ana/proj.htm'
	print '\n---+++   web page analyzer   +++---\n'
	print 'target_url:'+target_url+'\n'

	#target_url='http://ris.szpl.gov.cn/bol/building.aspx?id=16540&Branch=B&isBlock=ys'
	try:
		data=urllib2.urlopen(target_url)
	except urllib2.URLError:
		print 'url error'
	else:
		#print data.info()
		target_line=find_target_line(data)
		print 'data readed sample:'+target_line[0:300]
		print '\nlength of line:'+str(len(target_line)/1024)+'kb'
		sale_stat=abstract_string(target_line)
		#target_list=sale_stat['data_list']
		#del sale_stat['data_list']
		print '\nstring abstracted:'
		#for d in target_list[0:10]:print d
		print sale_stat
		#print str(sale_stat['sold']*100/sale_stat['total'])+'% sold'
		#print str((sale_stat['sold']+sale_stat['signed']+sale_stat['pre_signed'])*100/sale_stat['total'])+'% signed&sold'

	#print line.decode('utf-8','ignore')
	print '\n--++   exit   ++--\n'

