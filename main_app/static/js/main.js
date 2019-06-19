$(document).ready(function(){
    $('.mobile-nav-trigger').click(function(){
        $('.mobile-nav').toggleClass('active');
    });
    $('.mobile-nav-close').click(function(){
        $('.mobile-nav').toggleClass('active');
    })

    //Smooth Scroll
    $("a").on('click', function(event) {
        if (this.hash !== "") {
          event.preventDefault();
          var hash = this.hash;
          $('html, body').animate({
            scrollTop: $(hash).offset().top
          }, 800, function(){
            window.location.hash = hash;
          });
        } 
      });

      //landing page slider
      $('.slider').owlCarousel({
          loop:true,
          margin:10,
          nav:false,
          autoplay: true,
          items:1,
          mouseDrag: false,
          touchDrag: false,
          freeDrag: false,
          dots: true,
      });

      
        $('div.inline-group').sortable({
            /*containment: 'parent',
            zindex: 10, */
            items: 'div.inline-related',
            handle: 'h3:first',
            update: function() {
                $(this).find('div.inline-related').each(function(i) {
                    if ($(this).find('input[id$=name]').val()) {
                        $(this).find('input[id$=order]').val(i+1);
                    }
                });
            }
        });
        $('div.inline-related h3').css('cursor', 'move');
        $('div.inline-related').find('input[id$=order]').parent('div').hide();
    
});