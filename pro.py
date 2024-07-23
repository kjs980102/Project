def calculate_sling_requirements(weight_type, weight_spec, weight, sling_type):
    """
    중량물에 대한 줄걸이 수와 방법을 계산하는 함수

    Parameters:
    - weight_type (str): 중량물의 종류
    - weight_spec (str): 중량물의 규격
    - weight (float): 중량물의 무게 (kg)
    - sling_type (str): 줄걸이의 종류

    Returns:
    - dict: 줄걸이 수와 방법을 포함한 사전
    """
    # 줄걸이 종류에 따른 최대 허용 무게 (예시값)
    sling_capacities = {
        "chain": 5000,
        "wire_rope": 3000,
        "nylon_sling": 2000,
    }

    # 줄걸이 방법에 따른 안전 계수 (예시값)
    safety_factors = {
        "vertical": 1.0,
        "choker": 0.8,
        "basket": 2.0,
    }

    # 줄걸이 수 계산
    if sling_type in sling_capacities:
        max_capacity_per_sling = sling_capacities[sling_type]
    else:
        raise ValueError(f"Unknown sling type: {sling_type}")

    # 중량물 무게에 따른 적절한 줄걸이 수 계산
    num_slings = (weight / max_capacity_per_sling)

    # 줄걸이 방법 추천
    if num_slings <= 2:
        sling_method = "basket"
    elif num_slings <= 4:
        sling_method = "choker"
    else:
        sling_method = "vertical"

    # 최종 줄걸이 수 (올림 처리)
    num_slings = int(num_slings) if int(num_slings) == num_slings else int(num_slings) + 1

    return {
        "weight_type": weight_type,
        "weight_spec": weight_spec,
        "weight": weight,
        "sling_type": sling_type,
        "num_slings": num_slings,
        "sling_method": sling_method,
    }


# 예시 사용
result = calculate_sling_requirements("Steel Beam", "H-Beam 400x200", 6000, "wire_rope")
print(result)
