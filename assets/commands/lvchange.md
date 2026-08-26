# TAGLINE

更改 LVM 中逻辑卷的属性或激活状态

# TLDR

**激活**逻辑卷

```sudo lvchange -a y /dev/vg_name/lv_name```

**停用**逻辑卷

```sudo lvchange -a n /dev/vg_name/lv_name```

启用**自动激活**

```sudo lvchange -a ay /dev/vg_name/lv_name```

设置**只读**权限

```sudo lvchange -p r /dev/vg_name/lv_name```

**跳过激活**

```sudo lvchange -k y /dev/vg_name/lv_name```

**刷新**逻辑卷

```sudo lvchange --refresh /dev/vg_name/lv_name```

# SYNOPSIS

**lvchange** [_options_] _vg_/_lv_

# DESCRIPTION

**lvchange** 更改 LVM 中逻辑卷的属性或激活状态。它可以激活/停用卷、更改权限，并修改各种 LV 属性。

# PARAMETERS

**-a, --activate y|n|ay**
> 激活（y）、停用（n）或自动激活（ay）

**-p, --permission r|rw**
> 设置只读（r）或读写（rw）

**-k, --setactivationskip y|n**
> 设置激活跳过标志

**--refresh**
> 使用最新元数据刷新卷

**-Z, --zero y|n**
> 将新逻辑卷的前几个 KB 清零

**--addtag TAG**
> 为逻辑卷添加标签

# CAVEATS

需要 root 权限。某些操作要求先卸载卷。属于 LVM2 工具集。

# INSTALL

```apt: sudo apt install lvm2```

```dnf: sudo dnf install lvm2```

```pacman: sudo pacman -S lvm2```

```apk: sudo apk add lvm2```

```zypper: sudo zypper install lvm2```

```nix: nix profile install nixpkgs#lvm2```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[lvcreate](/man/lvcreate)(8), [lvdisplay](/man/lvdisplay)(8), [lvs](/man/lvs)(8), [lvm](/man/lvm)(8)
