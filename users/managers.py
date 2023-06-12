from django.contrib.auth.base_user import BaseUserManager


class AppUserManager(BaseUserManager):
    def get_queryset(self):
        from users.querysets import AppUserQuerySet
        return AppUserQuerySet(self.model, using=self._db)

    def create_user(self, email, password=None, **extra_fields):
        password = password or self.make_random_password()
        email = email.lower()
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields['is_staff'] = True
        extra_fields['is_superuser'] = True
        return self.create_user(email, password, **extra_fields)

    @classmethod
    def get_or_create_profile(cls, user):
        pass

    def admin(self):
        return self.get_queryset().admin()

    def staff(self):
        return self.get_queryset().staff()
