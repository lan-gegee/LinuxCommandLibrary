# TAGLINE

二进制差量压缩与补丁

# TLDR

**创建差量文件**

```xdelta delta [old_file] [new_file] [patch.xdelta]```

**应用补丁**

```xdelta patch [patch.xdelta] [old_file] [new_file]```

**以压缩方式创建**

```xdelta -9 delta [old_file] [new_file] [patch.xdelta]```

**显示补丁信息**

```xdelta info [patch.xdelta]```

**测试补丁**

```xdelta test [patch.xdelta] [old_file]```

# SYNOPSIS

**xdelta** _command_ [_options_] [_files_]

# PARAMETERS

**delta**
> 创建差量文件。

**patch**
> 应用差量文件。

**info**
> 显示补丁信息。

**test**
> 验证补丁。

**-0** 到 **-9**
> 压缩级别。

**-f**, **--force**
> 强制覆盖。

**-s** _SOURCE_
> 源文件。

# DESCRIPTION

**xdelta** 在一个文件的两个版本之间创建和应用二进制差量补丁。delta 命令将旧文件与新文件比较，生成只包含差异的紧凑补丁文件，其体积通常远小于直接分发完整的新文件。

patch 命令通过将差量应用到原始文件来重建新文件。可配置的压缩级别以处理时间换取更小的补丁体积。该工具常用于软件更新分发、ROM 补丁制作，以及只需传输变更内容的高效文件同步场景。

# CAVEATS

旧文件必须完全匹配。大文件需要较多内存。版本兼容性很重要。

# HISTORY

**xdelta** 为高效的二进制差异比较而创建。第 1 版演化为支持 VCDIFF 标准的 xdelta3。

# INSTALL

```apt: sudo apt install xdelta```

```dnf: sudo dnf install xdelta```

```brew: brew install xdelta```

```nix: nix profile install nixpkgs#xdelta```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[xdelta3](/man/xdelta3)(1), [bsdiff](/man/bsdiff)(1), [rdiff](/man/rdiff)(1)
