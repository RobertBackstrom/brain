// Copyright The Gang Sweden, Inc. All Rights Reserved.
// Curveball / BladeBallArena - online abstraction layer
// Getting match outcomes to something trusted enough to write progression.

#pragma once

#include "CoreMinimal.h"
#include "MLCOnlineTypes.h"

DECLARE_DELEGATE_TwoParams(FMLCReportComplete, EMLCOnlineResult /*Result*/, const FString& /*ServerMessage*/);

/**
 * Replaces the trusted-server half of LootLocker.
 *
 * Today ULootLockerServerGranter and ULootLockerServerLoadoutValidator use the
 * LootLocker SERVER key, which can write any player's inventory, wallet and
 * progression for the whole game. The client targets strip the server SDK
 * precisely so that key never reaches a player's machine. Under a listen server
 * the host IS a player's machine, so the key cannot ship and the grants have to
 * happen somewhere else.
 *
 * That somewhere is a small AP-hosted service holding the key. This interface is
 * the game's side of it. It stays an interface rather than a concrete class so
 * the sink can change (a console-cert-friendly endpoint, or a return to dedicated
 * servers if the game takes off) without touching any caller.
 *
 * Reporting is per round, not only at match end. A host quitting mid-match ends
 * the match for everyone in step 1, and round-boundary reporting is what stops
 * that also costing players the progression they had already earned.
 */
class IMatchResultReporter
{
public:
	virtual ~IMatchResultReporter() = default;

	/**
	 * Submit a completed round. Called by the host and by every client with their
	 * own independent view, which is what makes the service's cross-report
	 * comparison possible. A host reporting alone proves nothing.
	 */
	virtual void ReportRound(const FMLCMatchReport& Report, FMLCReportComplete OnComplete) = 0;

	/** Submit the whole-match summary. RoundIndex is -1 by convention. */
	virtual void ReportMatchEnd(const FMLCMatchReport& Report, FMLCReportComplete OnComplete) = 0;

	/**
	 * Whether reports are currently reaching the service.
	 *
	 * If this is false the match still plays; only persistence is affected. Callers
	 * should surface that to the player rather than failing the match, and reports
	 * queue for retry rather than being dropped.
	 */
	virtual bool IsReachable() const = 0;

	/** Reports accepted locally but not yet acknowledged. Diagnostics and QA. */
	virtual int32 GetPendingReportCount() const = 0;
};
