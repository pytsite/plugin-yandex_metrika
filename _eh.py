"""PytSite Google Analytics Pplugin Event Handlers.
"""
from pytsite import settings as _settings, assetman as _assetman, tpl as _tpl, auth as _auth, lang as _lang, \
    router as _router

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


def router_dispatch():
    """'pytsite.router.dispatch' handler.
    """
    counter_id = _settings.get('yandex_metrika.counter_id')
    if not counter_id and _auth.get_current_user().has_permission('yandex_metrika.settings.manage'):
        print('--- DONE', _router.request().path)
        _router.session().add_warning_message(_lang.t('yandex_metrika@plugin_setup_required_warning'))
    else:
        _assetman.add_inline(_tpl.render('yandex_metrika@counter', {'counter_id': counter_id}))
