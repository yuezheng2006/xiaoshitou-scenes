# Portable IP Pack · 可携带 IP 包

## 目的

IP Pack 是已确认 Profile 的可携带交付边界，负责把身份、动作和模式校准资产放进一个可导入目录。它不替代 Profile Manifest，而是把 Profile 的可公开资产复制出来，并用 `pack.manifest.json` 固化资产哈希、隐私级别和 QA 状态。

```text
Profile Manifest
  → create-ip-pack.py
  → pack.manifest.json + profile.manifest.json + assets/
  → validate-ip-pack.py
  → 导入后续模式
```

## Pack 状态

- `DRAFT`：包结构已创建，但身份或授权尚未完成。
- `CALIBRATING`：身份已录入，仍有模式校准或用户确认未完成。
- `READY`：身份 QA 通过、授权已确认，可以导入普通 Task。
- `DEPRECATED`：旧版本，仅供历史任务复现，不得作为新任务默认 Profile。

## 资产角色

- `canonical`：身份主锚点。
- `identity_sheet`：拟人设定或规范说明图。
- `identity_reference`：辅助身份参考。
- `action_sheet`：动作、姿态和小比例扩展。
- `calibration`：指定模式的校准图。
- `failure_example`：身份或模式失败案例，默认不作为生图参考。

每个资产都必须记录相对路径、SHA-256、字节数、可见性和角色。路径不得越出 Pack 根目录。

## 隐私边界

Builder 默认只复制 `public_assets`。复制 `private_assets` 必须同时显式传入：

```text
--include-private --consent CONFIRMED
```

原始真人照片、未授权品牌标和私有 IP 默认不能进入公共 Pack。`CONFIRMED` 只表示用户授权当前本地 Pack 使用，不自动表示可以公开分发。

## 导出与校验

```bash
python3 scene-skill-core/scripts/create-ip-pack.py \
  default-little-stone \
  --output /tmp/default-little-stone-pack \
  --consent CONFIRMED

python3 scene-skill-core/scripts/validate-ip-pack.py \
  /tmp/default-little-stone-pack/pack.manifest.json

python3 scene-skill-core/scripts/resolve-ip-assets.py \
  --pack /tmp/default-little-stone-pack/pack.manifest.json \
  --mode handdrawn \
  --action handoff
```

`READY` Pack 必须满足：

1. 至少有一个 canonical 资产。
2. 身份 QA 为 `PASS`。
3. consent 为 `CONFIRMED`。
4. 所有资产文件存在，字节数和 SHA-256 与 manifest 一致。
5. `AVAILABLE` 模式拥有对应校准资产。

## Resolver 输出

`resolve-ip-assets.py` 输出的是 Task Manifest 的可写入片段：

- `profile`、`mode`：任务身份和目标模式。
- `reference_protocol`：`none`、`single`、`dual` 或 `DEGRADED_TO_SINGLE`。
- `reference_assets`：按身份锚点 → identity sheet → 模式校准 → 动作表的顺序排列。
- `resolution.selected_assets`：保留每个文件的 `asset_id`、角色和模式来源。
- `resolution.warnings/errors/blocked`：记录降级、缺失和阻塞原因。

模式校准缺失时自动降级为 `single`，但不会伪称 `dual`；模式校准被明确标记为 `REJECTED` 时直接阻塞。
