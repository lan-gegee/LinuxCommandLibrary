# TAGLINE

显示动画终端屏保

# TLDR

**随机启动一个屏保**

```gh screensaver```

**启动指定的屏保**

```gh screensaver -s [fireworks|starfield|pipes|marquee|life|pollock]```

**列出**可用屏保

```gh screensaver -l```

运行 marquee 并自定义**消息**

```gh screensaver -s marquee -- --message="[Hello World]"```

运行 starfield 并自定义**密度**和**速度**

```gh screensaver -s starfield -- --density [500] --speed [8]```

# SYNOPSIS

**gh** **screensaver** [_options_]

# PARAMETERS

**-s**, **--saver** _name_
> 要运行的屏保（fireworks、starfield、pipes、marquee、life、pollock）。

**-l**, **--list**
> 列出可用屏保后退出。

**-R**, **--repo** _repository_
> 在某个仓库上下文中运行（目前未使用）。

# DESCRIPTION

**gh screensaver** 是一个 GitHub CLI 扩展，用于显示动画终端屏保。可用屏保包括：**fireworks**、**starfield**、**pipes**、**marquee**、**life**（Conway's Game of Life）以及 **pollock**（paint splotches）。不带 **-s** 时会随机选择一个屏保。

各屏保特有的选项需放在 **--** 之后传递。例如 marquee 支持 **--message** 和 **--font**；starfield 支持 **--density** 和 **--speed**；fireworks、pipes 和 life 支持 **--color**（full/off）；life 还支持 **--seed**（glider、noise、R、dragon、gun、pulsar）。

此扩展必须先用 **gh extension install vilmibm/gh-screensaver** 安装。按 **q** 或 **Ctrl+C** 可退出屏保。

# CAVEATS

需要安装 GitHub CLI（**gh**），且必须作为扩展安装。在颜色支持有限的终端上，部分动画可能无法正确渲染。

# INSTALL

```nix: nix profile install nixpkgs#gh-screensaver```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[gh](/man/gh)(1), [gh-extension](/man/gh-extension)(1), [cmatrix](/man/cmatrix)(1)
