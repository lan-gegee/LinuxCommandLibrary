# TAGLINE

简化的社区维护版 man page

# TLDR

**显示命令的 tldr 页面**

```tldr [command]```

**更新本地缓存**

```tldr --update```

**列出所有可用页面**

```tldr --list```

**显示特定平台的页面**

```tldr -p [linux] [command]```

**搜索匹配关键字的页面**

```tldr --search [keyword]```

# SYNOPSIS

**tldr** [_options_] [_command_]

# PARAMETERS

**-u**, **--update**
> 更新本地页面缓存

**-l**, **--list**
> 列出所有可用命令

**-p**, **--platform** _platform_
> 显示特定平台（linux、osx、windows、sunos、android）的页面

**-L**, **--language** _lang_
> 以指定语言显示页面

**-v**, **--version**
> 显示版本

**-h**, **--help**
> 显示帮助

# DESCRIPTION

**tldr** 提供专注于实用示例的简化社区维护 man page。tldr 页面不提供面面俱到的文档，而是展示常见用例及可直接复制粘贴的命令。

这个名字代表 "Too Long; Didn't Read"（太长不看），体现了其简洁优先于完备的理念。每个页面包含一段简要描述，随后是带有说明的示例命令。

页面由开源社区维护，覆盖多平台上千个命令。缓存存储在本地，可用 **--update** 更新。

存在多个客户端实现（Node.js、Python、Rust、Go 等），它们都使用同一套页面仓库。安装适合你环境的客户端即可。

# CAVEATS

Tldr 页面由社区维护，可能不涵盖所有选项或边缘情况。如需全面文档，请查阅 **man** 页面或官方文档。

部分命令有特定于平台的页面。使用 **--platform** 查看其他操作系统的页面。

本地缓存需要定期用 **--update** 更新，以获取新增和更新的页面。

# HISTORY

tldr-pages 项目始于 **2013 年**，旨在解决 man 页面过于复杂的问题。它已发展成为一个社区项目，有数千名贡献者维护着各大平台上实用的命令示例。

# INSTALL

```apt: sudo apt install tealdeer```

```dnf: sudo dnf install tldr```

```pacman: sudo pacman -S tealdeer```

```zypper: sudo zypper install tealdeer```

```brew: brew install tealdeer```

```nix: nix profile install nixpkgs#tealdeer```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [info](/man/info)(1), [cheat](/man/cheat)(1), [help](/man/help)(1)
