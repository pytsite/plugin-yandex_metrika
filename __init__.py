"""Yandex Metrika Pytsite Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load_uwsgi():
    from pytsite import lang, tpl, router
    from plugins import settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('yandex_metrika_admin_settings_url',
                         lambda language, args: settings.form_url('yandex_metrika'))

    # Settings
    settings.define('yandex_metrika', _settings_form.Form, 'yandex_metrika@yandex_metrika', 'fa fa-line-chart', 'dev')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
