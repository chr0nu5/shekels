shekels.controller('EntriesController', function($rootScope, $scope, $http, $sce, $compile, $location) {

    $rootScope.getProfile();

    $scope.entries = [];

    $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
    $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

    // get the current entries (month) and project on the chart
    $http({
            method: "GET",
            url: API_URL + "/entries/" + $rootScope.year + "/" + $rootScope.month + "/",
        })
        .then(function(data) {
            $scope.entries = data.data.entries;

            var data = [];

            $.each($scope.entries, function(i, e) {

                var income = 0;
                var expenses = 0;

                $.each(e.records, function(i, r) {
                    if (r.value) {
                        value = parseFloat(r.value.replace("$", ""));
                        if (value >= 0) {
                            income += value;
                        } else {
                            expenses += value;
                        }
                    }
                });

                data.push({
                    period: e.day,
                    income: income,
                    expenses: expenses,
                    balance: e.balance
                });


            });

            Morris.Line({
                element: 'month_projection',
                data: data,
                xkey: 'period',
                ykeys: ['income', 'expenses', 'balance'],
                labels: ['Income', 'Expenses', 'Balance'],
                pointSize: 2,
                fillOpacity: 0,
                lineWidth: 2,
                pointStrokeColors: ['#8BC34A', '#962828', '#f8b32d'],
                behaveLikeLine: true,
                grid: false,
                hideHover: 'auto',
                lineColors: ['#8BC34A', '#962828', '#f8b32d'],
                resize: true,
                gridTextColor: '#878787',
                gridTextFamily: "Roboto"

            });

        })
        .catch(function(data) {
            console.log(data.data);
        });

    // get the current entries (month) and project on the chart
    $http({
            method: "GET",
            url: API_URL + "/entries/" + $rootScope.year + "/",
        })
        .then(function(data) {
            $scope.year_entries = data.data.entries;

            var data = [];

            console.log($scope.year_entries);

            // $.each($scope.entries, function(i, e) {
            //     // console.log(e);

            //     var income = 0;
            //     var expenses = 0;

            //     $.each(e.records, function(i, r) {
            //         if (r.value) {
            //             value = parseFloat(r.value.replace("$", ""));
            //             if (value >= 0) {
            //                 income += value;
            //             } else {
            //                 expenses += value;
            //             }
            //         }
            //     });

            //     data.push({
            //         period: e.day,
            //         income: income,
            //         expenses: expenses,
            //         balance: e.balance
            //     });


            // });

            // console.log(data);

            // Morris.Line({
            //     element: 'month_projection',
            //     data: data,
            //     xkey: 'period',
            //     ykeys: ['income', 'expenses', 'balance'],
            //     labels: ['Income', 'Expenses', 'Balance'],
            //     pointSize: 2,
            //     fillOpacity: 0,
            //     lineWidth: 2,
            //     pointStrokeColors: ['#8BC34A', '#962828', '#f8b32d'],
            //     behaveLikeLine: true,
            //     grid: false,
            //     hideHover: 'auto',
            //     lineColors: ['#8BC34A', '#962828', '#f8b32d'],
            //     resize: true,
            //     gridTextColor: '#878787',
            //     gridTextFamily: "Roboto"

            // });

        })
        .catch(function(data) {
            console.log(data.data);
        });

});
