shekels.controller('JoinController', function($rootScope, $scope, $http, $sce, $location) {

    $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    $scope.form = {};

    // $http({
    //         method: 'GET',
    //         url: API_URL + '/v1/business_lines',
    //     })
    //     .success(function(data) {
    //         data.forEach(function(item) {
    //             $scope.business_lines.push({
    //                 id: item.id,
    //                 name: item.name
    //             })
    //         });
    //         var url = $location.path();
    //         if (url == '/h/cadastro-transportadora') {
    //             $rootScope.bg_number = 2;
    //         }
    //         if (url == '/h/cadastro-motorista') {
    //             $rootScope.bg_number = 5;
    //         }
    //         if (url == '/h/cadastro-empresa') {
    //             $rootScope.bg_number = 6;
    //         }
    //         console.log(url);
    //     });

    // $scope.cep = function() {
    //     var zip = $scope.form.address_zip;
    //     zip = zip.replace('.', '');
    //     zip = zip.replace('-', '');
    //     $rootScope.loader();
    //     $http({
    //             method: 'POST',
    //             data: $.param({
    //                 code: zip
    //             }),
    //             url: API_URL + '/v1/zip',
    //         })
    //         .then(function(data) {
    //             $rootScope.loaderRemove();
    //             if (!data.data) {
    //                 $rootScope.alertMessage = 'CEP não encontrado';
    //                 $('#alertWindow').modal('show');
    //                 $scope.form.address = "";
    //                 $scope.form.city = "";
    //                 $scope.form.zip_id = "";
    //                 $scope.form.address_zip = "";
    //             } else {
    //                 $('#city').val(data.data.city);
    //                 $('#address').val(data.data.street);
    //                 $scope.form.address = data.data.street;
    //                 $scope.form.city = data.data.city;
    //                 $scope.zip_id = data.data.id;
    //             }
    //         });
    // }
    // $scope.newDriver = function() {
    //     $('label').css({ color: "#555555" });
    //     if ($rootScope.validateForm($('#new_driver'))) {
    //         if ($scope.form.email == $scope.form.email_confirmation) {
    //             if ($scope.form.password.length >= 6 || $scope.form.password_confirmation.length >= 6) {
    //                 if (CPF.isValid($scope.form.cpf)) {
    //                     $('#cpf').parent().find('label').css({ color: "#555555" });
    //                     $scope.form.address_zip = $scope.zip_id;
    //                     $rootScope.loader();
    //                     $http({
    //                             method: 'POST',
    //                             data: $.param($scope.form),
    //                             url: API_URL + '/v1/drivers',
    //                         })
    //                         .then(function(data) {
    //                             $rootScope.loaderRemove();
    //                             if (data.data.error) {
    //                                 $rootScope.track('Cadastro', 'Motorista Erro');
    //                                 if (data.data.identifier == 'Drivers:EmailTaken') {
    //                                     $rootScope.alertMessage = 'Este email já está em uso.'
    //                                 } else if (data.data.identifier == 'Drivers:CPFTaken') {
    //                                     $rootScope.alertMessage = 'Este CPF já está em uso.'
    //                                 } else {
    //                                     $rootScope.alertMessage = "Não foi possivel realizar o cadastro. Verifique seus dados.";
    //                                     $scope.message = '';
    //                                 }
    //                                 $('#alertWindow').modal('show');
    //                             } else {
    //                                 $rootScope.track('Cadastro', 'Motorista Sucesso');
    //                                 $rootScope.alertMessage = 'Sua conta foi criada com sucesso. Você receberá um email para confirmar a conta.';
    //                                 $('#alertWindow').modal('show');
    //                                 $scope.message = '';
    //                                 $scope.form = {};
    //                             }
    //                         });
    //                 } else {
    //                     $scope.message = "CPF inválido.";
    //                     $('#cpf').parent().find('label').css({ color: "#ff0000" });
    //                 }
    //             } else {
    //                 $scope.message = "Senha precisar ter 6 ou mais caracteres";
    //                 $('#password').parent().find('label').css({ color: "#ff0000" });
    //                 $('#confirm_password').parent().find('label').css({ color: "#ff0000" });
    //             }
    //         } else {
    //             $scope.message = "Os Emails precisam ser iguais.";
    //             $('#email').parent().find('label').css({ color: "#ff0000" });
    //             $('#confirm_email').parent().find('label').css({ color: "#ff0000" });
    //         }
    //     } else {
    //         $scope.message = "Preencha os campos corretamente.";
    //     }

    // }
    // $scope.newShipping = function() {
    //     $('label').css({ color: "#555555" });
    //     if ($rootScope.validateForm($('#new_shipping'))) {
    //         if ($scope.form.password.length >= 6 || $scope.form.password_confirmation.length >= 6) {
    //             if ($scope.form.email == $scope.form.email_confirmation) {
    //                 if (CNPJ.isValid($scope.form.cnpj)) {
    //                     $scope.form.address_zip = $scope.zip_id;
    //                     $rootScope.loader();
    //                     $http({
    //                             method: 'POST',
    //                             data: $.param($scope.form),
    //                             url: API_URL + '/v1/shippers',
    //                         })
    //                         .then(function(data) {
    //                             $rootScope.loaderRemove();
    //                             if (data.data.error) {
    //                                 $rootScope.track('Cadastro', 'Transportadora Erro');
    //                                 if (data.data.identifier == 'Drivers:EmailTaken') {
    //                                     $rootScope.alertMessage = 'Este email já está em uso.'
    //                                 } else if (data.data.identifier == 'Drivers:CNPJTaken') {
    //                                     $rootScope.alertMessage = 'Este CNPJ já está em uso.'
    //                                 } else {
    //                                     $rootScope.alertMessage = "Não foi possivel realizar o cadastro. Verifique seus dados.";
    //                                     $scope.message = '';
    //                                 }
    //                                 $('#alertWindow').modal('show');
    //                             } else {
    //                                 $rootScope.track('Cadastro', 'Transportadora Sucesso');
    //                                 $rootScope.alertMessage = 'Sua conta foi criada com sucesso. Você receberá um email para confirmar a conta.';
    //                                 $('#alertWindow').modal('show');
    //                                 $scope.message = '';
    //                                 $scope.form = {};
    //                             }
    //                         });
    //                 } else {
    //                     $scope.message = "CNPJ inválido.";
    //                     $('#cnpj').parent().find('label').css({ color: "#ff0000" });
    //                 }
    //             } else {
    //                 $scope.message = "Os Emails precisam ser iguais.";
    //                 $('#email').parent().find('label').css({ color: "#ff0000" });
    //                 $('#confirm_email').parent().find('label').css({ color: "#ff0000" });
    //             }
    //         } else {
    //             $scope.message = "Senha precisar ter 6 ou mais caracteres";
    //             $('#password').parent().find('label').css({ color: "#ff0000" });
    //             $('#confirm_password').parent().find('label').css({ color: "#ff0000" });
    //         }
    //     } else {
    //         $scope.message = "Preencha os campos corretamente.";
    //     }
    // }
    // $scope.newCompany = function() {
    //     $('label').css({ color: "#555555" });
    //     if ($rootScope.validateForm($('#new_company'))) {
    //         if ($scope.form.password.length >= 6 || $scope.form.password_confirmation.length >= 6) {
    //             if (CNPJ.isValid($scope.form.cnpj)) {
    //                 $scope.form.address_zip = $scope.zip_id;
    //                 $rootScope.loader();
    //                 $http({
    //                         method: 'POST',
    //                         data: $.param($scope.form),
    //                         url: API_URL + '/v1/companies',
    //                     })
    //                     .then(function(data) {
    //                         $rootScope.loaderRemove();
    //                         if (data.data.error) {
    //                             $rootScope.track('Cadastro', 'Empresa Erro');
    //                             if (data.data.identifier == 'Companies:EmailTaken') {
    //                                 $rootScope.alertMessage = 'Este email já está em uso.'
    //                             } else if (data.data.identifier == 'Companies:CNPJTaken') {
    //                                 $rootScope.alertMessage = 'Este CNPJ já está em uso.'
    //                             } else {
    //                                 $rootScope.alertMessage = "Não foi possivel realizar o cadastro. Verifique seus dados.";
    //                                 $scope.message = '';
    //                             }
    //                             $('#alertWindow').modal('show');
    //                         } else {
    //                             $rootScope.track('Cadastro', 'Empresa Sucesso');
    //                             $rootScope.alertMessage = 'Sua conta foi criada com sucesso. Você receberá um email para confirmar a conta.';
    //                             $('#alertWindow').modal('show');
    //                             $scope.message = '';
    //                             $scope.form = {};
    //                         }
    //                     });
    //             } else {
    //                 $scope.message = "CNPJ inválido.";
    //                 $('#cnpj').parent().find('label').css({ color: "#ff0000" });
    //             }
    //         } else {
    //             $scope.message = "Senha precisar ter 6 ou mais caracteres";
    //             $('#password').parent().find('label').css({ color: "#ff0000" });
    //             $('#confirm_password').parent().find('label').css({ color: "#ff0000" });
    //         }

    //     } else {
    //         $scope.message = "Preencha os campos corretamente.";
    //     }
    // }
    // $('select.one').select2({
    //     placeholder: "Selecione"
    // });

    // $('select.four').select2({
    //     placeholder: "",
    //     maximumSelectionLength: 4
    // });

    // $rootScope.bg_number = 1;

});
