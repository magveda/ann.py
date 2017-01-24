from flask import Flask, send_from_directory, render_template, jsonify, request
import argparse
import os.path
import json
import glob
from lxml import etree
# import cv2

# ARGUMENTS
ap = argparse.ArgumentParser(description='Image annotation tool.')
ap.add_argument("-i", "--images", required=False, help="path to images folder")
ap.add_argument("-c", "--create", required=False, help="path to json file to create")
ap.add_argument("-e", "--edit", required=False, help="path to json file to edit")
args = vars(ap.parse_args())

# FLASK APP
app = Flask(__name__)

the_json = []


if args['create']:
	json_file_path = args['create']
	
	exists = False
	
	# check if file exists
	if os.path.isfile( json_file_path ):
		print ("[WARNING] output file exists - only appending new files")
		with open( json_file_path ) as data_file:    
			the_json = json.load(data_file)
	
	for image_file in glob.glob( os.path.join(args['images'], "*") ):
	# for image_file in glob.glob( os.path.join(args['images'], "*.jpg") ):
		image_path = os.path.abspath( image_file )
		print("[INFO] Processing file: {}".format(image_path))
		
		flag = False
		for check_file in the_json:
			if check_file['file'] == image_path:
				flag = True
				break
		if not flag:
			print("[INFO] appending... " )
			the_json.append({'file': image_path, 'boxes':[]})
		
		# image = cv2.imread(image_path)
		# (h, w) = image.shape[:2]
		# the_json.append({'file': image_path, 'box':{'x': 0, 'y': 0, 'x2': w, 'y2': h, 'w': w, 'h': h}})
		# the_json.append({'file': image_path, 'boxes':[{'x':0, 'y': 0, 'x2':10, 'y2':10}]})
		
		
	# print(json.dumps(the_json, sort_keys=True, indent=4, separators=(',', ': ')))

	# Write JSON
	with open(json_file_path, 'w') as f:
		json.dump(the_json, f, sort_keys=True, indent=4, separators=(',', ': '))

else:
	print ("[INFO] http://192.168.x.x:5000/")

	@app.route("/")
	def index():
		return render_template('index.html', name=1)
		
	@app.route("/get_json")
	def get_json():
		with open(args['edit']) as data_file:    
			the_json = json.load(data_file)
		# print(json.dumps(the_json, sort_keys=True, indent=4, separators=(',', ': ')))
		return json.dumps(the_json)
		
	@app.route('/save_json', methods=['GET', 'POST'])
	def save_json():
		
		# SAVE JSON
		the_json = request.json
		# print the_json
		with open(args['edit'], 'w') as f:
			json.dump(the_json, f, sort_keys=True, indent=4, separators=(',', ': '))
		
		# SAVE XML
		dataset = etree.Element("dataset")
		images = etree.SubElement(dataset, "images")
		for annotation in the_json:
			image = etree.SubElement(images, "image", file=annotation['file'])
			if annotation['boxes']:
				for box in annotation['boxes']:
					x = int(box['x'])
					y = int(box['y'])
					w = int(box['w'])
					h = int(box['h'])
					box = etree.SubElement( image, "box", top=str(y), left=str(x), width=str(w), height=str(h) )
		tree = etree.ElementTree(dataset)
		xml_filename = os.path.splitext( args['edit'] )[0] + ".xml"
		tree.write(xml_filename, pretty_print=True)
		return "success"
		
		
		
	@app.route('/js/<path:path>')
	def send_js(path):
		return send_from_directory('js', path)

	@app.route('/css/<path:path>')
	def send_css(path):
		return send_from_directory('css', path)
		
	@app.route('/img/<path:path>')
	def send_image(path):
		return send_from_directory('img', path)
		
		
		
	@app.route('/ann_img', methods=['GET', 'POST'])
	def send_ann_img():
		the_path = request.args['path']
		print ("[INFO] requested image file: {}".format(the_path))
		
		(path, file) = os.path.split(the_path)
		# print path, file
		# response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
		# response.headers['Pragma'] = 'no-cache'

		return send_from_directory(path, file)

	@app.after_request
	def add_header(response):
		response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
		response.headers['Pragma'] = 'no-cache'
		return response


	if __name__ == "__main__":
		app.run(debug=True, host= '0.0.0.0')