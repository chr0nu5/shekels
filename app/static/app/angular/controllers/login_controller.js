shekels.controller('LoginController', function($rootScope, $scope, $http, $sce, $location) {

    $http.defaults.headers.post["Content-Type"] = "application/json; charset=utf-8";
    $http.defaults.headers.post["Authorization"] = "Bearer " + TOKEN;

    $scope.login = {};

    $scope.auth = function() {
        $http({
                method: "POST",
                data: JSON.stringify($scope.login),
                contentType: "application/json",
                url: API_URL + "/login/"
            })
            .then(function(data) {
                var token = data.data.token;
                storage.set("token", token);
                $location.path('/app/');
            })
            .catch(function(data) {
                $rootScope.showErrors(data.data.errors);
            });
    }

});
