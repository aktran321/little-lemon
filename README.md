# little-lemon

URLS TO TEST:

1. Menu Endpoint
   GET, POST,
   http://localhost:8000/restaurant/menu/

2. Single Menu Item Endpoint
   GET, PUT, DELETE
   (needs trailing slash)
   http://localhost:8000/restaurant/menu/<int:pk>/

3. Booking Endpoint
   GET, POST
   http://localhost:8000/restaurant/booking/

4. DJOSER endpoint for token authentication
   http://localhost:8000/auth/

/users/
/users/me/
/users/confirm/
/users/resend_activation/
/users/set_password/
/users/reset_password/
/users/reset_password_confirm/
/users/set_username/
/users/reset_username/
/users/reset_username_confirm/
/token/login/
/token/logout/

5. Django Admin Interface
   http://localhost:8000/admin/

6. Django REST Framework Token Generation
   http://localhost:8000/restaurant/api-token-auth/
   Enter Username and Password to generate a token.
   Must Use Postman

UNIT TESTS:
The unit tests are located in the restaurant app instead of the project directory.
Enter

1. "python manage.py test restaurant.test.test_models"
   and
2. "python manage.py test restaurant.test.test_views"

in the command line to run the tests.
