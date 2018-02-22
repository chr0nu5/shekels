shekels.controller('MainController', function($rootScope, $scope, $http, $sce, $location, $routeParams) {

    changeDateFromUrl($rootScope, $routeParams);

    $rootScope.showErrors = function(errors) {
        $.toast().reset('all');
        Object.keys(errors).forEach(function(key) {
            $.toast({
                heading: '😱',
                text: firstLetterUppercase(key) + ": " + errors[key],
                position: 'top-right',
                loaderBg: '#892121',
                icon: 'error',
                hideAfter: 3000
            });
        });
    }

    // $scope.header_height = 250;
    // $scope.search = function() {
    //     $('html, body').animate({ scrollTop: 0 }, '1000', 'swing');
    //     $location.path('/h/search');
    // }
    $rootScope.logout = function() {
        storage.deleteKey('token');
        $location.path('/app/login/');
    }

    // $rootScope.goBack = function() {
    //     window.history.back();
    // }

    // $rootScope.loader = function() {
    //     $('.css3-spinner').fadeIn();
    // }

    // $rootScope.loaderRemove = function() {
    //     $('.css3-spinner').fadeOut();
    // }

    // if (storage.get('user')) {
    //     $http({
    //             method: 'GET',
    //             url: API_URL + '/v1/me'
    //         })
    //         .success(function(data) {
    //             storage.set('user', data);
    //         });
    // }

    // $rootScope.userInfo = storage.get('user');

    // $rootScope.info = {};

    // $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";

    // $http({
    //         method: 'GET',
    //         url: API_URL + '/v1/freights/info',
    //     })
    //     .success(function(data) {
    //         if (data.error) {

    //         } else {
    //             $rootScope.info = data;
    //         }
    //     });

    // $rootScope.searchResults = [];
    // $rootScope.states_origin = [];
    // $rootScope.states_destiny = [];
    // $rootScope.countries = [];

    // $http({
    //         method: 'GET',
    //         url: API_URL + '/v1/zip/states',
    //     })
    //     .success(function(data) {
    //         console.log(data);
    //         if (data.error) {

    //         } else {
    //             data.forEach(function(item) {
    //                 $rootScope.countries.push(item);
    //             });
    //             setTimeout(function() {
    //                 $rootScope.searchForm.country_origin = 'br';
    //                 $rootScope.searchForm.country_destiny = 'br';
    //                 $rootScope.originCountry();
    //                 $rootScope.destinyCountry();
    //             }, 1000);
    //         }
    //     });

    // $scope.first = "";
    // $scope.second = "";
    // $scope.count = 0;
    // $rootScope.country = function(e) {
    //     var country = e.currentTarget.attributes.id.value;
    //     if(!$("#" + country).hasClass("selected") && $scope.count < 2){
    //         if($scope.count == 0){
    //             $scope.first = country;
    //             $rootScope.searchForm.country_origin = country;
    //             $rootScope.searchForm.country_destiny = country;
    //             $rootScope.originCountry();
    //             $rootScope.destinyCountry();
    //             $("#" + country + "_orig").text("Origem");
    //             $("#" + country + "_dest").text("Destino");
    //         } else if ($scope.count == 1 ){
    //             $scope.second = country;
    //             $rootScope.searchForm.country_destiny = country;
    //             $rootScope.destinyCountry();
    //             $("#" + country + "_dest").text("Destino");
    //             $("#" + $scope.first + "_dest").text("");
    //         }
    //         $("#" + country).toggleClass("selected");
    //         $scope.count++;
    //     } else if ($("#" + country).hasClass("selected")){
    //         $scope.count--;
    //         if($scope.count == 1 && $scope.first == country){
    //             $("#" + $scope.second + "_orig").text("Origem");
    //             $scope.first = $scope.second;
    //             $rootScope.searchForm.country_origin = $scope.second;
    //             $rootScope.originCountry();
    //         }
    //         if($scope.count == 1 && country == $scope.second){
    //             $("#" + $scope.first + "_dest").text("Destino");
    //             $rootScope.searchForm.country_destiny = $scope.first;
    //             $rootScope.destinyCountry();
    //         }
    //         $("#" + country).toggleClass("selected");
    //         $("#" + country + "_orig").text("");
    //         $("#" + country + "_dest").text("");
    //     }
    // }

    // $rootScope.originCountry = function() {
    //     $rootScope.countries.forEach(function(c) {
    //         if (c.code == $rootScope.searchForm.country_origin) {
    //             $rootScope.states_origin = [];
    //             c.states.forEach(function(item) {
    //                 $rootScope.states_origin.push(item);
    //             });
    //         };
    //     });
    // }

    // $rootScope.destinyCountry = function() {
    //     $rootScope.countries.forEach(function(c) {
    //         if (c.code == $rootScope.searchForm.country_destiny) {
    //             $rootScope.states_destiny = [];
    //             c.states.forEach(function(item) {
    //                 $rootScope.states_destiny.push(item);
    //             });
    //         };
    //     });
    // }


    // $rootScope.getCities = function(id, array) {
    //     $http({
    //             method: 'GET',
    //             url: API_URL + '/v1/zip/states/' + id + '/cities',
    //         })
    //         .success(function(data) {
    //             if (data.error) {

    //             } else {
    //                 while (array.length > 0) {
    //                     array.pop();
    //                 }
    //                 data.forEach(function(city) {
    //                     array.push(city);
    //                 });
    //                 // $('select.custom-search').select2();
    //             }
    //         });
    // }

    // $rootScope.goToTop = function() {
    //     $('#gotoTop').trigger('click');
    // }


    // $rootScope.searchForm = {};
    // $rootScope.origin_cities = [];
    // $rootScope.destiny_cities = [];

    // $scope.originCity = function() {
    //     $rootScope.getCities($scope.searchForm.originState, $scope.origin_cities);
    // }

    // $scope.destinyCity = function() {
    //     $rootScope.getCities($scope.searchForm.destinyState, $scope.destiny_cities);
    // }

    // $rootScope.chatModel = {
    //     id: 0,
    //     from: {}
    // };
    // $rootScope.chatMessages = [];

    // var chatTimeout = 0;
    // var last = (new Date().getTime() / 1000) - 26000000;

    // $rootScope.reloadMessages = function(timestamp) {
    //     $http({
    //             method: 'GET',
    //             url: API_URL + '/v1/chats/' + $rootScope.chatModel.id + '/' + timestamp,
    //         })
    //         .success(function(data) {
    //             last = (new Date().getTime() / 1000) - 26000000;
    //             if (data.error) {

    //             } else {
    //                 var n1 = $rootScope.chatMessages.length;
    //                 var n2 = data.messages.length;
    //                 $rootScope.chatMessages = [];
    //                 data.messages.forEach(function(message) {
    //                     $rootScope.chatMessages.push(message);
    //                 });
    //                 chatTimeout = setTimeout(function() {
    //                     $rootScope.reloadMessages(last);
    //                 }, 1000);

    //             }
    //             reloadTimeout = setTimeout(function() {
    //                 if(n1 != n2){
    //                     $(".messageScroller").scrollTop(10000000);
    //                 }
    //             }, 2000);
    //         });


    // }

    // $('body').on('keypress', '.chatMessage', function(e) {
    //     if (e.which == 13) {
    //         $rootScope.sendMessage();
    //     }
    // })

    // $rootScope.sendMessage = function() {
    //     $http({
    //             method: 'POST',
    //             data: $.param({
    //                 message: $rootScope.chatModel.message
    //             }),
    //             url: API_URL + '/v1/chats/' + $rootScope.chatModel.id + '/message',
    //         })
    //         .then(function(data) {
    //             if (data.error) {

    //             } else {
    //                 $rootScope.chatModel.message = "";
    //             }
    //         });
    // }

    // $rootScope.openChat = function(id, to) {
    //     clearTimeout(chatTimeout);
    //     $rootScope.chatModel.id = id;
    //     $rootScope.chatModel.user = to;
    //     $rootScope.chatMessages = [];
    //     last = (new Date().getTime() / 1000) - 26000000;
    //     $rootScope.reloadMessages(last);
    //     $('#chatWindow').modal('show');
    // }

    // $rootScope.bid = {};
    // $rootScope.bids = [];

    // $rootScope.updateBids = function() {
    //     $http({
    //             method: 'GET',
    //             url: API_URL + '/v1/freights/' + $rootScope.bid.id,
    //         })
    //         .success(function(data) {
    //             if (data.error) {

    //             } else {
    //                 $rootScope.bids = [];
    //                 data.bids.forEach(function(bid) {
    //                     $rootScope.bids.push(bid);
    //                 });
    //                 $('#money').mask("#0.00", {
    //                     reverse: true
    //                 });
    //                 bidTimeout = setTimeout($rootScope.updateBids, 1000);
    //             }
    //         });
    // }

    // var bidTimeout;

    // $rootScope.openBid = function(id) {
    //     clearTimeout(bidTimeout);
    //     $rootScope.bid.id = id;
    //     $rootScope.updateBids();
    //     $('#bidWindow').modal('show');
    // }

    // $rootScope.completeBid = function() {
    //     $rootScope.loader();
    //     $http({
    //             method: 'POST',
    //             data: $.param({
    //                 value: $rootScope.bid.value
    //             }),
    //             url: API_URL + '/v1/auctions/' + $rootScope.bid.id + '/bid',
    //         })
    //         .then(function(data) {
    //             $rootScope.loaderRemove();
    //             $rootScope.bid.value = null;
    //         });
    // }

    // $rootScope.sendBid = function() {
    //     if ($rootScope.bid.value) {
    //         var low = $rootScope.bids[0];
    //         var first = false;
    //         if (!low || !low.value) {
    //             low = {};
    //             low.value = Number.MAX_SAFE_INTEGER + '';
    //             first = true;
    //         }
    //         low = low.value.replace('"', '');
    //         low = low.replace('"', '');
    //         var bid = parseFloat($rootScope.bid.value);
    //         var lower = false;
    //         var hasBid = false;

    //         $rootScope.bids.forEach(function(b) {
    //             b = b.value.replace('"', '');
    //             b = b.replace('"', '');
    //             b = parseFloat(b);
    //             if (b == bid) {
    //                 hasBid = true;
    //             }
    //         });

    //         if (hasBid) {
    //             $rootScope.alertMessage = 'Esse lance ja foi dado. Escolha outro valor.';
    //             $('#alertWindow').modal('show');
    //         } else {
    //             if (low * 0.8 > bid) {
    //                 lower = true;
    //             }
    //             if (first || !lower) {
    //                 $rootScope.completeBid();
    //             } else {
    //                 if (lower) {
    //                     bootbox.confirm({
    //                         message: "Seu lance é menor que 20% do menor lance. Tem certeza?",
    //                         buttons: {
    //                             confirm: {
    //                                 label: 'Sim',
    //                                 className: 'btn-success'
    //                             },
    //                             cancel: {
    //                                 label: 'Não',
    //                                 className: 'btn-danger'
    //                             }
    //                         },
    //                         callback: function(result) {
    //                             if (result) {
    //                                 $rootScope.completeBid();
    //                             }
    //                         }
    //                     });
    //                 }
    //             }
    //         }
    //     }
    // }

    // $rootScope.freightDetail = {};
    // $rootScope.freightDetail.price = "0";
    // $rootScope.openFreight = function(id) {
    //     $rootScope.track('Frete', 'Ver');

    //     if (!storage.get('user')) {
    //         window.location = '/h/minha-conta?url=/h/detalhe/' + id;
    //         // $location.path('/h/minha-conta?url=' + $location.path());
    //     } else {
    //         $rootScope.loader();
    //         $http({
    //                 method: 'GET',
    //                 url: API_URL + '/v1/freights/' + id,
    //             })
    //             .success(function(data) {
    //                 $rootScope.loaderRemove();
    //                 $rootScope.freightDetail = data;
    //                 $('#freightWindow').modal('show');
    //                 console.log($rootScope.freightDetail);
    //                 console.log($rootScope.freightDetail.vehicle_type);
    //                 console.log($rootScope.freightDetail.vehicle_body_type.name);
    //             });
    //     }

    // }


    // $scope.getCloseDrivers = function() {
    //     $scope.types = [];
    //     $scope.bodies = [];
    //     $scope.destiny = $rootScope.freightDetail.origin.id;
    //     $rootScope.freightDetail.vehicle_type.forEach(function(item){
    //         $scope.types.push(item.id);
    //     });
    //     $rootScope.freightDetail.vehicle_body_type.forEach(function(item){
    //         $scope.bodies.push(item.id);
    //     });
    //     $http({
    //         method: 'POST',
    //         url: API_URL + '/v1/drivers/availability',
    //         data: $.param({
    //             origin_id: $scope.destiny,
    //             vehicle_type_id: $scope.types.join(','),
    //             vehicle_body_type_id: $scope.bodies.join(',')
    //         })
    //     }).success(function(data){
    //         if(data.error){

    //         } else {
    //             $scope.closeDrivers = data;
    //         }
    //     }).then(function(){
    //         $rootScope.availableDrivers($scope.closeDrivers);
    //         $('#freightWindow').modal('hide');
    //     });
    // }

    // // $scope.getDistance = function() {
    // //     $http({
    // //         method: 'GET',
    // //         url: API_URL + '/v1/drivers/'+ 46 +'/positions/'+ 511 ,
    // //     }).success(function(data){
    // //         console.log(data);
    // //     });
    // // }
    // // $scope.getDistance();

    // $rootScope.validateForm = function(form) {
    //     var valid = true;
    //     form.find('.required').each(function(i, e) {
    //         if ($(this).hasClass('ng-empty') || $(this).val() == '') {
    //             valid = false;
    //             $(this).parent().find('label').css({ color: "#ff0000" });
    //         } else {
    //             $(this).parent().find('label').css({ border: "#555555" });
    //         }
    //     });
    //     return valid;
    // }

    // $rootScope.auctionModel = {};

    // $rootScope.viewAuction = function(id) {
    //     $rootScope.loader();
    //     $http({
    //             method: 'GET',
    //             url: API_URL + '/v1/freights/' + id,
    //         })
    //         .success(function(data) {
    //             $rootScope.loaderRemove();
    //             $rootScope.auctionModel = data;
    //             $('#auctionWindow').modal('show');
    //         });
    // }

    // $rootScope.closeByDrivers = [];
    // $rootScope.availableDrivers = function(list) {
    //     $rootScope.closeByDrivers = list;
    //     $('#driversWindow').modal('show');
    // }

    // setTimeout(function() {
    //     $("#top-cart-trigger").click(function(e) {
    //         $('#page-menu').toggleClass('pagemenu-active', false);
    //         $('#top-cart').toggleClass('top-cart-open');
    //         e.stopPropagation();
    //         e.preventDefault();
    //     });
    // }, 1000);

    // $rootScope.regions = [
    //     'Norte',
    //     'Nordeste',
    //     'Centro-Oeste',
    //     'Sudeste',
    //     'Sul'
    // ];

    // $rootScope.types = [
    //     'Transferência',
    //     'Milk Run',
    //     'Logistica Reversa',
    //     'Aereo',
    //     'Maritimo',
    //     'Compra'
    // ];

    // $rootScope.weights = [
    //     '0-10',
    //     '10.01 – 20',
    //     '20.01 - 30',
    //     '30.01 - 50',
    //     '50.01 - 70',
    //     '70.01 - 100',
    //     '100.01 - 150',
    //     '150.01 - 200',
    //     '200.01 - 500',
    //     '500.01 - 1000',
    //     '1000.01 - 3000',
    //     '6000.01 - 8000'
    // ];

    // $rootScope.motorcycle_areas = [
    //     'Administração',
    //     'Compras',
    //     'Diretoria',
    //     'Informática',
    //     'Manutenção',
    //     'Qualidade',
    //     'RH',
    //     'Segurança',
    //     'Vendas',
    //     'Outros'
    // ];

    // $scope.zeroPrice = function(price) {
    //     price = price.replace('"', '');
    //     price = price.replace('"', '');
    //     price = parseFloat(price);
    //     return price;
    // }

    // $rootScope.compareDate = function(dateString) {
    //     var dt1 = parseInt(dateString.substring(0, 2));
    //     var mon1 = parseInt(dateString.substring(3, 5));
    //     var yr1 = parseInt(dateString.substring(6, 10));
    //     var date1 = new Date(yr1, mon1 - 1, dt1);
    //     return date1;
    // }

    // $rootScope.url = $location.path();

    // $rootScope.textIndex = 0;
    // $rootScope.openHomeText = function(index) {
    //     $rootScope.textIndex = index;
    //     $('#homeTextModal').modal('show');
    // }

    // $rootScope.checkAuthentication = function() {
    //     if (!storage.get('user')) {
    //         window.location = '/h/minha-conta?url=' + $location.path();
    //         // $location.path('/h/minha-conta?url=' + $location.path());
    //     }
    // }

    // $rootScope.track = function(event_type, action) {
    //     ga('send', 'event', event_type, action);
    // }

});
