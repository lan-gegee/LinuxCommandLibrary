# TAGLINE

管理有序的补丁序列

# TLDR

**创建新补丁**

```quilt new [patch_name.patch]```

**将文件加入补丁**

```quilt add [file]```

**应用下一个补丁**

```quilt push```

**移除当前补丁**

```quilt pop```

**刷新补丁**

```quilt refresh```

**显示补丁序列**

```quilt series```

**显示当前更改的差异**

```quilt diff```

**应用序列中的全部补丁**

```quilt push -a```

**移除所有已应用的补丁**

```quilt pop -a```

**从序列中删除补丁**

```quilt delete [patch_name.patch]```

# SYNOPSIS

**quilt** _command_ [_options_]

# PARAMETERS

**new** _NAME_
> 以给定名称创建新补丁，并将其插入当前顶部补丁之后。

**add** _FILE_
> 在修改之前，将要跟踪的文件注册到当前最顶层的补丁中。

**push** [**-a**]
> 应用序列中下一个未应用的补丁。使用 **-a** 应用其余全部补丁。

**pop** [**-a**]
> 移除最顶层的已应用补丁并撤销其更改。使用 **-a** 移除所有已应用的补丁。

**refresh**
> 更新最顶层的补丁，使其反映对已跟踪文件的当前更改。

**series**
> 按顺序列出 series 文件中的所有补丁。

**diff** [**-z**]
> 显示已跟踪文件的当前状态与最顶层补丁之间的差异。

**delete** [**-r**] _NAME_
> 从 series 文件中移除补丁。使用 **-r** 同时从 patches 目录删除补丁文件。

**edit** _FILE_
> 将文件加入最顶层补丁，并在默认编辑器中打开它。

**top**
> 打印最顶层已应用补丁的名称。

**applied**
> 列出所有当前已应用的补丁。

**unapplied**
> 列出所有尚未应用的补丁。

# DESCRIPTION

**quilt** 管理针对源码树的有序补丁序列，允许独立地应用、移除和更新补丁。它维护一个按顺序列出补丁的 **series** 文件和一个存放补丁文件的 **patches/** 目录，为在上游代码之上维护修改提供了结构化的工作流。

典型工作流程是：用 **new** 创建新补丁，用 **add** 注册要跟踪的文件，进行修改，然后用 **refresh** 保存补丁。补丁可以用 **push** 逐个应用、用 **pop** 逐个移除，整个序列也可以重新排序或编辑。Quilt 广泛用于 Linux 发行版的打包工作，以便在上游源码之上维护下游补丁。

# CAVEATS

Quilt 会在工作目录中创建 **patches/** 目录和 **series** 文件。文件必须先用 **add** 注册再修改，否则更改不会被 **refresh** 捕获。补丁采用标准的 unified diff 格式。

# HISTORY

Quilt 的灵感来自 **Andrew Morton** 用于内核开发的补丁脚本。

# INSTALL

```dnf: sudo dnf install quilt```

```pacman: sudo pacman -S quilt```

```apk: sudo apk add quilt```

```zypper: sudo zypper install quilt```

```brew: brew install quilt```

```nix: nix profile install nixpkgs#quilt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[patch](/man/patch)(1), [diff](/man/diff)(1), [git](/man/git)(1)
