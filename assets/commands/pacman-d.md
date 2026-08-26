# TAGLINE

**pacman --database** 的简写形式，作用于软件包数据库

# TLDR

**将软件包标记为作为依赖安装**

```sudo pacman -D --asdeps [package]```

**将软件包标记为显式安装**

```sudo pacman -D --asexplicit [package]```

**检查本地数据库的一致性**

```pacman -Dk```

**检查本地数据库和同步数据库的一致性**

```pacman -Dkk```

**以安静模式检查**

```pacman -Dkq```

# SYNOPSIS

**pacman -D** [_options_] _package(s)_

# PARAMETERS

**--asdeps**
> 将软件包标记为作为依赖安装。会影响孤儿软件包检测。

**--asexplicit**
> 将软件包标记为显式安装。清理孤儿软件包时不会被移除。

**-k**, **--check**
> 检查本地软件包数据库的内部一致性。使用两次（`-kk`）还会检查同步数据库。

**-q**, **--quiet**
> 成功时抑制消息；只显示错误。

# DESCRIPTION

**pacman -D** 是 **pacman --database** 的简写形式，作用于软件包数据库。它允许修改存储在本地数据库中的软件包属性，而无需重新安装软件包。

最常见的用途是在依赖和显式安装之间更改软件包的安装原因。标记为依赖的软件包在没有其他软件包依赖它们时可能被 `pacman -Rs` 移除，而显式安装的软件包会被保留。

# CAVEATS

错误的标记会影响 `pacman -Qdtq` 的孤儿检测。标记为 `--asdeps` 的软件包在运行 `pacman -Rs` 时可能被移除。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-database](/man/pacman-database)(8), [pacman-query](/man/pacman-query)(8)
