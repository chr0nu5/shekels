var API_URL = "/api/v1";
var storage = $.jStorage;

var key = $("body").data("key");
var sec = $("body").data("sec");

var TOKEN = btoa(key + ":" + sec);

(function(i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r;
    i[r] = i[r] || function() {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date();
    a = s.createElement(o),
        m = s.getElementsByTagName(o)[0];
    a.async = 1;
    a.src = g;
    m.parentNode.insertBefore(a, m)
})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

ga('create', 'UA-114408941-1', 'auto');

var shekels = angular.module('shekels', ['ngTouch', 'ngRoute', 'ngAnimate', 'ngCookies', 'ngSanitize']);
shekels
    .config(function($routeProvider, $locationProvider, $httpProvider) {
        $routeProvider
            // home -> default route
            .when('/app/', {
                templateUrl: '/static/app/templates/entries.html',
                controller: 'EntriesController'
            })

            // user management views
            .when('/app/login/', {
                templateUrl: '/static/app/templates/login.html',
                controller: 'LoginController'
            })
            .when('/app/sign-up/', {
                templateUrl: '/static/app/templates/signup.html',
                controller: 'JoinController'
            })
            .when('/app/profile/', {
                templateUrl: '/static/app/templates/profile.html',
                controller: 'ProfileController'
            })
            // entries views
            .when('/app/:year/', {
                templateUrl: '/static/app/templates/entries.html',
                controller: 'EntriesController'
            })
            // entries views
            .when('/app/:year/:month/', {
                templateUrl: '/static/app/templates/entries.html',
                controller: 'EntriesController'
            });

        $routeProvider
            .otherwise({
                redirectTo: "/app"
            });

        $locationProvider.html5Mode(true);
    })
    .run(function($rootScope, $routeParams, $location) {
        $rootScope.$on('$routeChangeStart', function() {
            $('.preloader-it > .la-anim-1').removeClass('la-animate');
            $(".preloader-it").fadeIn(0);
            $('.preloader-it > .la-anim-1').addClass('la-animate');
        })
        $rootScope.$on('$routeChangeSuccess', function() {
            if (!storage.get("token") && $location.path() != '/app/sign-up/' && $location.path() != '/app/forgot-password/') {
                $rootScope.logout();
            }
            changeDateFromUrl($rootScope, $routeParams);
            $rootScope.changeQuote();
            $rootScope.updateSeconds();

            $('body').on('focus', 'input', function() {
                maskMoneyForMoneyFields()
            });
            $(".preloader-it").delay(500).fadeOut("slow");

            setTimeout(function() {
                $( document ).trigger( "enhance.tablesaw" );
            }, 100);

        })
    })
    .run(['$route', '$rootScope', '$location', function($route, $rootScope, $location) {
        ga('send', 'pageview', { page: $location.url() });
    }]);

String.prototype.replaceAll = function(str1, str2, ignore) {
    return this.replace(new RegExp(str1.replace(/([\/\,\!\\\^\$\{\}\[\]\(\)\.\*\+\?\|\<\>\-\&])/g, "\\$&"), (ignore ? "gi" : "g")), (typeof(str2) == "string") ? str2.replace(/\$/g, "$$$$") : str2);
}

Number.prototype.formatMoney = function(c, d, t){
var n = this,
    c = isNaN(c = Math.abs(c)) ? 2 : c,
    d = d == undefined ? "." : d,
    t = t == undefined ? "," : t,
    s = n < 0 ? "-" : "",
    i = String(parseInt(n = Math.abs(Number(n) || 0).toFixed(c))),
    j = (j = i.length) > 3 ? j % 3 : 0;
   return s + (j ? i.substr(0, j) + t : "") + i.substr(j).replace(/(\d{3})(?=\d)/g, "$1" + t) + (c ? d + Math.abs(n - i).toFixed(c).slice(2) : "");
 };

var maskMoneyForMoneyFields = function() {
    $("input.money").maskMoney({ prefix: '$', allowNegative: true, thousands: ',', decimal: '.', affixesStay: true });
}

var changeDateFromUrl = function(scope, params) {
    scope.year = parseInt(params.year) ? parseInt(params.year) : (new Date()).getFullYear();
    scope.previous_year = eval(scope.year - 1);
    scope.current_year = (new Date()).getFullYear();
    scope.current_month = (new Date()).getMonth() + 1;
    scope.next_year = eval(scope.year + 1);
    scope.month = parseInt(params.month) ? parseInt(params.month) : (new Date()).getMonth() + 1;

    if (!params.month && scope.year != (new Date()).getFullYear()) {
        scope.month = 1;
    }

}

var firstLetterUppercase = function(string) {
    return string.charAt(0).toUpperCase() + string.slice(1);
}

shekels.filter('format_money', function() {
    return function(input) {
        if (input) {
            return input.formatMoney(2, '.', ',');
        } else {
            return 0.00
        }
    };
});

shekels.filter('format_day', function() {
    return function(input) {
        if (input) {
            var date = input.split("-");
            var today = new Date();
            if (today.getFullYear() == date[0] && (today.getMonth()+1) == date[1] && today.getDate() == date[2]) {
                return "Today";
            }
            return date[2] + "/" + date[1] + "/" + date[0];
        }
        return ""
    };
});


shekels.filter('colored_today', function() {
    return function(input) {
        if (input) {

            var balance = input.balance;
            input = input.day;

            var today = new Date();
            var date = input.split("-");
            if (today.getFullYear() == date[0] && (today.getMonth()+1) == date[1] && today.getDate() == date[2]) {
                return (balance >= 0 ? "success" : "info");
            }
        }
        return ""
    };
});
