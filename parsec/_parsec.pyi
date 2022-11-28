from __future__ import annotations

from parsec._parsec_pyi import (
    DataError,
    EntryNameError,
)

from parsec._parsec_pyi.certif import (
    UserCertificate,
    DeviceCertificate,
    RevokedUserCertificate,
    RealmRoleCertificate,
)

from parsec._parsec_pyi.crypto import (
    SecretKey,
    HashDigest,
    SigningKey,
    VerifyKey,
    PrivateKey,
    PublicKey,
    generate_nonce,
)

from parsec._parsec_pyi.enumerate import (
    ClientType,
    InvitationDeletedReason,
    InvitationType,
    InvitationEmailSentStatus,
    InvitationStatus,
    InvitationType,
    RealmRole,
    UserProfile,
)

from parsec._parsec_pyi.ids import (
    OrganizationID,
    EntryID,
    BlockID,
    VlobID,
    ChunkID,
    HumanHandle,
    DeviceLabel,
    DeviceID,
    DeviceName,
    UserID,
    RealmID,
    SequesterServiceID,
    EnrollmentID,
    InvitationToken,
)

from parsec._parsec_pyi.invite import (
    SASCode,
    generate_sas_code_candidates,
    generate_sas_codes,
    InviteUserConfirmation,
    InviteDeviceData,
    InviteDeviceConfirmation,
    InviteUserData,
)

from parsec._parsec_pyi.addrs import (
    BackendAddr,
    BackendActionAddr,
    BackendInvitationAddr,
    BackendOrganizationAddr,
    BackendOrganizationBootstrapAddr,
    BackendOrganizationFileLinkAddr,
    BackendPkiEnrollmentAddr,
    export_root_verify_key,
)

from parsec._parsec_pyi.local_manifest import (
    Chunk,
    LocalFileManifest,
    LocalFolderManifest,
    LocalUserManifest,
    LocalWorkspaceManifest,
    local_manifest_decrypt_and_load,
)

from parsec._parsec_pyi.manifest import (
    EntryName,
    WorkspaceEntry,
    BlockAccess,
    FolderManifest,
    FileManifest,
    WorkspaceManifest,
    UserManifest,
    AnyRemoteManifest,
    manifest_decrypt_and_load,
    manifest_decrypt_verify_and_load,
    manifest_verify_and_load,
    manifest_unverified_load,
)

from parsec._parsec_pyi.message import (
    MessageContent,
    SharingGrantedMessageContent,
    SharingReencryptedMessageContent,
    SharingRevokedMessageContent,
    PingMessageContent,
)

from parsec._parsec_pyi.pki import (
    PkiEnrollmentAnswerPayload,
    PkiEnrollmentSubmitPayload,
)

from parsec._parsec_pyi.time import (
    DateTime,
    LocalDateTime,
    TimeProvider,
    mock_time,
)

from parsec._parsec_pyi.trustchain import (
    TrustchainContext,
    TrustchainError,
    TrustchainErrorException,
)

from parsec._parsec_pyi.local_device import LocalDevice, UserInfo, DeviceInfo

from parsec._parsec_pyi.file_operation import (
    prepare_read,
    prepare_reshape,
    prepare_resize,
    prepare_write,
)

from parsec._parsec_pyi.protocol import (
    # Cmd
    AnonymousAnyCmdReq,
    AuthenticatedAnyCmdReq,
    InvitedAnyCmdReq,
    # Block
    BlockCreateReq,
    BlockCreateRep,
    BlockCreateRepOk,
    BlockCreateRepAlreadyExists,
    BlockCreateRepInMaintenance,
    BlockCreateRepNotAllowed,
    BlockCreateRepNotFound,
    BlockCreateRepTimeout,
    BlockCreateRepUnknownStatus,
    BlockReadReq,
    BlockReadRep,
    BlockReadRepOk,
    BlockReadRepInMaintenance,
    BlockReadRepNotAllowed,
    BlockReadRepNotFound,
    BlockReadRepTimeout,
    BlockReadRepUnknownStatus,
    # Invite
    Invite1ClaimerWaitPeerRep,
    Invite1ClaimerWaitPeerRepInvalidState,
    Invite1ClaimerWaitPeerRepNotFound,
    Invite1ClaimerWaitPeerRepOk,
    Invite1ClaimerWaitPeerRepUnknownStatus,
    Invite1ClaimerWaitPeerReq,
    Invite1GreeterWaitPeerRep,
    Invite1GreeterWaitPeerRepAlreadyDeleted,
    Invite1GreeterWaitPeerRepInvalidState,
    Invite1GreeterWaitPeerRepNotFound,
    Invite1GreeterWaitPeerRepOk,
    Invite1GreeterWaitPeerRepUnknownStatus,
    Invite1GreeterWaitPeerReq,
    Invite2aClaimerSendHashedNonceRep,
    Invite2aClaimerSendHashedNonceRepAlreadyDeleted,
    Invite2aClaimerSendHashedNonceRepInvalidState,
    Invite2aClaimerSendHashedNonceRepNotFound,
    Invite2aClaimerSendHashedNonceRepOk,
    Invite2aClaimerSendHashedNonceRepUnknownStatus,
    Invite2aClaimerSendHashedNonceReq,
    Invite2aGreeterGetHashedNonceRep,
    Invite2aGreeterGetHashedNonceRepAlreadyDeleted,
    Invite2aGreeterGetHashedNonceRepInvalidState,
    Invite2aGreeterGetHashedNonceRepNotFound,
    Invite2aGreeterGetHashedNonceRepOk,
    Invite2aGreeterGetHashedNonceRepUnknownStatus,
    Invite2aGreeterGetHashedNonceReq,
    Invite2bClaimerSendNonceRep,
    Invite2bClaimerSendNonceRepInvalidState,
    Invite2bClaimerSendNonceRepNotFound,
    Invite2bClaimerSendNonceRepOk,
    Invite2bClaimerSendNonceRepUnknownStatus,
    Invite2bClaimerSendNonceReq,
    Invite2bGreeterSendNonceRep,
    Invite2bGreeterSendNonceRepAlreadyDeleted,
    Invite2bGreeterSendNonceRepInvalidState,
    Invite2bGreeterSendNonceRepNotFound,
    Invite2bGreeterSendNonceRepOk,
    Invite2bGreeterSendNonceRepUnknownStatus,
    Invite2bGreeterSendNonceReq,
    Invite3aClaimerSignifyTrustRep,
    Invite3aClaimerSignifyTrustRepInvalidState,
    Invite3aClaimerSignifyTrustRepNotFound,
    Invite3aClaimerSignifyTrustRepOk,
    Invite3aClaimerSignifyTrustRepUnknownStatus,
    Invite3aClaimerSignifyTrustReq,
    Invite3aGreeterWaitPeerTrustRep,
    Invite3aGreeterWaitPeerTrustRepAlreadyDeleted,
    Invite3aGreeterWaitPeerTrustRepInvalidState,
    Invite3aGreeterWaitPeerTrustRepNotFound,
    Invite3aGreeterWaitPeerTrustRepOk,
    Invite3aGreeterWaitPeerTrustRepUnknownStatus,
    Invite3aGreeterWaitPeerTrustReq,
    Invite3bClaimerWaitPeerTrustRep,
    Invite3bClaimerWaitPeerTrustRepInvalidState,
    Invite3bClaimerWaitPeerTrustRepNotFound,
    Invite3bClaimerWaitPeerTrustRepOk,
    Invite3bClaimerWaitPeerTrustRepUnknownStatus,
    Invite3bClaimerWaitPeerTrustReq,
    Invite3bGreeterSignifyTrustRep,
    Invite3bGreeterSignifyTrustRepAlreadyDeleted,
    Invite3bGreeterSignifyTrustRepInvalidState,
    Invite3bGreeterSignifyTrustRepNotFound,
    Invite3bGreeterSignifyTrustRepOk,
    Invite3bGreeterSignifyTrustRepUnknownStatus,
    Invite3bGreeterSignifyTrustReq,
    Invite4ClaimerCommunicateRep,
    Invite4ClaimerCommunicateRepInvalidState,
    Invite4ClaimerCommunicateRepNotFound,
    Invite4ClaimerCommunicateRepOk,
    Invite4ClaimerCommunicateRepUnknownStatus,
    Invite4ClaimerCommunicateReq,
    Invite4GreeterCommunicateRep,
    Invite4GreeterCommunicateRepAlreadyDeleted,
    Invite4GreeterCommunicateRepInvalidState,
    Invite4GreeterCommunicateRepNotFound,
    Invite4GreeterCommunicateRepOk,
    Invite4GreeterCommunicateRepUnknownStatus,
    Invite4GreeterCommunicateReq,
    InviteDeleteRep,
    InviteDeleteRepAlreadyDeleted,
    InviteDeleteRepNotFound,
    InviteDeleteRepOk,
    InviteDeleteRepUnknownStatus,
    InviteDeleteReq,
    InviteInfoRep,
    InviteInfoRepOk,
    InviteInfoRepUnknownStatus,
    InviteInfoReq,
    InviteListItem,
    InviteListRep,
    InviteListRepOk,
    InviteListRepUnknownStatus,
    InviteListReq,
    InviteNewRep,
    InviteNewRepAlreadyMember,
    InviteNewRepNotAllowed,
    InviteNewRepNotAvailable,
    InviteNewRepOk,
    InviteNewRepUnknownStatus,
    InviteNewReq,
    # Events
    EventsListenRep,
    EventsListenRepCancelled,
    EventsListenRepNoEvents,
    EventsListenRepOk,
    EventsListenRepOkInviteStatusChanged,
    EventsListenRepOkMessageReceived,
    EventsListenRepOkPinged,
    EventsListenRepOkPkiEnrollmentUpdated,
    EventsListenRepOkRealmMaintenanceFinished,
    EventsListenRepOkRealmMaintenanceStarted,
    EventsListenRepOkRealmRolesUpdated,
    EventsListenRepOkRealmVlobsUpdated,
    EventsListenRepUnknownStatus,
    EventsListenReq,
    EventsSubscribeRep,
    EventsSubscribeRepOk,
    EventsSubscribeRepUnknownStatus,
    EventsSubscribeReq,
    # Message
    MessageGetReq,
    MessageGetRep,
    MessageGetRepOk,
    MessageGetRepUnknownStatus,
    Message,
    # Organization
    OrganizationStatsReq,
    OrganizationStatsRep,
    OrganizationStatsRepOk,
    OrganizationStatsRepNotAllowed,
    OrganizationStatsRepNotFound,
    OrganizationStatsRepUnknownStatus,
    OrganizationConfigReq,
    OrganizationConfigRep,
    OrganizationConfigRepOk,
    OrganizationConfigRepNotFound,
    OrganizationConfigRepUnknownStatus,
    UsersPerProfileDetailItem,
    # Pki commands
    PkiEnrollmentAcceptRep,
    PkiEnrollmentAcceptRepActiveUsersLimitReached,
    PkiEnrollmentAcceptRepAlreadyExists,
    PkiEnrollmentAcceptRepInvalidCertification,
    PkiEnrollmentAcceptRepInvalidData,
    PkiEnrollmentAcceptRepInvalidPayloadData,
    PkiEnrollmentAcceptRepNoLongerAvailable,
    PkiEnrollmentAcceptRepNotAllowed,
    PkiEnrollmentAcceptRepNotFound,
    PkiEnrollmentAcceptRepOk,
    PkiEnrollmentAcceptRepUnknownStatus,
    PkiEnrollmentAcceptReq,
    PkiEnrollmentInfoRep,
    PkiEnrollmentInfoRepNotFound,
    PkiEnrollmentInfoRepOk,
    PkiEnrollmentInfoRepUnknownStatus,
    PkiEnrollmentInfoReq,
    PkiEnrollmentInfoStatus,
    PkiEnrollmentListItem,
    PkiEnrollmentListRep,
    PkiEnrollmentListRepNotAllowed,
    PkiEnrollmentListRepOk,
    PkiEnrollmentListRepUnknownStatus,
    PkiEnrollmentListReq,
    PkiEnrollmentRejectRep,
    PkiEnrollmentRejectRepNoLongerAvailable,
    PkiEnrollmentRejectRepNotAllowed,
    PkiEnrollmentRejectRepNotFound,
    PkiEnrollmentRejectRepOk,
    PkiEnrollmentRejectRepUnknownStatus,
    PkiEnrollmentRejectReq,
    PkiEnrollmentSubmitRep,
    PkiEnrollmentSubmitRepAlreadyEnrolled,
    PkiEnrollmentSubmitRepAlreadySubmitted,
    PkiEnrollmentSubmitRepEmailAlreadyUsed,
    PkiEnrollmentSubmitRepIdAlreadyUsed,
    PkiEnrollmentSubmitRepInvalidPayloadData,
    PkiEnrollmentSubmitRepOk,
    PkiEnrollmentSubmitRepUnknownStatus,
    PkiEnrollmentSubmitReq,
    # Realm
    RealmCreateReq,
    RealmCreateRep,
    RealmCreateRepOk,
    RealmCreateRepInvalidCertification,
    RealmCreateRepInvalidData,
    RealmCreateRepNotFound,
    RealmCreateRepAlreadyExists,
    RealmCreateRepBadTimestamp,
    RealmCreateRepUnknownStatus,
    RealmStatusReq,
    RealmStatusRep,
    RealmStatusRepOk,
    RealmStatusRepNotAllowed,
    RealmStatusRepNotFound,
    RealmStatusRepUnknownStatus,
    RealmStatsReq,
    RealmStatsRep,
    RealmStatsRepOk,
    RealmStatsRepNotAllowed,
    RealmStatsRepNotFound,
    RealmStatsRepUnknownStatus,
    RealmGetRoleCertificatesReq,
    RealmGetRoleCertificatesRep,
    RealmGetRoleCertificatesRepOk,
    RealmGetRoleCertificatesRepNotAllowed,
    RealmGetRoleCertificatesRepNotFound,
    RealmGetRoleCertificatesRepUnknownStatus,
    RealmUpdateRolesReq,
    RealmUpdateRolesRep,
    RealmUpdateRolesRepOk,
    RealmUpdateRolesRepNotAllowed,
    RealmUpdateRolesRepInvalidCertification,
    RealmUpdateRolesRepInvalidData,
    RealmUpdateRolesRepAlreadyGranted,
    RealmUpdateRolesRepIncompatibleProfile,
    RealmUpdateRolesRepNotFound,
    RealmUpdateRolesRepInMaintenance,
    RealmUpdateRolesRepUserRevoked,
    RealmUpdateRolesRepRequireGreaterTimestamp,
    RealmUpdateRolesRepBadTimestamp,
    RealmUpdateRolesRepUnknownStatus,
    RealmStartReencryptionMaintenanceReq,
    RealmStartReencryptionMaintenanceRep,
    RealmStartReencryptionMaintenanceRepOk,
    RealmStartReencryptionMaintenanceRepNotAllowed,
    RealmStartReencryptionMaintenanceRepNotFound,
    RealmStartReencryptionMaintenanceRepBadEncryptionRevision,
    RealmStartReencryptionMaintenanceRepParticipantMismatch,
    RealmStartReencryptionMaintenanceRepMaintenanceError,
    RealmStartReencryptionMaintenanceRepInMaintenance,
    RealmStartReencryptionMaintenanceRepBadTimestamp,
    RealmStartReencryptionMaintenanceRepUnknownStatus,
    RealmFinishReencryptionMaintenanceReq,
    RealmFinishReencryptionMaintenanceRep,
    RealmFinishReencryptionMaintenanceRepOk,
    RealmFinishReencryptionMaintenanceRepNotAllowed,
    RealmFinishReencryptionMaintenanceRepNotFound,
    RealmFinishReencryptionMaintenanceRepBadEncryptionRevision,
    RealmFinishReencryptionMaintenanceRepNotInMaintenance,
    RealmFinishReencryptionMaintenanceRepMaintenanceError,
    RealmFinishReencryptionMaintenanceRepUnknownStatus,
    MaintenanceType,
    # Ping
    AuthenticatedPingReq,
    AuthenticatedPingRep,
    AuthenticatedPingRepOk,
    AuthenticatedPingRepUnknownStatus,
    InvitedPingReq,
    InvitedPingRep,
    InvitedPingRepOk,
    InvitedPingRepUnknownStatus,
    # User
    UserGetReq,
    UserGetRep,
    UserGetRepOk,
    UserGetRepNotFound,
    UserGetRepUnknownStatus,
    UserCreateReq,
    UserCreateRep,
    UserCreateRepOk,
    UserCreateRepActiveUsersLimitReached,
    UserCreateRepAlreadyExists,
    UserCreateRepInvalidCertification,
    UserCreateRepInvalidData,
    UserCreateRepNotAllowed,
    UserCreateRepUnknownStatus,
    UserRevokeReq,
    UserRevokeRep,
    UserRevokeRepOk,
    UserRevokeRepAlreadyRevoked,
    UserRevokeRepInvalidCertification,
    UserRevokeRepNotAllowed,
    UserRevokeRepNotFound,
    UserRevokeRepUnknownStatus,
    DeviceCreateReq,
    DeviceCreateRep,
    DeviceCreateRepOk,
    DeviceCreateRepAlreadyExists,
    DeviceCreateRepBadUserId,
    DeviceCreateRepInvalidCertification,
    DeviceCreateRepInvalidData,
    DeviceCreateRepUnknownStatus,
    HumanFindReq,
    HumanFindRep,
    HumanFindRepOk,
    HumanFindRepNotAllowed,
    HumanFindRepUnknownStatus,
    Trustchain,
    HumanFindResultItem,
    # Vlob
    VlobCreateReq,
    VlobCreateRep,
    VlobCreateRepOk,
    VlobCreateRepAlreadyExists,
    VlobCreateRepNotAllowed,
    VlobCreateRepBadEncryptionRevision,
    VlobCreateRepInMaintenance,
    VlobCreateRepRequireGreaterTimestamp,
    VlobCreateRepBadTimestamp,
    VlobCreateRepNotASequesteredOrganization,
    VlobCreateRepSequesterInconsistency,
    VlobCreateRepRejectedBySequesterService,
    VlobCreateRepTimeout,
    VlobCreateRepUnknownStatus,
    VlobReadReq,
    VlobReadRep,
    VlobReadRepOk,
    VlobReadRepNotFound,
    VlobReadRepNotAllowed,
    VlobReadRepBadVersion,
    VlobReadRepBadEncryptionRevision,
    VlobReadRepInMaintenance,
    VlobReadRepUnknownStatus,
    VlobUpdateReq,
    VlobUpdateRep,
    VlobUpdateRepOk,
    VlobUpdateRepNotFound,
    VlobUpdateRepNotAllowed,
    VlobUpdateRepBadVersion,
    VlobUpdateRepBadEncryptionRevision,
    VlobUpdateRepInMaintenance,
    VlobUpdateRepRequireGreaterTimestamp,
    VlobUpdateRepBadTimestamp,
    VlobUpdateRepNotASequesteredOrganization,
    VlobUpdateRepSequesterInconsistency,
    VlobUpdateRepRejectedBySequesterService,
    VlobUpdateRepTimeout,
    VlobUpdateRepUnknownStatus,
    VlobPollChangesReq,
    VlobPollChangesRep,
    VlobPollChangesRepOk,
    VlobPollChangesRepNotFound,
    VlobPollChangesRepNotAllowed,
    VlobPollChangesRepInMaintenance,
    VlobPollChangesRepUnknownStatus,
    VlobListVersionsReq,
    VlobListVersionsRep,
    VlobListVersionsRepOk,
    VlobListVersionsRepNotFound,
    VlobListVersionsRepNotAllowed,
    VlobListVersionsRepInMaintenance,
    VlobListVersionsRepUnknownStatus,
    VlobMaintenanceGetReencryptionBatchReq,
    VlobMaintenanceGetReencryptionBatchRep,
    VlobMaintenanceGetReencryptionBatchRepOk,
    VlobMaintenanceGetReencryptionBatchRepNotFound,
    VlobMaintenanceGetReencryptionBatchRepNotAllowed,
    VlobMaintenanceGetReencryptionBatchRepNotInMaintenance,
    VlobMaintenanceGetReencryptionBatchRepBadEncryptionRevision,
    VlobMaintenanceGetReencryptionBatchRepMaintenanceError,
    VlobMaintenanceGetReencryptionBatchRepUnknownStatus,
    VlobMaintenanceSaveReencryptionBatchReq,
    VlobMaintenanceSaveReencryptionBatchRep,
    VlobMaintenanceSaveReencryptionBatchRepOk,
    VlobMaintenanceSaveReencryptionBatchRepNotFound,
    VlobMaintenanceSaveReencryptionBatchRepNotAllowed,
    VlobMaintenanceSaveReencryptionBatchRepNotInMaintenance,
    VlobMaintenanceSaveReencryptionBatchRepBadEncryptionRevision,
    VlobMaintenanceSaveReencryptionBatchRepMaintenanceError,
    VlobMaintenanceSaveReencryptionBatchRepUnknownStatus,
    ReencryptionBatchEntry,
)

from parsec._parsec_pyi.regex import Regex

__all__ = [
    # Data Error
    "DataError",
    "EntryNameError",
    # Certif
    "UserCertificate",
    "DeviceCertificate",
    "RevokedUserCertificate",
    "RealmRoleCertificate",
    # Crypto
    "SecretKey",
    "HashDigest",
    "SigningKey",
    "VerifyKey",
    "PrivateKey",
    "PublicKey",
    "generate_nonce",
    # Enumerate
    "ClientType",
    "InvitationDeletedReason",
    "InvitationType",
    "InvitationEmailSentStatus",
    "InvitationStatus",
    "InvitationType",
    "RealmRole",
    "UserProfile",
    # Ids
    "OrganizationID",
    "EntryID",
    "BlockID",
    "VlobID",
    "ChunkID",
    "HumanHandle",
    "DeviceLabel",
    "DeviceID",
    "DeviceName",
    "UserID",
    "RealmID",
    "SequesterServiceID",
    "EnrollmentID",
    "InvitationToken",
    # Invite
    "SASCode",
    "generate_sas_code_candidates",
    "generate_sas_codes",
    "InviteUserConfirmation",
    "InviteDeviceData",
    "InviteDeviceConfirmation",
    "InviteUserData",
    # Addrs
    "BackendAddr",
    "BackendActionAddr",
    "BackendInvitationAddr",
    "BackendOrganizationAddr",
    "BackendOrganizationBootstrapAddr",
    "BackendOrganizationFileLinkAddr",
    "BackendPkiEnrollmentAddr",
    "export_root_verify_key",
    # Local Manifest
    "Chunk",
    "LocalFileManifest",
    "LocalFolderManifest",
    "LocalUserManifest",
    "LocalWorkspaceManifest",
    "local_manifest_decrypt_and_load",
    # Manifest
    "EntryName",
    "WorkspaceEntry",
    "BlockAccess",
    "FolderManifest",
    "FileManifest",
    "WorkspaceManifest",
    "UserManifest",
    "AnyRemoteManifest",
    "manifest_decrypt_and_load",
    "manifest_decrypt_verify_and_load",
    "manifest_verify_and_load",
    "manifest_unverified_load",
    # Message
    "MessageContent",
    "SharingGrantedMessageContent",
    "SharingReencryptedMessageContent",
    "SharingRevokedMessageContent",
    "PingMessageContent",
    # Pki
    "PkiEnrollmentAnswerPayload",
    "PkiEnrollmentSubmitPayload",
    # Time
    "DateTime",
    "LocalDateTime",
    "TimeProvider",
    "mock_time",
    # Trustchain
    "TrustchainContext",
    "TrustchainError",
    "TrustchainErrorException",
    # Local Device
    "LocalDevice",
    "UserInfo",
    "DeviceInfo",
    # File Operations
    "prepare_read",
    "prepare_reshape",
    "prepare_resize",
    "prepare_write",
    # Protocol Cmd
    "AnonymousAnyCmdReq",
    "AuthenticatedAnyCmdReq",
    "InvitedAnyCmdReq",
    # Protocol Block
    "BlockCreateReq",
    "BlockCreateRep",
    "BlockCreateRepOk",
    "BlockCreateRepAlreadyExists",
    "BlockCreateRepInMaintenance",
    "BlockCreateRepNotAllowed",
    "BlockCreateRepNotFound",
    "BlockCreateRepTimeout",
    "BlockCreateRepUnknownStatus",
    "BlockReadReq",
    "BlockReadRep",
    "BlockReadRepOk",
    "BlockReadRepInMaintenance",
    "BlockReadRepNotAllowed",
    "BlockReadRepNotFound",
    "BlockReadRepTimeout",
    "BlockReadRepUnknownStatus",
    # Invite protocol
    "Invite1ClaimerWaitPeerRep",
    "Invite1ClaimerWaitPeerRepInvalidState",
    "Invite1ClaimerWaitPeerRepNotFound",
    "Invite1ClaimerWaitPeerRepOk",
    "Invite1ClaimerWaitPeerRepUnknownStatus",
    "Invite1ClaimerWaitPeerReq",
    "Invite1GreeterWaitPeerRep",
    "Invite1GreeterWaitPeerRepAlreadyDeleted",
    "Invite1GreeterWaitPeerRepInvalidState",
    "Invite1GreeterWaitPeerRepNotFound",
    "Invite1GreeterWaitPeerRepOk",
    "Invite1GreeterWaitPeerRepUnknownStatus",
    "Invite1GreeterWaitPeerReq",
    "Invite2aClaimerSendHashedNonceRep",
    "Invite2aClaimerSendHashedNonceRepAlreadyDeleted",
    "Invite2aClaimerSendHashedNonceRepInvalidState",
    "Invite2aClaimerSendHashedNonceRepNotFound",
    "Invite2aClaimerSendHashedNonceRepOk",
    "Invite2aClaimerSendHashedNonceRepUnknownStatus",
    "Invite2aClaimerSendHashedNonceReq",
    "Invite2aGreeterGetHashedNonceRep",
    "Invite2aGreeterGetHashedNonceRepAlreadyDeleted",
    "Invite2aGreeterGetHashedNonceRepInvalidState",
    "Invite2aGreeterGetHashedNonceRepNotFound",
    "Invite2aGreeterGetHashedNonceRepOk",
    "Invite2aGreeterGetHashedNonceRepUnknownStatus",
    "Invite2aGreeterGetHashedNonceReq",
    "Invite2bClaimerSendNonceRep",
    "Invite2bClaimerSendNonceRepInvalidState",
    "Invite2bClaimerSendNonceRepNotFound",
    "Invite2bClaimerSendNonceRepOk",
    "Invite2bClaimerSendNonceRepUnknownStatus",
    "Invite2bClaimerSendNonceReq",
    "Invite2bGreeterSendNonceRep",
    "Invite2bGreeterSendNonceRepAlreadyDeleted",
    "Invite2bGreeterSendNonceRepInvalidState",
    "Invite2bGreeterSendNonceRepNotFound",
    "Invite2bGreeterSendNonceRepOk",
    "Invite2bGreeterSendNonceRepUnknownStatus",
    "Invite2bGreeterSendNonceReq",
    "Invite3aClaimerSignifyTrustRep",
    "Invite3aClaimerSignifyTrustRepInvalidState",
    "Invite3aClaimerSignifyTrustRepNotFound",
    "Invite3aClaimerSignifyTrustRepOk",
    "Invite3aClaimerSignifyTrustRepUnknownStatus",
    "Invite3aClaimerSignifyTrustReq",
    "Invite3aGreeterWaitPeerTrustRep",
    "Invite3aGreeterWaitPeerTrustRepAlreadyDeleted",
    "Invite3aGreeterWaitPeerTrustRepInvalidState",
    "Invite3aGreeterWaitPeerTrustRepNotFound",
    "Invite3aGreeterWaitPeerTrustRepOk",
    "Invite3aGreeterWaitPeerTrustRepUnknownStatus",
    "Invite3aGreeterWaitPeerTrustReq",
    "Invite3bClaimerWaitPeerTrustRep",
    "Invite3bClaimerWaitPeerTrustRepInvalidState",
    "Invite3bClaimerWaitPeerTrustRepNotFound",
    "Invite3bClaimerWaitPeerTrustRepOk",
    "Invite3bClaimerWaitPeerTrustRepUnknownStatus",
    "Invite3bClaimerWaitPeerTrustReq",
    "Invite3bGreeterSignifyTrustRep",
    "Invite3bGreeterSignifyTrustRepAlreadyDeleted",
    "Invite3bGreeterSignifyTrustRepInvalidState",
    "Invite3bGreeterSignifyTrustRepNotFound",
    "Invite3bGreeterSignifyTrustRepOk",
    "Invite3bGreeterSignifyTrustRepUnknownStatus",
    "Invite3bGreeterSignifyTrustReq",
    "Invite4ClaimerCommunicateRep",
    "Invite4ClaimerCommunicateRepInvalidState",
    "Invite4ClaimerCommunicateRepNotFound",
    "Invite4ClaimerCommunicateRepOk",
    "Invite4ClaimerCommunicateRepUnknownStatus",
    "Invite4ClaimerCommunicateReq",
    "Invite4GreeterCommunicateRep",
    "Invite4GreeterCommunicateRepAlreadyDeleted",
    "Invite4GreeterCommunicateRepInvalidState",
    "Invite4GreeterCommunicateRepNotFound",
    "Invite4GreeterCommunicateRepOk",
    "Invite4GreeterCommunicateRepUnknownStatus",
    "Invite4GreeterCommunicateReq",
    "InviteDeleteRep",
    "InviteDeleteRepAlreadyDeleted",
    "InviteDeleteRepNotFound",
    "InviteDeleteRepOk",
    "InviteDeleteRepUnknownStatus",
    "InviteDeleteReq",
    "InviteInfoRep",
    "InviteInfoRepOk",
    "InviteInfoRepUnknownStatus",
    "InviteInfoReq",
    "InviteListItem",
    "InviteListRep",
    "InviteListRepOk",
    "InviteListRepUnknownStatus",
    "InviteListReq",
    "InviteNewRep",
    "InviteNewRepAlreadyMember",
    "InviteNewRepNotAllowed",
    "InviteNewRepNotAvailable",
    "InviteNewRepOk",
    "InviteNewRepUnknownStatus",
    "InviteNewReq",
    # Events
    "EventsListenRep",
    "EventsListenRepCancelled",
    "EventsListenRepNoEvents",
    "EventsListenRepOk",
    "EventsListenRepOkInviteStatusChanged",
    "EventsListenRepOkMessageReceived",
    "EventsListenRepOkPinged",
    "EventsListenRepOkPkiEnrollmentUpdated",
    "EventsListenRepOkRealmMaintenanceFinished",
    "EventsListenRepOkRealmMaintenanceStarted",
    "EventsListenRepOkRealmRolesUpdated",
    "EventsListenRepOkRealmVlobsUpdated",
    "EventsListenRepUnknownStatus",
    "EventsListenReq",
    "EventsSubscribeRep",
    "EventsSubscribeRepOk",
    "EventsSubscribeRepUnknownStatus",
    "EventsSubscribeReq",
    # Protocol Message
    "MessageGetReq",
    "MessageGetRep",
    "MessageGetRepOk",
    "MessageGetRepUnknownStatus",
    "Message",
    # Protocol Organization
    "OrganizationStatsReq",
    "OrganizationStatsRep",
    "OrganizationStatsRepOk",
    "OrganizationStatsRepNotAllowed",
    "OrganizationStatsRepNotFound",
    "OrganizationStatsRepUnknownStatus",
    "OrganizationConfigReq",
    "OrganizationConfigRep",
    "OrganizationConfigRepOk",
    "OrganizationConfigRepNotFound",
    "OrganizationConfigRepUnknownStatus",
    "UsersPerProfileDetailItem",
    # Pki commands
    "PkiEnrollmentAcceptRep",
    "PkiEnrollmentAcceptRepActiveUsersLimitReached",
    "PkiEnrollmentAcceptRepAlreadyExists",
    "PkiEnrollmentAcceptRepInvalidCertification",
    "PkiEnrollmentAcceptRepInvalidData",
    "PkiEnrollmentAcceptRepInvalidPayloadData",
    "PkiEnrollmentAcceptRepNoLongerAvailable",
    "PkiEnrollmentAcceptRepNotAllowed",
    "PkiEnrollmentAcceptRepNotFound",
    "PkiEnrollmentAcceptRepOk",
    "PkiEnrollmentAcceptRepUnknownStatus",
    "PkiEnrollmentAcceptReq",
    "PkiEnrollmentInfoRep",
    "PkiEnrollmentInfoRepNotFound",
    "PkiEnrollmentInfoRepOk",
    "PkiEnrollmentInfoRepUnknownStatus",
    "PkiEnrollmentInfoReq",
    "PkiEnrollmentInfoStatus",
    "PkiEnrollmentListItem",
    "PkiEnrollmentListRep",
    "PkiEnrollmentListRepNotAllowed",
    "PkiEnrollmentListRepOk",
    "PkiEnrollmentListRepUnknownStatus",
    "PkiEnrollmentListReq",
    "PkiEnrollmentRejectRep",
    "PkiEnrollmentRejectRepNoLongerAvailable",
    "PkiEnrollmentRejectRepNotAllowed",
    "PkiEnrollmentRejectRepNotFound",
    "PkiEnrollmentRejectRepOk",
    "PkiEnrollmentRejectRepUnknownStatus",
    "PkiEnrollmentRejectReq",
    "PkiEnrollmentSubmitRep",
    "PkiEnrollmentSubmitRepAlreadyEnrolled",
    "PkiEnrollmentSubmitRepAlreadySubmitted",
    "PkiEnrollmentSubmitRepEmailAlreadyUsed",
    "PkiEnrollmentSubmitRepIdAlreadyUsed",
    "PkiEnrollmentSubmitRepInvalidPayloadData",
    "PkiEnrollmentSubmitRepOk",
    "PkiEnrollmentSubmitRepUnknownStatus",
    "PkiEnrollmentSubmitReq",
    # Protocol Realm
    "RealmCreateReq",
    "RealmCreateRep",
    "RealmCreateRepOk",
    "RealmCreateRepInvalidCertification",
    "RealmCreateRepInvalidData",
    "RealmCreateRepNotFound",
    "RealmCreateRepAlreadyExists",
    "RealmCreateRepBadTimestamp",
    "RealmCreateRepUnknownStatus",
    "RealmStatusReq",
    "RealmStatusRep",
    "RealmStatusRepOk",
    "RealmStatusRepNotAllowed",
    "RealmStatusRepNotFound",
    "RealmStatusRepUnknownStatus",
    "RealmStatsReq",
    "RealmStatsRep",
    "RealmStatsRepOk",
    "RealmStatsRepNotAllowed",
    "RealmStatsRepNotFound",
    "RealmStatsRepUnknownStatus",
    "RealmGetRoleCertificatesReq",
    "RealmGetRoleCertificatesRep",
    "RealmGetRoleCertificatesRepOk",
    "RealmGetRoleCertificatesRepNotAllowed",
    "RealmGetRoleCertificatesRepNotFound",
    "RealmGetRoleCertificatesRepUnknownStatus",
    "RealmUpdateRolesReq",
    "RealmUpdateRolesRep",
    "RealmUpdateRolesRepOk",
    "RealmUpdateRolesRepNotAllowed",
    "RealmUpdateRolesRepInvalidCertification",
    "RealmUpdateRolesRepInvalidData",
    "RealmUpdateRolesRepAlreadyGranted",
    "RealmUpdateRolesRepIncompatibleProfile",
    "RealmUpdateRolesRepNotFound",
    "RealmUpdateRolesRepInMaintenance",
    "RealmUpdateRolesRepUserRevoked",
    "RealmUpdateRolesRepRequireGreaterTimestamp",
    "RealmUpdateRolesRepBadTimestamp",
    "RealmUpdateRolesRepUnknownStatus",
    "RealmStartReencryptionMaintenanceReq",
    "RealmStartReencryptionMaintenanceRep",
    "RealmStartReencryptionMaintenanceRepOk",
    "RealmStartReencryptionMaintenanceRepNotAllowed",
    "RealmStartReencryptionMaintenanceRepNotFound",
    "RealmStartReencryptionMaintenanceRepBadEncryptionRevision",
    "RealmStartReencryptionMaintenanceRepParticipantMismatch",
    "RealmStartReencryptionMaintenanceRepMaintenanceError",
    "RealmStartReencryptionMaintenanceRepInMaintenance",
    "RealmStartReencryptionMaintenanceRepBadTimestamp",
    "RealmStartReencryptionMaintenanceRepUnknownStatus",
    "RealmFinishReencryptionMaintenanceReq",
    "RealmFinishReencryptionMaintenanceRep",
    "RealmFinishReencryptionMaintenanceRepOk",
    "RealmFinishReencryptionMaintenanceRepNotAllowed",
    "RealmFinishReencryptionMaintenanceRepNotFound",
    "RealmFinishReencryptionMaintenanceRepBadEncryptionRevision",
    "RealmFinishReencryptionMaintenanceRepNotInMaintenance",
    "RealmFinishReencryptionMaintenanceRepMaintenanceError",
    "RealmFinishReencryptionMaintenanceRepUnknownStatus",
    "MaintenanceType",
    # Protocol Ping
    "AuthenticatedPingReq",
    "AuthenticatedPingRep",
    "AuthenticatedPingRepOk",
    "AuthenticatedPingRepUnknownStatus",
    "InvitedPingReq",
    "InvitedPingRep",
    "InvitedPingRepOk",
    "InvitedPingRepUnknownStatus",
    # Protocol User
    "UserGetReq",
    "UserGetRep",
    "UserGetRepOk",
    "UserGetRepNotFound",
    "UserGetRepUnknownStatus",
    "UserCreateReq",
    "UserCreateRep",
    "UserCreateRepOk",
    "UserCreateRepActiveUsersLimitReached",
    "UserCreateRepAlreadyExists",
    "UserCreateRepInvalidCertification",
    "UserCreateRepInvalidData",
    "UserCreateRepNotAllowed",
    "UserCreateRepUnknownStatus",
    "UserRevokeReq",
    "UserRevokeRep",
    "UserRevokeRepOk",
    "UserRevokeRepAlreadyRevoked",
    "UserRevokeRepInvalidCertification",
    "UserRevokeRepNotAllowed",
    "UserRevokeRepNotFound",
    "UserRevokeRepUnknownStatus",
    "DeviceCreateReq",
    "DeviceCreateRep",
    "DeviceCreateRepOk",
    "DeviceCreateRepAlreadyExists",
    "DeviceCreateRepBadUserId",
    "DeviceCreateRepInvalidCertification",
    "DeviceCreateRepInvalidData",
    "DeviceCreateRepUnknownStatus",
    "HumanFindReq",
    "HumanFindRep",
    "HumanFindRepOk",
    "HumanFindRepNotAllowed",
    "HumanFindRepUnknownStatus",
    "Trustchain",
    "HumanFindResultItem",
    # Protocol Vlob
    "VlobCreateReq",
    "VlobCreateRep",
    "VlobCreateRepOk",
    "VlobCreateRepAlreadyExists",
    "VlobCreateRepNotAllowed",
    "VlobCreateRepBadEncryptionRevision",
    "VlobCreateRepInMaintenance",
    "VlobCreateRepRequireGreaterTimestamp",
    "VlobCreateRepBadTimestamp",
    "VlobCreateRepNotASequesteredOrganization",
    "VlobCreateRepSequesterInconsistency",
    "VlobCreateRepRejectedBySequesterService",
    "VlobCreateRepTimeout",
    "VlobCreateRepUnknownStatus",
    "VlobReadReq",
    "VlobReadRep",
    "VlobReadRepOk",
    "VlobReadRepNotFound",
    "VlobReadRepNotAllowed",
    "VlobReadRepBadVersion",
    "VlobReadRepBadEncryptionRevision",
    "VlobReadRepInMaintenance",
    "VlobReadRepUnknownStatus",
    "VlobUpdateReq",
    "VlobUpdateRep",
    "VlobUpdateRepOk",
    "VlobUpdateRepNotFound",
    "VlobUpdateRepNotAllowed",
    "VlobUpdateRepBadVersion",
    "VlobUpdateRepBadEncryptionRevision",
    "VlobUpdateRepInMaintenance",
    "VlobUpdateRepRequireGreaterTimestamp",
    "VlobUpdateRepBadTimestamp",
    "VlobUpdateRepNotASequesteredOrganization",
    "VlobUpdateRepSequesterInconsistency",
    "VlobUpdateRepRejectedBySequesterService",
    "VlobUpdateRepTimeout",
    "VlobUpdateRepUnknownStatus",
    "VlobPollChangesReq",
    "VlobPollChangesRep",
    "VlobPollChangesRepOk",
    "VlobPollChangesRepNotFound",
    "VlobPollChangesRepNotAllowed",
    "VlobPollChangesRepInMaintenance",
    "VlobPollChangesRepUnknownStatus",
    "VlobListVersionsReq",
    "VlobListVersionsRep",
    "VlobListVersionsRepOk",
    "VlobListVersionsRepNotFound",
    "VlobListVersionsRepNotAllowed",
    "VlobListVersionsRepInMaintenance",
    "VlobListVersionsRepUnknownStatus",
    "VlobMaintenanceGetReencryptionBatchReq",
    "VlobMaintenanceGetReencryptionBatchRep",
    "VlobMaintenanceGetReencryptionBatchRepOk",
    "VlobMaintenanceGetReencryptionBatchRepNotFound",
    "VlobMaintenanceGetReencryptionBatchRepNotAllowed",
    "VlobMaintenanceGetReencryptionBatchRepNotInMaintenance",
    "VlobMaintenanceGetReencryptionBatchRepBadEncryptionRevision",
    "VlobMaintenanceGetReencryptionBatchRepMaintenanceError",
    "VlobMaintenanceGetReencryptionBatchRepUnknownStatus",
    "VlobMaintenanceSaveReencryptionBatchReq",
    "VlobMaintenanceSaveReencryptionBatchRep",
    "VlobMaintenanceSaveReencryptionBatchRepOk",
    "VlobMaintenanceSaveReencryptionBatchRepNotFound",
    "VlobMaintenanceSaveReencryptionBatchRepNotAllowed",
    "VlobMaintenanceSaveReencryptionBatchRepNotInMaintenance",
    "VlobMaintenanceSaveReencryptionBatchRepBadEncryptionRevision",
    "VlobMaintenanceSaveReencryptionBatchRepMaintenanceError",
    "VlobMaintenanceSaveReencryptionBatchRepUnknownStatus",
    "ReencryptionBatchEntry",
    # Regex
    "Regex",
]
