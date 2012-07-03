# coding:utf-8
from Tkinter import *
import time
import analyzer

#value_entered=StringVar()


class Application(Frame):
	def __init__(self,master=None):
		Frame.__init__(self,master)
		self.grid()
		self.value_entered=StringVar()
		self.result_display=StringVar()
		self.creatWidgets()

	def get_stat(self):
		target_url=self.value_entered.get()
		print 'entered url:'+target_url
		stat=analyzer.szpl_ana(target_url)
		print stat
		string_to_display='result:\n'
		for item in stat.keys():
			string_to_display+=item+':'+str(stat[item])+'\n'
		string_to_display+='\n'
		string_to_display+='{:.2%}'.format(stat['sold']['total']*1.0/stat['total'])+' sold'+'\n'
		string_to_display+='{:.2%}'.format((stat['sold']['total']+stat['signed']['total']+stat['pre_signed']['total'])*1.0/stat['total'])+'% signed&sold'+'\n'
		self.result_display.set(string_to_display)

		backup_file=open('./saved_data.txt','w')
		backup_file.write(time.asctime(time.localtime())+'\n')
		backup_file.write('target_url:'+target_url+'\n')
		backup_file.write(string_to_display)
		backup_file.close()


	def creatWidgets(self):
		self.quitButton=Button(self,text='quit',command=self.quit)
		self.quitButton.grid(column=2,row=2)

		self.valueEntry=Entry(self,width=70,textvariable=self.value_entered)
		self.valueEntry.grid(column=1,row=1)

		self.funButton=Button(self,text='get info',command=self.get_stat)
		self.funButton.grid(column=2,row=1)

		self.outputLabel=Label(self,height=10,width=70,justify=LEFT,textvariable=self.result_display)
		self.outputLabel.grid(column=1,row=2)


print '\n---+++   web page analyzer   +++---\n'
app=Application()
app.master.title("sz pl ris analyzer")
app.mainloop()
print '\n--++   exit   ++--\n'

