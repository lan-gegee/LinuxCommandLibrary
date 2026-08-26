# TAGLINE

显示软件包版本之间或本地软件包与 registry 之间的差异

# TLDR

**比较软件包的多个版本**

```npm diff --diff=[package]@[1.0.0] --diff=[package]@[2.0.0]```

**比较本地与 registry**

```npm diff --diff=[package-name]```

**比较指定文件**

```npm diff --diff=[pkg]@[1.0.0] --diff=[pkg]@[2.0.0] [./file.js]```

# SYNOPSIS

**npm** **diff** [_options_] [_paths_...]

# PARAMETERS

**--diff** _spec_
> 要比较的软件包 spec；使用两次可分别指定两侧。

**--diff-name-only**
> 只显示发生变化的文件名。

**--diff-unified** _n_
> 显示的上下文行数（默认 3）。

**--diff-ignore-all-space**
> 比较行时忽略空白字符。

**--diff-no-prefix**
> 输出中省略源与目标前缀。

**--diff-src-prefix** _prefix_
> 输出中的源前缀（默认 "a/"）。

**--diff-dst-prefix** _prefix_
> 输出中的目标前缀（默认 "b/"）。

**--diff-text**
> 将所有文件视为文本。

# DESCRIPTION

**npm diff** 显示软件包版本之间或本地软件包与 registry 之间的差异。适合在更新之前审查变更。

# INSTALL

```pacman: sudo pacman -S npm```

```apk: sudo apk add npm```

```brew: brew install npm```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[npm](/man/npm)(1), [npm-outdated](/man/npm-outdated)(1)
