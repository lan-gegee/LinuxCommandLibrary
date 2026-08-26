# TAGLINE

间隔重复记忆卡片程序

# TLDR

**启动** Anki

```anki```

以**指定配置文件**打开

```anki -p "[Profile Name]"```

导入一个**牌组**

```anki [deck.apkg]```

在**基础目录**中打开

```anki -b [~/.anki2]```

# SYNOPSIS

**anki** [_-p profile_] [_-b basedir_] [_file_]

# DESCRIPTION

**anki** 是一款间隔重复记忆卡片程序，帮助高效记忆信息。它使用智能调度算法，以最佳间隔显示卡片，在学习时间最少的前提下最大化记忆保持率。

该应用支持在卡片上使用文本、图像、音频和视频，并可通过卡片模板和插件进行深度定制。它通过 AnkiWeb 在多台设备间同步。

# PARAMETERS

**-p** _profile_
> 加载指定的用户配置

**-b** _directory_
> 使用替代的基础目录

**-l** _lang_
> 界面语言代码

**--syncserver** _url_
> 自定义同步服务器 URL

# CAVEATS

首次启动时构建数据库可能较慢。牌组导入可能体积较大。同步需要 AnkiWeb 账号。某些插件可能与最新版本不兼容。

# HISTORY

**Anki** 由 Damien Elmes 创建，于 **2006** 年首次发布。它基于 Piotr Wozniak 开发的 SM2 间隔重复算法。名称来自日语中表示"记忆"的词。

# INSTALL

```pacman: sudo pacman -S anki```

```apk: sudo apk add anki```

```nix: nix profile install nixpkgs#anki```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[man](/man/man)(1)
