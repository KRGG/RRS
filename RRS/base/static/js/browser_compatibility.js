$(window).load(function () {
	var isSafari = /Safari/.test(navigator.userAgent) && /Apple Computer/.test(navigator.vendor);
    if ( isSafari ) {
		$("#footer").css('position', 'absolute');
		$("#footer").css('bottom', '0px');
	}
});