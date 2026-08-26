# TAGLINE

重新生成 autotools 构建系统文件

# TLDR

**重新生成**全部 autotools 文件

```autoreconf```

重新生成时**补装**缺失文件

```autoreconf --install```

**强制**重新生成

```autoreconf --force --install```

以详细模式重新生成

```autoreconf --install --verbose```

# SYNOPSIS

**autoreconf** [_-f_] [_-i_] [_-v_] [_options_]

# DESCRIPTION

**autoreconf** 按正确顺序运行 autoconf、autoheader、automake 及相关工具。它是重新生成 autotools 项目中 configure 脚本及相关文件的推荐方式。

该工具会根据项目配置自动判断需要运行哪些程序。

# PARAMETERS

**-i**, **--install**
> 补充缺失的辅助文件

**-f**, **--force**
> 即使文件是最新的也强制重新生成

**-v**, **--verbose**
> 详细输出

**-s**, **--symlink**
> 与 --install 连用时，以符号链接而非复制的方式安装辅助文件

**-I** _dir_, **--include=**_dir_
> 将 dir 追加到 aclocal、autoconf 和 autoheader 搜索的包含路径

**-m**, **--make**
> 在适用时运行 ./config.status --recheck 和 ./config.status，然后执行 make 更新一切

**-W** _category_, **--warnings=**_category_
> 报告指定类别的警告（all、none、error 或某个具体类别）

**-d**, **--debug**
> 不删除临时文件

**--no-recursive**
> 不重建子目录（被配置的软件包）中的文件

# WORKFLOW

从 git 构建时的典型用法：
```bash
autoreconf --install
./configure
make
```

# CAVEATS

需要安装 autoconf、automake 及相关工具。大型项目上速度较慢。现代替代方案（CMake、Meson）通常更简单。

# HISTORY

**autoreconf** 被加入 autoconf，旨在简化按正确顺序重新生成 autotools 文件这一复杂过程。

# INSTALL

```dnf: sudo dnf install autoconf```

```pacman: sudo pacman -S autoconf```

```apk: sudo apk add autoconf```

```zypper: sudo zypper install autoconf```

```brew: brew install autoconf```

```nix: nix profile install nixpkgs#autoconf```

<!-- packages: 2026-07-22 -->
# SEE ALSO

[autoconf](/man/autoconf)(1), [automake](/man/automake)(1), [libtoolize](/man/libtoolize)(1)

# RESOURCES

```[Homepage](https://www.gnu.org/software/autoconf/)```

```[Documentation](https://www.gnu.org/software/autoconf/manual/)```

<!-- verified: 2026-06-17 -->
