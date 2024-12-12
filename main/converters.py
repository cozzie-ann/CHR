# main/converters.py
from django.urls import register_converter

class FloatConverter:
    regex = r'\d+(\.\d+)?'

    def to_python(self, value):
        return float(value)

    def to_url(self, value):
        return str(value)

# Register the converter
register_converter(FloatConverter, 'float')
