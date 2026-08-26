# TAGLINE

Valve 面向 Linux 的 Windows 游戏兼容层

# TLDR

**通过 Proton 运行 Windows 可执行文件**

```proton run [game.exe]```

**直接使用指定的 Proton 版本运行**

```~/.steam/steam/steamapps/common/Proton\ [7.0]/proton run [game.exe]```

**启用 Proton 日志，输出到 $HOME/steam-$APPID.log**

```PROTON_LOG=1 proton run [game.exe]```

**DirectX 转译时强制使用 OpenGL 而非 Vulkan**

```PROTON_USE_WINED3D=1 proton run [game.exe]```

**禁用 esync 和 fsync（针对不支持它们的内核）**

```PROTON_NO_ESYNC=1 PROTON_NO_FSYNC=1 proton run [game.exe]```

**等待上一个进程退出后再运行**

```proton waitforexitandrun [game.exe]```

# SYNOPSIS

**proton** _verb_ [_arguments_...]

# VERBS

**run**
> 在 Proton 下运行 Windows 可执行文件。

**waitforexitandrun**
> 等待残留的 Wine server 退出，然后运行可执行文件。Steam 在切换 prefix 时使用。

**runinprefix**
> 在当前已配置的 Proton prefix 内运行程序，而不创建新的 prefix。

**destroyprefix**
> 删除当前 Proton prefix，迫使 Steam 重新创建它。

**getcompatpath**
> 打印游戏的 pfx compatdata 路径。

**getnativepath**
> 打印与某个 Windows 路径对应的原生（Linux）路径。

# ENVIRONMENT VARIABLES

**STEAM_COMPAT_CLIENT_INSTALL_PATH**
> 必需。Steam 客户端安装路径（通常为 **~/.steam/steam**）。

**STEAM_COMPAT_DATA_PATH**
> 必需。Proton 存储 pfx、配置和缓存的目录。

**PROTON_LOG**
> 启用友好的日志记录，写入 **$HOME/steam-$APPID.log**。

**PROTON_USE_WINED3D**
> DirectX 使用 WineD3D（OpenGL）而非 DXVK/VKD3D。

**PROTON_NO_ESYNC**, **PROTON_NO_FSYNC**
> 禁用 esync 或 fsync 同步原语。

**PROTON_ENABLE_NVAPI**
> 启用 NVIDIA NVAPI，使 DLSS 和 Reflex 在受支持的 GPU 上可用。

**PROTON_FORCE_LARGE_ADDRESS_AWARE**
> 将 32 位可执行文件标记为大地址感知。

**PROTON_DUMP_DEBUG_COMMANDS**
> 导出辅助脚本，便于配合 winedbg、strace 等重新运行游戏进行调试。

# DESCRIPTION

**Proton** 是 Valve 的兼容层，用于通过 Steam 客户端在 Linux 上运行 Windows 游戏。它捆绑了打过补丁的 **Wine**、**DXVK** Direct3D 9/10/11 → Vulkan 转译器、面向 Direct3D 12 的 **VKD3D-Proton**、处理 XAudio2 的 **FAudio** 以及各种运行时库。Steam 通常通过 "Steam Play" 设置自动调用 proton；直接调用较为少见，主要用于故障排查。

每个游戏在 **$STEAM_COMPAT_DATA_PATH/pfx** 下都有自己的 Wine prefix。设置好所需的环境变量后，可以直接以 **run** 等动词调用 **proton** 脚本。

# CAVEATS

在 Steam 之外运行 proton 需要设置 **STEAM_COMPAT_CLIENT_INSTALL_PATH** 和 **STEAM_COMPAT_DATA_PATH**。并非所有 Windows 软件都能成功运行——兼容性报告请查阅 ProtonDB。带有内核级反作弊的游戏经常拒绝在 Proton 下运行。

# HISTORY

Proton 由 **Valve** 于 **2018 年 8 月**作为 Steam Play 计划的一部分发布，与 **CodeWeavers** 及 DXVK 作者 **Philip Rebohle** 合作开发。Proton Experimental 和 Proton-GE（社区分支）仍在持续获得频繁更新。

# SEE ALSO

[wine](/man/wine)(1), [steam](/man/steam)(1), [winetricks](/man/winetricks)(1)
