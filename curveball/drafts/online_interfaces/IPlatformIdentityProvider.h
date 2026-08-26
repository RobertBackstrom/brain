// Copyright The Gang Sweden, Inc. All Rights Reserved.
// Curveball / BladeBallArena - online abstraction layer
// Who the local player is on the current platform, and how to prove it to LootLocker.

#pragma once

#include "CoreMinimal.h"
#include "MLCOnlineTypes.h"

/** Ticket is a platform auth token (Steam encrypted app ticket today), hex-encoded. */
DECLARE_DELEGATE_TwoParams(FMLCAuthTicketReady, EMLCOnlineResult /*Result*/, const FString& /*Ticket*/);

/** Fires when a previously unresolved player gains its second identity half. */
DECLARE_MULTICAST_DELEGATE_OneParam(FMLCOnPlayerResolved, const FMLCPlayerHandle& /*Player*/);

/**
 * Platform identity, and the ULID <-> platform-id mapping the rest of the layer depends on.
 *
 * Step 1 implementation FSteamIdentityProvider mostly moves existing code: the Steam
 * auth-ticket path already exists inside ULootLockerLocalPlayerSubsystem and is lifted
 * here rather than rewritten. Step 2 FEOSIdentityProvider swaps the ticket for an EOS
 * Connect token, and LootLocker keeps working with no changes on its side, which is the
 * whole point of putting the seam here.
 */
class IPlatformIdentityProvider
{
public:
	virtual ~IPlatformIdentityProvider() = default;

	/** "Steam", "Epic", "Switch". Also the value LootLocker wants for its platform field. */
	virtual FString GetPlatformName() const = 0;

	/** False until the platform SDK has a signed-in user. Nothing else here is meaningful before that. */
	virtual bool IsReady() const = 0;

	/**
	 * Fetch a platform auth ticket for the LootLocker session handshake.
	 *
	 * Tickets are short-lived and single-use on some platforms, so this always
	 * goes to the platform rather than returning a cached value.
	 */
	virtual void GetAuthTicket(FMLCAuthTicketReady OnReady) = 0;

	/**
	 * The local player. AccountUlid is empty until BindLocalAccountUlid runs,
	 * so anything persistent must wait for IsFullyResolved().
	 */
	virtual FMLCPlayerHandle GetLocalPlayer() const = 0;

	/**
	 * Called once by the LootLocker bootstrap when a session is established.
	 *
	 * This is what closes the identity loop: after this, the local player's ULID is
	 * publishable as lobby member data and remote players become resolvable.
	 */
	virtual void BindLocalAccountUlid(const FString& Ulid) = 0;

	/**
	 * Learn a remote player's mapping, normally from lobby member data on join.
	 * Idempotent; a repeat with the same pair is not an error.
	 */
	virtual void RegisterRemotePlayer(const FMLCPlayerHandle& Player) = 0;

	/** Look up either direction. False if that player has not been seen this session. */
	virtual bool ResolveByPlatformId(const FString& PlatformId, FMLCPlayerHandle& Out) const = 0;
	virtual bool ResolveByAccountUlid(const FString& Ulid, FMLCPlayerHandle& Out) const = 0;

	/**
	 * Fires when RegisterRemotePlayer completes a mapping.
	 *
	 * Party UI needs this: a member can appear in a lobby a frame before its ULID
	 * arrives, and widgets keyed on ULID would otherwise render an empty row.
	 */
	virtual FMLCOnPlayerResolved& OnPlayerResolved() = 0;
};
