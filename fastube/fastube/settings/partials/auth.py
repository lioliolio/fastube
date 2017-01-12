# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
import os


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


# auth
AUTH_USER_MODEL = "users.User"

LOGIN_URL = "/login/"

SIGNUP_SUCCESS_MESSAGE = "성공적으로 회원가입 되었습니다."
LOGIN_SUCCESS_MESSAGE = "성공적으로 로그인 되었습니다."
LOGOUT_SUCCESS_MESSAGE = "성공적으로 로그아웃 되었습니다."

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)

AUTHENTICATION_BACKENDS = [
    "social_core.backends.facebook.FacebookOAuth2",

    "django.contrib.auth.backends.ModelBackend",
]

SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get("SOCIAL_AUTH_FACEBOOK_KEY")
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get("SOCIAL_AUTH_FACEBOOK_SECRET")

SOCIAL_AUTH_LOGIN_REDIRECT_URL = "/login/"
