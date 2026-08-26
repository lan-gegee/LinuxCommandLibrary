# TAGLINE

将旧的个人词典导入 GNU Aspell

# TLDR

**自动导入**旧的个人词典（Ispell 和 Aspell）

```aspell-import```

若缺少 /usr/bin/perl，**通过 Perl 显式调用**

```perl $(which aspell-import)```

# SYNOPSIS

**aspell-import**

# DESCRIPTION

**aspell-import** 是一个 Perl 脚本，它会搜索来自 **Ispell** 和早期版本 **Aspell** 的旧个人词典，然后将它们导入当前用户的 GNU Aspell 个人词表。它适合在安装 Aspell 或从 Ispell 升级后运行一次。

脚本会扫描用户主目录和标准字典位置，转换每个条目，并写入一行头部信息，使结果成为有效的 Aspell 个人词典。

# PARAMETERS

此命令不接受任何命令行选项。直接不带参数运行即可。

# CAVEATS

脚本必须能在 `/usr/bin/perl` 找到可用的 Perl 解释器。如果 Perl 安装在其他位置，请用 `perl /path/to/aspell-import` 调用脚本。现有的 Aspell 个人词典可能被覆盖，因此请先备份。Ispell 的词缀规则不会被迁移，只迁移词表。

# HISTORY

**aspell-import** 随 **GNU Aspell** 一起发布，添加它是为了让用户在从 Ispell 迁移到 Aspell 时能够带走积累的个人词表。

# INSTALL

```apt: sudo apt install aspell```

```dnf: sudo dnf install aspell```

```pacman: sudo pacman -S aspell```

```apk: sudo apk add aspell-utils```

```zypper: sudo zypper install aspell```

```brew: brew install aspell```

```nix: nix profile install nixpkgs#aspell```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[aspell](/man/aspell)(1), [ispell](/man/ispell)(1)
