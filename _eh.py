"""PytSite Google Analytics Pplugin Event Handlers.
"""
from pytsite import tpl as _tpl, lang as _lang, router as _router, reg as _reg
from plugins import assetman as _assetman, auth as _auth

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    counter_id = _reg.get('yandex_metrika.counter_id')
    if not counter_id and _auth.get_current_user().has_permission('yandex_metrika.settings.manage'):
        _router.session().add_warning_message(_lang.t('yandex_metrika@plugin_setup_required_warning'))
    else:
        _assetman.add_inline(_tpl.render('yandex_metrika@counter', {'counter_id': counter_id}))
