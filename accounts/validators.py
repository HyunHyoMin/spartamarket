from django.contrib.auth.password_validation import UserAttributeSimilarityValidator
from django.core.exceptions import ValidationError, FieldDoesNotExist
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.password_validation import exceeds_maximum_length_ratio
from difflib import SequenceMatcher
import re


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
        def validate(self, password, user=None):
            if not user:
                return

            password = password.lower()
            for attribute_name in self.user_attributes:
                value = getattr(user, attribute_name, None)
                if not value or not isinstance(value, str):
                    continue
                value_lower = value.lower()
                value_parts = re.split(r"\W+", value_lower) + [value_lower]
                for value_part in value_parts:
                    if exceeds_maximum_length_ratio(
                        password, self.max_similarity, value_part
                    ):
                        continue
                    if (
                        SequenceMatcher(a=password, b=value_part).quick_ratio()
                        >= self.max_similarity
                    ):
                        try:
                            verbose_name = str(
                                user._meta.get_field(attribute_name).verbose_name
                            )
                        except FieldDoesNotExist:
                            verbose_name = attribute_name
                        raise ValidationError(
                            _("비밀번호가 ID와 유사합니다."),
                            code="password_too_similar",
                            params={"verbose_name": verbose_name},
                        )
