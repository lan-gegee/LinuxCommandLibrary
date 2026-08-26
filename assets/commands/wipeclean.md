# TAGLINE

带动画效果的终端清屏

# TLDR

**清理终端**

```wipeclean```

**使用指定动画**

```wipeclean -a [1]```

**自定义速度**

```wipeclean -s [50]```

# SYNOPSIS

**wipeclean** [_-a animation_] [_-s speed_] [_options_]

# PARAMETERS

**-a** _N_
> 动画类型。

**-s** _SPEED_
> 动画速度。

**--help**
> 显示帮助。

# DESCRIPTION

**wipeclean** 是 clear 命令的有趣替代品，它以视觉动画的方式清除终端屏幕，而不是简单地滚动内容。提供多种动画样式，在屏幕内容被擦除时各自呈现不同的视觉效果。

动画速度可调，用于控制清除效果播放的快慢。它纯粹是装饰性的，相比标准 clear 命令没有任何功能优势，但能为终端工作流程增添一丝视觉趣味。

# CAVEATS

仅供娱乐。不比 clear 更快。Rust 实现。

# HISTORY

**wipeclean** 作为 clear 命令的趣味动画替代品而创建，用于终端清屏。

# INSTALL

```aur: yay -S wipeclean```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[clear](/man/clear)(1), [reset](/man/reset)(1), [cmatrix](/man/cmatrix)(1)
