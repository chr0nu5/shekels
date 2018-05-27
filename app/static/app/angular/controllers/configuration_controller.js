shekels.controller('ConfigurationController', function($rootScope, $scope, $http, $sce, $compile, $location) {

    $scope.profile_update = {};
    $scope.password_update = {};
    $scope.recurrent_entry = {
        "times": 0,
        "day": 1
    };

    $scope.getRecurrentEntries = function() {

        $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
        $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

        $scope.recurrent_entry = {
            "times": 0,
            "day": 1
        };

        // $('.preloader-it > .la-anim-1').removeClass('la-animate');
        $(".preloader-it").fadeIn(0);
        // $('.preloader-it > .la-anim-1').addClass('la-animate');

        // get the current entries (year) and project on the chart
        $http({
                method: "GET",
                url: API_URL + "/recurrent_entries/",
            })
            .then(function(data) {
                $scope.recurrent_entries = data.data.entries;
                $(".preloader-it").delay(500).fadeOut("slow");
            })
            .catch(function(data) {
                console.log(data.data);
                $(".preloader-it").delay(500).fadeOut("slow");
            });

    }

    $scope.getRecurrentEntries();

    $scope.recurrentEntry = function() {
        $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
        $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");
        $scope.recurrent_entry.value = $("#value").maskMoney('unmasked')[0];

        // $('.preloader-it > .la-anim-1').removeClass('la-animate');
        $(".preloader-it").fadeIn(0);
        // $('.preloader-it > .la-anim-1').addClass('la-animate');

        $http({
                method: "POST",
                data: JSON.stringify($scope.recurrent_entry),
                contentType: "application/json",
                url: API_URL + "/new_recurrent/"
            })
            .then(function(data) {
                $rootScope.showSuccess("Successfully created!");
                $scope.getRecurrentEntries();
            })
            .catch(function(data) {
                $rootScope.showErrors(data.data.errors);
                $(".preloader-it").delay(500).fadeOut("slow");
            });

    }

    $scope.deleteRecurrentEntry = function(id) {

        $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
        $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

        // $('.preloader-it > .la-anim-1').removeClass('la-animate');
        $(".preloader-it").fadeIn(0);
        // $('.preloader-it > .la-anim-1').addClass('la-animate');

        $http({
            method: "DELETE",
            url: API_URL + "/recurrent_entry/" + id + "/delete/"
        })
        .then(function(data) {
            $scope.getRecurrentEntries();
        })
        .catch(function(data) {
            $rootScope.showErrors(data.data.errors);
            $(".preloader-it").delay(500).fadeOut("slow");
        });
    }

    $scope.profile = function() {

        $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
        $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

        $scope.profile_update.credit = $("#credit").maskMoney('unmasked')[0];
        $scope.profile_update.savings = $("#savings").maskMoney('unmasked')[0];

        // $('.preloader-it > .la-anim-1').removeClass('la-animate');
        $(".preloader-it").fadeIn(0);
        // $('.preloader-it > .la-anim-1').addClass('la-animate');

        $http({
                method: "PUT",
                data: JSON.stringify($scope.profile_update),
                contentType: "application/json",
                url: API_URL + "/update_profile/"
            })
            .then(function(data) {
                $rootScope.showSuccess("Successfully updated!");
                $rootScope.getProfile(function() {
                    $scope.profile_update.first_name = $rootScope.user.first_name;
                    $scope.profile_update.last_name = $rootScope.user.last_name;
                });
                $(".preloader-it").delay(500).fadeOut("slow");
            })
            .catch(function(data) {
                $rootScope.showErrors(data.data.errors);
                $(".preloader-it").delay(500).fadeOut("slow");
            });
    }

    $scope.password = function() {

        if ($scope.password_update.password != $scope.password_update.confirm_password) {
            $rootScope.showErrors({
                "password": "Passwords do not match"
            })
            return;
        }

        $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
        $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

        // $('.preloader-it > .la-anim-1').removeClass('la-animate');
        $(".preloader-it").fadeIn(0);
        // $('.preloader-it > .la-anim-1').addClass('la-animate');

        $http({
                method: "PUT",
                data: JSON.stringify($scope.password_update),
                contentType: "application/json",
                url: API_URL + "/update_password/"
            })
            .then(function(data) {
                $scope.password_update = {};
                $rootScope.showSuccess("Successfully updated!");
                $rootScope.getProfile();
                $(".preloader-it").delay(500).fadeOut("slow");
            })
            .catch(function(data) {
                $rootScope.showErrors(data.data.errors);
                $(".preloader-it").delay(500).fadeOut("slow");
            });
    }

    $rootScope.getProfile(function() {
        $scope.profile_update.first_name = $rootScope.user.first_name;
        $scope.profile_update.last_name = $rootScope.user.last_name;
    });

});
