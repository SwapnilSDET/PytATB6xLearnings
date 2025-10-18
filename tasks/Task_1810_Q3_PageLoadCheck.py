"""
Simulate a page loading check using a while loop.
If page_loaded becomes True within 5 seconds, print success; else timeout.

Hint: Use a counter (like wait_time) and break condition.
"""
import time

# Initialization
wait_time = 1

# Condition
while wait_time <= 5:
    is_page_loaded = input("Do you see a page loading check? (True/False): ").strip()

    if is_page_loaded == 'True':
        print(f"The page loading check is {is_page_loaded} in {wait_time} seconds.")
        break
    # Updation
    time.sleep(1)
    wait_time = wait_time + 1

print("---------------------------")
if is_page_loaded == 'True':
    print("✅ Page loaded successfully in {wait_time} second(s)")
else:
    print("❌ Timeout: Page failed to load within 5 seconds.")