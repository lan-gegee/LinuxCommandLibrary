# TAGLINE

终端中的 Neofetch 风格音乐信息展示工具

# TLDR

**显示当前曲目信息**

```mufetch```

**搜索曲目**

```mufetch search -t "[track name]"```

**搜索艺术家**

```mufetch search -a "[artist name]"```

# SYNOPSIS

**mufetch** [_command_] [_options_]

# DESCRIPTION

**mufetch** 是一款在终端中展示音乐元数据的 CLI 工具，设计美学受 neofetch 启发。它显示曲目详情、专辑信息和艺术家元数据，并将专辑封面和艺术家照片直接渲染在终端里。

功能包括时长、热度、流派和粉丝数等指标、可点击的 Spotify 链接、带类型过滤（track、album、artist）的搜索命令，以及适配终端显示的自适应图像缩放。

# CAVEATS

音乐数据需要 Spotify API 凭据。图像显示取决于终端的能力。

# HISTORY

**mufetch** 由 **Ashish Kumar**（ashish0kumar）创建，使用 **Go** 编写。

# INSTALL

```brew: brew install mufetch```

```nix: nix profile install nixpkgs#mufetch```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[neofetch](/man/neofetch)(1)
