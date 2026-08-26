# TAGLINE

管理 uv 自身的安装

# TLDR

**将 uv 更新到最新版本**

```uv self update```

**将 uv 更新到指定版本**

```uv self update [0.6.0]```

**卸载 uv**

```uv self uninstall```

# SYNOPSIS

**uv** **self** _command_ [_options_]

# PARAMETERS

**update**
> 将 uv 更新到最新版本，或更新到指定版本。

**uninstall**
> 卸载 uv。

**--target-version** _version_
> 更新到特定版本（与 update 子命令配合使用）。

# DESCRIPTION

**uv self** 管理 uv 自身的安装。可用于将 uv 更新到最新版本、更新到特定版本或完全卸载 uv。update 命令会下载新的二进制文件并就地替换当前安装。

# SEE ALSO

[uv](/man/uv)(1), [uv-version](/man/uv-version)(1), [uv-pip](/man/uv-pip)(1), [uv-tool](/man/uv-tool)(1), [pip](/man/pip)(1)
