# TAGLINE

调整逻辑卷的大小，可扩展或缩减

# TLDR

将卷设置为**指定大小**

```sudo lvresize -L 120G [vg]/[lv]```

**扩展**并同时调整文件系统大小

```sudo lvresize -L +120G --resizefs [vg]/[lv]```

扩展到 **100% 的空闲**空间

```sudo lvresize -l 100%FREE [vg]/[lv]```

**缩减**并同时调整文件系统大小

```sudo lvresize -L -120G --resizefs [vg]/[lv]```

# SYNOPSIS

**lvresize** [_options_] **-L** _size_ _vg_/_lv_

# DESCRIPTION

**lvresize** 调整逻辑卷的大小，既可以扩展也可以缩减。它将 lvextend 和 lvreduce 的功能合并到单个命令中。

# PARAMETERS

**-L, --size SIZE**
> 新大小（+/- 表示相对变化）

**-l, --extents EXTENTS**
> 以 extent 表示的大小（100%FREE、+50%FREE）

**-r, --resizefs**
> 同时调整底层文件系统的大小

**-f, --force**
> 强制调整大小而不确认

**-n, --nofsck**
> 跳过文件系统检查

# CAVEATS

缩减时需要先调整文件系统大小或使用 --resizefs。扩展通常是安全的。缩减前务必备份。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvextend](/man/lvextend)(8), [lvreduce](/man/lvreduce)(8), [lvm](/man/lvm)(8)
