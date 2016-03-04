$(function()
{
	var the_json = {};
	var current_image = null;
	
	
	// jcrop
	// I did JSON.stringify(jcrop_api.tellSelect()) on a crop I liked:
	// var c = {"x":13,"y":7,"x2":487,"y2":107,"w":474,"h":100};
	
	function show_coords(c)
	{
		// $('#info').text( JSON.stringify(jcrop_api.tellSelect()) + "br" + JSON.stringify(the_json));
		// $('#info').text( JSON.stringify(the_json));
	};
	function save_coords(c)
	{
		// the_json[current_image].boxes = jcrop_api.tellSelect();
	};
	
	function clear_coords()
	{
		$('#info').text('');
	};
	
	// image looping
	$(document).on("keydown", function(e)
	{
		if (e.which == 74)
		{
			index = Math.min(current_image + 1, the_json.length-1 );
			change_current_image(index, 0)
			// console.log("up: " + index);
		}
		if (e.which == 75)
		{
			index = Math.max(current_image - 1, 0 );
			change_current_image(index, 0)
			// console.log("down: " + index);
		}
		if (e.which == 68)
		{// d - delete
			// console.log( draw_box[current_image].selection);
			// delete draw_box[current_image].selection;
			draw_box[current_image].removeShape( draw_box[current_image].selection );
		}
		// console.log(e.which);
	});
	
	// load files
	$.get( "/get_json", function( data )
	{
		the_json = $.parseJSON(data); ;
		$("#files-container").loadTemplate($("#template"), the_json);
		change_current_image(0, 500);
	});
	
	$("#save").on("click", function()
	{
		$.ajax("/save_json", {
			data : JSON.stringify(the_json),
			contentType : 'application/json',
			type : 'POST'
		});
		return false;
	});
	
	var draw_box = [];
	var image_width = 0;
	var image_height = 0;
	
	function change_current_image(image_index, selection_delay)
	{
		if (image_index != current_image)
		{
			if (!draw_box[image_index])
			{// going to new image
				var img = new Image();
				var url = the_json[image_index].file;
				img.onload = function()
				{
					console.log(this.width + 'x' + this.height);
					image_width = this.width;
					image_height = this.height;
					$("#target").height(this.height).width(this.width);
					var ctx = $("#canvas1")[0].getContext('2d');
					ctx.canvas.height = this.height;
					ctx.canvas.width = this.width;
					// $("#canvas1").height(this.height).width(this.width);
					//  imgdiv.append(this);
					
					draw_box[image_index] = new CanvasState(document.getElementById('canvas1'));
					draw_box[image_index].onChange = function ( shapes, shape )
					{
						// console.log( "updating json for image: " + image_index );
						update_json(image_index, shapes);
					}
					draw_boxes(image_index);
				}
				img.src = 'ann_img?path=' + url;
			
			
				
			} else
			{// going to old image
				
				$("#target").height(draw_box[image_index].height).width(draw_box[image_index].width);
				var ctx = $("#canvas1")[0].getContext('2d');
				ctx.canvas.height = draw_box[image_index].height;
				ctx.canvas.width = draw_box[image_index].width;
					
				draw_box[image_index].show();
				// console.log('draw_box.show: ' + image_index);
			}
			
			if (draw_box[current_image]) { draw_box[current_image].hide(); }
			
			// console.log(draw_box);
			
			$( "ul#files-container li:nth-child("+(current_image+1)+")" ).removeClass( "active" );
			
			current_image = image_index;
			$( "ul#files-container li:nth-child("+(current_image+1)+")" ).addClass( "active" );
			$("#target").attr('src', 'ann_img?path=' + the_json[current_image].file);
			
			
			
			
			// console.log( "naturalWidth" );
			// console.log( $("#target").width() );
			// console.log( $("#target").height() );
			
			if ( !jQuery.isEmptyObject( the_json[current_image].boxes ) )
			{
				var boxes = the_json[current_image].boxes;
				setTimeout(function(){ draw_boxes(boxes); }, selection_delay);
			} 
		}
			
	}
	
	function update_json(index, shapes)
	{
		the_json[index].boxes = [];
		$.each(shapes, function( index2, value )
		{
			the_json[index].boxes.push( {'x': value.x, 'y': value.y, 'x2': value.x+value.w, 'y2': value.y+value.h, 'w': value.w, 'h': value.h, } );
		});
		
		// $("#info").text( JSON.stringify(the_json) );
	}
	
	function draw_boxes(image_index)
	{
		var boxes = the_json[image_index].boxes;
		$.each(boxes, function( index, value )
		{
			draw_box[image_index].addShape(new Shape(draw_box[image_index], value.x, value.y, value.w, value.h, 'rgba(150,150,250,0.7)'));
		});
	}
});

$(document).foundation();