shekels.controller('EntriesController', function($rootScope, $scope, $http, $sce, $compile, $location) {

    $rootScope.getProfile();

    $scope.entries = [];

    $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
    $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

    $http({
            method: "GET",
            url: API_URL + "/entries/" + $rootScope.year + "/" + $rootScope.month + "/",
        })
        .then(function(data) {
            console.log(data.data.entries);
            $scope.entries = data.data.entries;
        })
        .catch(function(data) {
            console.log(data.data);
        });

});
