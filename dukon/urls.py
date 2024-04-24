from django.urls import path
from .views import home_view, about_view, contact_view,product_view, testimonial_view

# urlpatterns = [
#     path('', home_view, name="home-page"),
#     path('about/', about_view, name="about-page"),
#     path('contact/', contact_view, name="contact-page"),
#      path('product/', product_view, name="contact-page"),
# ]

urlpatterns = [
    path('', home_view, name="home-page"),
    path('about/', about_view, name="about-page"),
    path('contact/', contact_view, name="contact-page"),
    path('product/', product_view, name="product-page"),
    path('testimonial/', testimonial_view, name="testimonial-page"),
]


