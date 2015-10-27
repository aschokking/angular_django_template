'use strict';

// Declare app level module which depends on views, and components
angular.module('myApp', [
  'ngRoute',
  'ngCookies',
  'myControllers',
]).
config(['$routeProvider', function($routeProvider) {
    $routeProvider.
	when('/home', {
	    templateUrl: '/static/app/partials/home.html',
	    controller: 'HomeController'
	}).
	otherwise({
	    redirectTo: '/home'
	});
}]);
