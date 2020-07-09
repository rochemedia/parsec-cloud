# Parsec Cloud (https://parsec.cloud) Copyright (c) AGPLv3 2019 Scille SAS

from parsec.backend.postgresql.queries import (
    Q,
    q_realm_internal_id,
    q_user_internal_id,
    q_organization_internal_id,
)
from parsec.backend.vlob import VlobAccessError, VlobNotFoundError
from parsec.backend.postgresql.tables import STR_TO_REALM_ROLE


_q_check_realm_access = Q(
    f"""
WITH cte_current_realm_roles AS (
    SELECT DISTINCT ON(user_) user_, role
    FROM  realm_user_role
    WHERE realm = { q_realm_internal_id(organization_id="$organization_id", realm_id="$realm_id") }
    ORDER BY user_, certified_on DESC
)
SELECT role
FROM user_
LEFT JOIN cte_current_realm_roles
ON user_._id = cte_current_realm_roles.user_
WHERE user_._id = { q_user_internal_id(organization_id="$organization_id", user_id="$user_id") }
"""
)


async def query_check_realm_access(conn, organization_id, realm_id, author, allowed_roles):
    rep = await conn.fetchrow(
        *_q_check_realm_access(
            organization_id=organization_id, realm_id=realm_id, user_id=author.user_id
        )
    )

    if not rep:
        raise VlobNotFoundError(f"User `{author.user_id}` doesn't exist")

    if STR_TO_REALM_ROLE.get(rep[0]) not in allowed_roles:
        raise VlobAccessError()


_q_get_realm_id_from_vlob_id = Q(
    f"""
SELECT
    realm.realm_id
FROM vlob_atom
INNER JOIN vlob_encryption_revision
ON  vlob_atom.vlob_encryption_revision = vlob_encryption_revision._id
INNER JOIN realm
ON vlob_encryption_revision.realm = realm._id
WHERE vlob_atom._id = (
    SELECT _id
    FROM vlob_atom
    WHERE
        organization = { q_organization_internal_id("$organization_id") }
        AND vlob_id = $vlob_id
    LIMIT 1
)
LIMIT 1
"""
)


async def _get_realm_id_from_vlob_id(conn, organization_id, vlob_id):

    realm_id = await conn.fetchval(
        *_q_get_realm_id_from_vlob_id(organization_id=organization_id, vlob_id=vlob_id)
    )
    if not realm_id:
        raise VlobNotFoundError(f"Vlob `{vlob_id}` doesn't exist")
    return realm_id
