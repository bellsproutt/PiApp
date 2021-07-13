import kivy
kivy.require('2.0.0')

import datetime

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.properties import BooleanProperty, StringProperty
from kivy.clock import Clock

from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'width', '320')
Config.set('graphics', 'height', '240')



class MainTimerScreen(Screen):
	# Show main page and start main timer
	# button to pause then continue
	# button to go back
	# button to start break (maybe?)
	hours = StringProperty()
	minutes = StringProperty()
	seconds = StringProperty()
	running = False

	time_now = datetime.datetime.now()
	time_total = time_now + datetime.timedelta(seconds=1,hours=1)
	# (days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)¶

	# -------------------------------------------------

	def show_timer(self, *args):
		self.update()
		self.stop()

	def stop(self):
		if self.running:
			self.running = False
			Clock.unschedule(self.update) 
	
	def start(self):
		if not self.running:
			self.running = True
			Clock.schedule_interval(self.update, 0.05)


	def go(self):
		self.time_now = self.get_time_now()
		self.get_new_total_time()
		self.update()
		self.start()

	def reset(self, *args):
		self.time_now = self.get_time_now()
		self.get_new_total_time()
		self.update()
		self.stop()

	def start_stop_toggle(self):
		if self.running: # if running, stop
			self.stop()
		else: # if not running, start
			self.start()

	# 2021-07-13 13:23:12.739335
	def update(self, *kwargs):
		time = self.time_total - datetime.datetime.now()
		self.hours, self.minutes, seconds = str(time).split(":")[0:]
		self.seconds = seconds[:2]

		if int(self.hours) == 0:
			if int(self.minutes) == 0:
				if int(self.seconds.split(".")[0]) == 0:
					if int(self.seconds.split(".")[1]) < 20:
						self.seconds = "00.00"
						self.button.background_color = (1, 0, 0, 1)
						self.stop()



	def get_time_now(self):
		return datetime.datetime.now()

	def get_new_total_time(self):
		self.time_total = self.time_now + datetime.timedelta(seconds=1,hours=1)
		return self.time_total


	#def get_final_time(self):
	#	self.time_total = datetime.datetime.now() + datetime.timedelta(seconds=1,hours=1)
	#	return self.time_total



	
class MainBreakScreen(Screen):
	hours = StringProperty()
	minutes = StringProperty()
	seconds = StringProperty()
	running = False

	time_now = datetime.datetime.now()
	time_total = time_now + datetime.timedelta(seconds=1,minutes=10)
	# (days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)¶

	# -------------------------------------------------

	def show_timer(self, *args):
		self.update()
		self.stop()

	def stop(self):
		if self.running:
			self.running = False
			Clock.unschedule(self.update) 
	
	def start(self):
		if not self.running:
			self.running = True
			Clock.schedule_interval(self.update, 0.05)


	def go(self):
		self.time_now = self.get_time_now()
		self.get_new_total_time()
		self.update()
		self.start()

	def reset(self, *args):
		self.time_now = self.get_time_now()
		self.get_new_total_time()
		self.update()
		self.stop()

	def start_stop_toggle(self):
		if self.running: # if running, stop
			self.stop()
		else: # if not running, start
			self.start()

	# 2021-07-13 13:23:12.739335
	def update(self, *kwargs):
		time = self.time_total - datetime.datetime.now()
		self.hours, self.minutes, seconds = str(time).split(":")[0:]
		self.seconds = seconds[:2]

		if int(self.hours) == 0:
			if int(self.minutes) == 0:
				if int(self.seconds.split(".")[0]) == 0:
					if int(self.seconds.split(".")[1]) < 20:
						self.seconds = "00.00"
						self.button.background_color = (1, 0, 0, 1)
						self.stop()



	def get_time_now(self):
		return datetime.datetime.now()

	def get_new_total_time(self):
		self.time_total = self.time_now + datetime.timedelta(seconds=1,minutes=10)
		return self.time_total

class EditTimerScreen(Screen):
	pass
class EditBreakScreen(Screen):
	pass

class Interface(Screen):
	mainTimerScreen = MainTimerScreen()





class PiApp(App):
	def build(self):
		#Window.clearcolor = (1, 1, 1, 1)
		screen_manager = ScreenManager()
		screen_manager.add_widget(Interface(name="interface"))
		screen_manager.add_widget(MainTimerScreen(name="main_timer_screen"))
		screen_manager.add_widget(MainBreakScreen(name="main_break_screen"))
		screen_manager.add_widget(EditTimerScreen(name="edit_timer_screen"))
		screen_manager.add_widget(EditBreakScreen(name="edit_break_screen"))
		return screen_manager

		


	

		


if __name__ == "__main__":
	PiApp().run()