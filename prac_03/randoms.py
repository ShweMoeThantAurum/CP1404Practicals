# For line 1, I see generating a random integer between 5 and 20. The smallest number I could have seen was 5 and the
# largest was 20.

# For line 2, I see generating a random number with range 2 between 3 and 10. The smallest number I could have seen
# was 3 and the largest was 9. Line 2 couldn't produce a 4 because the start number is even and the step is 2. So,
# the results will always be odd.

# For line 3, I see generating random number between 2.5 and 5.5. The smallest number I could ever seen was
# 2.6125420634822203 and the largest was 5.33698345711287.

import random
print(random.randint(1, 100))