from authentication import views as auth_views
from callback import views as callback_views
from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView
from djoser import urls
from djoser import views as djoser_views
from djoser.urls import authtoken
from extract import views as extract_views
from oauth import views as oauth_views
from plans import views as plan_views
from rentability import views as rentability_views
from sales import views as sales_views
from simulator import views as simulator_views
from swagger import views as swagger_views

from rest_framework_expiring_authtoken import views

admin.autodiscover()

urlpatterns = [

    # url(r'^auth/', include('djoser.urls.authtoken')),

    # callback urls
    url(r'^v1/callback/config/$',
        oauth_views.OauthRegisterCallbackConfigView.as_view(),
        name='callback-config'),

    url(r'^v1/callback/config/url/$',
        oauth_views.OauthRegisterCallbackRegisterView.as_view(),
        name='callback-config-url'),

    url(r'^v1/callback/refund/$',
        callback_views.RefundCallbackView.as_view(),
        name='callback-refund-view'),

    # extract urls
    url(r'^v1/extract/$',
        extract_views.ExtractConsultView.as_view(),
        name='extract-consult'),

    # sales urls
    url(r'^v1/sales/proposal/$',
        sales_views.ProposalView.as_view(),
        name='proposal-view'),

    url(r'^v1/sales/consult/$',
        sales_views.ProposalConsultView.as_view(),
        name='proposal-consult-view'),

    url(r'^v1/sales/ticket/$',
        sales_views.TicketView.as_view(),
        name='ticket-view'),

    # sales update urls
    url(r'^v1/sales/participant/update/$',
        sales_views.ProposalParticipantUpdate.as_view(),
        name='participant-update-view'),

    url(r'^v1/sales/address/update/$',
        sales_views.ProposalAddresssUpdate.as_view(),
        name='participant-address-view'),

    url(r'^v1/sales/retirement/update/$',
        sales_views.ProposalRetirementUpdate.as_view(),
        name='participant-retirement-view'),

    url(r'^v1/sales/beneficiary/update/$',
        sales_views.ProposalBeneficiaryUpdate.as_view(),
        name='beneficiary-update-view'),

    url(r'^v1/sales/redemption/$',
        sales_views.RedemptionlView.as_view(),
        name='redemption-view'),

    # BB views
    url(r'^v1/simulation/bb/$',
        simulator_views.SimulatorViewBB.as_view(),
        name='bb-simulation-view'),

    url(r'^v1/sales/bb/$',
        sales_views.SaleViewBB.as_view(),
        name='bb-sales-view'),


    # auth urls
    url(r'^v1/auth/change-password/',
        auth_views.CustomSetPasswordView.as_view(),
        name='password-change'),

    url(r'^v1/auth/register/',
        auth_views.CustomRegistrationView.as_view(),
        name='registration'),

    url(r'^v1/auth/reset-password/',
        auth_views.CustomPasswordResetView.as_view(),
        name='password-reset'),

    url(r'^v1/auth/login/$',
        auth_views.CustomLoginView.as_view(),
        name='login'),

    url(r'^v1/auth/forgot-password/$',
        auth_views.ForgotPasswordView.as_view(),
        name='forgot-password'),

    url(r'^v1/auth/registration-update/$',
        auth_views.RegistrationUpdateView.as_view(),
        name='registration-update'),

    url(r'^v1/auth/security-questions/$',
        auth_views.SecurityQuestionsView.as_view(),
        name='security-question'),

    url(r'^v1/auth/email-validation/$',
        auth_views.EmailValidationView.as_view(),
        name='email-validation'),

    url(r'^v1/auth/email-confirmation-link/$',
        auth_views.EmailConfirmationLink.as_view(),
        name='email-confirmation-link'),

    url(r'^v1/auth/email-confirmation-link/resend/$',
        auth_views.EmailConfirmationLinkResend.as_view(),
        name='email-confirmation-link-resend'),

    url(r'^v1/auth/me/$',
        auth_views.MeView.as_view(),
        name='user-details'),

    url(r'^v1/plans/update/$',
        plan_views.PlanUpdateView.as_view(),
        name='plans-update'),

    url(r'^v1/plans/list/$',
        plan_views.PlanView.as_view(),
        name='plans-list'),

    url(r'^v1/plans/income-report/$',
        plan_views.IncomeReportView.as_view(),
        name='income-report'),

    url(r'^v1/rentability/list/$',
        rentability_views.RentabilityView.as_view(),
        name='rentability-list'),

    # url(r'^v1/rentability/teste/$',
    # rentability_views.GeneratePDF.as_view(),
    # name='rentability-test'),

    url(r'^v1/upload/$',
        auth_views.UploadView.as_view(),
        name='upload-image'),

    url(r'^v1/sendemail/$',
        auth_views.SendEmailView.as_view(),
        name='send-email'),

    url(r'^v1/auth/password-registration/$',
        auth_views.PasswordRegistrationView.as_view(),
        name='password-registration'),

    url(r'^v1/auth/email-confirmation/$',
        auth_views.EmailConfirmationView.as_view(),
        name='email-confirmation'),

    url(r'^v1/auth/code-checker/$',
        auth_views.CodeCheckerView.as_view(),
        name='code-checker'),

    url(r'^v1/auth/data-update/$',
        auth_views.DataUpdateView.as_view(),
        name='data-update'),

    # health check url
    url(r'^ht/', include('health_check.urls')),

    url(r'^v1/swagger.json', swagger_views.SwaggerView.as_view()),

    # Simulator
    url(r'^v1/simulator/$',
        simulator_views.SimulatorView.as_view(),
        name='simulator'),

    # IR Simulator
    url(r'^v1/simulator/ir/$',
        simulator_views.SimulatorIncomeReport.as_view(),
        name='SimulatorIncomeReport'),

    # TODO REMOVE THIS
    url(r'^v1/auth/exploit/',
        auth_views.CustomExploitView.as_view(),
        name='exploit'),

    # admin urls
    # url(r'^admin/', include(admin.site.urls)),

    # email template urls
    url(r'teste/welcome/$',
        TemplateView.as_view(template_name='email/welcome.html')),
    url(r'teste/reset-password/$',
        TemplateView.as_view(template_name='email/reset-password.html')),
    url(r'teste/password-updated/$',
        TemplateView.as_view(template_name='email/password-updated.html')),
    url(r'teste/email-validation/$',
        TemplateView.as_view(template_name='email/email-validation.html')),
    url(r'teste/registration-updated/$',
        TemplateView.as_view(template_name='email/registration-updated.html')
        ),
    url(r'teste/email-updated/$',
        TemplateView.as_view(template_name='email/email-updated.html')),
    url(r'teste/email-validation-reminder/$',
        TemplateView.as_view(
            template_name='email/email-validation-reminder.html'))
]
