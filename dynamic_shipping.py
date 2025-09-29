# simplified_shipping.py

def calculate_shipping_fee(
    order_value: float,
    distance: float,
    customer_type: str,
    is_oversized: bool,
) -> float:
    
    VALID_CUSTOMER_TYPES = {"VIP", "THUONG", "MOI"}
    customer_type_upper = customer_type.upper()

    if order_value < 0:
        raise ValueError("Giá trị đơn hàng không được âm.")
    if not (0 < distance <= 20):
        raise ValueError("Khoảng cách phải trong khoảng (0, 20] km.")
    if customer_type_upper not in VALID_CUSTOMER_TYPES:
        raise ValueError(f"Loại khách hàng không hợp lệ: {customer_type}")

    if is_oversized:
        return 70000.0
    if customer_type_upper == "MOI":
        return 0.0
    base_fee = 0.0
    if distance <= 5:
        base_fee = 20000.0
    elif distance <= 10:
        base_fee = 30000.0
    else: 
        base_fee = 30000.0 + (distance - 10) * 1500
    final_fee = base_fee
    if customer_type_upper == "VIP":
        if order_value >= 300000:
            final_fee = 0.0
        else:
            final_fee *= 0.7  
    elif customer_type_upper == "THUONG":
        if order_value >= 500000:
            final_fee = 0.0

    return final_fee