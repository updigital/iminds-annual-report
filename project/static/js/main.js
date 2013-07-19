// Gumby is ready to go
Gumby.ready(function() {
  console.log('Gumby is ready to go...', Gumby.debug());

  // placeholder polyfil
  if(Gumby.isOldie || Gumby.$dom.find('html').hasClass('ie9')) {
    $('input, textarea').placeholder();
  }
});

// Oldie document loaded
Gumby.oldie(function() {

});

// Document ready
$(function() {

    // FlowSlider
    $("#slider").FlowSlider({
        animation: "jQuery"                
        
    });

    // Boxgrid Overlay
    $(function() {

        Boxgrid.init();
    
    });

});

// initialize Gumby
window.Gumby.init();

// if AMD return Gumby object to define
if(typeof define == "function" && define.amd) {
	define(window.Gumby);
}

// section_january = $("section#january").addClass("old");

// $(window).scroll(function(d,h) {
//     section_january.each(function(i) {
//         a = $(this).offset().top + $(this).height();
//         b = $(window).scrollTop() + $(window).height();
//         if (a = b) $(this).addClass("new");
//         if (b < a) $(this).removeClass("new");
//     });
// });

// section_february = $("section#february").addClass("old");

// $(window).scroll(function(d,h) {
//     section_february.each(function(i) {
//         a = $(this).offset().top + $(this).height();
//         b = $(window).scrollTop() + $(window).height();
//         if (a < b) $(this).addClass("new");
//         if (a < b) $(this).removeClass("new");
//     });
// });