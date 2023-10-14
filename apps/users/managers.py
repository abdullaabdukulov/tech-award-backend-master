from django.contrib.auth.base_user import BaseUserManager
from rest_framework.exceptions import ValidationError


class UserManager(BaseUserManager):
    def _create_user(self, password, phone=None, email=None, **extra_fields):
        if phone is None and email is None:
            raise ValidationError("The given phone or email must be set")
        if email is None:
            user = self.model(phone=phone, **extra_fields)
        else:
            user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        phone = extra_fields.pop("phone", None)
        return self._create_user(
            email=email, password=password, phone=phone, **extra_fields
        )

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("role", self.model.Role.ADMIN)

        if extra_fields.get("is_staff") is not True:
            raise ValidationError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValidationError("Superuser must have is_superuser=True.")

        return self._create_user(email=email, password=password, **extra_fields)

    def register_user(self, data):
        email = data.get("email")
        password = data.get("password")
        user = self.create_user(email=email, password=password, **data)
        return user

    def admins(self, admin=None):
        if admin is not None:
            return (
                self.filter(
                    role__in=self.model.Role.admins(),
                    phone__isnull=True,
                )
                .exclude(pk=admin.id)
                .order_by("role")
            )
        return self.filter(role__in=self.model.Role.admins())

    def update_school_student(self, email, school, password=None):
        user = self.filter(shops__id=school.id).first()
        user.email = email
        if password is not None:
            user.set_password(password)
        user.save()
