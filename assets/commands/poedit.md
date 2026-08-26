# TAGLINE

gettext PO 翻译文件的图形化编辑器

# TLDR

**打开 PO 文件进行编辑**

```poedit [file.po]```

**从 POT 模板创建新翻译**

```poedit --new [template.pot]```

**打开文件并跳转到指定行**

```poedit --line [10] [file.po]```

# SYNOPSIS

**poedit** [_options_] [_files_]

# PARAMETERS

**--new** _file_
> 从 POT 创建新的翻译目录。

**--line** _num_
> 打开文件并定位到指定的行号。

**--help**
> 显示用法信息并退出。

**--version**
> 显示版本信息并退出。

# DESCRIPTION

**Poedit** 是 gettext PO 翻译文件的图形化编辑器。它为译者提供直观的界面，具备翻译记忆库、术语表和机器翻译集成等功能。

# CAVEATS

Poedit 是一个 GUI 应用，仅有极少的命令行界面。若要在命令行管理翻译，请直接使用 gettext 工具（msgfmt、xgettext、msginit、msgmerge）。

# HISTORY

Poedit 由 **Václav Slavík** 创建，是一个面向使用 gettext 的译者的开源工具。

# INSTALL

```dnf: sudo dnf install poedit```

```pacman: sudo pacman -S poedit```

```apk: sudo apk add poedit```

```zypper: sudo zypper install poedit```

```nix: nix profile install nixpkgs#poedit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[msgfmt](/man/msgfmt)(1), [xgettext](/man/xgettext)(1), [msginit](/man/msginit)(1), [msgmerge](/man/msgmerge)(1), [gettext](/man/gettext)(1)
