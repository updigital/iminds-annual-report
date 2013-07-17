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

});

// initialize Gumby
window.Gumby.init();

// if AMD return Gumby object to define
if(typeof define == "function" && define.amd) {
	define(window.Gumby);
}

$(function() {

    Boxgrid.init();
    
});

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

// $(document).ready(function(){       
//             var scroll_pos = 700;
//             $(document).scroll(function() { 
//                 scroll_pos = $(this).scrollTop();
//                 if(scroll_pos = 1400) {
//                     $("section").css('background-color', '');
//                 } else {
//                     $("section").css('background-color', '#fc0');
//                 }
//             });
//         });

// $(function() {

//     // Do our DOM lookups beforehand
//     var nav_container = $("");
//     var nav = $("section");
    
//     var top_spacing = 15;
//     var waypoint_offset = 50;

//     nav_container.waypoint({
//         handler: function(event, direction) {
            
//             if (direction == 'down') {
            
//                 nav_container.css({ 'height':nav.outerHeight() });      
//                 nav.stop().addClass("sticky").css("top",-nav.outerHeight()).animate({"top":top_spacing});
                
//             } else {
            
//                 nav_container.css({ 'height':'auto' });
//                 nav.stop().removeClass("sticky").css("top",nav.outerHeight()+waypoint_offset).animate({"top":""});
                
//             }
            
//         },
//         offset: function() {
//             return -nav.outerHeight()-waypoint_offset;
//         }
//     });
    
//     var sections = $("section");
//     var navigation_links = $("section");
    
//     sections.waypoint({
//         handler: function(event, direction) {
        
//             var active_section;
//             active_section = $(this);
//             if (direction === "up") active_section = active_section.prev();

//             var active_link = $('nav a[href="#' + active_section.attr("id") + '"]');
//             navigation_links.removeClass("selected");
//             active_link.addClass("selected");

//         },
//         offset: '1%'
//     })
    
    
//     navigation_links.click( function(event) {

//         $.scrollTo(
//             $(this).attr("href"),
//             {
//                 duration: 200,
//                 offset: { 'left':0, 'top':-0.15*$(window).height() }
//             }
//         );
//     });


// });





