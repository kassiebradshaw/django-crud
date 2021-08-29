# Lab 28: Django CRUD and Forms

*Author*: Kassie Bradshaw
[Link to my Pull Request](tbd)

## Overview

Add full CRUD functionality to your bag of tricks by building a Django project that allows creating, reading, updating and deleting.

## Feature Tasks & Requirements

* [x] Create `snacks_crud_project`
* [x] Create `snacks` app
* [x] Create `Snack` model
  * [x] Title field
  * [x] Purchaser field
  * [x] Description field
  * [x] Register model with admin

* [x] Create `SnackListView` that extends appropriate generic view
  * [x] Associated URL path is an empty string

* [x] Create `SnackDetailView` that extends appropriate generic view
  * [x] Associated URL path is `<int:pk>/`

* Create `SnackCreateView` that extends appropriate generic view
  * [x] Associated url path is `create/`

* Create `SnackUpdateView` that extends appropriate generic view
  * [x] Associated url path is `<int:pk>/update/`

* Create `SnackDeleteView` that extends appropriate generic view
  * [x] Associated URL path is `<int:pk>/delete/`

* [x] Add urls to support all views, with appropriate names
* [x] Add templates to support all views
* [x] Add navigation links in appropriate locations to access all pages
* [x] Make all necessary changes to project level files for project to run
  * [x] In other words, make it work.

## Stretch Goals

* [ ] Add multiple models
* [ ] Use an alternate test runner
* [ ] Add more advanced fields to the models, e.g.created timestamp
* [ ] Add styling

## User Acceptance Tests

* [x] Test all Views
* [x] Test Model
  * [x] String representation
  * [x] All fields
