shekels.controller("MainController", function($rootScope, $scope, $http, $sce, $location, $routeParams) {

    changeDateFromUrl($rootScope, $routeParams);

    $rootScope.QUOTES = [
        "Giving up doesn\'t always mean you are weak, sometimes it means that you are strong enough to let go",
        "Promises mean everything, but after they are broken, sorry means nothing.",
        "The longer the explanation, the bigger the lie.",
        "Be more concerned with your character than your reputation, because your character is what you really are, while your reputation is merely what others think you are.",
        "Knowledge speaks, but wisdom listens.",
        "Our character is what we do when we think no one is looking.",
        "Appear weak when you are strong, and strong when you are weak.",
        "Speak when you are angry, and you will make the best speech you\'ll ever regret.",
        "If you can dream it, you can do it.",
        "Where there is a will, there is a way. If there is a chance in a million that you can do something, anything, to keep what you want from ending, do it.",
        "Pry the door open or, if need be, wedge your foot in that door and keep it open.",
        "Press forward. Do not stop, do not linger in your journey, but strive for the mark set before you.",
        "The future belongs to those who believe in the beauty of their dreams.",
        "Don\’t watch the clock; do what it does. Keep going.",
        "We aim above the mark to hit the mark.",
        "Never give up, for that is just the place and time that the tide will turn."
    ]
    $rootScope.seconds = 0;

    $rootScope.changeQuote = function() {
        $rootScope.quote = $rootScope.QUOTES[Math.floor(Math.random() * $rootScope.QUOTES.length)];
    }

    $rootScope.updateSeconds = function() {
        var t1 = new Date();
        var t2 = new Date(2011, 7, 8, 9, 52);
        var dif = t1.getTime() - t2.getTime();
        var seconds = Math.floor(dif / 1000);
        var year = Math.floor(seconds / 31536000);
        var month = Math.floor((seconds % 31536000) / (31536000/12));
        $rootScope.seconds = year + " year(s), " + month + " month(s) and counting.";
    }

    $rootScope.showErrors = function(errors) {
        $.toast().reset("all");
        Object.keys(errors).forEach(function(key) {
            $.toast({
                heading: "😱",
                text: firstLetterUppercase(key) + ": " + errors[key],
                position: "top-right",
                loaderBg: "#892121",
                icon: "error",
                hideAfter: 3000
            });
        });
    }

    $rootScope.showSuccess = function(message) {
        $.toast().reset("all");
        $.toast({
            heading: "🐼",
            text: message,
            position: "top-right",
            loaderBg: "#892121",
            icon: "success",
            hideAfter: 3000
        });
    }

    $rootScope.getProfile = function(f) {

        $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
        $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

        $http({
                method: "GET",
                url: API_URL + "/profile/",
            })
            .then(function(data) {
                storage.set("user", data.data);
                $rootScope.user = data.data;
                if (f) {
                    f();
                }
            })
            .catch(function(data) {
                $rootScope.showErrors(data.data.errors);
                $rootScope.logout();
            });
    }

    $rootScope.logout = function() {
        storage.deleteKey("token");
        $location.path("/app/login/");
    }

    // resize the screen after the templates finished loading
    $scope.$on('$viewContentLoaded', function() {
        $(window).trigger('resize');
    });

});
