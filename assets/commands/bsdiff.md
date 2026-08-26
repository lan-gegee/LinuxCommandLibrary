# TAGLINE

创建和应用二进制补丁

# TLDR

**创建二进制补丁**

```bsdiff [oldfile] [newfile] [patch.bsdiff]```

**应用二进制补丁**

```bspatch [oldfile] [newfile] [patch.bsdiff]```

# SYNOPSIS

**bsdiff** _oldfile_ _newfile_ _patchfile_

**bspatch** _oldfile_ _newfile_ _patchfile_

# PARAMETERS

_oldfile_
> 原始文件（两个工具的输入）。

_newfile_
> 对 bsdiff 而言：用于比对的较新版本。对 bspatch 而言：要生成的输出文件。

_patchfile_
> 二进制补丁文件（bsdiff 的输出，bspatch 的输入）。

# DESCRIPTION

**bsdiff** 和 **bspatch** 在两个文件之间创建和应用二进制补丁。与面向文本的 diff/patch 不同，这些工具可以处理任意二进制数据，非常适合分发只需传输变更部分的软件更新。

bsdiff 使用后缀排序算法高效识别二进制文件之间的相似之处，生成高度压缩的补丁。即使是内部布局不同的文件（比如重新编译后的可执行文件），也常常能产生很小的补丁。

补丁文件使用 bzip2 压缩，进一步减小体积。bspatch 可以从旧文件和补丁精确重建新文件，并可通过校验和验证。

# CAVEATS

bsdiff 的内存占用约为旧文件大小的 17 倍，因此不适合非常大的文件。打补丁时旧文件必须完全一致（逐字节相同）；任何修改都会导致失败。补丁是单向的，没有原始文件就无法逆向还原。

# HISTORY

bsdiff 由 **Colin Percival** 创建，于 **2003** 年首次发布。该算法是他在开发 FreeBSD 二进制更新时设计的。此工具后来被广泛用于软件更新系统，包括 Google Chrome 和多个游戏平台。它处理二进制文件的高效性使其成为带宽受限环境下增量更新的标准选择。

# INSTALL

```apt: sudo apt install bsdiff```

```dnf: sudo dnf install bsdiff```

```zypper: sudo zypper install bsdiff```

```brew: brew install bsdiff```

```nix: nix profile install nixpkgs#bsdiff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[diff](/man/diff)(1), [patch](/man/patch)(1), [xdelta](/man/xdelta)(1), [rdiff](/man/rdiff)(1)

# RESOURCES

```[Homepage](http://www.daemonology.net/bsdiff/)```

<!-- verified: 2026-06-22 -->
