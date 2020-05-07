# -*- coding: utf-8 -*-
from django.shortcuts import render
from keystoneclient.v3 import client
from django.template.loader import get_template
from django.http import HttpResponse
from keystoneauth1.identity import v3
import glanceclient.v2.client as glclient
from keystoneauth1 import session
from keystoneauth1 import loading
from novaclient import client as nvclient
from glanceclient import Client
conn = client.Client(user_domain_name="default",
                     username="admin",
                   password="123456",
                   project_domain_name="default",
                   project_name="admin",
                    auth_url="http://localhost:5000/v3")
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(
    auth_url="http://localhost:5000/v3",
    username="admin",
    password="123456",
    project_name="admin",
    user_domain_name="default",
    project_domain_name="default"
)

token=conn.auth_token
session = session.Session(auth=auth)
glance = Client('2', session=session)
#glance=glclient.Client('http://localhost:9292',
#			token=token
#                          )
nova = nvclient.Client(2,session=session)                    
project = conn.projects.list()  
user=conn.users.list()
server=nova.servers.list()
tenants = conn.domains.list()  
image=glance.images.list()
a=[]
for image in glance.images.list():
    a.append(image)
flavor= nova.flavors.list()
f1=nova.flavors.find(name="m1.tiny")
f2=nova.networks.list()                
def ll(request):
    template = get_template('openstack2/index1.html')
    html = template.render(locals())
    return HttpResponse(html)


def add(request):
    a = request.POST['username']
    return HttpResponse(a)
def Project(request):
    project = conn.projects.list()
    return render(request, 'openstack2/admin.html', {'projects': project})

def Projects(request):
    username = request.POST['username']
    password = request.POST['password']
    conn = client.Client(user_domain_name="default",
                         username=username,
                         password=password,
                         project_domain_name="default",
                         project_name="admin",
                         auth_url="http://controller:5000/v3")
    project = conn.projects.list()
    token = conn.auth_token
    return render(request, 'openstack2/admin.html', {'projects': project})
    # template=get_template(request,'openstack2/index.html',{'projects':project})


# html=template.render(locals())
# print(project)
# return HttpResponse(html)
def get_keystone_creds():
    d = {}
    d['username'] = os.environ['OS_USERNAME']
    d['password'] = os.environ['OS_PASSWORD']
    d['auth_url'] = os.environ['OS_AUTH_URL']
    d['tenant_name'] = os.environ['OS_TENANT_NAME']
    return d

###################项目
def Del(request):
    id = request.GET['id']
    if id=="fcae570c3b0d456cb4057ab515599eaf" or id=="bef382a6c49a438786110411d98dcfad" or id=="6ec1b6a5f4044069acc47e8bacf53a49":
        return HttpResponse("这是管理员，不能删除")
    else:
        role1 = conn.projects.get(id)
        role1.delete()
        project = conn.projects.list()        
        return render(request, 'openstack2/admin.html', {'projects': project})
def Createproject(request):
 #   conn.projects.create(name="12",
  #                    domain=tenants[0].id,
#			          description="124"
 #                   )  
    return render(request, 'openstack2/create.html')
def Zeng(request):
    name = request.POST['name']
    description = request.POST['description']
    conn.projects.create(name=name,
                      domain=tenants[0].id,
			          description=description
                    )
    project = conn.projects.list()  
    return render(request, 'openstack2/admin.html', {'projects': project})
def project_bj(request):
    id = request.GET['id']
    project=conn.projects.get(id)
    projects=[project]
    return render(request, 'openstack2/projrct_bj.html', {'projects': projects})
def Projectbj(request):
    id = request.POST['id']
    name = request.POST['name']
    description = request.POST['description']
    conn.projects.update(project=id,
                 name=name,
                 description=description
                   )
    return render(request, 'openstack2/admin.html', {'projects': project})
##########用户
def User(request):
     user = conn.users.list()
     token = conn.auth_token
     return render(request, 'openstack2/user.html', {'users': user})
##########组
def Group(request):
     group = conn.groups.list()
     token = conn.auth_token     
     return render(request, 'openstack2/group.html', {'groups': group})
##########角色
def Role(request):
     role = conn.roles.list()
     token = conn.auth_token     
     return render(request, 'openstack2/role.html', {'roles': role})
##########实例
def Sl(request):
     server=nova.servers.list()
     for i in server:         
         token = conn.auth_token     
         return render(request, 'openstack2/sx.html', {'servers': server})
def Createsx(request):
    instance = nova.servers.create(
        name="1234",
        min_count=1,
        key_name="123456",

        availability_zone="nova",
        image=a[1],
        flavor=f1,
        nics=[{'net-id':'85b82084-c557-40b6-aeaa-840a974818d5'}]
            )
    return render(request, 'openstack2/admin.html', {'projects': project})
def Qd(request):
    id = request.GET['id']
    server=nova.servers.start(server=id)
    return render(request, 'openstack2/sl.html', {'servers': server})
def gb(request):
    id = request.GET['id']
    nova.servers.stop(server=id)
    return HttpResponse(id)
def sl_del(request):
    id = request.GET['id']
    nova.servers.delete(server=id)
    return HttpResponse(id)
def yx(request):
    image=glance.images.list()
    b=[]
    for image in glance.images.list():
        b.append(image)
    return render(request, 'openstack2/yx.html', {'images': b})
def image_add(request):   
    return render(request, 'openstack2/jing.html', {'projects': project})
def jing(request):
    name = request.POST['name']
    
    image = glance.images.create(name=name,
                             token=token,
                             disk_format='qcow2',
                             container_format='bare'
              )
    glance.images.upload(image.id,open('/home/lihui/mysite/openstack2/n.img','rb'))
    project=glance.images.list()
    return render(request, 'openstack2/yx.html', {'projects': project})
def jing_del(request):   
    id = request.GET['id'] 
    glance.images.delete(id)   
    return render(request, 'openstack2/yx.html', {'projects': project})
def cq(request):
    id = request.GET['id']
    server=nova.servers.reboot(server=id)
    return render(request, 'openstack2/sl.html', {'servers': server})
def sl_bj(request):
    id = request.GET['id']
    server=nova.servers.get(id)
    server1=[server]
    return render(request, 'openstack2/sl_bj.html', {'servers': server1})
def slbj(request):
    id = request.POST['id']
    name = request.POST['name']
   
    nova.servers.update(server=id,
                 name=name,
                 
                   )
    return render(request, 'openstack2/admin.html', {'projects': project})
# Create your views haere.
