# TAGLINE

项目模板生成器

# TLDR

**从模板创建项目**

```cookiecutter [https://github.com/user/template]```

**从本地模板创建**

```cookiecutter [/path/to/template]```

**跳过交互提示创建**（使用默认值）

```cookiecutter --no-input [template]```

**覆盖模板变量**

```cookiecutter [template] [project_name]="[MyProject]"```

**列出已安装的模板**

```cookiecutter --list-installed```

**重放上次创建过程**

```cookiecutter --replay [template]```

**输出到指定目录**

```cookiecutter -o [/output/path] [template]```

# SYNOPSIS

**cookiecutter** [_options_] _template_

# DESCRIPTION

**cookiecutter** 是一个用于从模板创建项目的命令行实用程序，免去了手动搭建样板代码和项目结构的麻烦。它接受一个模板目录（本地的或来自 Git 仓库），提示输入配置值，然后生成完整的项目，并在整个项目中代入这些值。

模板使用 Jinja2 语法在文件名和文件内容中进行变量替换。例如，模板可能提示输入 "project_name"，并用它来创建目录、填充 setup 文件以及定制代码注释。这样既保证了各项目间的一致性，又保留了自定义的空间。

该工具催生了庞大的社区模板生态，涵盖 Django、Flask、React 等众多框架。cookiecutter 与具体编程语言无关，可以为任何类型的项目套用模板。它支持条件性包含文件、生成前/后钩子，以及用于重现先前配置的重放文件等高级特性。该工具已成为 Python 开发中的标准配置，并影响了其他生态中的类似工具。

# PARAMETERS

**-o**, **--output-dir** _path_
> 所生成项目的输出目录。

**--no-input**
> 不作提示，直接使用默认值。

**-c**, **--checkout** _branch_
> 要检出的 Git 分支或标签。

**-v**, **--verbose**
> 打印调试信息。

**--replay**
> 使用之前输入过的值。

**--replay-file** _file_
> 使用指定文件中的值。

**-f**, **--overwrite-if-exists**
> 覆盖已存在的输出目录。

**-s**, **--skip-if-file-exists**
> 跳过已存在的文件。

**--list-installed**
> 列出已安装的模板。

**--config-file** _file_
> 用户配置文件。

# CAVEATS

模板必须遵循 cookiecutter 的约定。远程模板需要 Git。复杂模板可能有很多交互提示。模板中的 Jinja2 错误会导致失败。

# HISTORY

**cookiecutter** 由 **Audrey Roy Greenfeld** 于 **2013** 年创建。它在 Python 社区推广了项目模板化的理念，并启发了其他语言中的类似工具。该工具促成了面向各种框架和项目类型的成千上万个社区模板。

# INSTALL

```brew: brew install cookiecutter```

```nix: nix profile install nixpkgs#cookiecutter```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[copier](/man/copier)(1), [git](/man/git)(1)
