"""Rebuild lab8.ipynb from OG_lab8_v2_with_outputs.ipynb + implementation cells from current lab8.ipynb.

Implementation slots (same indices in reference and student notebook):
  6 softmax, 11 relu, 13 limit_weights, 23 forward_pass, 25 error_backpropagate,
  27 train_mlp, 30 initialize_mlp_from_dbn

Cell 17 (cdk + reconstruction_error) stays exactly as in the reference template.
"""
import json

REF = r"C:\Users\womackow\Zbiorczy\_WIN_AI_AGH_\WIN_sem_1\UMISI-sem1-DeepLearning\l8\OG_lab8_v2_with_outputs.ipynb"
WORK = r"C:\Users\womackow\Zbiorczy\_WIN_AI_AGH_\WIN_sem_1\UMISI-sem1-DeepLearning\l8\lab8.ipynb"
OUT = WORK

IMPL_INDICES = [6, 11, 13, 23, 25, 27, 30]


def cell_lines(nb: dict, i: int) -> list:
    src = "".join(nb["cells"][i].get("source", []))
    lines = src.splitlines(keepends=True)
    if lines and not lines[-1].endswith("\n"):
        lines[-1] += "\n"
    return lines


def main() -> None:
    with open(REF, encoding="utf-8") as f:
        nb = json.load(f)
    with open(WORK, encoding="utf-8") as f:
        wk = json.load(f)

    if len(nb["cells"]) != len(wk["cells"]):
        raise SystemExit(
            f"Cell count mismatch: ref={len(nb['cells'])} work={len(wk['cells'])}. "
            "Resize lab8.ipynb to match OG_lab8_v2_with_outputs.ipynb first."
        )

    for i in IMPL_INDICES:
        nb["cells"][i]["source"] = cell_lines(wk, i)

    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(nb, f, ensure_ascii=False, indent=1)

    src_all = "".join("".join(c.get("source", [])) for c in nb["cells"])
    assert "class Layer:" in src_all
    assert "class RestrictedBoltzmannMachine:" in src_all
    assert "TODO implement" not in src_all, "Implementation cells still contain TODO"
    print("OK:", OUT, "cells=", len(nb["cells"]))


if __name__ == "__main__":
    main()
