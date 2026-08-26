// Copyright The Gang Sweden, Inc. All Rights Reserved.
// Curveball / BladeBallArena - online abstraction layer
// Pre-match grouping: party membership, invites, ready state, mode selection.

#pragma once

#include "CoreMinimal.h"
#include "MLCOnlineTypes.h"

/** One member of a party. Maps 1:1 onto FPartyPlayerResponse for the Blueprint layer. */
USTRUCT()
struct FMLCPartyMember
{
	GENERATED_BODY()

	UPROPERTY()
	FMLCPlayerHandle Player;

	UPROPERTY()
	bool bIsLeader = false;

	UPROPERTY()
	bool bIsReady = false;
};

/**
 * Party state, shaped so UGamePartySubsystem can translate it into the existing
 * FPartyResponse without inventing or dropping fields.
 *
 * FPartyResponse carries two GameLift-era fields that Blueprint can see:
 * ticket_id and gamelift_matchmaking_configuration. Freezing the struct is not
 * enough if widgets branch on those being non-empty, so both are populated from
 * here (SessionId and ModeKey) rather than left blank.
 */
USTRUCT()
struct FMLCPartyState
{
	GENERATED_BODY()

	UPROPERTY()
	FString PartyId;

	UPROPERTY()
	TArray<FMLCPartyMember> Members;

	/** ULIDs with an invite outstanding. Matches FPartyResponse::pending_invites. */
	UPROPERTY()
	TArray<FString> PendingInvites;

	UPROPERTY()
	FString ModeKey;

	/** Feeds FPartyResponse::ticket_id. Never empty while a party exists. */
	UPROPERTY()
	FString SessionId;
};

USTRUCT()
struct FMLCPartyInvite
{
	GENERATED_BODY()

	UPROPERTY()
	FString PartyId;

	UPROPERTY()
	FMLCPlayerHandle From;
};

DECLARE_DELEGATE_TwoParams(FMLCPartyOpComplete, EMLCOnlineResult /*Result*/, const FMLCPartyState& /*State*/);

DECLARE_MULTICAST_DELEGATE_TwoParams(FMLCOnPartyUpdated, const FMLCPartyState& /*State*/, bool /*bHasActiveParty*/);
DECLARE_MULTICAST_DELEGATE_OneParam(FMLCOnPartyInviteReceived, const FMLCPartyInvite& /*Invite*/);
DECLARE_MULTICAST_DELEGATE_TwoParams(FMLCOnPartyReadyChanged, const FMLCPlayerHandle& /*Player*/, bool /*bIsReady*/);
DECLARE_MULTICAST_DELEGATE_OneParam(FMLCOnPartyMemberLoadoutChanged, const FMLCPlayerHandle& /*Player*/);
DECLARE_MULTICAST_DELEGATE(FMLCOnLeftParty);

/**
 * Replaces the eight /api/v1/parties/* endpoints and the party half of the
 * three-second message pump.
 *
 * The old design polled: every member asked the backend for party state on a timer,
 * and changes arrived as PARTY_UPDATED / PARTY_READY_STATE_UPDATED messages. Steam
 * lobbies are callback-driven, so state arrives when it changes rather than up to
 * three seconds later. UBackendMessagePump keeps its OnMessageReceived delegate and
 * becomes a local bus fed by these events, so every Blueprint subscriber survives.
 *
 * Two capabilities do not survive step 1 and callers must tolerate it:
 * invite timeouts (there is no Steam equivalent to the backend's BlockInvitesUntil,
 * so that becomes client-local), and presence for non-friends.
 */
class IPartyProvider
{
public:
	virtual ~IPartyProvider() = default;

	virtual bool IsReady() const = 0;

	virtual void CreateParty(FMLCPartyOpComplete OnComplete) = 0;
	virtual void LeaveParty(FMLCPartyOpComplete OnComplete) = 0;

	/**
	 * Invite a player. Requires Player.IsFullyResolved(): the invite goes out over
	 * the platform (needs PlatformId) while the pending-invite list the UI renders
	 * is keyed on ULID.
	 */
	virtual void SendInvite(const FMLCPlayerHandle& Player) = 0;
	virtual void AcceptInvite(const FString& PartyId, FMLCPartyOpComplete OnComplete) = 0;
	virtual void DeclineInvite(const FString& PartyId) = 0;

	/** Leader only. Non-leaders get Failed rather than a silent no-op. */
	virtual void KickMember(const FMLCPlayerHandle& Player) = 0;

	virtual void SetLocalReady(bool bReady) = 0;

	/** Leader only. Mode is party-wide, matching the old setpartygamemode semantics. */
	virtual void SetPartyMode(const FString& ModeKey) = 0;

	virtual bool GetParty(FMLCPartyState& Out) const = 0;
	virtual bool IsLocalPlayerLeader() const = 0;

	/**
	 * Presence for a party member or friend.
	 *
	 * On Steam this only answers for friends, where the backend answered for anyone
	 * the client registered interest in. Returns NotSupported-equivalent (false) for
	 * non-friends rather than guessing, so the UI can show unknown instead of offline.
	 */
	virtual bool IsPlayerOnline(const FMLCPlayerHandle& Player, bool& bOutIsOnline) const = 0;

	virtual FMLCOnPartyUpdated& OnPartyUpdated() = 0;
	virtual FMLCOnPartyInviteReceived& OnInviteReceived() = 0;
	virtual FMLCOnPartyReadyChanged& OnReadyChanged() = 0;
	virtual FMLCOnPartyMemberLoadoutChanged& OnMemberLoadoutChanged() = 0;
	virtual FMLCOnLeftParty& OnLeftParty() = 0;
};
