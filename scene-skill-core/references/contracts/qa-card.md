# QA Card · 质检卡

## 用途

质检卡记录候选图是否可以交付，以及失败发生在哪一层。它把返修从“重新试一次”变成可定位的修改。

## 字段

```text
任务名称：
本张编号：
Task Manifest：
Profile Version：
Prompt SHA-256：
状态：CONFIRMED / NEEDS_REVIEW / REJECT

Profile / Character Lock：PASS / FAIL / N/A
Persona Calibration：PASS / FAIL / N/A
Profile Contract：PASS / FAIL / N/A
Reference Protocol：none / single / dual / DEGRADED_TO_SINGLE
Reference Source：user_provided / generated_draft / none
内容准确性：PASS / FAIL
模式质量：PASS / FAIL
文字与标签：PASS / FAIL / N/A
事实与授权：PASS / FAIL / N/A

失败层：内容 / 方案 / 资产 / Prompt / 生成 / QA
具体问题：
返修动作：
是否只返修当前张：是 / 否
```

## Manifest 对齐

QA Card 与 `task-manifest.schema.json` 是同一张交付记录的两种视图：

- `Task Manifest` 必须指向本次任务的机器可读 manifest。
- `Profile Version`、`Reference Protocol`、`Reference Source` 必须与 manifest 一致。
- `Prompt SHA-256` 用于判断返修后是否仍是同一版生成指令；Prompt 改变时必须递增 `revision`。
- `CONFIRMED` 只能在 manifest 已记录实际输出文件、角色检查、模式检查、内容检查和事实/授权检查后成立。
- `REJECT` 必须记录失败层和具体返修动作；不得只写“再优化一下”。

## 交付规则

- `REJECT`：任一 Critical 角色、事实、授权或模式门禁失败，不得交付。
- `NEEDS_REVIEW`：非 Critical 问题需要标注后交给用户决定。
- `CONFIRMED`：公共 Confirm Gate 和当前模式 QA 均通过。

## IP 专属结构化评分

人工视觉检查或模型观察结果先写成结构化 observations，再由
`scripts/score-ip-qa.py` 计算分数。评分维度及权重固定为：

- `identity`：35%（身份锚点、比例、主色、核心特征）
- `style`：25%（当前模式的渲染语言与校准图一致）
- `action`：20%（主动作、姿态和物件关系成立）
- `role`：20%（IP 在叙事中的职责正确）

每个维度使用 `{ "passed": 数字, "total": 数字 }`。负向违规使用
`negative_violations` 数组，`CRITICAL` 直接 `REJECT`，`IMPORTANT` 至少
进入 `NEEDS_REVIEW`。无 Critical/Important 且总分 ≥ 85 才能 `CONFIRMED`。

示例：

```json
{
  "identity": { "passed": 5, "total": 5 },
  "style": { "passed": 4, "total": 4 },
  "action": { "passed": 3, "total": 3 },
  "role": { "passed": 2, "total": 2 },
  "negative_violations": []
}
```

评分器输出的 `task_manifest_qa` 可直接合并进任务 manifest；Profile 的
`failure_signals` 仍由 Profile 维护，评分器不重新发明身份定义。

## 规则

1. 先做公共 Character / Persona 检查，再做模式 QA。
2. QA 不重新定义 Profile 身份；身份问题回到 Profile 或资产层。
3. 返修必须写出具体修改，不使用“再优化一下”作为唯一结论。
