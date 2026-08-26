# TAGLINE

列出某个日期以来的提交

# TLDR

**显示昨天以来的提交**

```git commits-since yesterday```

**显示上周以来的提交**（未给日期时的默认行为）

```git commits-since "last week"```

**显示特定日期以来的提交**

```git commits-since "[2024-01-01]"```

**显示某个相对时间以来的提交**

```git commits-since "2 hours ago"```

# SYNOPSIS

**git** **commits-since** [_date_]

# DESCRIPTION

**git commits-since** 是 git-extras 提供的便捷命令，用于显示自指定日期以来的提交。不带参数调用时，默认显示 "last week" 以来的提交。

它接受自然语言日期表达式，如 "yesterday"、"last week"、"2 hours ago"、"3 o clock pm"，也接受 "2024-01-01" 这样的具体日期。该命令封装了带日期过滤的 git log，比手动构造 git log --since 命令的输出更易读。

它特别适合每日站会、周报回顾、生成更新日志，或者查看某次发布部署以来有哪些变更。

# INSTALL

```apt: sudo apt install git```

```dnf: sudo dnf install git```

```pacman: sudo pacman -S git```

```apk: sudo apk add git```

```zypper: sudo zypper install git```

```brew: brew install git```

```nix: nix profile install nixpkgs#git```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[git-log](/man/git-log)(1), [git-extras](/man/git-extras)(1)
