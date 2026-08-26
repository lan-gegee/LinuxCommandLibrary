# TAGLINE

自动化 Debian 软件包构建的程序集

# TLDR

**清理构建产物**

```dh_clean```

**将文件安装到软件包目录**

```dh_install```

**生成软件包依赖**

```dh_shlibdeps```

**压缩文档**

```dh_compress```

**生成 md5sums**

```dh_md5sums```

**使用 dh 序列器构建软件包**

```dh binary```

**执行完整构建序列**

```debian/rules binary```

# SYNOPSIS

**dh_**_command_ [_options_] [**--** _args_]

**dh** _target_ [_options_]

# COMMON COMMANDS

**dh_auto_configure**
> 运行上游 configure 脚本。

**dh_auto_build**
> 构建上游源码。

**dh_auto_install**
> 安装到 debian/tmp。

**dh_auto_test**
> 运行上游测试套件。

**dh_auto_clean**
> 清理上游构建产物。

**dh_install**
> 将文件安装到软件包目录。

**dh_installdocs**
> 安装文档。

**dh_installman**
> 安装 man page。

**dh_compress**
> 压缩软件包中的文件。

**dh_fixperms**
> 修正文件权限。

**dh_shlibdeps**
> 计算共享库依赖。

**dh_gencontrol**
> 生成 control 文件。

**dh_builddeb**
> 构建 .deb 文件。

# DESCRIPTION

**debhelper** 是一组程序（dh_*），用于自动化构建 Debian 软件包时的常见任务。维护者无需在 debian/rules 中编写 shell 命令，而是调用 debhelper 命令来正确处理标准操作。

**dh** 命令是一个序列器，按正确顺序运行相应的 debhelper 命令。借助 dh，一个最小的 debian/rules 只需三行代码，再通过覆盖目标进行定制。

Debhelper 从 debian/ 目录下的文件读取配置：install、docs、manpages 等。这种声明式方法简化了打包工作，同时保持了对复杂软件包的灵活性。

# MINIMAL RULES FILE

```makefile
#!/usr/bin/make -f
%:
	dh $@
```

# CAVEATS

Debhelper 是 Debian 特有的；其他发行版有各自的打包系统。兼容级别（debhelper-compat）会影响行为；务必指定级别。部分 dh 命令选项繁多，详情请查阅 man page。通过 debian/rules 中的覆盖目标可以定制 dh 行为。

# HISTORY

Debhelper 由 **Joey Hess** 于 **1997 年**创建，旨在简化 Debian 打包。在 debhelper 出现之前，每个软件包都要用 shell 脚本重新实现常见任务，导致不一致和 bug。dh 序列器在 debhelper 7（2008 年）中加入，大幅简化了 debian/rules 文件。Debhelper 已成为构建 Debian 软件包的标准方式。

# INSTALL

```dnf: sudo dnf install debhelper```

```zypper: sudo zypper install debhelper```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[dh](/man/dh)(1), [dpkg-buildpackage](/man/dpkg-buildpackage)(1), [debuild](/man/debuild)(1)
