import math


def calculate_lifting_requirements(weight, num_slings, sling_type, sling_method, safety_factor=1.5):
    """
    총 양중 무게, 필요 줄걸이 용량, 필요 샤클 용량을 계산하는 함수

    Parameters:
    - weight (float): 중량물의 총 무게 (kg)
    - num_slings (int): 사용될 줄걸이 수
    - sling_type (str): 줄걸이의 종류 (예: "chain", "wire_rope", "nylon_sling")
    - sling_method (str): 줄걸이 방법 (예: "vertical", "choker", "basket")
    - safety_factor (float): 안전 계수 (기본값: 1.5)

    Returns:
    - dict: 총 양중 무게, 필요 줄걸이 용량, 필요 샤클 용량을 포함한 사전
    """
    # 줄걸이 종류에 따른 최대 허용 무게 (예시값)
    sling_capacities = {
        "chain": 5000,
        "wire_rope": 3000,
        "nylon_sling": 2000,
    }

    # 줄걸이 방법에 따른 안전 계수 적용 (예시값)
    method_factors = {
        "vertical": 1.0,
        "choker": 0.8,
        "basket": 2.0,
    }

    if sling_type not in sling_capacities:
        raise ValueError(f"Unknown sling type: {sling_type}")

    if sling_method not in method_factors:
        raise ValueError(f"Unknown sling method: {sling_method}")

    # 총 양중 무게는 중량물의 총 무게와 동일
    total_lifting_weight = weight

    # 필요 줄걸이 용량 계산 (안전 계수 적용)
    required_sling_capacity = (weight * safety_factor) / (num_slings * method_factors[sling_method])

    # 필요 샤클 용량 계산 (줄걸이 용량과 동일하게 적용)
    required_shackle_capacity = required_sling_capacity

    return {
        "total_lifting_weight": total_lifting_weight,
        "required_sling_capacity": required_sling_capacity,
        "required_shackle_capacity": required_shackle_capacity,
    }


# 예시 사용
result = calculate_lifting_requirements(6000, 4, "wire_rope", "basket")
print(result)

