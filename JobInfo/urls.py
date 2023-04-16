from django.urls import path

from JobInfo import views
from JobInfo.views import user_signup, user_login, company_signup, company_login, job_search, apply_job, create_job, \
    update_job, admin_signup, admin_login, view_applicants, pending_jobs, change_status, accepted_jobs, all_companies, \
    delete_company

urlpatterns = [
    # Applicant
    path('user_signup/', user_signup),
    path('user_login/', user_login),
    path('job_search/', job_search),
    path('apply_job/', apply_job),
    # Company
    path('company_signup/', company_signup),
    path('company_login/', company_login),
    path('create_job/', create_job),
    path('edit_job/', update_job),
# Admin
    path('admin_signup/', admin_signup),
    path('admin_login/', admin_login),
    path('view_applicant/', view_applicants),
    path('pending_jobs/', pending_jobs),
    path('change_status/', change_status),
    path('accepted_jobs/', accepted_jobs),
    path('all_companies/', all_companies),
    path("delete_company/<int:myid>/", delete_company, name="delete_company"),
]