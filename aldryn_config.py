# -*- coding: utf-8 -*-
from aldryn_client import forms


class Form(forms.BaseForm):

    def to_settings(self, data, settings):
        # settings['ADDON_URLS_I18N'].insert(0, 'divio_wagtail_puput.urls')
        return settings
