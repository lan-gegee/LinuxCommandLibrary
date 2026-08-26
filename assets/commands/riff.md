# TAGLINE

针对 diff 输出的语法高亮工具

# TLDR

**高亮 diff 中发生变化的部分**

```git diff | riff```

**将 riff 设为默认的 git diff 分页器**

```git config --global pager.diff riff```

**高亮两个文件之间的差异**

```diff [file1.txt] [file2.txt] | riff```

# SYNOPSIS

_diff-command_ | **riff** [_options_]

# DESCRIPTION

**riff** 是 diff 的封装工具，可高亮行内发生变化的片段，并以不同颜色显示未变化的部分。它会为文件名和 hunk 头部创建指向源代码行的超链接，还能高亮合并冲突。它可以作为 git 的分页器集成，增强 diff 查看体验。

# HISTORY

**riff** 由 **Johan Walles**（walles）创建，使用 **Rust** 编写。

# INSTALL

```pacman: sudo pacman -S riff```

```apk: sudo apk add riff```

```zypper: sudo zypper install riff```

```brew: brew install riff```

```nix: nix profile install nixpkgs#riff```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[delta](/man/delta)(1), [diff-so-fancy](/man/diff-so-fancy)(1), [colordiff](/man/colordiff)(1)
