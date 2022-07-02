from flask_admin import AdminIndexView, expose
from flask_login import current_user
from flask import redirect, request
from flask_admin.contrib.sqla import ModelView

class GenericView(ModelView):
    form_excluded_columns = ('created_at', 'updated_at',)
    column_exclude_list = ('password', )

    def is_accessible(self):
        if current_user.is_authenticated and current_user.role_id == 1:
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        return redirect(f'/_admin/login?msg=Efetue login para acessar esta área.&msgType=warning&url={request.url_rule}')

class HomeView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin.html')

    def is_accessible(self):
        if current_user.is_authenticated and current_user.role_id == 1:
            return current_user.is_authenticated

    def inaccessible_callback(self, name, **kwargs):
        if current_user.is_authenticated:
            return redirect('/admin')
        return redirect(f'/_admin/login?msg=Efetue login para acessar esta área.&msgType=warning&url={request.url_rule}')


class UserView(GenericView):
    def on_model_change(self, form, User, is_created):
        if 'password' in form:
            if form.password.data is not None:
                User.set_password(form.password.data)
            else:
                del form.password
