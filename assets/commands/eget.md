# TAGLINE

GitHub 发布版二进制下载器

# TLDR

**下载最新发布版**的二进制

```eget [owner/repo]```

**下载特定的**二进制

```eget [owner/repo] --asset [linux-amd64]```

**下载到指定**目录

```eget [owner/repo] --to [/usr/local/bin]```

**下载特定版本**

```eget [owner/repo] --tag [v1.2.3]```

**从归档中提取特定文件**

```eget [owner/repo] --file [binary]```

**使用 SHA-256 校验和验证**

```eget [owner/repo] --sha256 [checksum]```

**下载源代码**而不是二进制

```eget [owner/repo] --source```

**仅下载而不解压**

```eget [owner/repo] --download-only```

# SYNOPSIS

**eget** [_options_] _repository_

# PARAMETERS

_REPOSITORY_
> owner/repo 格式的 GitHub 仓库。

**--asset** _PATTERN_
> 要下载的资源名称模式。

**--to** _DIR_
> 目标目录。

**--tag** _VERSION_
> 特定的版本标签。

**--file** _NAME_
> 从归档中提取特定文件。

**--sha256** _HASH_
> 用 SHA-256 校验和验证下载的文件。

**--source**
> 下载源代码归档而不是发布版二进制。

**--download-only**
> 仅下载资源而不解压。

**-q**, **--quiet**
> 抑制输出。

**--upgrade-only**
> 只有当有更新的版本时才下载。

**--help**
> 显示帮助信息。

# DESCRIPTION

**eget** 从 GitHub 发布中下载并解压预编译的二进制。它会自动检测适合你平台（操作系统和架构）的资源，并从归档中提取可执行文件。

该工具简化了安装通过 GitHub 发布分发二进制的 Go、Rust 及其他编译型工具的过程。它会自动处理 tar、zip 等归档格式。

eget 支持校验和验证，并可通过 dotfile 进行配置以管理多个工具。

# CAVEATS

需要访问 GitHub API。可能受到速率限制。请信任你所下载二进制的来源。平台检测不一定总是准确。

# HISTORY

eget 的诞生是为了简化从 GitHub 发布中下载和安装工具这一常见任务，用一条命令取代手动下载、解压和安装。

# INSTALL

```brew: brew install eget```

```nix: nix profile install nixpkgs#eget```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [curl](/man/curl)(1), [wget](/man/wget)(1)
