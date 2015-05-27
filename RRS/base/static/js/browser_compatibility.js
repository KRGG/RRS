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
	}
};

$(window).load(function () {
	setResponsiveCss();
});

$(window).resize(function () {
    setResponsiveCss();
});