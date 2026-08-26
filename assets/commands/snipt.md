# TAGLINE

终端文本片段展开工具

# TLDR

**启动后台守护进程**

```snipt start```

**添加新片段**

```snipt add --shortcut [email] --snippet "[user@example.com]"```

**显示所有已保存的片段**

```snipt list```

# SYNOPSIS

**snipt** _command_ [_options_]

# DESCRIPTION

**snipt** 是一个系统级文本片段展开工具，以后台守护进程的形式运行并监控键盘输入。你输入一个前缀字符加快捷词，snipt 会自动将其展开为预定义文本。它支持剪贴板集成、以 **!** 为前缀执行脚本、参数化片段以及文本变换。

# HISTORY

**snipt** 由 **snipt** 组织创建，使用 **Rust** 编写。

# INSTALL

```nix: nix profile install nixpkgs#snipt```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[espanso](/man/espanso)(1), [pet](/man/pet)(1), [nap](/man/nap)(1)
