var isSafari = /Safari/.test(navigator.userAgent) && /Apple Computer/.test(navigator.vendor);

function setResponsiveCss() {
	if ( isSafari ) {
		$("#branding").css("height", $(document).height() * 0.55);
		
		if ( $("#footer").offset().top < $("#body").offset().top + $("#body").outerHeight())
		{
			$("#footer").css("position", "");
			$("#footer").css("bottom", "");
		}
		
		else if ( $("#footer").offset().top + $("#footer").outerHeight() < $(window).height() )
		{
			$("#footer").css("position", "absolute");
			$("#footer").css("bottom", "0px");
		}
		
		$("#ui-datepicker-div").css("max-width", $(window).width() * 0.7);
		$("#ui-datepicker-div").css("max-height", $(window).height() * 0.6);
	}
};

$(window).load(function () {
	setResponsiveCss();
});

$(window).resize(function () {
    setResponsiveCss();
});