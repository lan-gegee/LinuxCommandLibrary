# TAGLINE

跨平台的基于终端的音乐播放器与服务器

# TLDR

**启动音乐播放器 TUI**

```musikcube```

**启动无界面音频服务器守护进程**

```musikcubed```

# SYNOPSIS

**musikcube**

**musikcubed**

# DESCRIPTION

**musikcube** 是一款用 C++ 编写的功能完备的终端音乐播放器、媒体库管理器和流式音频服务器。它在 Windows、macOS 和 Linux 上原生运行，提供用于浏览和播放音乐库的 TUI 界面。

配套的守护进程 **musikcubed** 以无头音频服务器形式运行，可将音乐串流到远程的 musikcube 客户端。媒体库会根据元数据自动索引和整理音乐文件。

界面完全由键盘驱动。按 **ESC** 进入命令模式，**Ctrl+D** 退出，**Alt+Enter** 打开上下文菜单。可以通过编辑 **~/.musikcube/hotkeys.json** 自定义键盘快捷键。

# CAVEATS

系统需要支持音频输出。大型音乐库的索引可能需要较长时间。该应用以交互为主，不接受传统的命令行参数。

# HISTORY

**musikcube** 由 **clangen** 创建，是一款开源、跨平台的终端音乐播放器。

# INSTALL

```brew: brew install musikcube```

```nix: nix profile install nixpkgs#musikcube```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmus](/man/cmus)(1), [mpd](/man/mpd)(1), [ncmpcpp](/man/ncmpcpp)(1), [mocp](/man/mocp)(1), [termusic](/man/termusic)(1)
