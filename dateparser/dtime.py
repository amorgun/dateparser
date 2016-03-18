# -*- coding: utf-8 -*-
from contextlib import contextmanager
from datetime import datetime as standart_datetime

class ConfigurableDatetime(standart_datetime):
    NOW = None

    @classmethod
    def utcnow(cls):
        if cls.NOW is not None:
            return cls.NOW
        return super(ConfigurableDatetime, cls).utcnow()

    @classmethod
    @contextmanager
    def set_now(cls, now):
        old_now = cls.NOW
        cls.NOW = now
        yield
        cls.NOW = old_now

datetime = ConfigurableDatetime
