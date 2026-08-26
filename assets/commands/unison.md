# TAGLINE

双向文件同步工具

# TLDR

**同步目录**

```unison [dir1] [dir2]```

**通过 SSH 同步**

```unison [local/path] ssh://[user@host]/[path]```

**批处理模式**

```unison -batch [dir1] [dir2]```

**使用配置档案**

```unison [profilename]```

**显示差异**

```unison -diff [dir1] [dir2]```

# SYNOPSIS

**unison** [_-batch_] [_profile_] _root1_ _root2_

# PARAMETERS

**-batch**
> 非交互式。

**-auto**
> 接受默认值。

**-diff**
> 显示差异。

**-force** _ROOT_
> 强制以某一侧为准。

**-ignore** _PATTERN_
> 忽略匹配模式。

**-path** _PATH_
> 只同步指定路径。

# DESCRIPTION

**unison** 是一个文件同步工具，可以在两个目录副本之间双向传播更改。与 rsync 这类单向同步工具不同，unison 会检测两侧的修改并进行协调，因此适合在多台机器之间保持目录同步。

当两个副本都被修改而产生冲突时，unison 会检测到冲突并给出解决选项，而不是静默覆盖更改。它可以通过 SSH 同步远程目录，也可以处理本地路径。该工具会跟踪各次同步之间的文件状态，因此只传输实际发生变化的文件。

Unison 支持将同步配置保存为配置档案以便重复使用，包括路径过滤器、忽略模式和连接设置。它可运行于 Unix、macOS 和 Windows，并且要求同步双方使用相同版本的 unison。

# CAVEATS

双方必须运行相同版本的 unison；版本不匹配会导致失败。冲突需要人工处理。对大型目录树的首次同步可能较慢。

# HISTORY

**Unison** 由宾夕法尼亚大学的 **Benjamin Pierce** 开发，大约在 **2001 年**首次发布。它用 OCaml 编写，基于文件同步理论的研究成果。

# INSTALL

```dnf: sudo dnf install unison```

```pacman: sudo pacman -S unison```

```apk: sudo apk add unison```

```zypper: sudo zypper install unison```

```brew: brew install unison```

```nix: nix profile install nixpkgs#unison```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rsync](/man/rsync)(1), [syncthing](/man/syncthing)(1), [rclone](/man/rclone)(1)
