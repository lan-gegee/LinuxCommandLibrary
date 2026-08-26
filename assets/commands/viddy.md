# TAGLINE

带时光机功能的现代 watch 命令

# TLDR

**以默认间隔监视命令**

```viddy '[ls -la]'```

**以 diff 高亮监视**

```viddy -d '[df -h]'```

**以自定义间隔监视**

```viddy -n [5] '[command]'```

# SYNOPSIS

**viddy** [_options_] _command_

# PARAMETERS

**-n**, **--interval** _SECONDS_
> 命令执行间隔（默认为 2）

**-d**, **--differences**
> 高亮显示更新之间的差异

**-t**, **--no-title**
> 禁用头部显示

**-b**, **--bell**
> 命令出错时响铃

**-p**, **--precise**
> 精确定时模式

**-s**, **--skip-empty-diffs**
> 输出未变化时跳过更新

# DESCRIPTION

**viddy** 是 Unix **watch** 命令的现代替代品。它周期性地执行命令并以彩色输出和 diff 高亮显示结果。其突出特性是时光机模式，可以回溯过去的命令输出。按 **Space** 切换时光机模式，然后使用方向键浏览历史。内置类 vim 键绑定和分页器。

# HISTORY

**viddy** 由 **sachaos** 开发。最初使用 Go 编写，自 1.0.0 版本起改用 **Rust** 重写。

# INSTALL

```apk: sudo apk add viddy```

```zypper: sudo zypper install viddy```

```brew: brew install viddy```

```nix: nix profile install nixpkgs#viddy```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[watch](/man/watch)(1), [hwatch](/man/hwatch)(1), [entr](/man/entr)(1)
