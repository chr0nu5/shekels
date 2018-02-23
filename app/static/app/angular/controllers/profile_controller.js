shekels.controller('ProfileController', function($rootScope, $scope, $http, $sce, $compile, $location) {

    $http.defaults.headers.put["Content-Type"] = "application/json; charset=utf-8";
    $http.defaults.headers.put["Authorization"] = "Bearer dGRZQ2hSdWpKcXk3Qm5yVUdmM2NxM3NxNjdtZ1NDcTQ6WHJ6M3NDQkNoVDg5dUNiVG9DdHo5bTZCcnFZRWZtVEhuSzhwOEd1TGNteWdrdEN0WmV0M2VwVUhWSlU2QnBaZA==";

    $scope.profile_update = {};
    $scope.password_update = {};

    $scope.profile = function() {
        $http({
                method: "PUT",
                data: JSON.stringify($scope.profile_update),
                contentType: "application/json",
                url: API_URL + "/update_funds/"
            })
            .then(function(data) {
                console.log(data.data);
            })
            .catch(function(data) {
                console.log(data.data);
                // $rootScope.showErrors(data.data.errors);
            });
    }



});
