// Copyright The Gang Sweden, Inc. All Rights Reserved.
// Curveball / BladeBallArena - online abstraction layer
// Owns the provider instances and picks which implementations to build.

#pragma once

#include "CoreMinimal.h"
#include "Subsystems/GameInstanceSubsystem.h"
#include "MLCOnlineTypes.h"

#include "MLCOnlineSubsystem.generated.h"

class IMatchSessionProvider;
class IPlatformIdentityProvider;
class IPartyProvider;
class IMatchResultReporter;

MOGADISHU_API DECLARE_LOG_CATEGORY_EXTERN(LogMLCOnline, Log, All);

/**
 * The single place that knows which platform we are on.
 *
 * Providers are chosen at startup from config, not compiled in, using the seam the
 * project already has: per-target CustomConfig ("Steam" / "Epic") selects a different
 * WindowsEngine.ini stack, and the packaging targets BladeBallArenaClient and
 * BladeBallArenaEpicClient already exist. So this reads:
 *
 *   [MLCOnline]
 *   SessionProvider=Steam
 *   IdentityProvider=Steam
 *   PartyProvider=Steam
 *   ResultReporterEndpoint=https://...
 *
 * from the active CustomConfig, and step 2 is a config file plus an implementation,
 * not a code change here.
 *
 * Nothing outside Private/Online/ includes a platform SDK header. If a compile error
 * ever mentions Steam outside that folder, an abstraction has leaked.
 */
UCLASS()
class MOGADISHU_API UMLCOnlineSubsystem : public UGameInstanceSubsystem
{
	GENERATED_BODY()

public:
	virtual void Initialize(FSubsystemCollectionBase& Collection) override;
	virtual void Deinitialize() override;

	/**
	 * Accessors return references, never null.
	 *
	 * When a provider cannot be constructed (platform SDK missing, offline dev build)
	 * a null-object implementation is installed instead: every call completes with
	 * EMLCOnlineResult::NotReady and every query returns empty. Callers get a
	 * degraded game rather than a crash, and PIE without Steam running keeps working,
	 * which matters because that is how most iteration happens.
	 */
	IPlatformIdentityProvider& Identity() const;
	IMatchSessionProvider& Sessions() const;
	IPartyProvider& Party() const;
	IMatchResultReporter& Results() const;

	/** True when every provider reports IsReady(). Cheap enough to poll from UI. */
	UFUNCTION(BlueprintCallable, Category = "MLC Online")
	bool IsOnlineReady() const;

	/** "Steam" / "Epic". Exposed for telemetry tagging and store-facing UI copy. */
	UFUNCTION(BlueprintCallable, Category = "MLC Online")
	FString GetPlatformName() const;

private:
	TSharedPtr<IPlatformIdentityProvider> IdentityProvider;
	TSharedPtr<IMatchSessionProvider> SessionProvider;
	TSharedPtr<IPartyProvider> PartyProvider;
	TSharedPtr<IMatchResultReporter> ResultReporter;
};
