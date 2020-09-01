// JavaScript Document

	(function($) {
		"use strict";
	
	
	$(document).ready(function() {

	$('.demo-1').percentcircle();

	$('.demo-2').percentcircle({
	animate : false,
	diameter : 100,
	guage: 3,
	coverBg: '#fff',
	bgColor: '#efefef',
	fillColor: '#242424',
	percentSize: '15px',
	percentWeight: 'normal'
	});

	$('.demo-3').percentcircle({
	animate : false,
	diameter : 100,
	guage: 3,
	coverBg: '#fff',
	bgColor: '#efefef',
	fillColor: '#DA4453',
	percentSize: '18px',
	percentWeight: 'normal'
	});
	$('.demo-4').percentcircle({
	animate : true,
	diameter : 100,
	guage: 3,
	coverBg: '#fd602c',
	bgColor: '#666666',
	fillColor: '#fd602c',
	percentSize: '18px',
	percentWeight: 'normal'
	});		
	$('.demo-5').percentcircle({
	animate : true,
	diameter : 100,
	guage: 3,
	coverBg: '#fff',
	bgColor: '#fff',
	fillColor: '#fd602c',
	percentSize: '18px',
	percentWeight: '20px'
	});	
	$('.demo-6').percentcircle({
	animate : true,
	diameter : 100,
	guage: 10,
	coverBg: '#fff',
	bgColor: '#efefef',
	fillColor: '#D870A9',
	percentSize: '18px',
	percentWeight: 'normal'
	});	

	
	
	
	
	
	
		});
	
	})(jQuery);