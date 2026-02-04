def reconstruct_sequence_simple(comparisons):
    """
    Simple and intuitive approach: assign based on relative ordering.

    Args:
        comparisons: List where comparisons[i] is None, '+', or '-'

    Returns:
        List representing a valid sequence satisfying the comparisons
    """
    n = len(comparisons) - 1

    # Create a list to track relative ordering
    # Start with 0 as a reference point
    relative = [0]

    # Build relative positions based on comparisons
    for i in range(1, len(comparisons)):
        if comparisons[i] == '+':
            # Higher than all previous in current ascending run
            relative.append(relative[-1] + 1)
        else:  # '-'
            # Lower than previous
            relative.append(relative[-1] - 1)
    import pdb;pdb.set_trace()
    # Normalize to [0, n] range
    min_val = min(relative)
    result = [x - min_val for x in relative]

    # Map to actual values while maintaining order
    sorted_positions = sorted(range(len(result)), key=lambda i: result[i])
    final_result = [0] * len(result)
    for rank, pos in enumerate(sorted_positions):
        final_result[pos] = rank

    return final_result


def reconstruct_stack(comparisons):
    """
    O(N) approach using a Stack.
    Correctly handles [None, +, +, -, +]
    """
    n = len(comparisons)
    result = []
    stack = []

    # We need numbers 0 to n-1
    # We iterate through the inputs (indices 0 to n-1)
    for i in range(n):
        # Push the current number index
        stack.append(i)

        # We pop from stack if:
        # 1. We are at the very end
        # 2. OR the NEXT element is a '+' (meaning the current run of '-' is over)

        if i == n - 1 or comparisons[i+1] == '+':
            while stack:
                result.append(stack.pop())

    return result

# Test and visualize
if __name__ == "__main__":
    test_cases = [
        [None, '+', '+', '-', '+'],
        [None, '+', '+', '+'],
        [None, '-', '-', '-'],
        [None, '+', '-', '+', '-'],
        [None, '+', '+', '-', '+'],
        [None, '-', '+', '-', '+', '-'],
    ]

    print("Testing sequence reconstruction:\n")

    for comparisons in test_cases:
        #result = reconstruct_sequence_simple(comparisons)
        result = reconstruct_stack(comparisons)
        print(f"result: {result}")
        # Verify the result
        valid = True
        for i in range(1, len(comparisons)):
            if comparisons[i] == '+' and result[i] <= result[i-1]:
                valid = False
            elif comparisons[i] == '-' and result[i] >= result[i-1]:
                valid = False

        # Check all numbers 0 to n are used
        n = len(comparisons) - 1
        all_present = set(result) == set(range(n + 1))

        status = "✓ Valid" if (valid and all_present) else "✗ Invalid"
        print(f"Comparisons: {comparisons}")
        print(f"Result:      {result} {status}")

        # Show the actual comparisons
        comp_str = "  "
        for i in range(1, len(result)):
            if result[i] > result[i-1]:
                comp_str += "  >  "
            else:
                comp_str += "  <  "
            comp_str += " "
        print(f"Verification: {result[0]}{comp_str[2:]}")
        print()