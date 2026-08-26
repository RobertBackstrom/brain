// Copyright The Gang Sweden, Inc. All Rights Reserved.
// Curveball / BladeBallArena - online abstraction layer
// Finding, creating and joining the session a match is played in.

#pragma once

#include "CoreMinimal.h"
#include "MLCOnlineTypes.h"

DECLARE_DELEGATE_TwoParams(FMLCSessionOpComplete, EMLCOnlineResult /*Result*/, const FMLCSessionInfo& /*Session*/);

DECLARE_MULTICAST_DELEGATE_OneParam(FMLCOnSessionStateChanged, EMLCSessionState /*NewState*/);

/** A player left or joined the session we are in. Not party membership; that is IPartyProvider. */
DECLARE_MULTICAST_DELEGATE_TwoParams(FMLCOnSessionMemberChanged, const FMLCPlayerHandle& /*Player*/, bool /*bJoined*/);

/**
 * Replaces the GameLift placement path.
 *
 * What the old flow did: POST start-solo-matchmaking, poll get-solo-matchmaking-status
 * until the backend handed back an IP, a Port and a PlayerSessionId for a dedicated
 * server it had spun up. What this does instead: search the platform's session list,
 * join the best result, and host if there is nothing to join.
 *
 * UMatchmakingSubsystem keeps its exact Blueprint surface on top of this, including
 * the seven-parameter FStatusUpdateEvent. IP carries FMLCSessionInfo::ConnectString,
 * Port goes unused, PlayerSessionId carries SessionId.
 */
class IMatchSessionProvider
{
public:
	virtual ~IMatchSessionProvider() = default;

	virtual EMLCSessionState GetState() const = 0;

	/** False until the platform session interface is usable. */
	virtual bool IsReady() const = 0;

	/**
	 * Find a joinable session for this mode, or create one and host.
	 *
	 * Deliberately one call rather than Find then Create. Every caller wants
	 * "get me into a match", and splitting it pushes the find-failed-so-host
	 * race onto the caller, which is where that bug would live.
	 *
	 * MaxPlayers applies only if this ends up creating. Pass the mode's configured
	 * value; the old backend held these numbers and we do not have them yet.
	 */
	virtual void FindOrHost(const FString& ModeKey, int32 MaxPlayers, FMLCSessionOpComplete OnComplete) = 0;

	/**
	 * Host without searching first. Used when a party leader starts a match: the
	 * party has already decided who plays together, so searching would be wrong.
	 */
	virtual void HostSession(const FString& ModeKey, int32 MaxPlayers, FMLCSessionOpComplete OnComplete) = 0;

	/** Join a specific known session, e.g. following a party leader or an accepted invite. */
	virtual void JoinSession(const FString& SessionId, FMLCSessionOpComplete OnComplete) = 0;

	/** Abort an in-flight FindOrHost. Completes the original callback with Cancelled. */
	virtual void CancelSearch() = 0;

	virtual void LeaveSession(FMLCSessionOpComplete OnComplete) = 0;

	virtual bool GetCurrentSession(FMLCSessionInfo& Out) const = 0;

	/**
	 * Platform-native invite to the current session (Steam overlay today).
	 * No-op returning NotSupported on platforms without an overlay invite path.
	 */
	virtual void InviteToSession(const FMLCPlayerHandle& Player) = 0;

	/**
	 * How long the current search has been running, and how many candidates it has
	 * seen. There is no queue any more, but FStatusUpdateEvent still carries
	 * EstimatedWaitTime and QueuedPlayerCount to Blueprint, and those widgets are
	 * still wired. This gives the subsystem something honest to put in them.
	 */
	virtual float GetSearchElapsedSeconds() const = 0;
	virtual int32 GetCandidateSessionCount() const = 0;

	virtual FMLCOnSessionStateChanged& OnStateChanged() = 0;
	virtual FMLCOnSessionMemberChanged& OnMemberChanged() = 0;
};
