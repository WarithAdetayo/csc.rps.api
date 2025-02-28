from django.contrib.auth.base_user import BaseUserManager


class CSCRPSUserManager(BaseUserManager):
    """Custom user manger for CSC RPS User accounts
    """

    def _create_user(self, email, password, **extra_fields):
        """Create and save a user with the given email and password
        """

        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        return self._create_user(email=email, password=password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email=email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)
        return user
