# TAGLINE

将 markdown 转换为 man page 和 HTML

# TLDR

**转换为 man page**

```ronn [file.ronn]```

**转换为 HTML**

```ronn --html [file.ronn]```

**同时转换两种格式**

```ronn --roff --html [file.ronn]```

**在浏览器中预览**

```ronn --server [file.ronn]```

**指定输出目录**

```ronn --output-dir [man/] [file.ronn]```

# SYNOPSIS

**ronn** [_options_] _files_...

# PARAMETERS

**--roff**
> 生成 roff（man page）。

**--html**
> 生成 HTML。

**--fragment**
> 仅生成 HTML 片段。

**--server**, **-S**
> 预览服务器。

**--style** _style_
> HTML 样式。

**--output-dir** _dir_
> 输出目录。

**--manual** _name_
> 手册名称。

**--organization** _org_
> 页脚中的组织名称。

**--date** _YYYY-MM-DD_
> 页脚中的发布日期。

**-w**
> 在 stderr 上显示 troff 警告。

**-W**
> 禁用 troff 警告。

# DESCRIPTION

**Ronn** 将类 Markdown 文本转换为 Unix man page 和 HTML。它使用扩展的 Markdown 语法，以易读的格式编写手册页。

# EXAMPLES

```bash
# Generate man page
ronn mycommand.1.ronn

# Generate HTML
ronn --html mycommand.1.ronn

# Both formats
ronn --roff --html mycommand.1.ronn

# Preview
ronn --server mycommand.1.ronn

# Install man page
ronn mycommand.1.ronn
sudo cp mycommand.1 /usr/local/share/man/man1/
```

# RONN FORMAT

```markdown
mycommand(1) -- short description
=============================================

## SYNOPSIS

`mycommand` [options] <file>

## DESCRIPTION

Description of the command.

## OPTIONS

  * `-h`, `--help`:
    Show help message.
```

# CAVEATS

Ruby gem（gem install ronn-ng）。文件名约定：name.section.ronn。

# HISTORY

Ronn 由 **Ryan Tomayko** 创建，用于简化 man page 的编写。ronn-ng 是持续维护的分支。

# INSTALL

```apk: sudo apk add ronn```

```brew: brew install ronn```

```nix: nix profile install nixpkgs#ronn```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[man](/man/man)(1), [pandoc](/man/pandoc)(1), [groff](/man/groff)(1)
