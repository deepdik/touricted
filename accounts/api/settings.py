from django.conf import settings

from .serializers import (  
    PasswordResetSerializer as DefaultPasswordResetSerializer,
    
    )
from .utils import import_callable
serializers = getattr(settings, 'REST_AUTH_SERIALIZERS', {})

PasswordResetSerializer = import_callable(
    serializers.get(
        'PASSWORD_RESET_SERIALIZER',
        DefaultPasswordResetSerializer
    )
)

