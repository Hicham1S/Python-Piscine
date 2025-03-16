import time

timepast = time.time()

formatted_time = f"{timepast:,.4f}"
scientific_notation = f"{timepast:.2e}"

print(
    f"Seconds since January 1, 1970: {formatted_time} "
    f"or {scientific_notation} in scientific notation$"
)
print(time.strftime("%b %d %Y"))
