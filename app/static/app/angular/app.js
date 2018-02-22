var API_URL = '/api/v1';
var storage = $.jStorage;

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
        // .when('/app/forgot-password/', {
        //     templateUrl: '/static/app/templates/forgot-password.html'
        // });

        $routeProvider
            .otherwise({
                redirectTo: "/app"
            });

        $locationProvider.html5Mode(true);
    })
    .run(function($rootScope, $routeParams, $location) {
        $rootScope.$on('$routeChangeSuccess', function() {
            if (!storage.get("token") && $location.path() != '/app/sign-up/' && $location.path() != '/app/forgot-password/') {
                $rootScope.logout();
            }
            changeDateFromUrl($rootScope, $routeParams);
        })
    })
    .run(['$route', '$rootScope', '$location', function($route, $rootScope, $location) {
        ga('send', 'pageview', { page: $location.url() });
    }]);

var changeDateFromUrl = function(scope, params) {
    scope.year = parseInt(params.year) ? parseInt(params.year) : new Date().getFullYear();
    scope.previous_year = eval(scope.year - 1);
    scope.next_year = eval(scope.year + 1);
    scope.month = parseInt(params.month) ? parseInt(params.month) : new Date().getMonth() + 1;

    if (!params.month && scope.year != new Date().getFullYear()) {
        scope.month = 1;
    }

}

var firstLetterUppercase = function(string)
{
    return string.charAt(0).toUpperCase() + string.slice(1);
}
