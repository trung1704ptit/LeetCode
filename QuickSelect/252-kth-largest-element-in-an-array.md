# Solution
Quick Select = Select + Partition

## Partition
- Pull element at pivot index from array
- Put smaller elements on left
- Put larger elements on right
- Replace pivot element

## Select
Select (left, right, k)
- Start with Select(0,n,k)
- Put k-th smallest element in k-th position
- Partion around k-th element