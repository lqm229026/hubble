# -*- encoding: utf-8 -*-
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import api_views, views

urlpatterns = [
    path('snippets/', views.snippet_list),  # regular django api view
    path('snippets/<int:pk>', views.snippet_detail),
    path('api_snippets/', api_views.snippet_list),  # function-based API View
    path('api_snippets/<int:pk>', api_views.snippet_detail),
    path('api_class_snippets/', api_views.SnippetListView.as_view()),  # class-based API View
    path('api_class_snippets/<int:pk>', api_views.SnippetDetailView.as_view()),
    path('api_mixin_snippets/', api_views.SnippetListWithMixin.as_view()),  # class-based API View using mixins
    path('api_mixin_snippets/<int:pk>', api_views.SnippetDetailWithMixin.as_view()),
    path('api_generic_snippets/', api_views.SnippetListWithGeneric.as_view()),  # class-based API View using generics
    path('api_generic_snippets/<int:pk>', api_views.SnippetDetailWithGeneric.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)  # 给view传递format参数表示请求的格式
