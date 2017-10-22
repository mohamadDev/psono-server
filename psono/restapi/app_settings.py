from django.conf import settings

from .serializers import (
    LoginSerializer as DefaultLoginSerializer,
    GAVerifySerializer as DefaultGAVerifySerializer,
    YubikeyOTPVerifySerializer as DefaultYubikeyOTPVerifySerializer,
    ActivateTokenSerializer as DefaultActivateTokenSerializer,
    LogoutSerializer as DefaultLogoutSerializer,
    VerifyEmailSerializeras as DefaultVerifyEmailSerializer,
    RegisterSerializer as DefaultRegisterSerializer,
    UserSearchSerializer as DefaultUserSearchSerializer,
    UserUpdateSerializer as DefaultUserUpdateSerializer,
    NewGASerializer as DefaultNewGASerializer,
    NewYubikeyOTPSerializer as DefaultNewYubikeyOTPSerializer,
    CreateShareRightSerializer as DefaultCreateShareRightSerializer,
    UpdateShareRightSerializer as DefaultUpdateShareRightSerializer,
    DeleteShareRightSerializer as DefaultDeleteShareRightSerializer,
    CreateRecoverycodeSerializer as DefaultCreateRecoverycodeSerializer,
    EnableNewPasswordSerializer as DefaultEnableNewPasswordSerializer,
    SetNewPasswordSerializer as DefaultSetNewPasswordSerializer,
    ShareTreeSerializer as DefaultShareTreeSerializer,
    CreateShareSerializer as DefaultCreateShareSerializer,
    UpdateShareSerializer as DefaultUpdateShareSerializer,
    DatastoreOverviewSerializer as DefaultDatastoreOverviewSerializer,
    CreateDatastoreSerializer as DefaultCreateDatastoreSerializer,
    DeleteDatastoreSerializer as DefaultDeleteDatastoreSerializer,
    DeleteMembershipSerializer as DefaultDeleteMembershipSerializer,
    SecretOverviewSerializer as DefaultSecretOverviewSerializer,
    ShareOverviewSerializer as DefaultShareOverviewSerializer,
    ShareRightAcceptSerializer as DefaultShareRightAcceptSerializer,
    ShareRightDeclineSerializer as DefaultShareRightDeclineSerializer,
    MoveSecretLinkSerializer as DefaultMoveSecretLinkSerializer,
    DeleteSecretLinkSerializer as DefaultDeleteSecretLinkSerializer,
    CreateGroupSerializer as DefaultCreateGroupSerializer,
    ReadGroupRightsSerializer as DefaultReadGroupRightsSerializer,
    CreateSecretSerializer as DefaultCreateSecretSerializer,
    UpdateSecretSerializer as DefaultUpdateSecretSerializer,
    CreateMembershipSerializer as DefaultCreateMembershipSerializer,
    UpdateMembershipSerializer as DefaultUpdateMembershipSerializer,
    UpdateGroupSerializer as DefaultUpdateGroupSerializer,
    MembershipAcceptSerializer as DefaultMembershipAcceptSerializer,
    MembershipDeclineSerializer as DefaultMembershipDeclineSerializer,
)
from .utils import import_callable


serializers = getattr(settings, 'RESTAPI_AUTH_SERIALIZERS', {})

LoginSerializer = import_callable(
    serializers.get('LOGIN_SERIALIZER', DefaultLoginSerializer)
)

GAVerifySerializer = import_callable(
    serializers.get('GA_VERIFY_SERIALIZER', DefaultGAVerifySerializer)
)

YubikeyOTPVerifySerializer = import_callable(
    serializers.get('YUBIKEY_OTP_VERIFY_SERIALIZER', DefaultYubikeyOTPVerifySerializer)
)

ActivateTokenSerializer = import_callable(
    serializers.get('ACTIVATE_TOKEN_SERIALIZER', DefaultActivateTokenSerializer)
)

LogoutSerializer = import_callable(
    serializers.get('LOGOUT_SERIALIZER', DefaultLogoutSerializer)
)


RegisterSerializer = import_callable(
    serializers.get(
        'REGISTER_SERIALIZER',
        DefaultRegisterSerializer
    )
)


VerifyEmailSerializer = import_callable(
    serializers.get(
        'VERIFY_EMAIL_SERIALIZER',
        DefaultVerifyEmailSerializer
    )
)


UserSearchSerializer = import_callable(
    serializers.get(
        'USER_SEARCH_SERIALIZER',
        DefaultUserSearchSerializer
    )
)

UserUpdateSerializer = import_callable(
    serializers.get(
        'USER_UPDATE_SERIALIZER',
        DefaultUserUpdateSerializer
    )
)

NewGASerializer = import_callable(
    serializers.get(
        'NEW_GA_SERIALIZER',
        DefaultNewGASerializer
    )
)

NewYubikeyOTPSerializer = import_callable(
    serializers.get(
        'NEW_YUBIKEY_OTP_SERIALIZER',
        DefaultNewYubikeyOTPSerializer
    )
)


CreateShareRightSerializer = import_callable(
    serializers.get(
        'CREATE_SHARE_RIGHT_SERIALIZER',
        DefaultCreateShareRightSerializer
    )
)

UpdateShareRightSerializer = import_callable(
    serializers.get(
        'UPDATE_SHARE_RIGHT_SERIALIZER',
        DefaultUpdateShareRightSerializer
    )
)

DeleteShareRightSerializer = import_callable(
    serializers.get(
        'DELETE_SHARE_RIGHT_SERIALIZER',
        DefaultDeleteShareRightSerializer
    )
)


CreateRecoverycodeSerializer = import_callable(
    serializers.get(
        'CREATE_RECOVERYCODE_SERIALIZER',
        DefaultCreateRecoverycodeSerializer
    )
)


EnableNewPasswordSerializer = import_callable(
    serializers.get(
        'PASSWORD_SERIALIZER',
        DefaultEnableNewPasswordSerializer
    )
)


SetNewPasswordSerializer = import_callable(
    serializers.get(
        'PASSWORD_SERIALIZER',
        DefaultSetNewPasswordSerializer
    )
)

ShareTreeSerializer = import_callable(
    serializers.get(
        'SHARE_RIGHT_INHERIT_SERIALIZER',
        DefaultShareTreeSerializer
    )
)


CreateShareSerializer = import_callable(
    serializers.get(
        'CREATE_SHARE_SERIALIZER',
        DefaultCreateShareSerializer
    )
)


UpdateShareSerializer = import_callable(
    serializers.get(
        'UPDATE_SHARE_SERIALIZER',
        DefaultUpdateShareSerializer
    )
)

DatastoreOverviewSerializer = import_callable(
    serializers.get(
        'DATASTORE_OVERVIEW_SERIALIZER',
        DefaultDatastoreOverviewSerializer
    )
)

CreateDatastoreSerializer = import_callable(
    serializers.get(
        'CREATE_DATASTORE_SERIALIZER',
        DefaultCreateDatastoreSerializer
    )
)

DeleteDatastoreSerializer = import_callable(
    serializers.get(
        'DELETE_DATASTORE_SERIALIZER',
        DefaultDeleteDatastoreSerializer
    )
)


DeleteMembershipSerializer = import_callable(
    serializers.get(
        'DELETE_MEMBERSHIP_SERIALIZER',
        DefaultDeleteMembershipSerializer
    )
)

SecretOverviewSerializer = import_callable(
    serializers.get(
        'SECRET_OVERVIEW_SERIALIZER',
        DefaultSecretOverviewSerializer
    )
)

ShareOverviewSerializer = import_callable(
    serializers.get(
        'SHARE_OVERVIEW_SERIALIZER',
        DefaultShareOverviewSerializer
    )
)

ShareRightAcceptSerializer = import_callable(
    serializers.get(
        'SHARE_RIGHT_ACCEPT_SERIALIZER',
        DefaultShareRightAcceptSerializer
    )
)

ShareRightDeclineSerializer = import_callable(
    serializers.get(
        'SHARE_RIGHT_DECLINE_SERIALIZER',
        DefaultShareRightDeclineSerializer
    )
)

MoveSecretLinkSerializer = import_callable(
    serializers.get(
        'MOVE_SECRET_LINK_SERIALIZER',
        DefaultMoveSecretLinkSerializer
    )
)

DeleteSecretLinkSerializer = import_callable(
    serializers.get(
        'DELETE_SECRET_LINK_SERIALIZER',
        DefaultDeleteSecretLinkSerializer
    )
)

CreateGroupSerializer = import_callable(
    serializers.get(
        'CREATE_GROUP_SERIALIZER',
        DefaultCreateGroupSerializer
    )
)

ReadGroupRightsSerializer = import_callable(
    serializers.get(
        'READ_GROUP_RIGHTS_SERIALIZER',
        DefaultReadGroupRightsSerializer
    )
)

CreateSecretSerializer = import_callable(
    serializers.get(
        'CREATE_SECRET_SERIALIZER',
        DefaultCreateSecretSerializer
    )
)

UpdateSecretSerializer = import_callable(
    serializers.get(
        'UPDATE_SECRET_SERIALIZER',
        DefaultUpdateSecretSerializer
    )
)

CreateMembershipSerializer = import_callable(
    serializers.get(
        'CREATE_MEMBERSHIP_SERIALIZER',
        DefaultCreateMembershipSerializer
    )
)

UpdateMembershipSerializer = import_callable(
    serializers.get(
        'CREATE_MEMBERSHIP_SERIALIZER',
        DefaultUpdateMembershipSerializer
    )
)

UpdateGroupSerializer = import_callable(
    serializers.get(
        'UPDATE_GROUP_SERIALIZER',
        DefaultUpdateGroupSerializer
    )
)

MembershipAcceptSerializer = import_callable(
    serializers.get(
        'MEMBERSHIP_ACCEPT_SERIALIZER',
        DefaultMembershipAcceptSerializer
    )
)

MembershipDeclineSerializer = import_callable(
    serializers.get(
        'MEMBERSHIP_DECLINE_SERIALIZER',
        DefaultMembershipDeclineSerializer
    )
)


EMAIL_VERIFICATION = 'mandatory'
