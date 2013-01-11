from django.conf import settings
from django.conf.urls.defaults import patterns, url
from django.contrib import admin
from django.contrib.admin.util import unquote
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.utils.translation import ugettext_lazy as _


class OrderedModelAdmin(admin.ModelAdmin):
    UP_LINK_FORMAT = '<a href="{url}"><img src="' + settings.STATIC_URL + 'ordered_model/arrow-up.gif" alt="Move up" /></a>'
    DOWN_LINK_FORMAT = '<a href="{url}"><img src="' + settings.STATIC_URL + 'ordered_model/arrow-down.gif" alt="Move down" /></a>'

    @property
    def _model_info(self):
        return '{0}_{1}_'.format(
            self.model._meta.app_label,
            self.model._meta.module_name,
        )

    def get_urls(self):
        return patterns(
            '',
            url(r'^(.+)/move-up/$', self.admin_site.admin_view(self.move_up), name=self._model_info + 'move_up'),
            url(r'^(.+)/move-down/$', self.admin_site.admin_view(self.move_down), name=self._model_info + 'move_down'),
        ) + super(OrderedModelAdmin, self).get_urls()

    def move_up(self, request, object_id):
        obj = get_object_or_404(self.model, pk=unquote(object_id))
        obj.move_up()
        return HttpResponseRedirect(reverse('admin:{0}changelist'.format(self._model_info)))

    def move_down(self, request, object_id):
        obj = get_object_or_404(self.model, pk=unquote(object_id))
        obj.move_down()
        return HttpResponseRedirect(reverse('admin:{0}changelist'.format(self._model_info)))

    def move_up_down_links(self, obj):
        up_url = reverse('admin:{0}move_up'.format(self._model_info), args=[obj.id])
        down_url = reverse('admin:{0}move_down'.format(self._model_info), args=[obj.id])
        return self.UP_LINK_FORMAT.format(url=up_url) + ' ' + self.DOWN_LINK_FORMAT.format(url=down_url)

    move_up_down_links.allow_tags = True
    move_up_down_links.short_description = _(u'Move')
