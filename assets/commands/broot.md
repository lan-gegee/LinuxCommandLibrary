# TAGLINE

交互式目录树导航器

# TLDR

**安装** br shell 函数

```broot --install```

开始**交互式**导航

```broot```

显示文件**大小**

```broot -s```

显示**权限**

```broot -p```

**仅显示目录**

```broot -f```

显示**隐藏**文件

```broot -h```

在**指定目录**中启动

```broot path/to/directory```

# SYNOPSIS

**broot** [_options_] [_path_]

# DESCRIPTION

**broot** 是一款交互式目录树导航器，提供了更好的目录浏览方式。它支持模糊搜索、文件预览，并可通过 br 函数与 shell 集成。

# PARAMETERS

**--install**
> 安装或重新安装 br shell 函数。

**-s, --sizes**
> 显示文件和目录的大小。

**-p, --permissions**
> 显示文件权限。

**-f, --only-folders**
> 仅显示目录（不显示文件）。

**-h, --hidden**
> 显示隐藏文件和目录。

**-d, --dates**
> 显示文件的修改日期。

**-g, --git-status**
> 显示文件的 git 状态。

**-w, --whale-hierarchical**
> 显示分层的目录大小。

**--cmd COMMAND**
> 启动时执行命令。

**-c, --conf PATH**
> 使用指定的配置文件。

**--outcmd PATH**
> 将命令写入文件以供 shell 集成使用。

# CONFIGURATION

**~/.config/broot/conf.hjson**
> Hjson 格式的主配置文件。控制按键绑定、动词（verb）、皮肤和显示设置。

**~/.config/broot/conf.toml**
> TOML 格式的备选配置文件。若存在则替代 conf.hjson 使用。

# CAVEATS

要切换目录，推荐使用 br shell 函数而不是直接调用 broot。用 --install 安装后，请用 br 代替 broot 以获得完整的 shell 集成体验。

# HISTORY

**broot** 作为 tree 和 cd 的现代替代品而创建，提供模糊搜索、可视化导航以及对大型目录树的高效处理。

# INSTALL

```apt: sudo apt install broot```

```pacman: sudo pacman -S broot```

```apk: sudo apk add broot```

```zypper: sudo zypper install broot```

```brew: brew install broot```

```nix: nix profile install nixpkgs#broot```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[tree](/man/tree)(1), [ranger](/man/ranger)(1), [lf](/man/lf)(1), [nnn](/man/nnn)(1)

# RESOURCES

```[Source code](https://github.com/Canop/broot)```

```[Homepage](https://dystroy.org/broot/)```

<!-- verified: 2026-06-22 -->
