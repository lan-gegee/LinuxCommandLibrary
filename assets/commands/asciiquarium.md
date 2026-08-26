# TAGLINE

在终端中显示动态 ASCII 艺术水族箱

# TLDR

**运行**水族箱

```asciiquarium```

以**经典**模式运行（只保留 1.0 版原有的生物）

```asciiquarium -c```

# SYNOPSIS

**asciiquarium** [_-c_]

# PREVIEW

```
   ><(((°>     .
  __         ><>
 (__)   ~  ___
 ||||  ~   |#|
```

# DESCRIPTION

**asciiquarium** 在终端中显示一个动态的 ASCII 艺术水族箱。其中有游动的鱼、城堡、海草、气泡，还有偶尔出没的鲨鱼或海怪，带来类似屏保的放松动画。

程序会一直运行直到被中断，并能自适应终端大小。

# PARAMETERS

**-c**
> 经典模式：只显示 1.0 版中已有的物种。

# CONTROLS

按 **q** 退出，按 **r** 重绘所有实体，或按 **p** 切换暂停状态。

# CAVEATS

需要 Term::Animation Perl 模块。在支持 256 色的终端上效果最佳。在某些系统上 CPU 占用较高。

# HISTORY

**asciiquarium** 由 Kirk Baucom 编写，是一个通过 ASCII 动画艺术提供终端娱乐的 Perl 脚本。

# INSTALL

```dnf: sudo dnf install asciiquarium```

```pacman: sudo pacman -S asciiquarium```

```apk: sudo apk add asciiquarium```

```brew: brew install asciiquarium```

```nix: nix profile install nixpkgs#asciiquarium```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[cmatrix](/man/cmatrix)(1), [sl](/man/sl)(6), [cowsay](/man/cowsay)(1)

# RESOURCES

```[Source code](https://github.com/cmatsuoka/asciiquarium)```

```[Homepage](https://robobunny.com/projects/asciiquarium/html/)```

<!-- verified: 2026-06-17 -->
