# 各金属の物理特性（参考値、単位は SI 系）
metals = {
    "Ti": {"conductivity": 2.38e6, "density": 4.5, "specific_heat": 0.523, "melting_point": 1668},
    "Sn": {"conductivity": 8.7e6, "density": 7.3, "specific_heat": 0.227, "melting_point": 232},
    "Au": {"conductivity": 4.1e7, "density": 19.3, "specific_heat": 0.129, "melting_point": 1064}
}

# 混合比（重量比と仮定）
composition = {"Ti": 0.85, "Sn": 0.12, "Au": 0.03}

# 合金の推定特性（加重平均でシンプルに計算）
alloy_properties = {}
for prop in ["conductivity", "density", "specific_heat", "melting_point"]:
    alloy_properties[prop] = sum(
        composition[metal] * metals[metal][prop] for metal in composition
    )

# 結果表示
for key, value in alloy_properties.items():
    print(f"{key.capitalize()}: {value:.3f}")