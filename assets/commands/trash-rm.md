# TAGLINE

从回收站删除匹配模式的文件

# TLDR

从回收站中删除所有名为 **foo** 的文件

```trash-rm foo```

从回收站中删除所有以 **.o** 结尾的文件

```trash-rm '*.o'```

从回收站中删除具有特定**原始路径**的文件

```trash-rm /absolute/path/to/file```

# SYNOPSIS

**trash-rm** _PATTERN_

# DESCRIPTION

**trash-rm** 从回收站中删除所有匹配给定模式的文件。它依据 freedesktop.org 回收站规范永久删除匹配的回收站文件。模式会与原始文件名或路径进行匹配。

# INSTALL

```dnf: sudo dnf install trash-cli```

```pacman: sudo pacman -S trash-cli```

```apk: sudo apk add trash-cli```

```zypper: sudo zypper install trash-cli```

```brew: brew install trash-cli```

```nix: nix profile install nixpkgs#trash-cli```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[trash](/man/trash)(1), [trash-put](/man/trash-put)(1), [trash-list](/man/trash-list)(1), [trash-empty](/man/trash-empty)(1), [trash-restore](/man/trash-restore)(1)
