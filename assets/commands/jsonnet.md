# TAGLINE

生成 JSON 的数据模板语言

# TLDR

**求值 Jsonnet 文件**

```jsonnet [file.jsonnet]```

**输出到文件**

```jsonnet [file.jsonnet] -o [output.json]```

**使用外部变量求值**

```jsonnet --ext-str [name=value] [file.jsonnet]```

**多文件输出**

```jsonnet -m [output_dir] [file.jsonnet]```

**求值表达式**

```jsonnet -e "[{a: 1, b: 2}]"```

**格式化 Jsonnet 文件**

```jsonnetfmt [file.jsonnet]```

# SYNOPSIS

**jsonnet** [_options_] _file_

# PARAMETERS

**-o** _file_
> 输出文件。

**-m** _dir_
> 多文件输出目录。

**-e** _code_
> 求值表达式。

**--ext-str** _name=value_
> 外部字符串变量。

**--ext-code** _name=code_
> 外部代码变量。

**-J** _dir_
> 添加库搜索路径。

**-S**, **--string**
> 以字符串形式输出。

**--tla-str** _name=value_
> 顶层参数字符串。

# DESCRIPTION

**Jsonnet** 是一种生成 JSON 的数据模板语言。它在 JSON 基础上增加了变量、条件语句、函数和导入功能，让配置文件更易于维护。

Jsonnet 常用于生成 Kubernetes 清单、Prometheus 配置以及其他 JSON/YAML 配置。它的求值结果是纯 JSON。

# EXAMPLE

```jsonnet
local person(name, age) = {
  name: name,
  age: age,
};

{
  people: [
    person("Alice", 30),
    person("Bob", 25),
  ]
}
```

# CAVEATS

输出始终是 JSON（如需 YAML 需另行转换）。没有副作用，纯函数式。引用库需要 -J 指定路径。不适合运行时配置。

# HISTORY

Jsonnet 由 **Google** 的 **Dave Cunningham** 于 **2014 年**前后开发。它解决了云基础设施中配置代码 DRY 化的需求，随后在 Kubernetes 生态中获得广泛采用。

# INSTALL

```apt: sudo apt install jsonnet```

```dnf: sudo dnf install jsonnet```

```apk: sudo apk add jsonnet```

```brew: brew install jsonnet```

```nix: nix profile install nixpkgs#jsonnet```

<!-- packages: 2026-07-22 -->

# SEE ALSO

[jq](/man/jq)(1), [yq](/man/yq)(1), [dhall](/man/dhall)(1)
