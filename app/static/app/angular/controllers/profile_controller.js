shekels.controller('ProfileController', function($rootScope, $scope, $http, $sce, $compile, $location) {

    $scope.profile_update = {};
    $scope.password_update = {};

    $scope.profile = function() {

        $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
        $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

        $scope.profile_update.credit = $("#credit").maskMoney('unmasked')[0];
        $scope.profile_update.savings = $("#savings").maskMoney('unmasked')[0];

        console.log($scope.profile_update);

        $http({
                method: "PUT",
                data: JSON.stringify($scope.profile_update),
                contentType: "application/json",
                url: API_URL + "/update_profile/"
            })
            .then(function(data) {
                console.log(data.data);
                $rootScope.showSuccess("Successfully updated!");
                $rootScope.getProfile(function() {
                    $scope.profile_update.first_name = $rootScope.user.first_name;
                    $scope.profile_update.last_name = $rootScope.user.last_name;
                });
            })
            .catch(function(data) {
                console.log(data.data);
                $rootScope.showErrors(data.data.errors);
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
            })
            .catch(function(data) {
                $rootScope.showErrors(data.data.errors);
            });
    }

    $rootScope.getProfile(function() {
        $scope.profile_update.first_name = $rootScope.user.first_name;
        $scope.profile_update.last_name = $rootScope.user.last_name;
    });

});
