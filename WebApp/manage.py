                                                                                                                                                                                    #!/usr/bin/env python3
import os
import sys
import re, string
re_tok = re.compile(f'([{string.punctuation}“”¨«»®´·º½¾¿¡§£₤‘’])')
# def tokenize(s):
#     return re_tok.sub(r' \1', s).split()

if __name__ == "__main__":

    def tokenize(s):
        return re_tok.sub(r' \1', s).split()
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "speechtox.settings")
    try:               
        from django.core.management import execute_from_command_line
    except ImportError:
        # The above import may fail for some other reason. Ensure that the
        # issue is really that Django is missing to avoid masking other
        # exceptions on Python 2.
        try:
            import django
        except ImportError:
            raise ImportError(
                "Couldn't import Django. Are you sure it's installed and "
                "available on your PYTHONPATH environment variable? Did you "
                "forget to activate a virtual environment?"
            )
        raise
    execute_from_command_line(sys.argv)
