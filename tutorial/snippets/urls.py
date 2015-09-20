from django.conf.urls import url,patterns
from snippets import views


urlpatterns = patterns( '',
	url(r'^snippets/$',views.snippet_list),
	url(r'^snippets/(?P<pk>[0-9]+)/$',views.snippet_detail),
)