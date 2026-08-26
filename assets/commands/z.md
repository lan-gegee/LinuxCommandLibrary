# TAGLINE

跳转到常用目录

# TLDR

**跳转到匹配模式且 frecent 值最高的目录**

```z [pattern]```

**跳转到匹配多个模式的目录**

```z [foo] [bar]```

**按 frecency 排序列出匹配的目录**

```z -l [pattern]```

**只跳转到排名最高的匹配**

```z -r [pattern]```

**跳转到最近访问的匹配**

```z -t [pattern]```

**将当前目录从数据库中移除**

```z -x```

# SYNOPSIS

**z** [**-chlrtx**] [_pattern_...]

# PARAMETERS

**-c**
> 将匹配限制在当前目录的子目录内

**-h**
> 显示帮助

**-l**
> 列出匹配项而不跳转

**-r**
> 仅按访问频率（rank）匹配

**-t**
> 仅按最近程度（recency）匹配

**-x**
> 从数据文件中移除当前目录

# DESCRIPTION

**z** 会跟踪你最常使用的目录，让你用最少的按键跳转过去。它使用 "frecency"——频率（frequency）与最近度（recency）的结合——来对目录排序。

当你用 cd 导航时，z 会学习你访问最多的目录。输入 **z foo** 即可跳转到路径中包含 "foo" 的 frecent 值最高的目录。多个参数按顺序匹配：**z foo bar** 匹配路径中先出现 "foo" 后出现 "bar" 的条目。

数据库默认存储在 **~/.z**，在切换目录时通过 shell 钩子自动更新。

# CAVEATS

需要 shell 集成。在 shell 配置文件（.bashrc、.zshrc）中加入 **source /path/to/z.sh**，它才能跟踪目录。

新安装时数据库为空，z 需要一段时间才能学会你的使用模式。

默认大小写不敏感匹配，但可以配置。

类似工具还有 **zoxide**、**autojump**、**fasd**，功能相近但各有特点。

# INSTALL

```dnf: sudo dnf install z```

```pacman: sudo pacman -S z```

```zypper: sudo zypper install z```

```brew: brew install z```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[cd](/man/cd)(1), [zoxide](/man/zoxide)(1), [autojump](/man/autojump)(1), [pushd](/man/pushd)(1)
