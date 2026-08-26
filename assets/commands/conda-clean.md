# TAGLINE

移除未使用的软件包和缓存文件

# TLDR

**移除未使用的软件包和缓存**

```conda clean --all```

**仅移除软件包 tarball**

```conda clean --tarballs```

**仅移除未使用的软件包**

```conda clean --packages```

**移除索引缓存**

```conda clean --index-cache```

**演练运行**而不实际移除

```conda clean --all --dry-run```

# SYNOPSIS

**conda** **clean** [_options_]

# PARAMETERS

**-a**, **--all**
> 移除全部（索引缓存、锁文件、tarball、未使用的软件包）。

**-t**, **--tarballs**
> 移除缓存的软件包 tarball。

**-p**, **--packages**
> 移除未使用的软件包。

**-i**, **--index-cache**
> 移除缓存的频道索引文件。

**--dry-run**
> 显示将被移除的内容但不实际移除。

# DESCRIPTION

**conda clean** 通过清除 conda 在软件包操作过程中积累的各类缓存数据来回收磁盘空间。随着时间推移，conda 的缓存可能增长到数 GB，因为它会为所有下载过的软件包保存 tarball、解压后的软件包以及索引元数据。

缓存系统的存在是为了复用先前下载的软件包以加速安装，但一旦软件包被安装到环境中，缓存副本就不再是严格必需的了。--packages 选项移除当前未被任何环境使用的已解压软件包文件，而 --tarballs 则移除压缩归档。--index-cache 选项清空频道元数据，这些数据会在下一次 conda 操作时重新下载。

--all 是最彻底的选项，会清空所有类型的缓存并释放最大量的磁盘空间。--dry-run 旗标允许预览将被移除的内容而不实际删除任何东西，有助于了解可回收多少空间。此命令可以放心运行，因为它绝不会触碰实际环境中已安装的软件包，只处理集中式的软件包缓存。

# INSTALL

```dnf: sudo dnf install conda```

```nix: nix profile install nixpkgs#conda```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[conda](/man/conda)(1), [conda-remove](/man/conda-remove)(1)

# RESOURCES

```[Source code](https://github.com/conda/conda)```

```[Documentation](https://docs.conda.io/projects/conda/en/stable/commands/clean.html)```

<!-- verified: 2026-06-22 -->
