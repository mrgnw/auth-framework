'use strict';

var controllersModule = angular.module('angularProject.controllers', [])

    .controller('homeCtrl', function ($scope, $http, User, Address, Recipe, Restangular) {

//        $scope.$on('event:login-confirmed', function() {
//            $scope.users = User.query();
//            $scope.addresses = Address.query();
//            $scope.recipes = Recipe.query();
//        });

        $scope.users = User.query();
        $scope.addresses = Address.query();
        //$scope.recipes = Recipe.query(); // Using $http
        Restangular.all('recipes').getList().then(function (response) { // Using Restangular.
            $scope.recipes = response;
        })
    })

    .controller('recipeCtrl', function ($scope, $http, Recipe, $routeParams, Restangular, $window) {
        $scope.recipeID = $routeParams.recipeID;
        Restangular.one('recipes', $scope.recipeID).get().then(function (response) {
            $scope.recipe = response;
            $window.document.title = $scope.recipe.recipe_name;
            $scope.recipe_photo = response.photo;

            Restangular.one('tags', $scope.recipe.tag).get().then(function (response) {
                $scope.tag = response;
            })
        })
    })


    .controller('editRecipeCtrl', function ($scope, $http, Recipe, $routeParams, Restangular, $window){
//        Add a URL route that loads this view
        $scope.recipeID = $routeParams.recipeID;
        Restangular.one('recipes', $scope.recipeID).get().then(function (response) {
            $scope.recipe = response;
            $window.document.title = $scope.recipe.recipe_name;
            $scope.recipe_photo = response.photo;

            Restangular.one('tags', $scope.recipe.tag).get().then(function (response) {
                $scope.tag = response;
            })


//            Edit the recipe

        })
    })

    .controller('addRecipeCtrl', function ($scope, $http, Recipe, $routeParams, Restangular, $window) {

        $scope.recipe = Object();
        $scope.recipeList = null;
        $scope.tag = null;
        $scope.name = null;
        $scope.submitted = false;

        Restangular.all('tags').getList().then(function (response) {
            $scope.tags = response;
        });


        Restangular.all('recipelists').getList().then(function (response) {
            $scope.recipeLists = response;
        });


        $scope.uploadFile = function (files) {
            $scope.recipe.photo = files[0];
            alert(files[0])
        }

        $scope.save = function () {
            if ($scope.submitted == false) {
                $scope.recipe.recipe_name = $scope.name;

//                alert($scope.photo);
                $scope.recipe.recipe_description = $scope.description;
                $scope.recipe.recipe_prep_time = $scope.prep;
                $scope.recipe.recipe_cook_time = $scope.cook;
                $scope.recipe.recipe_total_time = $scope.total;
                $scope.recipe.tag = $scope.tag;
                $scope.recipe.recipe_list = $scope.recipeList;
                $scope.recipe.user = 1;
//                Restangular.one('recipes').customPOST($scope.recipe).then(function (data) {
//                    $scope.submitted = true;
//                });

                var fd = new FormData();
                //Take the first selected file
                fd.append("recipe_name", $scope.recipe.recipe_name);
                fd.append("user", 1);
                fd.append("tag", $scope.recipe.tag);
                fd.append("recipe_lists", $scope.recipe.recipe_list);
                fd.append("photo", $scope.recipe.photo);
                alert($scope.recipe.recipe_list);

                $http.post('http://localhost:8001/recipes', fd, {
//                    withCredentials: true,
                    headers: {'Content-Type': undefined },
                    transformRequest: angular.identity
                }).success(alert("Success!")).error(alert("FAILED"))


            }
        }

        $scope.addTag = function () {
            $scope.newTag = Object();
            $scope.newTag.tag_name = $scope.newTagName;


            Restangular.one('tags').customPOST($scope.newTag).then(function (response) {
                $scope.tags.push(response);
            })
        };


        $scope.addList = function () {
            $scope.newList = Object();
            $scope.newList.recipe_list_name = $scope.newListName;


            Restangular.one('recipelists').customPOST($scope.newList).then(function (response) {
                $scope.recipeLists.push(response);
            })
        }
    })

