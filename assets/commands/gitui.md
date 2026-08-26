# TAGLINE

用 Rust 编写的高速 Git 终端界面

# TLDR

**启动 GitUI**

```gitui```

在指定目录中启动

```gitui -d [path]```

使用自定义主题

```gitui --theme [theme.ron]```

使用文件系统监视器而非轮询

```gitui --watcher```

生成错误报告

```gitui --bugreport```

# SYNOPSIS

**gitui** [_options_]

# PARAMETERS

**-d** _PATH_, **--directory** _PATH_
> 设置 git 目录（默认为 `.` 或 `$GIT_DIR`）。

**-w** _PATH_, **--workdir** _PATH_
> 设置工作目录（默认为当前目录或 `$GIT_WORK_TREE`）。

**-t** _FILE_, **--theme** _FILE_
> 设置颜色主题文件名，从配置目录加载（默认：`theme.ron`）。

**-f** _FILE_, **--file** _FILE_
> 启动时在文件标签页中选中某个文件。

**-k** _FILE_, **--key-bindings** _FILE_
> 使用自定义按键绑定文件。

**-s** _FILE_, **--key-symbols** _FILE_
> 使用自定义符号文件。

**-l**, **--logging**
> 将日志输出保存到缓存目录下的文件中。

**--logfile** _FILE_
> 将日志输出保存到指定文件（隐含 **--logging**）。

**--watcher**
> 使用基于 notify 的文件系统监视器，替代默认的基于 tick 的轮询。

**--bugreport**
> 生成错误报告。

**-h**, **--help**
> 显示帮助信息。

**-V**, **--version**
> 显示版本信息。

# DESCRIPTION

**gitui** 是一个高速的 Git 终端界面。它提供键盘驱动的操作方式，可在终端内完成暂存、提交、分支管理和查看 diff。

**gitui** 用 Rust 编写，轻量且响应迅速。它在分栏界面中显示状态、日志、diff 和暂存信息，并采用类 vim 的按键绑定。

# CONFIGURATION

**~/.config/gitui/theme.ron**
> RON 格式的主题配置文件，用于自定义颜色和外观。

**~/.config/gitui/key_bindings.ron**
> 按键绑定自定义文件。

# CAVEATS

终端界面需要合适的终端支持。与完整 GUI 相比部分功能受限。主题须采用 RON 格式。默认情况下，gitui 每隔几秒轮询一次工作目录的变化；在 notify 可靠可用的平台上，传入 **--watcher** 可以获得更快的变更检测。

# HISTORY

gitui 由 **Stephan Dilly** 创建，是一个用 Rust 编写的高速、以键盘为中心的 git 终端界面。

# INSTALL

```dnf: sudo dnf install gitui```

```pacman: sudo pacman -S gitui```

```apk: sudo apk add gitui```

```zypper: sudo zypper install gitui```

```brew: brew install gitui```

```nix: nix profile install nixpkgs#gitui```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tig](/man/tig)(1), [lazygit](/man/lazygit)(1), [git-gui](/man/git-gui)(1)

# RESOURCES

```[Source code](https://github.com/gitui-org/gitui)```

```[FAQ](https://github.com/gitui-org/gitui/blob/master/FAQ.md)```

<!-- verified: 2026-07-17 -->
