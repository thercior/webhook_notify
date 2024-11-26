def format_currency(value, *args, **kwargs):
    value_str = f"{float(value):.2f}"
    integer_part, decimal_part = value_str.split(".")

    value_integer = f"{int(integer_part):,}".replace(",", ".")

    return f"R$ {value_integer},{decimal_part}"
