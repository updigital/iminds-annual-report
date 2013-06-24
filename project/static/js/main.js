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


$(document).ready(function() {
			/*
			 *  Simple image gallery. Uses default settings
			 */

			$('.fancybox').fancybox();


			/*
			 *  Different effects
			 */

			// Change title type, overlay closing speed
			$(".fancybox-effects-a").fancybox({
				helpers: {
					title : {
						type : 'outside'
					},
					overlay : {
						speedOut : 0
					}
				}
			});

			// Disable opening and closing animations, change title type
			$(".fancybox-effects-b").fancybox({
				openEffect  : 'none',
				closeEffect	: 'none',

				helpers : {
					title : {
						type : 'over'
					}
				}
			});

			// Set custom style, close if clicked, change title type and overlay color
			$(".fancybox-effects-c").fancybox({
				wrapCSS    : 'fancybox-custom',
				closeClick : true,

				openEffect : 'none',

				helpers : {
					title : {
						type : 'inside'
					},
					overlay : {
						css : {
							'background' : 'rgba(238,238,238,0.85)'
						}
					}
				}
			});

			// Remove padding, set opening and closing animations, close if clicked and disable overlay
			$(".fancybox-effects-d").fancybox({
				padding: 0,

				openEffect : 'elastic',
				openSpeed  : 150,

				closeEffect : 'elastic',
				closeSpeed  : 150,

				closeClick : true,

				helpers : {
					overlay : null
				}
			});

			/*
			 *  Button helper. Disable animations, hide close button, change title type and content
			 */

			$('.fancybox-buttons').fancybox({
				openEffect  : 'none',
				closeEffect : 'none',

				prevEffect : 'none',
				nextEffect : 'none',

				closeBtn  : false,

				helpers : {
					title : {
						type : 'inside'
					},
					buttons	: {}
				},

				afterLoad : function() {
					this.title = 'Image ' + (this.index + 1) + ' of ' + this.group.length + (this.title ? ' - ' + this.title : '');
				}
			});


		});

$(document).ready(function(){
    //$('#nav').localScroll(800);
    
    RepositionNav();
    
    $(window).resize(function(){
        RepositionNav();
    }); 
    
    //.parallax(xPosition, adjuster, inertia, outerHeight) options:
    //xPosition - Horizontal position of the element
    //adjuster - y position to start from
    //inertia - speed to move relative to vertical scroll. Example: 0.1 is one tenth the speed of scrolling, 2 is twice the speed of scrolling
    //outerHeight (true/false) - Whether or not jQuery should use it's outerHeight option to determine when a section is in the viewport
    $('#intro').parallax("50%", 0, 0.1, true);
    $('#second').parallax("50%", 0, 0.1, true);
    $('.bg').parallax("50%", 2500, 0.4, true);
    $('#third').parallax("50%", 2750, 0.3, true);
    
    var deck = new $.scrolldeck({
        slides: '.slide',
        buttons: '#nav li a',
        easing: 'easeInOutExpo'
    });

})


        $(function() {

            var $sidescroll = (function() {
                    
                    // the row elements
                var $rows           = $('#ss-container > div.ss-row'),
                    // we will cache the inviewport rows and the outside viewport rows
                    $rowsViewport, $rowsOutViewport,
                    // navigation menu links
                    $links          = $('#ss-links > a'),
                    // the window element
                    $win            = $(window),
                    // we will store the window sizes here
                    winSize         = {},
                    // used in the scroll setTimeout function
                    anim            = false,
                    // page scroll speed
                    scollPageSpeed  = 2000 ,
                    // page scroll easing
                    scollPageEasing = 'easeInOutExpo',
                    // perspective?
                    hasPerspective  = true,
                    
                    perspective     = hasPerspective && Modernizr.csstransforms3d,
                    // initialize function
                    init            = function() {
                        
                        // get window sizes
                        getWinSize();
                        // initialize events
                        initEvents();
                        // define the inviewport selector
                        defineViewport();
                        // gets the elements that match the previous selector
                        setViewportRows();
                        // if perspective add css
                        if( perspective ) {
                            $rows.css({
                                '-webkit-transform'           : 'none',
                                '-webkit-transform'    : 'none'
                            });
                        }
                        // show the pointers for the inviewport rows
                        $rowsViewport.find('a.ss-circle').addClass('ss-circle-deco');
                        // set positions for each row
                        placeRows();
                        
                    },
                    // defines a selector that gathers the row elems that are initially visible.
                    // the element is visible if its top is less than the window's height.
                    // these elements will not be affected when scrolling the page.
                    defineViewport  = function() {
                    
                        $.extend( $.expr[':'], {
                        
                            inviewport  : function ( el ) {
                                if ( $(el).offset().top < winSize.height ) {
                                    return true;
                                }
                                return false;
                            }
                        
                        });
                    
                    },
                    // checks which rows are initially visible 
                    setViewportRows = function() {
                        
                        $rowsViewport       = $rows.filter(':inviewport');
                        $rowsOutViewport    = $rows.not( $rowsViewport )
                        
                    },
                    // get window sizes
                    getWinSize      = function() {
                    
                        winSize.width   = $win.width();
                        winSize.height  = $win.height();
                    
                    },
                    // initialize some events
                    initEvents      = function() {
                        
                        // navigation menu links.
                        // scroll to the respective section.
                        $links.on( 'click.Scrolling', function( event ) {
                            
                            // scroll to the element that has id = menu's href
                            $('html, body').stop().animate({
                                scrollTop: $( $(this).attr('href') ).offset().top
                            }, scollPageSpeed, scollPageEasing );
                            
                            return false;
                        
                        });
                        
                        $(window).on({
                            // on window resize we need to redefine which rows are initially visible (this ones we will not animate).
                            'resize.Scrolling' : function( event ) {
                                
                                // get the window sizes again
                                getWinSize();
                                // redefine which rows are initially visible (:inviewport)
                                setViewportRows();
                                // remove pointers for every row
                                $rows.find('a.ss-circle').removeClass('ss-circle-deco');
                                // show inviewport rows and respective pointers
                                $rowsViewport.each( function() {
                                
                                    $(this).find('div.ss-left')
                                           .css({ left   : '0%' })
                                           .end()
                                           .find('div.ss-right')
                                           .css({ right  : '0%' })
                                           .end()
                                           .find('a.ss-circle')
                                           .addClass('ss-circle-deco');
                                
                                });
                            
                            },
                            // when scrolling the page change the position of each row  
                            'scroll.Scrolling' : function( event ) {
                                
                                // set a timeout to avoid that the 
                                // placeRows function gets called on every scroll trigger
                                if( anim ) return false;
                                anim = true;
                                setTimeout( function() {
                                    
                                    placeRows();
                                    anim = false;
                                    
                                }, 10 );
                            
                            }
                        });
                    
                    },
                    // sets the position of the rows (left and right row elements).
                    // Both of these elements will start with -50% for the left/right (not visible)
                    // and this value should be 0% (final position) when the element is on the
                    // center of the window.
                    placeRows       = function() {
                        
                            // how much we scrolled so far
                        var winscroll   = $win.scrollTop(),
                            // the y value for the center of the screen
                            winCenter   = winSize.height / 2 + winscroll;
                        
                        // for every row that is not inviewport
                        $rowsOutViewport.each( function(i) {
                            
                            var $row    = $(this),
                                // the left side element
                                $rowL   = $row.find('div.ss-left'),
                                // the right side element
                                $rowR   = $row.find('div.ss-right'),
                                // top value
                                rowT    = $row.offset().top;
                            
                            // hide the row if it is under the viewport
                            if( rowT > winSize.height + winscroll ) {
                                
                                if( perspective ) {
                                
                                    $rowL.css({
                                        '-webkit-transform' : 'none',
                                        'opacity'           : 0
                                    });
                                    $rowR.css({
                                        '-webkit-transform' : 'none',
                                        'opacity'           : 1
                                    });
                                
                                }
                                else {
                                
                                    $rowL.css({ left        : '0' });
                                    $rowR.css({ right       : '0' });
                                
                                }
                                
                            }
                            // if not, the row should become visible (0% of left/right) as it gets closer to the center of the screen.
                            else {
                                    
                                    // row's height
                                var rowH    = $row.height(),
                                    // the value on each scrolling step will be proporcional to the distance from the center of the screen to its height
                                    factor  = ( ( ( rowT + rowH / 2 ) - winCenter ) / ( winSize.height / 2 + rowH / 2 ) ),
                                    // value for the left / right of each side of the row.
                                    // 0% is the limit
                                    val     = Math.max( factor * 50, 0 );
                                    
                                if( val <= 0 ) {
                                
                                    // when 0% is reached show the pointer for that row
                                    if( !$row.data('pointer') ) {
                                    
                                        $row.data( 'pointer', true );
                                        $row.find('.ss-circle').addClass('ss-circle-deco');
                                    
                                    }
                                
                                }
                                else {
                                    
                                    // the pointer should not be shown
                                    if( $row.data('pointer') ) {
                                        
                                        $row.data( 'pointer', false );
                                        $row.find('.ss-circle').removeClass('ss-circle-deco');
                                    
                                    }
                                    
                                }
                                
                                // set calculated values
                                if( perspective ) {
                                    
                                    var t       = Math.max( factor * 75, 0 ),
                                        r       = Math.max( factor * 90, 0 ),
                                        o       = Math.min( Math.abs( factor - 1 ), 1 );
                                    
                                    $rowL.css({
                                        '-webkit-transform' : 'none',
                                        'opacity'           : o
                                    });
                                    $rowR.css({
                                        '-webkit-transform' : 'none',
                                        'opacity'           : o
                                    });
                                
                                }
                                else {
                                    
                                    $rowL.css({ left    : - val + '%' });
                                    $rowR.css({ right   : - val + '%' });
                                    
                                }
                                
                            }   
                        
                        });
                    
                    };
                
                return { init : init };
            
            })();
            
            $sidescroll.init();
            
        });

