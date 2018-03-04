from flask import Flask, flash, redirect, render_template, request, session, abort
import sys, os
sys.path.append(os.getcwd() + '/audio-reactive-led-strip/python/')#append entire directory
import logging
import multiprocessing
import light_control, visualization

app = Flask(__name__)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
global stop 
stop = False
p = multiprocessing.Process()

def terminate_process():
	global p
	if p.is_alive():
		p.terminate()
def loop_rainbow_cycle_successive(name):
	global stop
	while 1:
		if stop == True:
			break
		light_control.rainbow_cycle_successive()

def loop_rainbow_cycle(name):
	global stop
	while 1:
		if stop == True:
			break
		light_control.rainbow_cycle()

def loop_rainbow_colors(name):
	global stop
	while 1:
		if stop == True:
			break
		light_control.rainbow_colors()
def loop_visualization(name, effect):
	if effect == "visualize_energy":
		visualization.visualization_effect = visualization.visualize_energy
	elif effect == "visualize_scroll":
		visualization.visualization_effect = visualization.visualize_scroll
	elif effect == "visualize_spectrum":
		visualization.visualization_effect = visualization.visualize_spectrum
	else:
		visualization.visualization_effect = visualization.visualize_spectrum

	# Initialize LEDs
	visualization.led.update()
	# Start listening to live audio stream
	visualization.microphone.start_stream(visualization.microphone_update)
	
RGB = ()
@app.route("/")
def index():
     return render_template(
        'index.html')
@app.route("/getColor/", methods=['POST'])
def getColor():
	terminate_process()
	RGB = (request.form['r'],request.form['g'],request.form['b'])
	light_control.setColor(RGB)
	return render_template('index.html')
@app.route("/useFunction/", methods=['POST'])
def useFunction():
	global stop
	global p
	stop = False
	func = request.form['function']
	if func == "rainbow_cycle_successive":
		terminate_process()
		p = multiprocessing.Process(target=loop_rainbow_cycle_successive, args=("loop_rainbow_cycle_successive", ))
		p.start()
		
	elif func == "rainbow_cycle":
		terminate_process()
		p = multiprocessing.Process(target=loop_rainbow_cycle, args=("loop_rainbow_cycle", ))
		p.start()
		
	elif func == "rainbow_colors":
		terminate_process()
		p = multiprocessing.Process(target=loop_rainbow_colors, args=("loop_rainbow_cycle", ))
		p.start()
	elif func == "visualization":
		terminate_process()
		effect = request.form['visualization_effect']
		p = multiprocessing.Process(target=loop_visualization, args=("loop_visualization", effect ))
		p.start()
	elif func == "inc_brightness":
		light_control.increaseBrightness()
	elif func == "dec_brightness":
		light_control.decreaseBrightness()
	elif func == "STOP":
		stop = True
		terminate_process()
		light_control.clear_pixels()

	return render_template('index.html')
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
