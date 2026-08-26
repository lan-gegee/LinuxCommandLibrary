# TAGLINE

Immich 照片服务器的命令行界面

# TLDR

**上传照片**

```immich upload [/path/to/photos]```

**上传并指定相册**

```immich upload --album [AlbumName] [/path/to/photos]```

**登录服务器**

```immich login [https://server] [api-key]```

**查看服务器信息**

```immich server-info```

**试运行上传**

```immich upload --dry-run [/path/to/photos]```

# SYNOPSIS

**immich** _command_ [_options_]

# PARAMETERS

_COMMAND_
> 要运行的子命令。

**upload**
> 上传文件。

**login**
> 向服务器进行身份验证。

**server-info**
> 显示服务器信息。

**--album** _NAME_
> 目标相册。

**--dry-run**
> 模拟上传。

**--help**
> 显示帮助信息。

# DESCRIPTION

**immich-cli** 是 Immich 照片服务器的命令行界面。它支持批量上传和服务器管理。

该工具通过 API 密钥进行身份验证，并上传照片/视频。它支持分配相册和重复项检测。

# CAVEATS

需要 Immich 服务器。使用 API 密钥身份验证。基于 Node.js。

# HISTORY

immich-cli 是 **Immich** 照片管理服务器的官方 CLI。

# INSTALL

```brew: brew install immich-cli```

```nix: nix profile install nixpkgs#immich-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[immich](/man/immich)(1), [immich-go](/man/immich-go)(1), [rclone](/man/rclone)(1)
