# TAGLINE

查看并管理 pip 的 wheel 缓存

# TLDR

**显示缓存目录**

```pip cache dir```

**列出缓存的软件包**

```pip cache list```

**显示缓存信息**

```pip cache info```

**从缓存中移除特定软件包**

```pip cache remove [package]```

**清空全部缓存**

```pip cache purge```

# SYNOPSIS

**pip** **cache** _command_ [_options_]

# PARAMETERS

**dir**
> 打印缓存目录路径。

**info**
> 显示缓存大小和位置。

**list** [_pattern_]
> 列出当前缓存中的 wheel 文件，可选用 glob _pattern_ 或软件包名进行过滤。

**remove** _pattern_
> 移除匹配 _pattern_（glob 或软件包名）的缓存 wheel 文件。

**purge**
> 移除缓存中的所有 wheel 文件和 HTTP 响应。

**--format** _FORMAT_
> **list** 的输出格式：**human**（默认）或 **abspath**（完整文件路径）。也可通过 **PIP_FORMAT** 配置。

# DESCRIPTION

**pip cache** 管理 pip 的 HTTP 响应缓存和已构建 wheel 缓存。pip 将下载的以及本地构建的 wheel 存储在每用户缓存目录下（例如 Linux 上为 **~/.cache/pip**，macOS 上为 **~/Library/Caches/pip**，Windows 上为 **%LocalAppData%\pip\Cache**），这样后续安装相同版本时就可以跳过网络往返和构建步骤。

要对单次安装绕过缓存，使用 **pip install --no-cache-dir** _pkg_；要覆盖缓存位置，可设置 **PIP_CACHE_DIR** 环境变量或传入 **pip --cache-dir** _DIR_。

# CAVEATS

**pip cache list** 和 **remove** 只作用于 wheel 缓存，不包括 HTTP 响应缓存；而 **purge** 会同时清空两者。HTTP 缓存使用 ETag/Last-Modified 校验，因此随时可以安全删除。

# INSTALL

```apk: sudo apk add py3-pip```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pip](/man/pip)(1), [pip-install](/man/pip-install)(1)
