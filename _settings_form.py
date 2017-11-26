"""PytSite Yandex Metrika Plugin Settings Form.
"""
from pytsite import lang as _lang, validation as _validation
from plugins import widget as _widget, settings as _settings

__author__ = 'Alexander Shepetko'
__email__ = 'a@shepetko.com'
__license__ = 'MIT'


class Form(_settings.Form):
    def _on_setup_widgets(self):
        self.add_widget(_widget.input.Number(
            uid='setting_counter_id',
            weight=10,
            label=_lang.t('yandex_metrika@counter_id'),
            required=True,
            help=_lang.t('yandex_metrika@counter_id_setup_help'),
            rules=_validation.rule.Integer()
        ))

        super()._on_setup_widgets()
