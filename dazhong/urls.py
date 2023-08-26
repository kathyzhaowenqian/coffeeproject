# -*- coding: utf-8 -*-

from django.contrib import admin
from django.urls import path
from. import views


urlpatterns = [
    path('coffee_store_analysis', views.coffee_store_analysis3),
    path('coffee_store_analysis/pyecharts1', views.pyecharts1),
    path('coffee_store_analysis/pyecharts2', views.pyecharts2),
    path('coffee_store_analysis/pyecharts3', views.pyecharts3),
    path('coffee_store_analysis/countryanalysis', views.countryanalysis),
    path('coffee_store_analysis/piecharts', views.piecharts),
    path('coffee_store_analysis/RegionRankDetailBar', views.RegionRankDetailBar),
    path('coffee_store_analysis/region_boxplot', views.region_boxplot),
    path('coffee_store_analysis/citybrandrank', views.citybrandrank),
    path('coffee_store_analysis/BrandRankDetailBar', views.BrandRankDetailBar),
    path('coffee_vime_video',views.VimeVideo),
    path('coffee_store_analysis_public', views.coffee_store_analysis1),
    ]



