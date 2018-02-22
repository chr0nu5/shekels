shekels.controller('JoinController', function($rootScope, $scope, $http, $sce, $location) {

    $http.defaults.headers.post["Content-Type"] = "application/json; charset=utf-8";
    $http.defaults.headers.post["Authorization"] = "Bearer dGRZQ2hSdWpKcXk3Qm5yVUdmM2NxM3NxNjdtZ1NDcTQ6WHJ6M3NDQkNoVDg5dUNiVG9DdHo5bTZCcnFZRWZtVEhuSzhwOEd1TGNteWdrdEN0WmV0M2VwVUhWSlU2QnBaZA==";

    $scope.join = {};

    $scope.register = function() {

        if ($scope.join.password != $scope.join.confirm_password) {
            $rootScope.showErrors({
                "password": "Passwords do not match"
            })
            return;
        }

        $scope.join.email = $scope.join.username;

        $http({
                method: "POST",
                data: JSON.stringify($scope.join),
                contentType: "application/json",
                url: API_URL + "/register/"
            })
            .then(function(data) {
                $http({
                        method: "POST",
                        data: JSON.stringify({
                            "username": $scope.join.username,
                            "password": $scope.join.password
                        }),
                        contentType: "application/json",
                        url: API_URL + "/login/"
                    })
                    .then(function(data) {
                        var token = data.data.token;
                        storage.set("token", token);
                        $location.path('/app/');
                    });
            })
            .catch(function(data) {
                $rootScope.showErrors(data.data.errors);
            });
    }

});
