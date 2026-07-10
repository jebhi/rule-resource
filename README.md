# rule-resource

个人代理规则与相关资源的集中仓库。

## 目录结构

```text
.
├── rules/
│   ├── domain/
│   │   └── apple.yaml
│   └── classical/
│       └── openai.yaml
├── snippets/
│   └── instagram.list
├── scripts/
│   └── sync-legacy.sh
├── .github/workflows/
│   └── validate-rules.yml
├── apple.yaml                  # 旧 Raw URL 兼容文件
├── openai.yaml                 # 旧 Raw URL 兼容文件
└── instagram (2).list          # 旧 Raw URL 兼容文件
```

## 文件类型

- `rules/domain/`：仅包含域名匹配项，适合域名类 rule-provider。
- `rules/classical/`：包含 `DOMAIN`、`DOMAIN-SUFFIX`、`IP-CIDR` 等不同规则类型的完整规则集。
- `snippets/`：用于直接嵌入主配置的片段，不保证能作为独立 rule-provider 使用。

## 兼容策略

根目录的三个旧文件暂时保留，避免已经配置在客户端中的 Raw URL 失效。新的规范文件是主要维护入口：

- `rules/domain/apple.yaml`
- `rules/classical/openai.yaml`
- `snippets/instagram.list`

修改规范文件后，运行：

```bash
bash scripts/sync-legacy.sh
```

该脚本会同步更新根目录兼容文件。GitHub Actions 也会检查两份内容是否一致。

## 维护约定

1. 文件名统一使用小写英文和连字符，避免空格、括号及自动生成的重复编号。
2. 新规则先确认格式，再放入对应目录。
3. 外部来源的规则应保留作者、来源仓库和更新时间。
4. 不在本仓库混放无关网页项目；独立网页或程序应使用单独仓库。
