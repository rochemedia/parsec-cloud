from typing import List, Optional, Tuple
from parsec._parsec_pyi.ids import BlockID, RealmID, SequesterServiceID, VlobID, DeviceID
from parsec._parsec_pyi.time import DateTime

class AuthenticatedAnyCmdReq:
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> BlockReadReq: ...

class InvitedAnyCmdReq:
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> BlockReadReq: ...

class RepWithReason:
    def __init__(self, reason: Optional[str]) -> None: ...
    @property
    def reason(self) -> Optional[str]: ...

class UnknownStatus(RepWithReason):
    @property
    def status(self) -> str: ...

# Block

class BlockCreateReq:
    def __init__(self, block_id: BlockID, realm_id: RealmID, block: bytes) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: BlockCreateReq) -> bool: ...
    def __ne__(self, other: BlockCreateReq) -> bool: ...
    @property
    def block_id(self) -> BlockID: ...
    @property
    def realm_id(self) -> RealmID: ...
    @property
    def block(self) -> bytes: ...
    def dump(self) -> bytes: ...

class BlockCreateRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: BlockCreateRep) -> bool: ...
    def __ne__(self, other: BlockCreateRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> BlockCreateRep: ...

class BlockCreateRepOk(BlockCreateRep): ...
class BlockCreateRepAlreadyExists(BlockCreateRep): ...
class BlockCreateRepNotFound(BlockCreateRep): ...
class BlockCreateRepTimeout(BlockCreateRep): ...
class BlockCreateRepNotAllowed(BlockCreateRep): ...
class BlockCreateRepInMaintenance(BlockCreateRep): ...
class BlockCreateRepUnknownStatus(UnknownStatus, BlockCreateRep): ...

class BlockReadReq:
    def __init__(self, block_id: BlockID) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: BlockReadReq) -> bool: ...
    def __ne__(self, other: BlockReadReq) -> bool: ...
    @property
    def block_id(self) -> BlockID: ...
    def dump(self) -> bytes: ...

class BlockReadRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: BlockReadRep) -> bool: ...
    def __ne__(self, other: BlockReadRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> BlockReadRep: ...

class BlockReadRepOk(BlockReadRep):
    def __init__(self, block: bytes) -> None: ...
    @property
    def block(self) -> bytes: ...

class BlockReadRepNotFound(BlockReadRep): ...
class BlockReadRepTimeout(BlockReadRep): ...
class BlockReadRepNotAllowed(BlockReadRep): ...
class BlockReadRepInMaintenance(BlockReadRep): ...
class BlockReadRepUnknownStatus(UnknownStatus, BlockReadRep): ...

# Vlob

class VlobCreateReq:
    def __init__(
        self,
        realm_id: RealmID,
        encryption_revision: int,
        vlob_id: VlobID,
        timestamp: DateTime,
        blob: bytes,
        sequester_blob: Optional[dict[SequesterServiceID, bytes]],
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobCreateReq) -> bool: ...
    def __ne__(self, other: VlobCreateReq) -> bool: ...
    @property
    def realm_id(self) -> RealmID: ...
    @property
    def encryption_revision(self) -> int: ...
    @property
    def vlob_id(self) -> VlobID: ...
    @property
    def timestamp(self) -> DateTime: ...
    @property
    def blob(self) -> bytes: ...
    @property
    def sequester_blob(self) -> Optional[dict[SequesterServiceID, bytes]]: ...
    def dump(self) -> bytes: ...

class VlobCreateRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobCreateRep) -> bool: ...
    def __ne__(self, other: VlobCreateRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> VlobCreateRep: ...

class VlobCreateRepRequireGreaterTimestamp(VlobCreateRep):
    def __init__(self, strictly_greater_than: DateTime): ...
    @property
    def strictly_greater_than(self) -> DateTime: ...

class VlobCreateRepBadTimestamp(RepWithReason, VlobCreateRep):
    def __init__(
        self,
        reason: Optional[str],
        ballpark_client_early_offset: float,
        ballpark_client_late_offset: float,
        backend_timestamp: DateTime,
        client_timestamp: DateTime,
    ) -> None: ...
    @property
    def ballpark_client_early_offset(self) -> float: ...
    @property
    def ballpark_client_late_offset(self) -> float: ...
    @property
    def backend_timestamp(self) -> DateTime: ...
    @property
    def client_timestamp(self) -> DateTime: ...

class VlobCreateRepSequesterInconsistency(VlobCreateRep):
    def __init__(
        self, sequester_authority_certificate: bytes, sequester_services_certificates: Tuple[bytes]
    ) -> None: ...
    @property
    def sequester_authority_certificate(self) -> bytes: ...
    @property
    def sequester_services_certificates(self) -> Tuple[bytes]: ...

class VlobCreateRepOk(VlobCreateRep): ...
class VlobCreateRepAlreadyExists(RepWithReason, VlobCreateRep): ...
class VlobCreateRepNotAllowed(VlobCreateRep): ...
class VlobCreateRepBadEncryptionRevision(VlobCreateRep): ...
class VlobCreateRepInMaintenance(VlobCreateRep): ...
class VlobCreateRepNotASequesteredOrganization(VlobCreateRep): ...
class VlobCreateRepUnknownStatus(UnknownStatus, VlobCreateRep): ...

class VlobReadReq:
    def __init__(
        self,
        encryption_revision: int,
        vlob_id: VlobID,
        version: Optional[int],
        timestamp: Optional[DateTime],
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobReadReq) -> bool: ...
    def __ne__(self, other: VlobReadReq) -> bool: ...
    @property
    def encryption_revision(self) -> int: ...
    @property
    def vlob_id(self) -> VlobID: ...
    @property
    def version(self) -> Optional[int]: ...
    @property
    def timestamp(self) -> Optional[DateTime]: ...
    def dump(self) -> bytes: ...

class VlobReadRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobReadRep) -> bool: ...
    def __ne__(self, other: VlobReadRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> VlobReadRep: ...

class VlobReadRepOk(VlobReadRep):
    def __init__(
        self,
        version: int,
        blob: bytes,
        author: DeviceID,
        timestamp: DateTime,
        author_last_role_granted_on: Optional[DateTime],
    ) -> None: ...
    @property
    def version(self) -> int: ...
    @property
    def blob(self) -> bytes: ...
    @property
    def author(self) -> DeviceID: ...
    @property
    def timestamp(self) -> DateTime: ...
    @property
    def author_last_role_granted_on(self) -> Optional[DateTime]: ...

class VlobReadRepNotFound(RepWithReason, VlobReadRep): ...
class VlobReadRepNotAllowed(VlobReadRep): ...
class VlobReadRepBadVersion(VlobReadRep): ...
class VlobReadRepBadEncryptionRevision(VlobReadRep): ...
class VlobReadRepInMaintenance(VlobReadRep): ...
class VlobReadRepUnknownStatus(UnknownStatus, VlobReadRep): ...

class VlobUpdateReq:
    def __init__(
        self,
        encryption_revision: int,
        vlob_id: VlobID,
        timestamp: DateTime,
        version: int,
        blob: bytes,
        sequester_blob: Optional[dict[SequesterServiceID, bytes]],
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobUpdateReq) -> bool: ...
    def __ne__(self, other: VlobUpdateReq) -> bool: ...
    @property
    def encryption_revision(self) -> int: ...
    @property
    def vlob_id(self) -> VlobID: ...
    @property
    def timestamp(self) -> DateTime: ...
    @property
    def version(self) -> int: ...
    @property
    def blob(self) -> bytes: ...
    @property
    def sequester_blob(self) -> Optional[dict[SequesterServiceID, bytes]]: ...
    def dump(self) -> bytes: ...

class VlobUpdateRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobUpdateRep) -> bool: ...
    def __ne__(self, other: VlobUpdateRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> VlobUpdateRep: ...

class VlobUpdateRepRequireGreaterTimestamp(VlobUpdateRep):
    def __init__(self, strictly_greater_than: DateTime): ...
    @property
    def strictly_greater_than(self) -> DateTime: ...

class VlobUpdateRepBadTimestamp(RepWithReason, VlobUpdateRep):
    def __init__(
        self,
        reason: Optional[str],
        ballpark_client_early_offset: float,
        ballpark_client_late_offset: float,
        backend_timestamp: DateTime,
        client_timestamp: DateTime,
    ) -> None: ...
    @property
    def ballpark_client_early_offset(self) -> float: ...
    @property
    def ballpark_client_late_offset(self) -> float: ...
    @property
    def backend_timestamp(self) -> DateTime: ...
    @property
    def client_timestamp(self) -> DateTime: ...

class VlobUpdateRepSequesterInconsistency(VlobUpdateRep):
    def __init__(
        self, sequester_authority_certificate: bytes, sequester_services_certificates: Tuple[bytes]
    ) -> None: ...
    @property
    def sequester_authority_certificate(self) -> bytes: ...
    @property
    def sequester_services_certificates(self) -> Tuple[bytes]: ...

class VlobUpdateRepOk(VlobUpdateRep): ...
class VlobUpdateRepNotFound(RepWithReason, VlobUpdateRep): ...
class VlobUpdateRepNotAllowed(VlobUpdateRep): ...
class VlobUpdateRepBadVersion(VlobUpdateRep): ...
class VlobUpdateRepBadEncryptionRevision(VlobUpdateRep): ...
class VlobUpdateRepInMaintenance(VlobUpdateRep): ...
class VlobUpdateRepNotASequesteredOrganization(VlobUpdateRep): ...
class VlobUpdateRepUnknownStatus(UnknownStatus, VlobUpdateRep): ...

class VlobPollChangesReq:
    def __init__(
        self,
        realm_id: RealmID,
        last_checkpoint: int,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobPollChangesReq) -> bool: ...
    def __ne__(self, other: VlobPollChangesReq) -> bool: ...
    @property
    def realm_id(self) -> RealmID: ...
    @property
    def last_checkpoint(self) -> int: ...
    def dump(self) -> bytes: ...

class VlobPollChangesRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobPollChangesRep) -> bool: ...
    def __ne__(self, other: VlobPollChangesRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> VlobPollChangesRep: ...

class VlobPollChangesRepOk(VlobPollChangesRep):
    def __init__(
        self,
        changes: dict[VlobID, int],
        current_checkpoint: int,
    ) -> None: ...
    @property
    def changes(self) -> dict[VlobID, int]: ...
    @property
    def current_checkpoint(self) -> int: ...

class VlobPollChangesRepNotFound(RepWithReason, VlobPollChangesRep): ...
class VlobPollChangesRepNotAllowed(VlobPollChangesRep): ...
class VlobPollChangesRepInMaintenance(VlobPollChangesRep): ...
class VlobPollChangesRepUnknownStatus(UnknownStatus, VlobPollChangesRep): ...

class VlobListVersionsReq:
    def __init__(
        self,
        vlob_id: VlobID,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobListVersionsReq) -> bool: ...
    def __ne__(self, other: VlobListVersionsReq) -> bool: ...
    @property
    def vlob_id(self) -> VlobID: ...
    def dump(self) -> bytes: ...

class VlobListVersionsRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobListVersionsRep) -> bool: ...
    def __ne__(self, other: VlobListVersionsRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> VlobListVersionsRep: ...

class VlobListVersionsRepOk(VlobListVersionsRep):
    def __init__(
        self,
        versions: dict[int, Tuple[DateTime, DeviceID]],
    ) -> None: ...
    @property
    def versions(self) -> dict[int, Tuple[DateTime, DeviceID]]: ...

class VlobListVersionsRepNotFound(RepWithReason, VlobListVersionsRep): ...
class VlobListVersionsRepNotAllowed(VlobListVersionsRep): ...
class VlobListVersionsRepInMaintenance(VlobListVersionsRep): ...
class VlobListVersionsRepUnknownStatus(UnknownStatus, VlobListVersionsRep): ...

class VlobMaintenanceGetReencryptionBatchReq:
    def __init__(
        self,
        realm_id: RealmID,
        encryption_revision: int,
        size: int,
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobMaintenanceGetReencryptionBatchReq) -> bool: ...
    def __ne__(self, other: VlobMaintenanceGetReencryptionBatchReq) -> bool: ...
    @property
    def realm_id(self) -> RealmID: ...
    @property
    def encryption_revision(self) -> int: ...
    @property
    def size(self) -> int: ...
    def dump(self) -> bytes: ...

class VlobMaintenanceGetReencryptionBatchRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobMaintenanceGetReencryptionBatchRep) -> bool: ...
    def __ne__(self, other: VlobMaintenanceGetReencryptionBatchRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> VlobMaintenanceGetReencryptionBatchRep: ...

class VlobMaintenanceGetReencryptionBatchRepOk(VlobMaintenanceGetReencryptionBatchRep):
    def __init__(
        self,
        batch: List[ReencryptionBatchEntry],
    ) -> None: ...
    @property
    def batch(self) -> Tuple[ReencryptionBatchEntry]: ...

class VlobMaintenanceGetReencryptionBatchRepNotFound(
    RepWithReason,
    VlobMaintenanceGetReencryptionBatchRep,
): ...
class VlobMaintenanceGetReencryptionBatchRepNotAllowed(VlobMaintenanceGetReencryptionBatchRep): ...
class VlobMaintenanceGetReencryptionBatchRepNotInMaintenance(
    RepWithReason,
    VlobMaintenanceGetReencryptionBatchRep,
): ...
class VlobMaintenanceGetReencryptionBatchRepBadEncryptionRevision(
    VlobMaintenanceGetReencryptionBatchRep
): ...
class VlobMaintenanceGetReencryptionBatchRepMaintenanceError(
    RepWithReason, VlobMaintenanceGetReencryptionBatchRep
): ...
class VlobMaintenanceGetReencryptionBatchRepUnknownStatus(
    UnknownStatus, VlobMaintenanceGetReencryptionBatchRep
): ...

class VlobMaintenanceSaveReencryptionBatchReq:
    def __init__(
        self,
        realm_id: RealmID,
        encryption_revision: int,
        batch: Tuple[ReencryptionBatchEntry],
    ) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobMaintenanceSaveReencryptionBatchReq) -> bool: ...
    def __ne__(self, other: VlobMaintenanceSaveReencryptionBatchReq) -> bool: ...
    @property
    def realm_id(self) -> RealmID: ...
    @property
    def encryption_revision(self) -> int: ...
    @property
    def batch(self) -> Tuple[ReencryptionBatchEntry]: ...
    def dump(self) -> bytes: ...

class VlobMaintenanceSaveReencryptionBatchRep:
    def __init__(self) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: VlobMaintenanceSaveReencryptionBatchRep) -> bool: ...
    def __ne__(self, other: VlobMaintenanceSaveReencryptionBatchRep) -> bool: ...
    def dump(self) -> bytes: ...
    def load(buf: bytes) -> VlobMaintenanceSaveReencryptionBatchRep: ...

class VlobMaintenanceSaveReencryptionBatchRepOk(VlobMaintenanceSaveReencryptionBatchRep):
    def __init__(
        self,
        total: int,
        done: int,
    ) -> None: ...
    @property
    def total(self) -> int: ...
    @property
    def done(self) -> int: ...

class VlobMaintenanceSaveReencryptionBatchRepNotFound(
    RepWithReason,
    VlobMaintenanceSaveReencryptionBatchRep,
): ...
class VlobMaintenanceSaveReencryptionBatchRepNotAllowed(
    VlobMaintenanceSaveReencryptionBatchRep
): ...
class VlobMaintenanceSaveReencryptionBatchRepNotInMaintenance(
    RepWithReason,
    VlobMaintenanceSaveReencryptionBatchRep,
): ...
class VlobMaintenanceSaveReencryptionBatchRepBadEncryptionRevision(
    VlobMaintenanceSaveReencryptionBatchRep
): ...
class VlobMaintenanceSaveReencryptionBatchRepMaintenanceError(
    RepWithReason,
    VlobMaintenanceSaveReencryptionBatchRep,
): ...
class VlobMaintenanceSaveReencryptionBatchRepUnknownStatus(
    UnknownStatus, VlobMaintenanceSaveReencryptionBatchRep
): ...

class ReencryptionBatchEntry:
    def __init__(self, vlob_id: VlobID, version: int, blob: bytes) -> None: ...
    def __repr__(self) -> str: ...
    def __eq__(self, other: ReencryptionBatchEntry) -> bool: ...
    def __ne__(self, other: ReencryptionBatchEntry) -> bool: ...
    @property
    def vlob_id(self) -> VlobID: ...
    @property
    def version(self) -> int: ...
    @property
    def blob(self) -> bytes: ...
