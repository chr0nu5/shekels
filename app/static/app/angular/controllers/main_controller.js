shekels.controller("MainController", function($rootScope, $scope, $http, $sce, $location, $routeParams) {

    changeDateFromUrl($rootScope, $routeParams);

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
