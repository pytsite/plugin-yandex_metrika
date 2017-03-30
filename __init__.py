"""Yandex Metrika Pytsite Plugin
"""

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def _init():
    from pytsite import lang, tpl, permissions, settings, events, router
    from . import _settings_form, _eh

    # Resources
    lang.register_package(__name__, alias='yandex_metrika')
    tpl.register_package(__name__, alias='yandex_metrika')

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


_init()
