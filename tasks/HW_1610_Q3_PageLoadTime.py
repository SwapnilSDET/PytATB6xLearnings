"""
You want to check whether a web page loads within 3 seconds (performance test condition).
load_time = 4.2
⚠️ Page load too slow: 4.2 seconds
"""

page_load_time = int(input("What is the page load time (in seconds)?: "))
if page_load_time <= 3:
    print("✅ Page load time is as expected. ")
else:
    print("⚠️ Page load time is too slow. ")