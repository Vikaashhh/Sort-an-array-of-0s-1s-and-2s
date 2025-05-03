# 🚀 Day 21 of #gfg160 | #geekstreak2025
---
## 🔢 Problem: Sort an array consisting of only 0s, 1s, and 2s — without using in-built sorting.
---
## 🎯 Approach: Dutch National Flag Algorithm 🇳🇱
- It’s a classic 3-pointer technique — blazing fast and in-place!


## ⚙️ Logic Breakdown:
1. low: Pointer for 0s

2. mid: Current element

3. high: Pointer for 2s

## 📌 Steps:

1. If arr[mid] == 0: Swap with arr[low], increment both.

2. If arr[mid] == 1: Just move forward.

3. If arr[mid] == 2: Swap with arr[high], decrement high, but don’t increment mid!

## 📊 Complexity Analysis:
- Time: O(n) – Single pass

- Space: O(1) – In-place swap

💬 Have you implemented this using any other technique? Share your version below!
🔄 Keep optimizing, keep growing.
