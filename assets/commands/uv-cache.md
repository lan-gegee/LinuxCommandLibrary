# TAGLINE

管理 uv 的软件包下载与构建缓存

# TLDR

**显示缓存目录**的位置

```uv cache dir```

**清除所有缓存数据**

```uv cache clean```

**清除指定软件包的缓存数据**

```uv cache clean [requests]```

**清除未使用的缓存条目**（过时/孤立的）

```uv cache prune```

**清除所有解压后的缓存数据**，同时保留下载文件

```uv cache prune --ci```

# SYNOPSIS

**uv cache** _command_ [_options_]

# PARAMETERS

**dir**
> 显示缓存目录的路径。

**clean** [_package_]
> 清除所有缓存数据；若指定了软件包，则只清除该软件包的数据。

**prune**
> 清除不再被任何项目需要的未使用缓存条目。

**--ci**
> 与 prune 配合使用，清除所有解压后的源代码发行版和预构建归档，针对只需要压缩归档的 CI 环境进行优化。

# DESCRIPTION

**uv cache** 管理 uv 的软件包缓存，其中存储着已下载的发行版、已构建的 wheel 和源码归档。该缓存通过避免重复下载和构建，显著加快后续安装的速度。

默认缓存位置在 Linux 上是 **$XDG_CACHE_HOME/uv** 或 **~/.cache/uv**，在 macOS 上是 **~/Library/Caches/uv**，在 Windows 上是 **%LOCALAPPDATA%\uv\cache**。可以通过 **UV_CACHE_DIR** 环境变量或 **--cache-dir** 全局选项覆盖。

# CAVEATS

prune 只会移除缓存元数据中未被任何项目锁文件引用的条目。如果怀疑缓存损坏，请使用 `clean` 进行完全重置。在 CI 环境中缓存可能会变得很大；可使用 `prune --ci` 将磁盘占用降到最低。

# INSTALL

```dnf: sudo dnf install uv```

```pacman: sudo pacman -S uv```

```apk: sudo apk add uv```

```brew: brew install uv```

```nix: nix profile install nixpkgs#uv```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[uv](/man/uv)(1), [uv-pip](/man/uv-pip)(1), [pip-cache](/man/pip-cache)(1)
