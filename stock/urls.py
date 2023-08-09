from django.urls import path

from stock import views

urlpatterns=[

    path('',views.main,name="main"),
    path('add_and_manage_expert',views.add_and_manage_expert,name="add_and_manage_expert"),
    path('add_complaint',views.add_complaint,name="add_complaint"),
    path('add_expert', views.add_expert, name="add_expert"),
    path('add_notification',views.add_notification,name="add_notification"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('ask_doubt',views.ask_doubt,name="ask_doubt"),
    path('block_unblock',views.block_unblock,name="block_unblock"),
    path('expert_add',views.expert_add,name="expert_add"),
    path('expert_home',views.expert_home,name="expert_home"),
    path('notifications',views.notifications,name="notifications"),
    path('register',views.register,name="register"),
    path('reply',views.reply,name="reply"),
    path('send_complaint',views.send_complaint,name="send_complaint"),
    path('send_doubt_reply',views.send_doubt_reply,name="send_doubt_reply"),
    path('send_doubts',views.send_doubts,name="send_doubts"),
    path('send_ratings',views.send_ratings,name="send_ratings"),
    path('send_tips',views.send_tips,name="send_tips"),
    path('tips_send_user',views.tips_send_user,name="tips_send_user"),
    path('user_home',views.user_home,name="user_home"),
    path('user_rating',views.user_rating,name="user_rating"),
    path('view_complaint',views.view_complaint,name="view_complaint"),
    path('view_doubts_and_reply', views.view_doubts_and_reply, name="view_doubts_and_reply"),
    path('view_expert', views.view_expert, name="view_expert"),
    path('view_notification', views.view_notification,name="view_notification"),
    path('view_rating', views.view_rating, name="view_rating"),
    path('view_rating_expert', views.view_rating_expert, name="view_rating_expert"),
    path('view_tips', views.view_tips, name="view_tips"),
    path('regcode',views.regcode,name="regcode"),
    path('logincode',views.logincode,name="logincode"),
    path('expertcode',views.expertcode,name="expertcode"),
    path('addnoticode',views.addnoticode,name="addnoticode"),
    path('addtipcode',views.addtipcode,name="addtipcode"),
    path('addsendrating',views.addsendrating,name="addsendrating"),
    path('expert_edit/<int:id>',views.expert_edit,name="expert_edit"),
    path('exeditcode',views.exeditcode,name="exeditcode"),
    path('exdeletecode/<int:id>',views.exdeletecode,name="exdeletecode"),
    path('notification_edit/<int:id>',views.notification_edit,name="notification_edit"),
    path('notieditcode',views.notieditcode,name="notieditcode"),
    path('notidelcode/<int:id>',views.notidelcode,name="notidelcode"),
    path('blockuser/<int:id>',views.blockuser,name="blockuser"),
    path('unblockuser/<int:id>',views.unblockuser,name="unblockuser"),
    path('addsenddoubt',views.addsenddoubt,name="addsenddoubt"),
    path('addcomplaintcode',views.addcomplaintcode,name="addcomplaintcode"),
    path('viewratingcode',views.viewratingcode,name="viewratingcode"),
    path('complaintreply',views.complaintreply,name="complaintreply"),
    path('rep/<int:id>',views.rep,name="rep"),
    path('repl/<int:id>',views.repl,name="repl"),
    path('doubtreply',views.doubtreply,name="doubtreply"),
    path('logout',views.logout,name="logout"),
    path('forecasting',views.forecasting,name="forecasting"),



























]