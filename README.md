# rest-framework-with-unittest
Django Rest Framework ( Test Driven Development )
<h2>Installation</h2>
<pre>$ pip install djangorestframework</pre>
<h2>Usage</h2>
<b>Update setting.py</b>
<i>settings.py</i>
<pre> 
# REST Framework
INSTALLED_APPS = [
'rest_framework'
]
REST_FRAMEWORK = {    
    'DEFAULT_PERMISSION_CLASSES': [],
    'TEST_REQUEST_DEFAULT_FORMAT': 'json'
}
</pre>
<b>Create the Database</b>

<pre>
python manage.py makemigrations
python manage.py migrate
</pre>

<h2>Unit Tests</h2>
<b>Run tests</b>
<pre>
python manage.py test
</pre>
