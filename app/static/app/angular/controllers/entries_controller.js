shekels.controller('EntriesController', function($rootScope, $scope, $http, $sce, $compile, $location) {

    $http.defaults.headers.common["Content-Type"] = "application/json; charset=utf-8";
    $http.defaults.headers.common["Authorization"] = "Token " + storage.get("token");

    $rootScope.getProfile();

    $scope.entries = [];

    $scope.saveEntry = function($event, type) {

        var money_element = $($event.target);

        if (type == 0) {
            money_element = money_element.parent().find('input.money');
        }

        var day = money_element.parent().data("day");
        var id = money_element.data("id");
        var order = money_element.data("order");
        var value = money_element.maskMoney('unmasked')[0];
        var comment = money_element.parent().find(".comment").val();

        if (id > 0) {

            if (comment.length == 0) {
                comment = undefined;
            }

            $http({
                    method: "PUT",
                    data: JSON.stringify({
                        "value": value,
                        "comment": comment
                    }),
                    contentType: "application/json",
                    url: API_URL + "/entry/" + id + "/"
                })
                .then(function(data) {
                    $scope.updateEntries();
                })
                .catch(function(data) {
                    $rootScope.showErrors(data.data.errors);
                });
        } else {
            if (value != 0) {

                if (comment.length == 0) {
                    comment = undefined;
                }

                $http({
                        method: "POST",
                        data: JSON.stringify({
                            "order": order,
                            "date": day,
                            "value": value,
                            "comment": comment
                        }),
                        contentType: "application/json",
                        url: API_URL + "/new_entry/"
                    })
                    .then(function(data) {
                        $scope.updateEntries();
                    })
                    .catch(function(data) {
                        $rootScope.showErrors(data.data.errors);
                    });
            }

        }
    }

    $scope.updateEntries = function() {
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
                        period: "" + parseInt(e.day.split("-")[2]),
                        income: income,
                        expenses: expenses * -1,
                        balance: e.balance
                    });

                });

                $("#month_projection").empty();
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
                    grid: true,
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

        // get the current entries (year) and project on the chart
        $http({
                method: "GET",
                url: API_URL + "/entries/" + $rootScope.year + "/",
            })
            .then(function(data) {
                $scope.year_entries = data.data.entries;

                var data = [];
                var months = [
                    "January",
                    "February",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December",
                ]

                $.each(months, function(i_m, m) {

                    var income = 0;
                    var expenses = 0;
                    var balance = 0;

                    $.each($scope.year_entries, function(i_d, d) {
                        var month = parseInt(d.day.split("-")[1]);
                        if (month == (i_m + 1)) {
                            $.each(d.records, function(i_r, r) {
                                if (r.value) {
                                    var value = parseFloat(r.value.replace("$", ""));
                                    if (value >= 0) {
                                        income += value;
                                    } else {
                                        expenses += value;
                                    }
                                }
                            });
                            balance = d.balance;
                            date = d.day
                        }
                    });

                    data.push({
                        period: "" + parseInt(date.split("-")[1]),
                        income: income,
                        expenses: expenses * -1,
                        balance: parseFloat(balance)
                    });

                });

                $("#year_projection").empty();
                Morris.Line({
                    element: 'year_projection',
                    data: data,
                    xkey: 'period',
                    ykeys: ['income', 'expenses', 'balance'],
                    labels: ['Income', 'Expenses', 'Balance'],
                    pointSize: 2,
                    fillOpacity: 0,
                    lineWidth: 1,
                    pointStrokeColors: ['#8BC34A', '#962828', '#f8b32d'],
                    behaveLikeLine: true,
                    grid: true,
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
    }

    $scope.updateEntries();


});
