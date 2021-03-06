"""
Django settings for projectsapling project.

Generated by 'django-admin startproject' using Django 2.1.5.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'y8)ahmo4#n)aoatj@en2r#f_u99l&b)%9z22+r--j7(+aq)w57'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]


# Application definition
# 'feincms',  
# 'django_mptt_admin',
#
INSTALLED_APPS = [
    'simpleui',
    'rest_framework',
    'django_filters',
    'import_export',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projectsapling',
    'AppModel',
    'corsheaders',
    'mptt',
]

# env need pip install django-cors-headers
CORS_ORIGIN_ALLOW_ALL = True

MIDDLEWARE = [
    # 'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 'dwebsocket.middleware.WebSocketMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'projectsapling.urls'

# 'DIRS': [os.path.join(BASE_DIR, 'templates')],
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR+'/templates'],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'projectsapling.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-Hans'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'


# simple ui setting

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#]
# 首页信息是否展示
SIMPLEUI_HOME_INFO = False

# 操作是否展示
SIMPLEUI_HOME_ACTION = True

# 数据分析是否展示

SIMPLEUI_ANALYSIS = False

# 批量导入数据
IMPORT_EXPORT_USE_TRANSACTIONS = True

STATIC_ROOT = os.path.join(BASE_DIR, "static")

SIMPLEUI_CONFIG = {
    'menus': [{
        'app': 'AppModel',
        'name': '系统管理',
        'icon': 'fab fa-dashcube',
        'models': [{
            'name': '组织机构管理',
            'url': 'AppModel/category',
            'icon': 'fa fa-tags'
        },{
            'name': '组织机构列表',
            'url': 'AppModel/post',
            'icon': 'fa fa-tags'
        }, {
            'name': '联网单位信息',
            'url': 'AppModel/companyinfo',
            'icon': 'fa fa-id-card'
        }, {
            'name': '用户管理',
            'url': 'AppModel/userinfo/',
            'icon': 'fa fa-user-circle'
        }]
        }, {
        'name': '设备管理',
        'icon': 'fa fa-bars',
        'models': [{
            'name': '设备管理',
            'url': 'AppModel/deviceinfo/',
            'icon': 'fa fa-server'
        }, {
            'name': '上线记录',
            'url': 'AppModel/mappinguserinfodevicename/',
            'icon': 'fa fa-paper-plane'
        }]
        },{
        'app': 'auth',
        'name': '权限认证',
        'icon': 'fas fa-user-shield',
        'models': [{
            'name': '系统用户',
            'icon': 'fa fa-user',
            'url': 'auth/user/'
        },{
            'name': '用户组',
            'icon': 'fa fa-users',
            'url': 'auth/group/'
        }]
    },{
        'name': '消防管理',
        'icon': 'fa fa-fire-extinguisher',
        'models': [{
            'name': '巡检管理',
            'url': 'AppModel/patrolscheme',
            'icon': 'fa fa-fire-extinguisher'
        }, {
            'name': '隐患整改',
            'url': 'AppModel/dangerrectification',
            'icon': 'far fa-surprise'
        }, {
            'name': '维修保养',
            'url': 'AppModel/maintenanceinfo',
            'icon': 'fa fa-bell-slash'
        }]
    },{
        'name': '监控中心',
        'icon': 'fab fa-cloudversify',
        'models': [{
            'name': '设备中心',
            'url': 'AppModel/onlinedeviceinfo',
            'icon': 'far fa-surprise'
        }, {
            'name': '报警中心',
            'url': 'AppModel/alarminfo',
            'icon': 'fa fa-phone'
        }, {
            'name': '事件历史',
            'url': 'AppModel/eventinfo',
            'icon': 'fa fa-terminal'
        }, {
            'name': '视频中心',
            'url': '',
            'icon': 'fa fa-terminal'
        }]
    },{
        'name': '系统设置',
        'icon': 'fa fa-tasks',
        'models': [{
            'name': '系统设置',
            'url': '',
            'icon': 'fa fa-tasks'
        }]
    }]
}

MPTT_ADMIN_LEVEL_INDENT = 20

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'
