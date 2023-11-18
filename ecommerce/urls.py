from django.contrib import admin
from django.urls import path,include
from ecom import views
from django.contrib.auth.views import LoginView,LogoutView
from django.conf import settings
from django.conf.urls.static import static
import ecomadmin
from ecomadmin import AdminViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('logout', LogoutView.as_view(template_name='ecom/logout.html'),name='logout'),
    path('aboutus', views.aboutus_view),
    path('contactus', views.contactus_view,name='contactus'),
    path('search', views.search_view,name='search'),
    path('send-feedback', views.send_feedback_view,name='send-feedback'),
    path('view-feedback', views.view_feedback_view,name='view-feedback'),

    path('adminclick', views.adminclick_view),
    path('adminlogin', LoginView.as_view(template_name='ecom/adminlogin.html'),name='adminlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),

    path('view-customer', views.view_customer_view,name='view-customer'),
    path('delete-customer/<int:pk>', views.delete_customer_view,name='delete-customer'),
    path('update-customer/<int:pk>', views.update_customer_view,name='update-customer'),

    path('admin-products', views.admin_products_view,name='admin-products'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('admin-view-booking', views.admin_view_booking_view,name='admin-view-booking'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-order/<int:pk>', views.update_order_view,name='update-order'),


    path('customersignup', views.customer_signup_view),
    path('customerlogin', LoginView.as_view(template_name='ecom/customerlogin.html'),name='customerlogin'),
    path('customer-home', views.customer_home_view,name='customer-home'),
    path('my-order', views.my_order_view,name='my-order'),
    path('my-profile', views.my_profile_view,name='my-profile'),
    path('edit-profile', views.edit_profile_view,name='edit-profile'),
    path('download-invoice/<int:orderID>/<int:productID>', views.download_invoice_view,name='download-invoice'),


    path('add-to-cart/<int:pk>', views.add_to_cart_view,name='add-to-cart'),
    path('cart', views.cart_view,name='cart'),
    path('remove-from-cart/<int:pk>', views.remove_from_cart_view,name='remove-from-cart'),
    path('customer-address', views.customer_address_view,name='customer-address'),
    path('payment-success', views.payment_success_view,name='payment-success'),

    path('product/<int:pk>/', views.product_page, name='product-page'),
    path('main-page', views.main_page_view,name='main-page'),

    path('admindashboard/', include('ecomadmin.adminurls', namespace='ecomadmin')),

    # ----------------------------------------------------------------
    
    path('customadmin/', ecomadmin.views.adminLogin,name="admin_login"),
    path('demo',ecomadmin.views.demoPage),
    path('demoPage',ecomadmin.views.demoPageTemplate),
    path('admin_login_process',ecomadmin.views.adminLoginProcess,name="admin_login_process"),
    path('admin_logout_process',ecomadmin.views.adminLogoutProcess,name="admin_logout_process"),

    # PAGE FOR ADMIN
    path('admin_home',ecomadmin.AdminViews.admin_home,name="admin_home"),

    #Merchant User
    path('merchant_create',ecomadmin.AdminViews.MerchantUserCreateView.as_view(),name="merchant_create"),
    path('merchant_list',ecomadmin.AdminViews.MerchantUserListView.as_view(),name="merchant_list"),
    path('merchant_update/<slug:pk>',ecomadmin.AdminViews.MerchantUserUpdateView.as_view(),name="merchant_update"),

    #Products
    path('product_create',ecomadmin.AdminViews.ProductView.as_view(),name="product_view"),
    path('product_list',ecomadmin.AdminViews.ProductListView.as_view(),name="product_list"),
    path('product_edit/<str:product_id>',ecomadmin.AdminViews.ProductEdit.as_view(),name="product_edit"),
    path('product_add_media/<str:product_id>',ecomadmin.AdminViews.ProductAddMedia.as_view(),name="product_add_media"),
    path('product_edit_media/<str:product_id>',ecomadmin.AdminViews.ProductEditMedia.as_view(),name="product_edit_media"),
    path('product_media_delete/<str:id>',ecomadmin.AdminViews.ProductMediaDelete.as_view(),name="product_media_delete"),
    path('product_add_stocks/<str:product_id>',ecomadmin.AdminViews.ProductAddStocks.as_view(),name="product_add_stocks"),
    path('file_upload',ecomadmin.AdminViews.file_upload,name="file_upload"),

    #Staff User
    path('staff_create',ecomadmin.AdminViews.StaffUserCreateView.as_view(),name="staff_create"),
    path('staff_list',ecomadmin.AdminViews.StaffUserListView.as_view(),name="staff_list"),
    path('staff_update/<slug:pk>',ecomadmin.AdminViews.StaffUserUpdateView.as_view(),name="staff_update"),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
