# -*- coding: utf-8 -*-
from flask_admin import Admin
from flask_admin.menu import MenuLink
from flask_admin.contrib.sqla import ModelView

from admin.Views import HomeView, UserView

from models.Weapon import Brand, Category, Equipaments, Weapon, WeaponRating, UserWeapon
from models.User import User, Role, Patent, Team

def start_views(app, db):
    admin = Admin(app, name='Meu Operador', base_template='admin/base.html', template_mode='bootstrap3', index_view=HomeView())
    admin.add_view(ModelView(Role, db.session, "Funções",  category="Usuários"))
    admin.add_view(UserView(User, db.session, "Usuários", category="Usuários"))
    admin.add_view(ModelView(Patent, db.session, "Patentes", category="Equipes"))
    admin.add_view(ModelView(Team, db.session, "Equipes", category="Equipes"))
    admin.add_view(ModelView(Brand, db.session, "Marcas", category="Armas"))
    admin.add_view(ModelView(Category, db.session, "Categoria de armas", category="Armas"))
    admin.add_view(ModelView(Weapon, db.session, "Armas", category="Armas"))
    admin.add_view(ModelView(WeaponRating, db.session, "Avaliações", category="Armas"))
    admin.add_view(ModelView(UserWeapon, db.session, "Armas do usuário", category="Armas"))
    admin.add_view(ModelView(Equipaments, db.session, "Upgrades", category="Armas"))

    admin.add_link(MenuLink(name='Logout', url='/_admin/logout'))