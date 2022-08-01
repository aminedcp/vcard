/*
Template Name: Mentoring - Bootstrap HTML Mobile Template
Author: Dreamguy's Technologies
Version: 1.1
*/

"use strict";

//Sidebar menu
$('header .left .hamburgar-icon').on('click', function(e) {
	e.preventDefault();
	$('.side-menu').addClass('show-menu');
	$('body').addClass('overlay-body');
});
$('.side-menu .close-btn').on('click', function(e) {
	e.preventDefault();
	$('.side-menu').removeClass('show-menu');
	$('body').removeClass('overlay-body');
});

//Sticky Header
$(window).scroll(function(){
  var sticky = $('header'),
      scroll = $(window).scrollTop();

  if (scroll >= 50) sticky.addClass('fixed');
  else sticky.removeClass('fixed');
});

//Filter chat list
$("#search-chat").on("keyup", function() {
	var value = $(this).val().toLowerCase();
	$(".chat-list ul li").filter(function() {
	  $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
	});
});

// Checkbox Changed
$('input[type=checkbox]').change(function(){
  	if($(this).is("input[type=checkbox]:checked")) {
      	$(this).parent().closest('.item-content').addClass("menuitemshow");
  	} else {
      	$(this).parent().closest('.item-content').removeClass("menuitemshow");
  	}
});

// Select 2
if ($('.select').length > 0) {
    $('.select').select2({
        minimumResultsForSearch: -1,
        width: '100%'
    });
}


//Datepicker
if($('.datetimepicker').length > 0) {
	$('.datetimepicker').datetimepicker({
		format: 'DD/MM/YYYY',
		icons: {
			up: "fas fa-chevron-up",
			down: "fas fa-chevron-down",
			next: 'fas fa-chevron-right',
			previous: 'fas fa-chevron-left'
		}
	});
}

//Apex chart
if($('#chart').length > 0) {
var options = {
  	series: [{
  	name: 'series1',
  	data: [31, 40, 28, 51, 42, 109, 100]
}, {
  	name: 'series2',
  	data: [11, 32, 45, 32, 34, 52, 41]
}],
  	chart: {
  	height: 350,
  	type: 'area',
},
dataLabels: {
  	enabled: false
},
stroke: {
  	curve: 'smooth'
},
fill: {
    type: "gradient",
    gradient: {
      shadeIntensity: 1,
      opacityFrom: 0.7,
      opacityTo: 0.7,
      stops: [205, 210, 253, 1]
    }
 },
xaxis: {
  	type: 'month',	
},
tooltip: {
  	x: {
    	format: 'dd/MM/yy HH:mm'
  	},
	},
};

var chart = new ApexCharts(document.querySelector("#chart"), options);
chart.render();
}

if($('#chart1').length > 0) {
var options = {
          series: [{
            name: "Desktops",
            data: [20, 40, 10, 20, 40, 80]
        }],
          chart: {
          height: 350,
          type: 'line',
          zoom: {
            enabled: false
          }
        },
        dataLabels: {
          enabled: false
        },
        stroke: {
          curve: 'smooth'
        },
        title: {
          text: 'Set your financial goal every day of you need',
          align: 'left',
          style: {
                fontSize: "10px",
                fontweight:"400",
                color:"#555",
            }
        },
        grid: {
          row: {
            colors: ['#f3f3f3', 'transparent'],
            opacity: 0.5
          },
        },
        xaxis: {
          categories: ['Mo', 'Tu', 'We', 'Th', 'Fri', 'Sa'],
        }
        };

        var chart = new ApexCharts(document.querySelector("#chart1"), options);
        chart.render();
        }
  
