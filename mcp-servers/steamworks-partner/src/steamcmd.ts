/**
 * SteamCMD wrapper for build uploads
 *
 * Handles generating VDF build scripts and executing SteamCMD
 * to upload builds to Steam.
 */

import { execFile } from 'child_process';
import { promisify } from 'util';
import * as fs from 'fs/promises';
import * as path from 'path';

const execFileAsync = promisify(execFile);

export interface SteamCMDConfig {
  username: string;
  password?: string;
  steamcmdPath?: string; // defaults to 'steamcmd' in PATH
  guardCode?: string; // Steam Guard code if needed
}

export interface BuildScriptOptions {
  appId: number;
  depotId: number;
  contentRoot: string; // path to files to upload
  outputPath: string; // where to write VDF files
  buildDescription: string;
  setLive?: string; // branch to set live after upload (e.g., 'default', 'beta')
  localContentPath?: string; // relative to contentRoot
}

/**
 * Generate VDF build script for SteamCMD
 */
export async function generateBuildScript(options: BuildScriptOptions): Promise<string> {
  const {
    appId,
    depotId,
    contentRoot,
    outputPath,
    buildDescription,
    setLive,
    localContentPath = '*',
  } = options;

  const appBuildVdf = `"AppBuild"
{
  "AppID" "${appId}"
  "Desc" "${buildDescription}"
  "BuildOutput" "${outputPath}"
  "ContentRoot" "${contentRoot}"
  ${setLive ? `"SetLive" "${setLive}"` : ''}
  "Depots"
  {
    "${depotId}"
    {
      "FileMapping"
      {
        "LocalPath" "${localContentPath}"
        "DepotPath" "."
        "Recursive" "1"
      }
    }
  }
}`;

  const scriptPath = path.join(outputPath, `app_build_${appId}.vdf`);
  await fs.mkdir(outputPath, { recursive: true });
  await fs.writeFile(scriptPath, appBuildVdf, 'utf-8');

  return scriptPath;
}

/**
 * Execute SteamCMD to upload a build
 */
export async function uploadBuild(
  config: SteamCMDConfig,
  buildScriptPath: string
): Promise<{ stdout: string; stderr: string }> {
  const steamcmdPath = config.steamcmdPath || 'steamcmd';

  const args = [
    '+login',
    config.username,
    config.password || '',
  ];

  if (config.guardCode) {
    args.push(config.guardCode);
  }

  args.push(
    '+run_app_build',
    buildScriptPath,
    '+quit'
  );

  try {
    const result = await execFileAsync(steamcmdPath, args, {
      maxBuffer: 10 * 1024 * 1024, // 10MB buffer for output
    });
    return result;
  } catch (error: any) {
    throw new Error(`SteamCMD execution failed: ${error.message}\nStderr: ${error.stderr}`);
  }
}

/**
 * Check if SteamCMD is installed and accessible
 */
export async function checkSteamCMDInstalled(steamcmdPath = 'steamcmd'): Promise<boolean> {
  try {
    await execFileAsync(steamcmdPath, ['+quit']);
    return true;
  } catch {
    return false;
  }
}

/**
 * Generate a complete build upload workflow
 *
 * @returns Path to the generated build script
 */
export async function prepareBuildUpload(options: BuildScriptOptions): Promise<string> {
  // Validate paths exist
  try {
    await fs.access(options.contentRoot);
  } catch {
    throw new Error(`Content root does not exist: ${options.contentRoot}`);
  }

  // Generate VDF script
  const scriptPath = await generateBuildScript(options);

  return scriptPath;
}
