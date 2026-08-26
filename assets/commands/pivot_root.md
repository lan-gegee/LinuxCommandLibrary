# TAGLINE

切换根文件系统的挂载点

# TLDR

将根目录切换到**新目录**

```sudo pivot_root [/new_root] [/new_root/old_root]```

显示**帮助**

```pivot_root -h```

# SYNOPSIS

**pivot_root** [**-h**|**--help**] _new_root_ _put_old_

# PARAMETERS

**new_root**
> 成为新根文件系统的目录

**put_old**
> new_root 下用于挂载旧根的目录

**-h, --help**
> 显示帮助信息

# DESCRIPTION

**pivot_root** 将根文件系统更改为新目录，并把当前根移动到新根的一个子目录中。这在系统启动期间的 initramfs 阶段很常用，用于从初始 RAM 文件系统切换到真正的根文件系统。

该操作是原子性的，会影响整个系统。执行 pivot_root 后，旧根在指定的 put_old 位置仍然可以访问，直到被卸载。

# CAVEATS

需要 root 权限。new_root 必须是挂载点。调用 pivot_root 的进程的当前工作目录不会改变。主要用于系统初始化脚本。

# HISTORY

**pivot_root** 被添加到 Linux 内核是为了在启动期间提供一种干净的根文件系统切换方式。它取代了以往结合 chroot 与各种挂载操作的做法。

# INSTALL

```apt: sudo apt install util-linux```

```dnf: sudo dnf install util-linux```

```pacman: sudo pacman -S util-linux```

```apk: sudo apk add util-linux-misc```

```zypper: sudo zypper install util-linux```

```brew: brew install util-linux```

```nix: nix profile install nixpkgs#util-linux```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[chroot](/man/chroot)(8), [mount](/man/mount)(8), [switch_root](/man/switch_root)(8)
