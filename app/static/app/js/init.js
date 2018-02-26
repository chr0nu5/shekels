$(document).ready(function() {
    droopy();
});

var setHeightWidth = function() {
    var height = $(window).height();
    var width = $(window).width();
    $('.full-height').css('height', (height));
    $('.page-wrapper').css('min-height', (height));

    if (width <= 1007) {
        $('#chat_list_scroll').css('height', (height - 270));
        $('.fixed-sidebar-right .chat-content').css('height', (height - 279));
        $('.fixed-sidebar-right .set-height-wrap').css('height', (height - 219));

    } else {
        $('#chat_list_scroll').css('height', (height - 204));
        $('.fixed-sidebar-right .chat-content').css('height', (height - 213));
        $('.fixed-sidebar-right .set-height-wrap').css('height', (height - 153));
    }

    var verticalTab = $(".vertical-tab");
    if (verticalTab.length > 0) {
        for (var i = 0; i < verticalTab.length; i++) {
            var $this = $(verticalTab[i]);
            $this.find('ul.nav').css(
                'min-height', ''
            );
            $this.find('.tab-content').css(
                'min-height', ''
            );
            height = $this.find('ul.ver-nav-tab').height();
            $this.find('ul.nav').css(
                'min-height', height + 40
            );
            $this.find('.tab-content').css(
                'min-height', height + 40
            );
        }
    }
};

var droopy = function() {

    $(document).on('click', '#toggle_nav_btn,#open_right_sidebar,#setting_panel_btn', function(e) {
        $(".dropdown.open > .dropdown-toggle").dropdown("toggle");
        return false;
    });

    $(document).on('click', '#toggle_nav_btn', function(e) {
        $(".wrapper").removeClass('open-right-sidebar open-setting-panel').toggleClass('slide-nav-toggle');
        return false;
    });

    $(document).on("mouseenter mouseleave", ".wrapper > .fixed-sidebar-left", function(e) {
        if (e.type == "mouseenter") {
            $(".wrapper").addClass("sidebar-hover");
        } else {
            $(".wrapper").removeClass("sidebar-hover");
        }
        return false;
    });
};

var boxLayout = function() {
    if ((!$(".wrapper").hasClass("rtl-layout")) && ($(".wrapper").hasClass("box-layout")))
        $(".box-layout .fixed-sidebar-right").css({ right: $(".wrapper").offset().left + 300 });
    else if ($(".wrapper").hasClass("box-layout rtl-layout"))
        $(".box-layout .fixed-sidebar-right").css({ left: $(".wrapper").offset().left });
}
boxLayout();

$(window).on("resize", function() {
    setHeightWidth();
    boxLayout();
}).resize();
