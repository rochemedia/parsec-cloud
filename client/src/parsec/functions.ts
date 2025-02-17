// Parsec Cloud (https://parsec.cloud) Copyright (c) BUSL-1.1 2016-present Scille SAS

import {
  libparsec,
  InviteListItem,
} from '@/plugins/libparsec';

import {
  AvailableDevice,
  ClientConfig,
  DeviceAccessStrategyPassword,
  ClientEvent,
  Handle,
  ClientStartError,
  Result,
  ClientStopError,
  UserInvitation,
  WorkspaceID,
  WorkspaceName,
  InvitationToken,
  InvitationEmailSentStatus,
  NewUserInvitationError,
  ClientListWorkspacesError,
  ClientCreateWorkspaceError,
  InvitationStatus,
  ListInvitationsError,
  NewDeviceInvitationError,
  DeleteInvitationError,
  BootstrapOrganizationError,
  OrganizationID,
  DeviceFileType,
  ParsedBackendAddr,
  BackendAddr,
  ClientEventPing,
  ParseBackendAddrError,
  UserInfo,
  ClientInfo,
  ClientInfoError,
  UserProfile,
  GetWorkspaceNameError,
  ClientListUsersError,
  WorkspaceInfo,
  WorkspaceRole,
  DeviceInfo,
  ClientListUserDevicesError,
  UserID,
  UserTuple,
  ClientListWorkspaceUsersError,
  ClientShareWorkspaceError,
  CreateOrganizationError,
} from '@/parsec/types';
import { getParsecHandle } from '@/parsec/routing';
import { DateTime } from 'luxon';
import { DEFAULT_HANDLE, MOCK_WAITING_TIME, getClientConfig, wait } from '@/parsec/internals';

export async function listAvailableDevices(): Promise<Array<AvailableDevice>> {
  return await libparsec.listAvailableDevices(window.getConfigDir());
}

export async function login(device: AvailableDevice, password: string): Promise<Result<Handle, ClientStartError>> {
  function parsecEventCallback(event: ClientEvent): void {
    console.log('Event received', event);
  }

  if (window.isDesktop()) {
    const clientConfig = getClientConfig();
    const strategy: DeviceAccessStrategyPassword = {
      tag: 'Password',
      password: password,
      keyFile: device.keyFilePath,
    };
    return await libparsec.clientStart(clientConfig, parsecEventCallback, strategy);
  } else {
    return new Promise<Result<Handle, ClientStartError>>((resolve, _reject) => {
      if (password === 'P@ssw0rd.' || password === 'AVeryL0ngP@ssw0rd') {
        resolve({ok: true, value: DEFAULT_HANDLE });
      }
      resolve({ok: false, error: {tag: 'LoadDeviceDecryptionFailed', error: 'WrongPassword'}});
    });
  }
}

export async function logout(): Promise<Result<null, ClientStopError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    return await libparsec.clientStop(handle);
  } else {
    return new Promise<Result<null, ClientStopError>>((resolve, _reject) => {
      resolve({ok: true, value: null});
    });
  }
}

export async function inviteUser(email: string): Promise<Result<[InvitationToken, InvitationEmailSentStatus], NewUserInvitationError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    const ret = await libparsec.clientNewUserInvitation(handle, email, true);
    if (ret.ok) {
      return {ok: true, value: [ret.value.token, ret.value.emailSentStatus] };
    } else {
      return ret;
    }
  } else {
    return new Promise<Result<[InvitationToken, InvitationEmailSentStatus], NewUserInvitationError>>((resolve, _reject) => {
      resolve({ ok: true, value: ['1234', InvitationEmailSentStatus.Success] });
    });
  }
}

export async function listWorkspaces(): Promise<Result<Array<WorkspaceInfo>, ClientListWorkspacesError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    const result = await libparsec.clientListWorkspaces(handle);

    if (result.ok) {
      const returnValue: Array<WorkspaceInfo> = [];
      for (let i = 0; i < result.value.length; i++) {
        const sharingResult = await getWorkspaceSharing(result.value[i].id, false);
        const info: WorkspaceInfo = {
          id: result.value[i].id,
          name: result.value[i].name,
          selfRole: result.value[i].selfRole,
          sharing: [],
          size: 0,
          lastUpdated: DateTime.now(),
          availableOffline: false,
        };
        if (sharingResult.ok) {
          info.sharing = sharingResult.value;
        }
        returnValue.push(info);
      }
      return new Promise<Result<Array<WorkspaceInfo>, ClientListWorkspacesError>>((resolve, _reject) => {
        resolve({ok: true, value: returnValue});
      });
    } else {
      return result;
    }
  } else {
    const value: Array<WorkspaceInfo> = [{
      'id': '1', 'name': 'Trademeet', 'selfRole': WorkspaceRole.Owner, size: 934_583, lastUpdated: DateTime.now().minus(2000),
      availableOffline: false, sharing: [],
    }, {
      'id': '2', 'name': 'The Copper Coronet', 'selfRole': WorkspaceRole.Manager, size: 3_489_534_274, lastUpdated: DateTime.now(),
      availableOffline: false, sharing: [],
    }];

    for (let i = 0; i < value.length; i++) {
      const result = await getWorkspaceSharing(value[i].id, false);
      if (result.ok) {
        value[i].sharing = result.value;
      }
    }

    return new Promise<Result<Array<WorkspaceInfo>, ClientListWorkspacesError>>((resolve, _reject) => {
      resolve({ok: true, value: value});
    });
  }
}

export async function createWorkspace(name: WorkspaceName): Promise<Result<WorkspaceID, ClientCreateWorkspaceError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    return await libparsec.clientCreateWorkspace(handle, name);
  } else {
    return new Promise<Result<WorkspaceID, ClientCreateWorkspaceError>>((resolve, _reject) => {
      resolve({ ok: true, value: '1337' });
    });
  }
}

export async function inviteDevice(sendEmail: boolean):
  Promise<Result<[InvitationToken, InvitationEmailSentStatus], NewDeviceInvitationError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    const ret = await libparsec.clientNewDeviceInvitation(handle, sendEmail);
    if (ret.ok) {
      return {ok: true, value: [ret.value.token, ret.value.emailSentStatus] };
    } else {
      return ret;
    }
  }
  return new Promise<Result<[InvitationToken, InvitationEmailSentStatus], NewDeviceInvitationError>>((resolve, _reject) => {
    resolve({ ok: true, value: ['1234', InvitationEmailSentStatus.Success] });
  });
}

export async function listUserInvitations(): Promise<Result<Array<UserInvitation>, ListInvitationsError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    const result = await libparsec.clientListInvitations(handle);

    if (!result.ok) {
      return result;
    }
    // No need to add device invitations
    result.value = result.value.filter((item: InviteListItem) => item.tag === 'User');
    // Convert InviteListItemUser to UserInvitation
    result.value = result.value.map((item) => {
      item.createdOn = DateTime.fromSeconds(item.createdOn as any as number);
      return item;
    });
    return result as any;
  } else {
    return new Promise<Result<Array<UserInvitation>, ListInvitationsError>>((resolve, _reject) => {
      const ret: Array<UserInvitation> = [{
        tag: 'User',
        token: '1234',
        createdOn: DateTime.now(),
        claimerEmail: 'shadowheart@swordcoast.faerun',
        status: InvitationStatus.Ready,
      }, {
        tag: 'User',
        token: '5678',
        createdOn: DateTime.now(),
        claimerEmail: 'gale@waterdeep.faerun',
        status: InvitationStatus.Ready,
      }];
      resolve({ ok: true, value: ret });
    });
  }
}

export async function cancelInvitation(token: InvitationToken): Promise<Result<null, DeleteInvitationError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    return await libparsec.clientDeleteInvitation(handle, token);
  } else {
    return new Promise<Result<null, DeleteInvitationError>>((resolve, _reject) => {
      resolve({ok: true, value: null});
    });
  }
}

export async function createOrganization(
  backendAddr: BackendAddr, orgName: OrganizationID, userName: string, email: string, password: string, deviceLabel: string,
): Promise<Result<AvailableDevice, BootstrapOrganizationError>> {
  function parsecEventCallback(event: ClientEventPing): void {
    console.log('On event', event);
  }

  const bootstrapAddr = await libparsec.buildBackendOrganizationBootstrapAddr(backendAddr, orgName);

  if (window.isDesktop()) {
    const config: ClientConfig = {
      configDir: window.getConfigDir(),
      dataBaseDir: window.getDataBaseDir(),
      mountpointBaseDir: window.getMountpointDir(),
      workspaceStorageCacheSize: {tag: 'Default'},
    };
    const result = await libparsec.bootstrapOrganization(
      config,
      parsecEventCallback,
      bootstrapAddr,
      {tag: 'Password', password: password},
      {label: userName, email: email},
      deviceLabel,
      null,
    );
    if (!result.ok && result.error.tag === CreateOrganizationError.BadTimestamp) {
      result.error.clientTimestamp = DateTime.fromSeconds(result.error.clientTimestamp as any as number);
      result.error.serverTimestamp = DateTime.fromSeconds(result.error.serverTimestamp as any as number);
    }
    return result;
  } else {
    await wait(MOCK_WAITING_TIME);
    return new Promise<Result<AvailableDevice, BootstrapOrganizationError>>((resolve, _reject) => {
      resolve({ok: true, value: {
        keyFilePath: '/path',
        organizationId: 'MyOrg',
        deviceId: 'deviceid',
        humanHandle: {
          label: 'A',
          email: 'a@b.c',
        },
        deviceLabel: 'a@b',
        slug: 'slug',
        ty: DeviceFileType.Password,
      }});
    });
  }
}

export async function parseBackendAddr(addr: string): Promise<Result<ParsedBackendAddr, ParseBackendAddrError>> {
  return await libparsec.parseBackendAddr(addr);
}

export async function getClientInfo(): Promise<Result<ClientInfo, ClientInfoError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    return await libparsec.clientInfo(handle);
  } else {
    return new Promise<Result<ClientInfo, ClientInfoError>>((resolve, _reject) => {
      resolve({ok: true, value: {
        organizationAddr: 'parsec://example.com/MyOrg',
        organizationId: 'MyOrg',
        deviceId: 'device1',
        deviceLabel: 'My First Device',
        userId: 'me',
        currentProfile: UserProfile.Admin,
        humanHandle: {
          email: 'user@host.com',
          label: 'Gordon Freeman',
        },
      }});
    });
  }
}

export async function getWorkspaceName(workspaceId: WorkspaceID): Promise<Result<WorkspaceName, GetWorkspaceNameError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    const result = await libparsec.clientListWorkspaces(handle);
    if (result.ok) {
      const workspace = result.value.find((info) => {
        if (info.id === workspaceId) {
          return true;
        }
        return false;
      });
      if (workspace) {
        return new Promise<Result<WorkspaceName, GetWorkspaceNameError>>((resolve, _reject) => {
          resolve({ok: true, value: workspace.name});
        });
      }
    }
    return new Promise<Result<WorkspaceID, GetWorkspaceNameError>>((resolve, _reject) => {
      resolve({ok: false, error: {tag: 'NotFound'}});
    });
  } else {
    return new Promise<Result<WorkspaceID, GetWorkspaceNameError>>((resolve, _reject) => {
      if (workspaceId === '1') {
        resolve({ok: true, value: 'Trademeet'});
      } else if (workspaceId === '2') {
        resolve({ok: true, value: 'The Copper Coronet'});
      } else {
        resolve({ok: true, value: 'My Workspace'});
      }
    });
  }
}

export async function isValidWorkspaceName(name: string): Promise<boolean> {
  return await libparsec.validateEntryName(name);
}

export async function isValidPath(path: string): Promise<boolean> {
  return await libparsec.validatePath(path);
}

export async function isValidUserName(name: string): Promise<boolean> {
  return await libparsec.validateHumanHandleLabel(name);
}

export async function isValidEmail(email: string): Promise<boolean> {
  return await libparsec.validateEmail(email);
}

export async function isValidDeviceName(name: string): Promise<boolean> {
  return await libparsec.validateDeviceLabel(name);
}

export async function isValidInvitationToken(token: string): Promise<boolean> {
  return await libparsec.validateInvitationToken(token);
}

export async function listUsers(skipRevoked = true): Promise<Result<Array<UserInfo>, ClientListUsersError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    const result = await libparsec.clientListUsers(handle, skipRevoked);
    if (result.ok) {
      result.value.map((item) => {
        item.createdOn = DateTime.fromSeconds(item.createdOn as any as number);
        if (item.revokedOn) {
          item.revokedOn = DateTime.fromSeconds(item.revokedOn as any as number);
        }
        (item as UserInfo).isRevoked = (): boolean => item.revokedOn !== null;
        return item;
      });
    }
    return result as any as Promise<Result<Array<UserInfo>, ClientListUsersError>>;
  } else {
    return new Promise<Result<Array<UserInfo>, ClientListUsersError>>((resolve, _reject) => {
      const value: Array<UserInfo> = [{
        id: 'id1',
        // cspell:disable-next-line
        humanHandle: {label: 'Cernd', email: 'cernd@gmail.com'},
        currentProfile: UserProfile.Standard,
        createdOn: DateTime.now(),
        createdBy: 'device',
        revokedOn: null,
        revokedBy: null,
        isRevoked: (): boolean => false,
      }, {
        id: 'id2',
        // cspell:disable-next-line
        humanHandle: {label: 'Jaheira', email: 'jaheira@gmail.com'},
        currentProfile: UserProfile.Admin,
        createdOn: DateTime.now(),
        createdBy: 'device',
        revokedOn: null,
        revokedBy: null,
        isRevoked: (): boolean => false,
      }, {
        id: 'me',
        humanHandle: {
          email: 'user@host.com',
          label: 'Gordon Freeman',
        },
        currentProfile: UserProfile.Admin,
        createdOn: DateTime.now(),
        createdBy: 'device',
        revokedOn: null,
        revokedBy: null,
        isRevoked: (): boolean => false,
      }];
      if (!skipRevoked) {
        value.push({
          id: 'id3',
          // cspell:disable-next-line
          humanHandle: {label: 'Valygar Corthala', email: 'val@gmail.com'},
          currentProfile: UserProfile.Standard,
          createdOn: DateTime.now(),
          createdBy: 'device',
          revokedOn: DateTime.now(),
          revokedBy: 'device',
          isRevoked: (): boolean => true,
        });
      }
      resolve({ok: true, value: value});
    });
  }
}

export async function getWorkspaceSharing(workspaceId: WorkspaceID, includeAllUsers = false, includeSelf = false):
  Promise<Result<Array<[UserTuple, WorkspaceRole | null]>, ClientListWorkspaceUsersError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    let selfId: UserID | null = null;

    if (!includeSelf) {
      const clientResult = await getClientInfo();
      if (clientResult.ok) {
        selfId = clientResult.value.userId;
      }
    }

    const result = await libparsec.clientListWorkspaceUsers(handle, workspaceId);
    if (result.ok) {
      const value: Array<[UserTuple, WorkspaceRole | null]> = [];

      for (const sharing of result.value) {
        if (includeSelf || (!includeSelf && selfId !== sharing.userId)) {
          value.push([{id: sharing.userId, humanHandle: sharing.humanHandle || {label: sharing.userId, email: ''}}, sharing.role]);
        }
      }
      if (includeAllUsers) {
        const usersResult = await libparsec.clientListUsers(handle, true);
        if (usersResult.ok) {
          for (const user of usersResult.value) {
            if (!value.find((item) => item[0].id === user.id) && (includeSelf || (!includeSelf && user.id !== selfId))) {
              value.push([{id: user.id, humanHandle: user.humanHandle || {label: user.id, email: ''}}, null]);
            }
          }
        }
      }
      return new Promise<Result<Array<[UserTuple, WorkspaceRole | null]>, ClientListWorkspaceUsersError>>((resolve, _reject) => {
        resolve({ok: true, value: value});
      });
    }
    return new Promise<Result<Array<[UserTuple, WorkspaceRole | null]>, ClientListWorkspaceUsersError>>((resolve, _reject) => {
      resolve({ok: false, error: result.error});
    });
  } else {
    const value: Array<[UserTuple, WorkspaceRole | null]> = [[
      // cspell:disable-next-line
      {id: '1', humanHandle: {label: 'Korgan Bloodaxe', email: 'korgan@gmail.com'}}, WorkspaceRole.Reader,
    ], [
      // cspell:disable-next-line
      {id: '2', humanHandle: {label: 'Cernd', email: 'cernd@gmail.com'}}, WorkspaceRole.Contributor,
    ]];

    if (includeSelf) {
      value.push([{id: 'me', humanHandle: {email: 'user@host.com', label: 'Gordon Freeman'}}, WorkspaceRole.Owner]);
    }

    if (includeAllUsers) {
      // cspell:disable-next-line
      value.push([{id: '3', humanHandle: {label: 'Jaheira', email: 'jaheira@gmail.com'}}, null]);
    }

    return new Promise<Result<Array<[UserTuple, WorkspaceRole | null]>, ClientListWorkspaceUsersError>>((resolve, _reject) => {
      resolve({ok: true, value: value});
    });
  }
}

export async function listUserDevices(user: UserID): Promise<Result<Array<DeviceInfo>, ClientListUserDevicesError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    const result = await libparsec.clientListUserDevices(handle, user);
    if (result.ok) {
      result.value.map((item) => {
        item.createdOn = DateTime.fromSeconds(item.createdOn as any as number);
        return item;
      });
    }
    return result as any as Promise<Result<Array<DeviceInfo>, ClientListUserDevicesError>>;
  } else {
    return new Promise<Result<Array<DeviceInfo>, ClientListUserDevicesError>>((resolve, _reject) => {
      resolve({ok: true, value: [{
        id: 'device1',
        deviceLabel: 'My First Device',
        createdOn: DateTime.now(),
        createdBy: 'some_device',
      }, {
        id: 'device2',
        deviceLabel: 'My Second Device',
        createdOn: DateTime.now(),
        createdBy: 'device1',
      }]});
    });
  }
}

export async function shareWorkspace(workspaceId: WorkspaceID, userId: UserID, role: WorkspaceRole | null):
  Promise<Result<null, ClientShareWorkspaceError>> {
  const handle = getParsecHandle();

  if (handle !== null && window.isDesktop()) {
    return await libparsec.clientShareWorkspace(handle, workspaceId, userId, role);
  } else {
    return new Promise<Result<null, ClientShareWorkspaceError>>((resolve, _reject) => {
      resolve({ok: true, value: null});
    });
  }
}
