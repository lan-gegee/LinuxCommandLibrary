# TAGLINE

为从标准输入读取的程序提供行编辑能力

# TLDR

**以行编辑方式运行命令**

```ledit [command]```

**以行编辑方式运行 OCaml**

```ledit ocaml```

**使用 vi 风格编辑**

```ledit -v [command]```

**指定历史文件**

```ledit -h [~/.ledit_history] [command]```

# SYNOPSIS

**ledit** [_options_] _command_ [_args_...]

# PARAMETERS

**-v**
> 使用 vi 风格编辑模式。

**-e**
> 使用 emacs 风格编辑模式（默认）。

**-h** _file_
> 指定历史文件。

**-x**
> 按空格键时展开历史条目。

# DESCRIPTION

**ledit** 为从标准输入读取的程序提供行编辑能力。它会包装目标命令，为其添加 readline 风格的编辑、命令历史和行补全。

对于缺乏内置行编辑支持的解释器和 REPL，ledit 尤其实用，例如较旧版本的 OCaml。

# CAVEATS

自带 readline 的程序不需要它。可能会干扰某些交互式程序。历史文件格式为 ledit 专有。

# HISTORY

ledit 由 **Daniel de Rauglaudre** 编写，是 Camlp5 项目的一部分，供 OCaml 及其他缺少行编辑功能的解释器使用。

# INSTALL

```apt: sudo apt install ledit```

```brew: brew install ledit```

```nix: nix profile install nixpkgs#ledit```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rlwrap](/man/rlwrap)(1), [readline](/man/readline)(3), [ocaml](/man/ocaml)(1)
