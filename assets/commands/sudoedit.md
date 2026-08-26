# TAGLINE

以提升的权限安全地编辑文件

# TLDR

**以 root 身份编辑文件**

```sudoedit [/etc/hosts]```

**使用指定编辑器编辑**

```SUDO_EDITOR=[vim] sudoedit [/etc/fstab]```

**编辑多个文件**

```sudoedit [/etc/file1] [/etc/file2]```

**以其他用户身份编辑**

```sudoedit -u [username] [file]```

# SYNOPSIS

**sudoedit** [_-u user_] [_options_] _files_

# PARAMETERS

**-u**, **--user** _USER_
> 以指定用户身份编辑。

**-g**, **--group** _GROUP_
> 以指定组身份编辑。

**-H**
> 设置 HOME。

**-n**, **--non-interactive**
> 非交互模式。

# ENVIRONMENT

**SUDO_EDITOR** - 首选编辑器
**VISUAL** - 可视化编辑器
**EDITOR** - 默认编辑器

# DESCRIPTION

**sudoedit** 以提升的权限安全地编辑文件。它等价于 sudo -e。

文件会被复制到临时位置，用户用自己的编辑器进行编辑。

编辑完成后，改动被复制回去，原文件以原子方式替换。

用户的环境保持不变，编辑器以用户身份而非 root 身份运行。

比直接以 root 身份运行编辑器更安全，可降低提权风险。

# CAVEATS

编辑器插件以用户身份运行，某些编辑器可能无法正常工作。临时文件会短暂存在。

# HISTORY

**sudoedit** 是 **sudo** 的组成部分，提供安全的文件编辑功能。它可以防止通过编辑器扩展以 root 权限执行任意代码。

# INSTALL

```apt: sudo apt install sudo```

```dnf: sudo dnf install sudo```

```pacman: sudo pacman -S sudo```

```apk: sudo apk add sudo```

```zypper: sudo zypper install sudo```

```nix: nix profile install nixpkgs#sudo```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[sudo](/man/sudo)(8), [visudo](/man/visudo)(8), [vi](/man/vi)(1)
