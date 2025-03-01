import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _

from appdata.models.abstract.a_model_audit_mixin import AModelAuditMixin


class Level(AModelAuditMixin):

    level_id = models.CharField(verbose_name=_('Level Id'),
                                primary_key=True,
                                default=uuid.uuid4,
                                max_length=64)

    level = models.PositiveIntegerField(verbose_name=_('Level'),
                                        null=False,
                                        blank=False,
                                        unique=True)

    class Meta:
        verbose_name = _('Department Level')
        verbose_name_plural = _('Department Levels')
        db_table = 'level'

    def __str__(self):
        return f"{self.level}lv"
