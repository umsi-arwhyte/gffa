from __future__ import unicode_literals

# from django.conf.urls import patterns, url, include
from django.contrib import admin
from django.urls import path
# from rest_framework import routers
# from resources import views as resource_views
from . import views


# admin.autodiscover()
# router = routers.DefaultRouter()

# router.register(r"sentient_beings", resource_views.sentient_beingViewSet)
# router.register(r"planets", resource_views.PlanetViewSet)
# router.register(r"films", resource_views.FilmViewSet)
# router.register(r"species", resource_views.SpeciesViewSet)
# router.register(r"vehicles", resource_views.VehicleViewSet)
# router.register(r"starships", resource_views.StarshipViewSet)


# urlpatterns = patterns("",
#     url(r"^admin/", include(admin.site.urls)),
#     url(r"^$", "swapi.views.index"),
#     url(r"^documentation$", "swapi.views.documentation"),
#     url(r"^about$", "swapi.views.about"),
#     url(r"^stats$", "swapi.views.stats"),
#     url(r"^stripe/donation", "swapi.views.stripe_donation"),
#     url(r"^api/sentient_beings/schema$", "resources.schemas.sentient_beings"),
#     url(r"^api/planets/schema$", "resources.schemas.planets"),
#     url(r"^api/films/schema$", "resources.schemas.films"),
#     url(r"^api/species/schema$", "resources.schemas.species"),
#     url(r"^api/vehicles/schema$", "resources.schemas.vehicles"),
#     url(r"^api/starships/schema$", "resources.schemas.starships"),
#     url(r"^api/", include(router.urls)),
# )

urlpatterns = [
    # path(r"^admin/", include(admin.site.urls)),
    path('', views.HomePageView.as_view(), name='home'),
    path('contributers/', views.ContributerPageView.as_view(), name='contributers'),
    path('docs/', views.DocsPageView.as_view(), name='docs'),
    path('about/', views.AboutPageView.as_view(), name='about'),
    path('root/', views.RootPageView.as_view(), name='root'),
    path('films/', views.FilmListView.as_view(), name='films'),
    path('films/new/', views.FilmCreateView.as_view(), name='film_new'),
    path('films/<int:pk>/', views.FilmDetailView.as_view(), name='film_detail'),
    path('films/<int:pk>/delete/', views.FilmDeleteView.as_view(), name='film_delete'),
    path('films/<int:pk>/update/', views.FilmUpdateView.as_view(), name='film_update'),
    path('films_docs/', views.FilmPageView.as_view(), name='film_docs'),
    path('planets/', views.PlanetListView.as_view(), name='planets'),
    path('planets/new/', views.PlanetCreateView.as_view(), name='planet_new'),
    path('planets/<int:pk>/', views.PlanetDetailView.as_view(), name='planet_detail'),
	path('planets/<int:pk>/delete/', views.PlanetDeleteView.as_view(), name='planet_delete'),
	path('planets/<int:pk>/update/', views.PlanetUpdateView.as_view(), name='planet_update'),
    path('planets_docs/', views.PlanetPageView.as_view(), name='planet_docs'),
    path('sentient_beings/', views.SentientBeingListView.as_view(), name='sentient_beings'),
    # path('sentient_beings/new/', views.SentientBeingCreateView.as_view(), name='sentient_beings_new'),
    path('sentient_beings/<int:pk>/', views.SentientBeingDetailView.as_view(), name='sentient_being_detail'),
    # path('sentient_beings/<int:pk>/delete/', views.SentientBeingDeleteView.as_view(), name='sentient_beings_delete'),
	# path('sentient_beings/<int:pk>/update/', views.SentientBeingUpdateView.as_view(), name='sentient_beings_update'),
    path('sentient_beings_docs/', views.SentientBeingPageView.as_view(), name='sentient_being_docs'),
    path('vehicles/', views.VehicleListView.as_view(), name='vehicles'),
    path('vehicles/new/', views.VehicleCreateView.as_view(), name='vehicle_new'),
	path('vehicles/<int:pk>/', views.VehicleDetailView.as_view(), name='vehicle_detail'),
	path('vehicles/<int:pk>/delete/', views.VehicleDeleteView.as_view(), name='vehicle_delete'),
	path('vehicles/<int:pk>/update/', views.VehicleUpdateView.as_view(), name='vehicle_update'),
    path('vehicles_docs/', views.VehiclePageView.as_view(), name='vehicle_docs'),
    # path(r"^stats$", "swapi.views.stats"),
    # path(r"^stripe/donation", "swapi.views.stripe_donation"),
     # path(r"^api/films/schema$", "resources.schemas.films"),
    # path(r"^api/sentient_beings/schema$", "resources.schemas.sentient_beings"),
    # path(r"^api/planets/schema$", "resources.schemas.planets"),
    # path(r"^api/vehicles/schema$", "resources.schemas.vehicles"),
    # path(r"^api/", include(router.urls)),
]
