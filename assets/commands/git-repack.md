# TAGLINE

将松散对象打包进包文件

# TLDR

**重新打包对象**

```git repack```

**激进地重新打包**

```git repack -a -d```

**使用增量压缩重新打包**

```git repack -a -d --depth=[250] --window=[250]```

**重新打包所有对象**

```git repack -A -d```

**按几何规则重新打包**

```git repack --geometric=[2]```

# SYNOPSIS

**git** **repack** [_options_]

# PARAMETERS

**-a**
> 打包所有对象。

**-A**
> 打包所有可达对象。

**-d**
> 移除冗余的包文件。

**-f**
> 强制重新计算增量（delta）。

**--depth** _n_
> 增量链深度。

**--window** _n_
> 增量窗口大小。

**--geometric** _factor_
> 按几何规则重新打包。

**-l**
> 仅处理本地对象。

# DESCRIPTION

**git repack** 将松散对象整合进包文件，以提升存储效率和访问速度。它通过把单个松散对象合并为压缩的包来重组仓库的对象数据库。

在大量小提交之后或导入对象之后，重新打包很有用。`-a -d` 组合常用于激进的重新打包，可移除冗余的包文件。

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

[git-gc](/man/git-gc)(1)
