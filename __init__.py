"""Yandex Metrika Pytsite Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def plugin_load():
    from pytsite import lang, tpl, router
    from plugins import permissions, settings
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__)
    tpl.register_package(__name__)

    # Lang globals
    lang.register_global('yandex_metrika_admin_settings_url',
                         lambda language, args: settings.form_url('yandex_metrika'))

    # Permissions
    permissions.define_permission('yandex_metrika.settings.manage',
                                  'yandex_metrika@manage_yandex_metrika_settings', 'app')

    # Settings
    settings.define('yandex_metrika', _settings_form.Form, 'yandex_metrika@yandex_metrika',
                    'fa fa-line-chart', 'yandex_metrika.settings.manage')

    # Event handlers
    router.on_dispatch(_eh.router_dispatch)
