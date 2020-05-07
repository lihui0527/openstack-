from django.shortcuts import render
from keystoneclient.v3 import client
from django.template.loader import get_template
from django.http import HttpResponse
from keystoneclient import session
import glanceclient
import glanceclient.v2.client as glclient
conn = client.Client(user_domin_name="default",
                         username="admin",
                         password="123456",
                         project_domain_name="default",
                         project_name="admin",
                         auth_url="http://localhost:5000/v3")
project=conn.users.list()   
print(project)
