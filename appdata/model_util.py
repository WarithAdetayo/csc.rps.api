def jsonify_itcc_user(instance) -> dict:
    if instance is None:
        return {}
    return {
        'user_id': instance.id,
        'email': instance.email,
        'first_name': instance.first_name,
        'last_name': instance.last_name,
        'is_staff': instance.is_staff,
        'is_superuser': instance.is_superuser
    }
