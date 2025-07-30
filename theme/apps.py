from django.apps import AppConfig
from tailwind.apps import TailwindConfig  # This is important

class ThemeConfig(TailwindConfig):  # Only this class is needed
    name = 'theme'
