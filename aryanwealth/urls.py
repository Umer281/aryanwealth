from django.contrib import admin
from django.urls import path
from aryanwealth_website import views
urlpatterns = [

    # path('admin/', admin.site.urls),
    path('', views.indexV , name='home_page'),
    path('index', views.indexV , name='home_page'),
    path('login', views.loginV, name='login_page'),
    path('about', views.aboutV, name="about_us_page"),
    path('complaint', views.complaintV),
    path('contact', views.contactV, name='contact_us_page'),
    path('day_wise_summary_profit_and_loss', views.day_wise_summary_profit_and_lossV),
    path('disclaimer', views.disclaimerV),
    path('faq', views.faqV, name='faq_page'),
    path('mycourses', views.mycoursesV),
    path('past_performance', views.past_performanceV, name='past_performance_page'),

    #path('pastperformance', views.pastperformanceV),
    path('refund', views.refundV),
    path('register', views.registerV, name='register_page'),
    path('services', views.servicesV, name='services_page'),
    path('stock_wise_details_profit_and_loss', views.stock_wise_details_profit_and_lossV),
    path('terms_and_conditions', views.terms_and_conditionsV),
    path('welcome', views.welcomeV),


#------------------------------------------admin pannel code here-------------------------

    path('admin/', admin.site.urls),
    # path('admin/', views.admin_loginV, name='admin_login'),
    path('admin/dashboard', views.admin_dashboardV),
    path('admin/total_user', views.admin_total_userV),
    path('admin_table', views.admin_tableV,name="admin_table"),
    # path('admin/swing', views.swingV),
    path('admin/change_password', views.admin_change_passwordV),
    #path('admin/logout', views.logoutV),
    path('dashboard', views.admin_tableV,name="admin_table"),
    
    path('addtouser/<i_id>', views.addtouser, name='addtouser'),
    path('edit/<i_id>', views.edit, name='edit'),

    path('users_table', views.users_tableV),
    path('users/ajaxdata', views.ajaxdata, name='ajaxdata'),
    path('admin_home', views.admin_home,name="admin_home"),

    path('delete/<int:id>', views.delete, name='delete'),

    # path('admin/', views.admin_loginV, name='admin_login'),

    path('admin/swing', views.admin_swing),

    path('users/swing', views.users_swing),
    path('users/table', views.users_tableV),

    path('day_wise_summary_profit_and_loss', views.day_wise_summary_profit_and_lossV,name='day_wise_summary_profit_and_loss'),

    path('stock_wise_details_profit_and_loss', views.stock_wise_details_profit_and_lossV,name='stock_wise_summary_profit_and_loss'),

]