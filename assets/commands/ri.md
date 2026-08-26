# TAGLINE

查看 Ruby API 文档

# TLDR

**查看类文档**

```ri [Array]```

**查看方法文档**

```ri [Array#map]```

**查看实例方法**

```ri [String#split]```

**查看类方法**

```ri [File.open]```

**列出所有类**

```ri -l```

# SYNOPSIS

**ri** [_options_] [_name_...]

# PARAMETERS

**-l**, **--list**
> 列出所有类。

**-f**, **--format** _name_
> 输出格式。

**-i**, **--interactive**
> 交互模式。

**-T**, **--no-pager**
> 不使用分页器。

**--doc-dir** _dir_
> 文档目录。

# DESCRIPTION

**ri**（Ruby Information）在命令行中显示 Ruby 文档。它读取由 RDoc 生成的文档，让你快速查阅类和方法信息。

# EXAMPLES

```bash
# Class documentation
ri Array
ri String

# Instance method (use #)
ri Array#each
ri String#gsub

# Class method (use .)
ri File.read
ri Dir.glob

# Search for method
ri -l | grep map

# Interactive mode
ri -i
```

# NOTATION

```
Class          - ri Array
Class#method   - Instance method (ri Array#map)
Class.method   - Class method (ri File.open)
Class::Const   - Constant (ri File::SEPARATOR)
```

# CAVEATS

必须先安装文档。可使用 gem rdoc --all 生成 gem 文档。ri 是 Ruby 标准库的一部分。

# HISTORY

ri 是 **Ruby** RDoc 系统的组成部分，自 Ruby 早期版本起就提供命令行文档访问功能。

# INSTALL

```apt: sudo apt install ruby```

```dnf: sudo dnf install ruby```

```pacman: sudo pacman -S ruby```

```apk: sudo apk add ruby-rdoc```

```zypper: sudo zypper install ruby```

```brew: brew install ruby```

```nix: nix profile install nixpkgs#ruby```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[rdoc](/man/rdoc)(1), [ruby](/man/ruby)(1), [irb](/man/irb)(1)
