# menutree

Task :
You need to make a django app that will implement a tree menu, observing the following conditions:
1) The menu is implemented through the template tag
2) Everything above the selected item is expanded. 
The first level of nesting under the selected item is also expanded.
3) Stored in the database.
4) Edited in the standard Django admin
5) The active menu item is determined based on the URL of the current page
6) There can be several menus on one page. They are identified by name.
7) When you click on the menu, you go to the URL specified in it. 
The URL can be specified either explicitly or via named url.
8) To draw each menu, exactly 1 query to the database is required
  We need django-app, which allows you to add menus (one or more) to the database through the admin panel, 
  and draw menus by name on any desired page.
  {% draw_menu 'main_menu' %}
  When doing the job from libraries, you should only use Django and the Python standard library.

Задача :
Нужно сделать django app, который будет реализовывать древовидное меню, соблюдая следующие условия:
1) Меню реализовано через template tag
2) Все, что над выделенным пунктом - развернуто. Первый уровень вложенности под выделенным пунктом тоже развернут.
3) Хранится в БД.
4) Редактируется в стандартной админке Django
5) Активный пункт меню определяется исходя из URL текущей страницы
6 )Меню на одной странице может быть несколько. Они определяются по названию.
7) При клике на меню происходит переход по заданному в нем URL. URL может быть задан как явным образом, так и через named url.
8)На отрисовку каждого меню требуется ровно 1 запрос к БД
 Нужен django-app, который позволяет вносить в БД меню (одно или несколько) через админку, и нарисовать на любой нужной странице меню по названию.
 {% draw_menu 'main_menu' %}
 При выполнении задания из библиотек следует использовать только Django и стандартную библиотеку Python.
