# ann.py - simple python annotation tool 

I needed a simple customizable multi rectangle annotation tool. Rectangles are movable and resizable.

The code is in ALPHA: ugly, but working!

![ann.py](https://raw.githubusercontent.com/magveda/ann.py/master/img/ann.png "python annotation tool example")

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
	            { "h": 70, "w": 145, "x": 786, "x2": 931, "y": 650, "y2": 720 }
	        ],
	        "file": "/vision/lab/datasets/image1.jpg"
	    },
	    {
	        "boxes": [
	            { "h": 52, "w": 97, "x": 180, "x2": 277, "y": 621, "y2": 673 },
	            { "h": 86, "w": 174, "x": 834, "x2": 1008, "y": 735, "y2": 821 }
	        ],
	        "file": "/vision/lab/datasets/image2.jpg"
	    }
	]
```
## Dependencies

On Centos 7:

```bash
	pip install Flask
	pip install argparse
	yum install -y python-lxml
```

## Changelog

<!-- https://github.com/olivierlacan/keep-a-changelog -->

* 2017-01-24
 * `fixed` issues with browser caching - addded `no-cache` headers and other fixes
* 2016-03-02
 * `added` feature: if provided json file for creation already exists, the script only appends new files if found
 * `added` feature: the script creates `XML` file with the same name, that is compatible for using with [`dlib`](https://github.com/davisking/dlib)
 * `fixed` image resizing when going back with key `k`
* 2016-03-01
 * `added` icon "move", when hovering selected feature

## TODO

### GUI

* Add aspect ratio functionality

<!-- ### CLI

* Add option to append new image files to existing json list:
 * `python ann.py -i ../../datasets/sareme/20140429 -a sareme.json`
* Add only unique images to the list
* Add option to save in dlib compatible XML format -->
