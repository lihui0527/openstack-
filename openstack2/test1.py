# -*- coding: utf-8 -*-
from django.shortcuts import render
from glanceclient import Client
from keystoneclient.v3 import client
from glanceclient.v2 import client as glclient
from keystoneauth1.identity import v3
from novaclient import client as nvclient
from keystoneauth1 import session
from keystoneauth1 import loading
conn = client.Client(user_domain_name="default",
                      username="admin",
                     password="123456",
                     project_domain_name="default",
                      project_name="admin",
                      auth_url="http://localhost:5000/v3")
project=conn.projects.list()
token=conn.auth_token
loader = loading.get_plugin_loader('password')
auth = loader.load_from_options(
    auth_url="http://localhost:5000/v3",
    username="admin",
    password="123456",
    project_name="admin",
    user_domain_name="default",
    project_domain_name="default"
)
session = session.Session(auth=auth)
glance = Client('2', session=session)
nova = nvclient.Client(2,session=session)
image=glance.images.list()
a=[]
for image in glance.images.list():
    a.append(image)
flavor= nova.flavors.list()
f1=nova.flavors.find(name="m1.small")
f2=nova.networks.list()
print(a[0].id)
#instance = nova.servers.create(
 #       name="1234",
  #      min_count=2,
   #     key_name="123456",

    #    availability_zone="nova",
     #   image=a[1],
      #  flavor=f1,
       # nics=[{'net-id':'85b82084-c557-40b6-aeaa-840a974818d5'}]
#)
#network="85b82084-c557-40b6-aeaa-840a974818d5"
ll=nova.servers.list()
#print(ll[0].state)
#nova.servers.start(server="c37c981e-1b84-4b62-a73b-ff1fe461b899"
#)
n=len(ll)
l=[]
for i in range(n):
    l.append(ll[i].image)
#print(l)
#for j in range(n):
 #   print(l[j].id)
#print(image)
#print(flavor)
#print(f1)
#镜像创建
image1 = glance.images.create(name="mage",
                             token=token,disk_format='qcow2',container_format='bare'
)
#glance2=glance.images.get(image1.id)
#glance1=glance.images.delete(image1.id)
#使用token认证glance
#glance=glclient.Client('http://localhost:9292',
#			token=token
 #                         )
#image=glance.images.list()
#a=[]
#for image in glance.images.list():
 #   a.append(image)
#b=a[1].id
#镜像下载
glance.images.upload(image1.id,open('n.img','rb'))
#glance.images.delete(b)
#image1=glance.images.get(id)
#image1 = glance.images.create(name='fff')
#a

#conn.roles.create(name='1x223'
 #                 )#鍒涘缓瑙掕壊
 #鍒涘缓鐢ㄦ埛
#tenants = conn.domains.list()
#projects=conn.projects.list()
#role=conn.roles.list()
#m=conn.roles.get('f8864aca1992448990c01a974798c90f')
#修改角色名字
#conn.roles.update(role='f8864aca1992448990c01a974798c90f',
#name="1234")
#修改项目名字
#conn.projects.update(project='d8b3f38b5f6e4b10b28b34cba6995714',
#name="1234",
#description="1234"
#)
#conn.users.create(name="124",
 #                 password="123456",
 #	          domain=tenants[0].id,
#		  email=None,
#		  desciption=None,
#	 	  enabled=True,
#		  )#创建用户        
#创建项目a
#创建组:wq

#conn.groups.create(name="12",
 #                       description="124",
  #                    domain=tenants[0].id
   #                 )
#conn.projects.create(name="12",
#                      domain=tenants[0].id,
#			description="124"
#
#                    )       
#role=conn.roles.get('38c1a06ef8da4255a06614e67ca76677')
#role.delete()#闁荤喐鐟︾敮鐔哥珶婵犲洤绀嗛柣妯肩帛閻濓拷
#role1=conn.projects.get('33668bc528a24c1b8f101b276e0e3b76')
#role1.delete()#婵＄偑鍊曞﹢鍗灻烘导鏉戠闁绘绮悵锟�
#role2=conn.users.get('42c315f3395d42269b2423680cb256ee')
#role2.delete()#闂佺儵鍋撻崝宥夊春濞戙垹绀嗛柣妯肩帛閻濓拷
#role3=conn.groups.get('0e17f3a5340f4e76a0d0160113bc3dfb')
#role3.delete()#婵炴垶鎹侀褔宕硅ぐ鎺撯挃闁跨噦鎷�
#m= projects.ProjectManager(
#    name="123",
#    domain="default",
#    description=None,
#    enabled=True,
#    parent=None
 #              ) 
