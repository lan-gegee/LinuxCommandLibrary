# TAGLINE

**pacman --remove** 的简写形式，从系统中移除软件包

# TLDR

**移除软件包**

```sudo pacman -R [package]```

**移除软件包及其不再需要的依赖**

```sudo pacman -Rs [package]```

**移除软件包、其依赖及配置文件**

```sudo pacman -Rns [package]```

**移除软件包而不检查依赖**（危险）

```sudo pacman -Rdd [package]```

**列出将被移除的软件包**（试运行）

```pacman -Rsp [package]```

查看原始命令的文档

```tldr pacman remove```

# SYNOPSIS

**pacman -R** [_options_] _package(s)_

# PARAMETERS

**-c**, **--cascade**
> 移除所有目标软件包以及依赖于它们的软件包。

**-n**, **--nosave**
> 移除配置文件而不是将其保存为 .pacsave 文件。

**-s**, **--recursive**
> 移除其他软件包不再需要的依赖。

**-u**, **--unneeded**
> 仅当目标不被任何其他软件包需要时才移除它们。

**-p**, **--print**
> 打印目标而不执行操作。

**-d**, **--nodeps**
> 跳过依赖检查。传入两次（-dd）还会跳过反向依赖检查。

# DESCRIPTION

**pacman -R** 是 **pacman --remove** 的简写形式，用于从系统中移除软件包。它会处理依赖检查，并可选择移除配置文件和孤立的依赖。

# CAVEATS

使用 **-Rdd** 会绕过所有依赖检查，可能破坏系统。**-Rns** 组合是最干净的移除方式，同时移除备份配置文件和孤立的依赖。

# INSTALL

```apt: sudo apt install pacman-package-manager```

```dnf: sudo dnf install pacman```

```pacman: sudo pacman -S pacman```

```apk: sudo apk add pacman```

```nix: nix profile install nixpkgs#pacman```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[pacman](/man/pacman)(8), [pacman-remove](/man/pacman-remove)(8)
