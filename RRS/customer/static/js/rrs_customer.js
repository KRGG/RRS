$(function() {
    $("#date-input").datepicker({
      showOn: "button",
      buttonText: "<span class=\"caret\"></span>"
    });
    $(".for-input > li").click(function(){
    	$(this).parent().siblings("input").val($(this).text());
    });
	$("#time-input-trigger").click(function(){
	  $(".ui-timepicker-input").timepicker("show");
	});
    $("#time-input").timepicker();
    $(".ui-timepicker-input").click(function(){
	  $(".ui-timepicker-input").timepicker("hide");
	});
	$(".ui-timepicker-input").click(function(){
	  $(".ui-timepicker-input").timepicker("hide");
	});
	$("#restaurant-property-input").attr('size',$("#restaurant-property-input").attr('placeholder').length);
});