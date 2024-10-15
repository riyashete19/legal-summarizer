# settings.py

# Other settings...

DEBUG = True  # Set this to True during development

ALLOWED_HOSTS = ['localhost', '127.0.0.1']  # Allow local development

SECRET_KEY = 'your-generated-secret-key-here'  # Ensure this is kept secret

# Specify the URL configuration module
ROOT_URLCONF = 'legal_summarizer.urls'  # Add this line

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    # Your apps...
    'summarizer',  # Your summarization app
    'corsheaders',  # CORS headers for frontend-backend communication
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # Enable CORS middleware
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Other middleware...
]

# CORS settings
CORS_ALLOW_ALL_ORIGINS = True  # Development setting only, restrict this in production

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

# Templates settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],  # You can specify template directories here
        'APP_DIRS': True,  # Allow searching for templates in app directories
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Add any other settings below...
