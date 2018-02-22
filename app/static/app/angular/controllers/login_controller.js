shekels.controller('LoginController', function($rootScope, $scope, $http, $sce, $location) {

    $http.defaults.headers.post["Content-Type"] = "application/json; charset=utf-8";
    $http.defaults.headers.post["Authorization"] = "Bearer dGRZQ2hSdWpKcXk3Qm5yVUdmM2NxM3NxNjdtZ1NDcTQ6WHJ6M3NDQkNoVDg5dUNiVG9DdHo5bTZCcnFZRWZtVEhuSzhwOEd1TGNteWdrdEN0WmV0M2VwVUhWSlU2QnBaZA==";

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

    // var url = $location.search().url;
    // $rootScope.url = $location.path();

    // $scope.auth = function() {
    //     $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    //     $rootScope.loader();
    //     $rootScope.track('Login','Tentativa');
    //     $http({
    //             method: 'POST',
    //             data: $.param($scope.login),
    //             url: API_URL + '/oauth/token',
    //         })
    //         .then(function(data) {
    //             if (data.data.error) {
    //                 $rootScope.track('Login','Erro');
    //                 if (data.data.identifier == 'OAuth:AccountNotConfirmed') {
    //                     $scope.message = "Conta não confirmada.";
    //                     storage.deleteKey('token');
    //                     $rootScope.loaderRemove();
    //                 } else {
    //                     $scope.message = "Email ou senha inválidos.";
    //                     storage.deleteKey('token');
    //                     $rootScope.loaderRemove();
    //                     console.log(data.data.error);
    //                 }
    //             } else {
    //                 $rootScope.track('Login','Sucesso');
    //                 $http({
    //                         method: 'POST',
    //                         url: API_URL + '/save/token',
    //                         data: $.param({
    //                             token: data.data.token
    //                         })
    //                     })
    //                     .success(function(data) {
    //                         if (data.error) {
    //                         } else {
    //                             $http({
    //                                     method: 'GET',
    //                                     url: API_URL + '/v1/me'
    //                                 })
    //                                 .success(function(data) {
    //                                     $rootScope.loaderRemove();
    //                                     if (data.error) {

    //                                     } else {
    //                                         storage.set('user', data);
    //                                         if (url) {
    //                                             window.location = url;
    //                                         } else {
    //                                             $location.path("/u");
    //                                         }
    //                                     }
    //                                 });
    //                         }
    //                     });
    //             }
    //         });
    // }

    // $rootScope.bg_number = 3;

});
