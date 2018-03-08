# Tour Lead CRUD Test

## Overview

This test is for a simple Django CRUD views to add, edit and display tour leaders.

UI mockup is in [crud-test.html](crud-test.html).

Just implement as much functionality as you can in a time-box of 2 hours focusing fist on quality rather than quantity.

There're a lot of requirements so you're not expected to complete all of them, implement what you can and do it well,
And don't leave half implemented code and functionality, remove anything that's not completely finished in the final result.

At least the fist function (Add Lead) has to be implemented perfectly from every perspective (function, logic, code quality, tests, UX).

## Functionality to implement (in order of priority)

### 1. Add Tour Lead view

![](https://raw.githubusercontent.com/lucifurtun/crud-test/master/images/1.png)


Fields:

* Name
    - Required
* Gender
    - Required
    - Widget: Horizontal radio buttons
* Languages
    - Required: at least one language should be added
    - Widget: Dropdown
* Card number
    - Length: 8-15
    - Only numbers and capital letters: X, T, W are allowed
* Expiry date
    - Required if Card number is not empty
    - Has to be at least 6 months into the future
    - Widget: Datepicker
* Professional
    - Required
    - Widget: horizontal radio buttons

### 2. Tour Leads List view

![](https://raw.githubusercontent.com/lucifurtun/crud-test/master/images/2.png)

### 3. Edit Tour Lead view

Same as add

### 4. Tour Lead Detail view

![](https://raw.githubusercontent.com/lucifurtun/crud-test/master/images/3.png)

### 5. Delete Tour Lead

![](https://raw.githubusercontent.com/lucifurtun/crud-test/master/images/4.png)

### 6. Pagination

![](https://raw.githubusercontent.com/lucifurtun/crud-test/master/images/5.png)

### 7. Batch Delete

![](https://raw.githubusercontent.com/lucifurtun/crud-test/master/images/6.png)

## Project setup

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Run django server:

```
python manage.py runserver
```

3. Open http://localhost:8000/leads/ in a browser

## Good Luck!
