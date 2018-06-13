# -*- coding: utf-8 -*-
from aldryn_client import forms

class Form(forms.BaseForm):

    def to_settings(self, data, settings):

        settings['ADDON_URLS'].insert(0, 'divio_wagtail_puput.urls')
        if 'aldryn-wagtail' in settings['INSTALLED_ADDONS']:
            settings['PUPUT_AS_PLUGIN'] = True
            settings['PUPUT_USERNAME_REGEX'] = '\w.+'

        return settings
