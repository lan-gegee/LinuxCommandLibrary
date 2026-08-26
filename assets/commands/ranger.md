# TAGLINE

带 vim 按键绑定的终端文件管理器

# TLDR

**在当前目录启动 ranger**

```ranger```

**在指定目录启动 ranger**

```ranger [path/to/directory]```

**启动时显示隐藏文件**

```ranger --show-hidden```

**生成默认配置文件**

```ranger --copy-config=all```

**退出时打印选中的文件**（用于 Shell 集成）

```ranger --choosefile=[target_file]```

# SYNOPSIS

**ranger** [**--version**] [**--help**] [**--copy-config**=_which_] [**--choosefile**=_target_] [_path_]

# PARAMETERS

**--copy-config**=_which_
> 将默认配置文件复制到 ~/.config/ranger（rc、scope、rifle、commands 或 all）

**--choosefile**=_target_
> 退出时将选中文件的路径写入目标文件（用于 Shell 集成）

**--choosedir**=_target_
> 退出时将最后访问的目录写入目标文件

**--show-hidden**
> 默认显示隐藏文件

**--cmd**=_command_
> 启动后执行 ranger 命令

**--version**
> 显示版本信息

**--help**
> 显示帮助信息

# DESCRIPTION

**ranger** 是一个基于控制台的文件管理器，采用 Vi 风格的按键绑定。它具有三栏布局，可同时显示父目录、当前目录和文件预览。

界面支持使用 hjkl 键（或方向键）即时导航：**h** 进入父目录，**j/k** 在文件列表中上下移动，**l** 打开目录或文件。其他类 Vim 命令包括 **gg** 跳到列表顶部、**G** 跳到底部，以及 **/** 进行搜索。

文件操作遵循 Vim 模式：**yy** 复制（yank）、**dd** 剪切、**pp** 粘贴、**dD** 删除。用 **cw** 重命名，用 **:mkdir** 创建目录，按 **r** 选择应用程序打开文件。

Ranger 内置 **rifle**——一个根据文件类型自动选择合适应用程序的文件打开器。它支持图片预览（需要相应的终端支持）、语法高亮的文本预览以及归档内容查看。

# KEY BINDINGS

**h/j/k/l** 或方向键：导航目录和文件
**gg/G**：跳到列表顶部/底部
**zh**：切换隐藏文件显示
**yy**：复制（yank）文件
**dd**：剪切文件
**pp**：粘贴文件
**dD**：删除文件
**cw**：重命名文件
**Space**：选中文件
**:**: 进入命令模式
**q** 或 **ZZ**：退出 ranger
**m**_x_：设置书签 x
**\`**_x_：跳转到书签 x
**S**：在当前目录打开 Shell

# CONFIGURATION

**~/.config/ranger/rc.conf**
> 主配置文件，控制按键绑定、设置和启动命令。

**~/.config/ranger/rifle.conf**
> 文件打开规则，定义每种文件类型由哪个应用程序处理。

**~/.config/ranger/scope.sh**
> 文件预览脚本，决定第三栏中文件的预览方式。

**~/.config/ranger/commands.py**
> 自定义 Python 命令，扩展 ranger 的内置功能。

# CAVEATS

图片预览需要支持图片的终端（kitty、iTerm2、w3m）及相应配置。文本预览可能需要 **highlight** 等额外工具来实现语法着色。

Ranger 用 Python 编写，对于包含大量文件的目录可能比原生文件管理器慢。追求更快性能可以考虑 **lf** 或 **nnn**。

配置存储在 **~/.config/ranger/**。运行 **ranger --copy-config=all** 可生成可编辑的配置文件。

# HISTORY

Ranger 由 **Roman Zimbelmann** 创建，首个版本发布于 **2009 年**。其设计目标是将 Vim 高效的按键绑定哲学带入文件管理。该项目开源，并在 GitHub 上持续活跃维护。

# INSTALL

```dnf: sudo dnf install ranger```

```pacman: sudo pacman -S ranger```

```apk: sudo apk add ranger```

```zypper: sudo zypper install ranger```

```brew: brew install ranger```

```nix: nix profile install nixpkgs#ranger```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[mc](/man/mc)(1), [vifm](/man/vifm)(1), [nnn](/man/nnn)(1), [lf](/man/lf)(1)
