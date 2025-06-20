from functools import wraps
from typing import Optional, Callable, TypeVar, Dict, Type

from django.db import transaction
from django.db.models import Model

M = TypeVar("M", bound=Model)


def safe_executor(with_transaction=False, re_raise=False, default=None, default_factory=None, with_log=False):
    def decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            kwargs.update(
                with_transaction=with_transaction,
                re_raise=re_raise,
                default=default,
                default_factory=default_factory,
                with_log=with_log,
            )
            return safe_execute(func, *args, **kwargs)

        return wrapped

    return decorator

@safe_executor(with_transaction=True, with_log=True)
def save_data(model_class: Type[M], data: Dict, instance: Optional[M] = None) -> M:
    """
    Generic save method for any Django model.
    :param model_class: the model class to instantiate if no instance is provided
    :param data: dictionary of field data
    :param instance: optional existing instance to update
    :return: saved model instance
    """
    obj = instance or model_class()
    update_fields = [field for field in data if hasattr(obj, field)]

    for field in update_fields:
        setattr(obj, field, data[field])

    if obj.pk and update_fields:
        obj.save(update_fields=update_fields)
    else:
        obj.save()
    return obj


def safe_execute(func, *args, **kwargs):
    with_transaction = kwargs.pop("with_transaction", False)
    re_raise = kwargs.pop("re_raise", False)
    default = kwargs.pop("default", None)
    default_factory: Optional[Callable] = kwargs.pop("default_factory", None)
    with_log = kwargs.pop("with_log", True)
    try:
        if with_transaction:
            with transaction.atomic():
                result = func(*args, **kwargs)
        else:
            result = func(*args, **kwargs)
    except Exception as e:
        if with_log:
            print(e)
        if re_raise:
            raise e
        if default_factory is not None:
            return default_factory()
        return default
    return result

