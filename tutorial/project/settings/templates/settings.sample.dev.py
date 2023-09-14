DEBUG = True

SECRET_KEY = 'django-insecure-!(iqgp0k*l=^7inhr034w!w&dqy*2*ilek(16ajhs*+4_*z=sl'

LOGGING['formatters']['colored'] = {  # type: ignore # noqa: F821
    '()':
    'colorlog.ColoredFormatter',
    'format':
    '%(log_color)s%(asctime)s %(levelname)s %(name)s %(bold_white)s%(message)s',
}
LOGGING['loggers']['core']['level'] = 'DEBUG'  # type: ignore # noqa: F821
LOGGING['handlers']['console']['level'] = 'DEBUG'  # type: ignore  # noqa: F821
LOGGING['handlers']['console'][  # type: ignore  # noqa: F821
    'formatter'] = 'colored'  # type: ignore  # noqa: F821
