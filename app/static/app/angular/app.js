var API_URL = '/api/v1/';
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
            .when('/app', {
                templateUrl: '/static/app/templates/entries.html',
                controller: 'EntriesController'
            })

            // user management views
            .when('/app/login', {
                templateUrl: '/static/app/templates/login.html',
                controller: 'LoginController'
            })
            .when('/app/sign-up', {
                templateUrl: '/static/app/templates/signup.html',
                controller: 'JoinController'
            })

            // entries views
            .when('/app/:year/:month/', {
                templateUrl: '/static/app/templates/entries.html',
                controller: 'EntriesController'
            });

            // .when('/app/forgot-password', {
            //     templateUrl: '/static/app/templates/forgot-password.html'
            // });

        $routeProvider
            .otherwise({
                redirectTo: "/app"
            });

        $locationProvider.html5Mode(true);
    })
    .run(function($rootScope, $location, $http) {
        $rootScope.$on('$routeChangeSuccess', function() {
            // do anything on routechange
        })
    })
    .run(['$route', '$rootScope', '$location', function($route, $rootScope, $location) {
        ga('send', 'pageview', { page: $location.url() });
    }]);
