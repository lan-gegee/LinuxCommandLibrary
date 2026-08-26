# TAGLINE

快速的异步终端文件管理器

# TLDR

**启动文件管理器**

```yazi```

**打开特定目录**

```yazi [/path/to/directory]```

**退出时切换目录**

```ya () { local tmp="$(mktemp -t "yazi-cwd.XXXXX")"; yazi "$@" --cwd-file="$tmp"; cd "$(cat "$tmp")"; rm "$tmp"; }```

**以指定的配置目录启动**

```yazi --config-dir [~/.config/yazi]```

**显示调试信息**

```yazi --debug```

# SYNOPSIS

**yazi** [_path_] [_--cwd-file file_] [_--chooser-file file_] [_options_]

# PARAMETERS

**--cwd-file** _FILE_
> 退出时将当前工作目录写入文件。

**--chooser-file** _FILE_
> 将选中的文件写入文件。

**--config-dir** _DIR_
> 自定义配置目录。

**--clear-cache**
> 清除缩略图缓存。

**--debug**
> 打印用于 bug 报告的调试信息。

**--version**
> 显示版本。

**--help**
> 显示帮助。

# KEYBOARD SHORTCUTS

**h / l**
> 返回上级目录 / 进入目录。

**j / k**
> 向下 / 向上移动。

**gg / G**
> 跳到第一个 / 最后一个条目。

**Space**
> 切换选中状态。

**Enter**
> 打开文件。

**y**
> 复制（yank）选中项。

**d**
> 删除选中项。

**p**
> 粘贴。

**r**
> 重命名。

**a**
> 创建文件。

**/**
> 搜索。

**n / N**
> 下一个 / 上一个搜索结果。

**Tab**
> 切换到下一个标签页。

**q**
> 退出。

**~**
> 回到主目录。

**?**
> 显示帮助。

# DESCRIPTION

**yazi** 是一款用 Rust 编写、速度极快的终端文件管理器。它通过异步 I/O 和现代渲染技术着重提升性能。

导航默认使用类似 vim 的按键绑定。预览窗格可以显示文件内容、图片（通过终端图形协议）、视频、PDF 以及归档。代码文件会应用语法高亮。

选择操作可跨目录进行。多个文件可以批量剪切/复制/粘贴，行为与 GUI 文件管理器一致。

标签页支持同时查看多个目录。分屏窗格可以并排比较目录。书签可以收藏常用位置。

插件通过 Lua 脚本扩展功能。主题可以自定义颜色和图标。配置涵盖按键绑定、排序和预览行为。

图片预览需要终端支持图形协议（Kitty、iTerm2、Sixel）。不支持时回退为 ASCII 图形。

# CAVEATS

终端图形预览需要兼容的终端。部分功能依赖外部工具（视频预览需要 ffmpegthumbnailer）。Lua 配置有一定学习曲线。这是一个较新的项目，特性仍在演进。退出时切换目录需要 Shell 包装函数。

# HISTORY

**yazi** 由 **sxyazi** 于 **2023 年**前后创建。名字在中文里意为"鸭子"。它采用 Rust 编写并基于异步架构，作为 ranger 和 lf 的更快速替代品而出现。该项目凭借其性能和现代特性迅速获得广泛采用。

# INSTALL

```pacman: sudo pacman -S yazi```

```apk: sudo apk add yazi```

```zypper: sudo zypper install yazi```

```brew: brew install yazi```

```nix: nix profile install nixpkgs#yazi```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[ranger](/man/ranger)(1), [lf](/man/lf)(1), [nnn](/man/nnn)(1), [vifm](/man/vifm)(1), [ya](/man/ya)(1)
