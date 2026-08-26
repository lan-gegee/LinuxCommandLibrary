# TAGLINE

录制和回放终端会话

# TLDR

**录制**终端会话（3.0 及以上版本必须提供文件名）

```asciinema rec [recording.cast]```

**回放**已录制的会话

```asciinema play [recording.cast]```

**上传**到 asciinema.org

```asciinema upload [recording.cast]```

以指定**标题**录制

```asciinema rec -t "[My recording]" [recording.cast]```

以**空闲时间上限**录制

```asciinema rec --idle-time-limit=[2] [recording.cast]```

对终端会话进行**直播**

```asciinema stream -l```

# SYNOPSIS

**asciinema** _rec_|_play_|_cat_|_convert_|_upload_|_stream_|_session_|_auth_ [_options_] [_file_]

# DESCRIPTION

**asciinema** 用于录制和回放终端会话。它捕获终端输出及其时间信息，生成轻量的录像文件，可以分享或嵌入网页。

与视频屏幕录制不同，asciinema 的录像是基于文本的，回放时可以复制粘贴其中的内容，而且文件体积很小。

# PARAMETERS

**rec** _file_
> 录制终端会话。在 3.0+ 中必须提供文件名，且 rec 不再自动上传（请使用 upload 命令）。

**play** _file_
> 回放已录制的会话

**cat** _file..._
> 将两个或更多录像合并为一个（3.0+）。

**convert** _input_ _output_
> 将录像转换为另一种 asciicast 格式（3.0+）。

**upload** _file_
> 将录像上传到 asciinema.org

**stream**
> 直播终端会话（3.0+）。

**session**
> 通用会话，可录制、可直播，或两者兼用（3.0+）。

**auth**
> 用你的 asciinema 服务器账号验证本次安装

**-t** _title_, **--title** _title_
> 录像标题

**-c** _cmd_, **--command** _cmd_
> 要录制的命令（默认：$SHELL）

**--idle-time-limit** _sec_
> 帧之间的最大空闲时间

**-i** _sec_
> --idle-time-limit 的简写形式

**-s** _speed_, **--speed** _speed_
> 回放速度倍率

**--cols** _n_ / **--rows** _n_
> 覆盖终端尺寸

# CONFIGURATION

**~/.config/asciinema/config.toml**
> CLI 3.0+ 的用户配置文件（TOML 格式），用于默认录制设置、服务器 URL 和身份验证。更早的 2.x 版本使用的是 **~/.config/asciinema/config**。

# CAVEATS

录像会原样捕获终端中显示的所有内容，包括敏感数据。上传前请先检查。回放要求终端具备与录制时相同的能力。

# HISTORY

**asciinema** 由 Marcin Kulik 创建，第一个版本于 **2011** 年前后发布。它已成为终端录制与分享的标准工具。

# INSTALL

```dnf: sudo dnf install asciinema```

```pacman: sudo pacman -S asciinema```

```apk: sudo apk add asciinema```

```zypper: sudo zypper install asciinema```

```brew: brew install asciinema```

```nix: nix profile install nixpkgs#asciinema```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[script](/man/script)(1), [ttyrec](/man/ttyrec)(1), [agg](/man/agg)(1)

# RESOURCES

```[Source code](https://github.com/asciinema/asciinema)```

```[Homepage](https://asciinema.org)```

```[Documentation](https://docs.asciinema.org)```

<!-- verified: 2026-06-17 -->
