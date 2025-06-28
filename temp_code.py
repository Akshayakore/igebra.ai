def max_product_subarray(nums):
    if not nums:
        return 0

    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        current = nums[i]
        # Swap if current number is negative
        if current < 0:
            max_product, min_product = min_product, max_product

        max_product = max(current, max_product * current)
        min_product = min(current, min_product * current)

        result = max(result, max_product)

    return result

# Example usage:
nums = [2, 3, -2, 4]
print("Maximum product of subarray:", max_product_subarray(nums))
