# TAGLINE

基于 Electron 的可定制文本编辑器

# TLDR

**打开** Atom 编辑器

```atom```

打开**指定文件**

```atom [file.txt]```

打开**目录**

```atom [project/]```

以**指定软件包**打开

```atom --package [package-name]```

**等待**窗口关闭

```atom --wait [file.txt]```

# SYNOPSIS

**atom** [_options_] [_paths_]

# DESCRIPTION

**Atom** 曾是 GitHub 开发的可定制文本编辑器，基于 Electron 构建。它通过软件包、主题和内置包管理器提供了高度的可扩展性。

该编辑器强调社区软件包生态和 Git 集成。

# PARAMETERS

**-n**, **--new-window**
> 在新窗口中打开

**-a**, **--add**
> 添加到当前窗口

**-w**, **--wait**
> 等待窗口关闭

**--dev**
> 以开发模式运行

**--safe**
> 禁用所有软件包

**--package** _name_
> 加载指定软件包运行

**--clear-window-state**
> 重置窗口状态

# CONFIGURATION

**~/.atom/config.cson**
> 主配置文件，包含设置、主题和软件包选项。

**~/.atom/init.coffee**
> Atom 启动时执行的启动脚本。

**~/.atom/keymap.cson**
> 自定义键盘快捷键绑定。

**~/.atom/styles.less**
> 编辑器界面的自定义 CSS/LESS 样式。

# CAVEATS

**Atom 已于 2022 年 12 月被 GitHub 弃用。** 项目已归档且不再维护。用户已迁移至 VS Code、Sublime Text 等替代品或社区分支。

# HISTORY

**Atom** 由 GitHub 于 **2014** 年发布，是一款开源、可定制的编辑器。它于 **2022** 年 12 月 15 日正式停止服务，开发随之终止。

# SEE ALSO

[code](/man/code)(1), [vim](/man/vim)(1), [emacs](/man/emacs)(1)

# RESOURCES

```[Source code](https://github.com/atom/atom)```

<!-- verified: 2026-06-17 -->
