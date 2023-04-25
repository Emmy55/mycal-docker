from django.urls import path

from . import views

urlpatterns = [
    path('', views.layout, name='layout'),
    path('ans', views.ansbook, name='ansbook'),
    path('ans1', views.ansbook1, name='ansbook1'),
    path('ans2', views.ansbook2, name='ansbook2'),
    path('ans3', views.ansbook3, name='ansbook3'),
    path('ans4', views.ansbook4, name='ansbook4'),
    path('ans5', views.ansbook5, name='ansbook5'),
    path('ans7', views.ansbook7, name='ansbook7'),
    path('ans8', views.ansbook8, name='ansbook8'),
    path('varians', views.varians, name='varians'),
    path('quad', views.quad, name='quad'),
    path('simul', views.simul, name='simul'),
    path('addition', views.addition , name='addition'),
    path('area', views.area , name='area'),
    path('inverse', views.inverse , name='inverse'),
    path('inverses', views.inverses , name='inverses'),
    path('joint', views.joint , name='joint'),
    path('joints', views.joints , name='joints'),
    path('partial', views.partial , name='partial'),
    # path('', views. , name=''),
    path('perimeter', views.perimeter , name='perimeter'),
    path('square', views.square , name='square'),
    path('sqrt', views.square_root , name='square_root'),
    path('subtraction', views.subtraction , name='subtraction'),
    path('division', views.division , name='division'),
    path('multiplication', views.multiplication , name='multiplication'),
    path('quadratic', views.quadratic , name='quadratic'),
    path('simultaneous', views.simultaneous , name='simultaneous'),
    path('circle', views.circle , name='circle'),
    path('calculus', views.calculus , name='calculus'),
    path('variation', views.variation , name='variation'),
    path('matrix', views.matrix , name='matrix'),
    path('matt', views.matt, name='matt'),
    path('sqmatt', views.sqmatt, name='sqmatt'),
    path('sqmat', views.sqmat, name='sqmat'),
    path('invmat', views.invmat, name="invmat"),
    path('invmatt', views.invmatt, name="invmatt"),
    path('det', views.det, name="det"),
    path('dett', views.dett, name="dett"),
    path('polygon', views.polygon , name='polygon'),
]


