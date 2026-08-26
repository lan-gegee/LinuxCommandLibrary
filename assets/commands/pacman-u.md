# TAGLINE

**pacman --upgrade** 的简写形式，从本地软件包文件安装或升级

# TLDR

此命令是 **pacman --upgrade** 的别名。完整文档见：

```tldr pacman upgrade```

**安装本地软件包文件**

```sudo pacman -U [package.pkg.tar.zst]```

用通配符**安装多个本地软件包**

```sudo pacman -U [*.pkg.tar.zst]```

**从 URL 安装软件包**

```sudo pacman -U [https://example.com/package.pkg.tar.zst]```

**从 pacman 缓存降级**

```sudo pacman -U [/var/cache/pacman/pkg/package-oldver-x86_64.pkg.tar.zst]```

**安装时跳过依赖版本检查**

```sudo pacman -Udd [package.pkg.tar.zst]```

# SYNOPSIS

**pacman** {**-U** | **--upgrade**} [_options_] _file_|_url_ ...

# DESCRIPTION

**pacman -U**（长格式 `--upgrade`）从本地软件包文件或 URL 安装或升级软件包，绕过已配置的仓库。这是安装本地构建的软件包（来自 `makepkg`/AUR 助手）、从缓存降级以及手动下载的软件包的方式。

与根据同步数据库解析名称的 `-S` 不同，`-U` 直接作用于 `.pkg.tar.zst`（或 `.pkg.tar.xz`、`.pkg.tar.gz`）文件。依赖仍然会对照同步数据库进行解析，因此建议先通过 `pacman -Sy` 完成完整刷新。

# COMMON OPTIONS

**-d**, **--nodeps**
> 跳过依赖版本检查。加倍使用（`-dd`）则完全跳过依赖检查。

**--asdeps**
> 将安装的软件包标记为依赖（非显式请求）。

**--asexplicit**
> 将安装的软件包标记为显式安装。

**--needed**
> 若相同版本已安装则跳过安装。

**--overwrite** _GLOB_
> 覆盖匹配 _GLOB_ 的冲突文件（请谨慎使用）。

**--noconfirm**
> 不请求任何确认。

**-v**, **--verbose**
> 详细输出。

# CAVEATS

需要 root 权限（使用 `sudo`）。软件包必须针对相同架构且由受信任的密钥签名，否则需要传入 `--nosigcheck`（危险）。降级可能破坏依赖较新版本的软件包。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-upgrade](/man/pacman-upgrade)(8), [pacman-key](/man/pacman-key)(8), [makepkg](/man/makepkg)(8)
