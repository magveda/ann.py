# ann.py - simple python annotation tool 

The idea was to have customizable multi rectangle annotation tool. Rectangles are movable and resizable.

The code is in ALPHA: ugly, but working!

<!-- ![ann.py]( "python annotation tool example") -->

## Usage

Let's assume you have a folder of images called `dataset/images/`. These images should contain examples of the objects you want to learn to detect.  You can use the ann.py tool to label these objects.

This will create a file called `annotations.json` which simply lists the images in `dataset/images/`:

* `python ann.py -i dataset/images/ -c ../annotations.json`

To annotate them run:

* `python ann.py -e ../annotations.json`

Now you can open browser http://192.168.1.163:5000/ (change IP). Window will appear showing all the images.

You can move between images using `j` and `k` keys.

To create new rectangle - double click on the image. To delete a rectangle - select it with mouse and press `d`.

Example annotations.json file:

```json
	[
	    {
	        "boxes": [
	            {
	                "h": 70,
	                "w": 145,
	                "x": 786,
	                "x2": 931,
	                "y": 650,
	                "y2": 720
	            }
	        ],
	        "file": "/vision/lab/datasets/image1.jpg"
	    },
	    {
	        "boxes": [
	            {
	                "h": 52,
	                "w": 97,
	                "x": 180,
	                "x2": 277,
	                "y": 621,
	                "y2": 673
	            },
	            {
	                "h": 86,
	                "w": 174,
	                "x": 834,
	                "x2": 1008,
	                "y": 735,
	                "y2": 821
	            }
	        ],
	        "file": "/vision/lab/datasets/image2.jpg"
	    }
	]
```

## TODO:

* Add option to append new image files to existing json list:
 * `python ann.py -i ../../datasets/sareme/20140429 -a sareme.json`
* Add only unique images to the list