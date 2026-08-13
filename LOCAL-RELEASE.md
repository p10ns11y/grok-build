# Local release (build, CPU, PATH)

Operator notes for building this tree and putting a **side-by-side**
`local-grok` (or shorter `loc-grok`) on `PATH`. Leave the official `grok`
binary and updater alone. Upstream install and first-run commands live in
[`README.md`](README.md).

## Why a local release pegs the CPUs

All-cores-at-100% during a compile is expected. Cargo + rustc + LLVM use every
job they can. That is compile load, not the machine thrashing.

This is a large workspace. Parallel crate builds plus LLVM in `--release` fill
the host. Two profiles matter:

| Profile | Command | Cost | Use |
|---|---|---|---|
| `release` | `cargo build -p xai-grok-pager-bin --release` | Heavy, but **no** LTO / no `codegen-units = 1` | Daily local “fast” release |
| `release-dist` | `cargo build -p xai-grok-pager-bin --profile release-dist` | Much heavier: **thin LTO + `codegen-units = 1`** | Shipping-quality binary |

Default `--release` is already the lighter local profile. `release-dist` is
what official shipping builds use.

Day to day, prefer **debug** (`cargo run` / `cargo build` without `--release`).
Pay for release only when you want a binary on `PATH`.

Always target the binary crate. A full-workspace `--release` is slower and hotter.

## Cap CPU so the desktop stays usable

Leave a few cores free. Example on a 12-core host:

```bash
# ~half the machine (12 cores → 6 jobs)
CARGO_BUILD_JOBS=6 cargo build -p xai-grok-pager-bin --release

# or:
cargo build -p xai-grok-pager-bin --release -j 4
```

Optional extras if the box still feels slammed:

```bash
export CARGO_BUILD_JOBS=4
export RAYON_NUM_THREADS=4   # some crates honor this
```

Do **not** use `--profile release-dist` unless you specifically want official
shipping optimizations. That profile is the one that used to feel like
“release eats the machine.”

## Build + put `local-grok` on PATH

Prereqs (once): Rust via `rustup` (toolchain is pinned in
[`rust-toolchain.toml`](rust-toolchain.toml)), and `dotslash` on `PATH` so
`bin/protoc` works. See [Building from source](README.md#building-from-source).

### 1. Local debug (fastest, fine for iterating)

```bash
cargo run -p xai-grok-pager-bin
# binary: target/debug/xai-grok-pager
```

### 2. Local release + install as `local-grok`

Never install over `grok`. Official CLI stays `grok` (`~/.grok/bin/grok`).
This tree installs as `local-grok` (preferred) or `loc-grok` (shorter alias).

```bash
CARGO_BUILD_JOBS=6 cargo build -p xai-grok-pager-bin --release

# Artifact is named xai-grok-pager; do not name it grok
install -m 0755 target/release/xai-grok-pager ~/.local/bin/local-grok
# optional shorter name:
# ln -sf local-grok ~/.local/bin/loc-grok
hash -r
local-grok --version
which grok local-grok   # grok = official; local-grok = this tree
```

`~/.local/bin` is typically on `PATH`. Official installs land at
`~/.grok/bin/grok` (often a symlink to a downloaded versioned binary). Keep
that path untouched so the official updater still owns `grok`. If
`~/.local/bin/grok` is a leftover symlink or copy from an earlier local
install, remove it so `grok` resolves back to `~/.grok/bin/grok`.

### 3. Dist-quality (only when you want shipping opts)

```bash
CARGO_BUILD_JOBS=4 cargo build -p xai-grok-pager-bin --profile release-dist
install -m 0755 target/release-dist/xai-grok-pager ~/.local/bin/local-grok
```

Expect this to take longer and stay hotter even with `-j 4`.

### 4. Official prebuilt (no compile)

```bash
curl -fsSL https://x.ai/cli/install.sh | bash
# lands at ~/.grok/bin/grok  — leave this name for official only
```

Do not replace `~/.grok/bin/grok` or `~/.local/bin/grok`. Keep official
`grok`; put the self-built binary at `~/.local/bin/local-grok`.

## Practical split

- Iterate in this repo: `cargo run -p xai-grok-pager-bin` (debug).
- Use a self-built CLI from any directory: `--release` + `install` into
  `~/.local/bin/local-grok`, with `CARGO_BUILD_JOBS=4` or `6`.
- Match official performance/size: `--profile release-dist`, then the same
  `install`.
- Type `grok` for the official binary; type `local-grok` (or `loc-grok`) for
  this checkout.
