# TAGLINE

终端里的无意义活动生成器

# TLDR

**运行**随机的假活动场景

```genact```

**显示帮助**和选项

```genact --help```

**仅运行选定的模块**

```genact -m [cargo]```

# SYNOPSIS

**genact** [*OPTIONS*]

# DESCRIPTION

**genact** 在终端里假装很忙：它播放各种假场景（编译器、网络转储、安装过程之类的视觉表演），让看起来正在干大事，实际上什么有用的事都没做。多开几个实例可以让混乱加倍。项目主页上还有一个 WebAssembly 网页版。

可通过发布二进制文件、**cargo install genact**、Homebrew、FreeBSD **pkg**、Scoop 及其他软件包安装。无需外部服务。

# PARAMETERS

常用选项（权威列表请以你的构建版本中的 **genact --help** 为准）：

**-l**, **--list-modules**

> 列出可用的场景/模块。

**-m**, **--modules** *name*

> 只运行选定的模块。

**-s**, **--speed-factor** *n*

> 速度倍率。

**-h**, **--help** / **-V**, **--version**

> 帮助与版本信息。

# CAVEATS

纯粹为了视觉效果；不会执行真实的构建或网络工作（超出场景模拟的范围）。定位是幽默和演示用途，不是生产工具。

# INSTALL

```pacman: sudo pacman -S genact```

```brew: brew install genact```

```nix: nix profile install nixpkgs#genact```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cmatrix](/man/cmatrix)(1), [sl](/man/sl)(1)


# RESOURCES

```[Source code](https://github.com/svenstaro/genact)```

```[Homepage](https://svenstaro.github.io/genact/)```

<!-- verified: 2026-07-19 -->
